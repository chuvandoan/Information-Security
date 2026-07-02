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

```sudo python3 hello_world.py```

Sau đó mở 1 terminal khác và thực thi các lệnh tạo process

![](./img/1_hello_world.png)


