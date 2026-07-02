>Phần này hướng dẫn phát triển các công cụ và chương trình bcc sử dụng python gồm khả năng quan sát và mạng.

# Observability

## 1. Hello World

**code file hello_world.py**

```python
from bcc import BPF
BPF(text='int kprobe__sys_clone(void *ctx) { bpf_trace_printk("Hello, World!\\n"); return 0; }').trace_print()
```

**Giải thích code**

1. ```from bcc import BPF```: Import class BPF từ framework BCC, BPF dùng để:

- Biên dịch code eBPF C;

- Nạp chương trình eBPF vào kernel;

- Attach eBPF vào hook;

- Đọc output từ kernel;

2. ```text='...'```: Phần này dùng để định nghĩa một chương trình BPF nội tuyến. Chương trình được viết bằng ngôn ngữ C.

3. ```kprobe__sys_clone()```: Đây là hàm eBPF, ```kprobe__sys_clone``` nghĩa là gắn eBPF vào kernel function ```sys_clone```. Khi hệ thống gọi `sys_clone()` để tạo `process/thread` mới, hàm này sẽ chạy

4. ```void *ctx```: `ctx` là tham số, tuy nhiên trong trường hợp này chúng ta chưa sử dụng đến, nên chúng ta chỉ cần ép kiểu nó thành ```void *```

5. `bpf_trace_printk()`: Đây là hàm đơn giản để eBPF in thông tin debug ra file ```/sys/kernel/debug/tracing/trace_pipe```.
Nhưng nó có những hạn chế: 
- chỉ hỗ trợ tối đa 3 tham số nên dùng nhiều biến sẽ không phù hợp;
- chỉ hỗ trợ 1 `%&` nên sẽ không phù hợp để in nhiều chuỗi cùng một dòng;
- `trace_pipe` là tài nguyên dùng chung toàn hệ thống, nếu nhiều chương trình eBPF cùng ghi log, ouput có thể bị lẫn với nhau;
- không phù hợp cho collector nghiêm túc, vì output không có cấu trúc rõ ràng, khó parse thành JSON/event
- nên dùng `BPF_PERF_OUTPUT()`

6. ```return 0;```: thủ tục kết thúc chương trình.
7. ```.trace_print()```: Hàm bcc đọc trace_pipe và in ra kết quả


**Thực thi**

```bash
sudo python3 hello_world.py
```

Sau đó mở 1 terminal khác và thực thi các lệnh tạo process

![](./img/1_hello_world.png)


## 2. sys_sync()

Viết một chương trình theo dõi hàm kernel sys_sync(). In ra "sys_sync() called" khi chương trình chạy. Kiểm tra bằng cách chạy lệnh sync trong một phiên khác trong khi đang theo dõi.in ra "Tracing sys_sync()... Ctrl-C to end." khi chương trình bắt đầu

**Code cho file sync_trace.py**

```python
from bcc import BPF

print("Tracing sys_sync()... Ctrl-C to end.")

BPF(text="""
int kprobe__sys_sync(void *ctx)
{
    bpf_trace_printk("sys_sync() called\\n");
    return 0;
}
""").trace_print()
```

![](./img/2_sys_sync.png)

## 3. Hello fields

Đây là chương trình tách các trường như thời gian, tên process, PID, message rồi in thành bảng.

**Code cho file hello_fields.py**

```python
from bcc import BPF
from bcc.utils import printb

# define BPF program
prog = """
int hello(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""

# load BPF program
b = BPF(text=prog)
b.attach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello")

# header
print("%-18s %-16s %-6s %s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))

# format output
while 1:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    except KeyboardInterrupt:
        exit()
    printb(b"%-18.9f %-16s %-6d %s" % (ts, task, pid, msg))
```

**Giải thích code**

1. `from bcc.utils import printb`: import BCC, pirntb dùng để in dữ liệu dạng `bytes`, vì output từ BCC thường là bytes.
2. `prog =`: Khai báo chương trình C dưới dạng một biến, và sau đó tham chiếu đến nó, dùng để thêm một phép thay thế chuỗi dựa trên các đối số.
3. `hello()`: 
- khai báo một hàm C thay vì sử dụng cú pháp viết tắt `kpobe__`;
- tất cả các hàm C được khai báo trong chương trình BPF đều được kỳ vọng sẽ được thực thi khi có sự kiện thăm dò, do đó chúng đều cần nhận một con trỏ pt_reg* ctx làm đối số đầu tiên;
- Nếu cần định nghĩa một số hàm trợ giúp mà không được thực thi khi có sự kiện thăm dò, chúng cần được định nghĩa là static inline để trình biên dịch có thể gọi nội tuyến;
- hàm này sẽ chạy khi hook được kích hoạt.
4. `b = BPF(text=prog)`: BCC biên dịch code C trong biến `prog`, nạp chương trình eBPF vào kernel.
5. `b.attach_kprobe(event=b.get_syscall_fnname("clone"), fn_name="hello")`
- gắn hàm eBPF `hello()`vào syscall `clone`, `clone` là syscall dùng để tạo process/thread mới. Đơn giản là khi `clone()` được gọi thì hàm `hello()` chạy;
- `b.get_syscall_fnname("clone")`: giúp BCC tự tìm đúng tên hàm syscall trên kernel hiện tại;
- chúng ta có thể gọi `attach_kprobe()` nhiều laanmf và gắn hàm C của mình vào nhiều hàm nhân bản khác nhau;
- `fn_name="hello"`: nghĩa là khi syscall `clone()` được gọi, thì sẽ chạy hàm eBPF là `hello()`, hàm này được định nghĩa trong code C;
- luồng chạy như sau:
```bash
Process tạo process/thread mới
        ↓
gọi syscall clone()
        ↓
kernel chạy hàm clone tương ứng
        ↓
kprobe được kích hoạt
        ↓
eBPF function hello() chạy
        ↓
in "Hello, World!" vào trace_pipe
```
6. `print("%-18s %-16s %-6s %s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))`
- dùng để in tiêu đề bảng theo format cố định;
- chuỗi định dạng bảng:

| Phần    | Ý nghĩa                                      |
| ------- | -------------------------------------------- |
| `%s`    | in dữ liệu kiểu string                       |
| `%-18s` | in string, căn trái, chiếm 18 ký tự          |
| `%-16s` | in string, căn trái, chiếm 16 ký tự          |
| `%-6s`  | in string, căn trái, chiếm 6 ký tự           |
| `%s`    | in string bình thường, không cố định độ rộng |

7. `while 1`: tạo vòng lặp vô hạn, tương đương với `while true`.
8. `(task, pid, cpu, flags, ts, msg) = b.trace_fields()`
- đọc một dòng output từ `trace_pipe`, rồi tách các trường, sau đó trả về các giá trị `task, pid, cpu, flags, ts, msg`;
- ý nghĩa các trường:

| Biến    | Ý nghĩa                               |
| ------- | ------------------------------------- |
| `task`  | tên process gây ra event              |
| `pid`   | PID của process                       |
| `cpu`   | CPU core xử lý event                  |
| `flags` | cờ tracing nội bộ                     |
| `ts`    | timestamp, thời điểm event xảy ra     |
| `msg`   | message do `bpf_trace_printk()` in ra |

9. 

```
except ValueError:
    continue
```

- nếu `b.trace_fields()` không tách được dòng trace thành đúng 6 trường, nó sẽ gây lỗi ValueError, khi đó `continue` sẽ bỏ qua dòng lỗi đó và quay lại đầu vòng lặp để đọc dòng tiếp theo.

10. 

```
except KeyboardInterrupt:
    exit()
```
- khi sử dụng tổ hợp phím `Ctr +C` python sẽ sinh ra lỗi KeyboardInterrupt, câu lệnh này bắt lỗi đó và thoát chương trình gọn gàng.

11. `printb(b"%-18.9f %-16s %-6d %s" % (ts, task, pid, msg))`
- in event ra terminal bằng printb
- format:

| Phần      | Ý nghĩa                                                    |
| --------- | ---------------------------------------------------------- |
| `%-18.9f` | in số thực, căn trái, rộng 18 ký tự, 9 chữ số sau dấu chấm |
| `%-16s`   | in string/bytes, căn trái, rộng 16 ký tự                   |
| `%-6d`    | in số nguyên, căn trái, rộng 6 ký tự                       |
| `%s`      | in string/bytes bình thường                                |

![](./img/3_hello_fields.png)