>Phần này hướng dẫn phát triển các công cụ và chương trình bcc sử dụng python gồm khả năng quan sát và mạng.

# Observability

## 1. Hello World

**code file hello_world.py**

```python
from bcc import BPF
BPF(text='int kprobe__sys_clone(void *ctx) { bpf_trace_printk("Hello, World!\\n"); return 0; }').trace_print()
```

**Giải thích code**


1. ```from bcc import BPF```

Import class BPF từ framework BCC, BPF dùng để:

- Biên dịch code eBPF C;

- Nạp chương trình eBPF vào kernel;

- Attach eBPF vào hook;

- Đọc output từ kernel;

2. ```text='...'```

Phần này dùng để định nghĩa một chương trình BPF nội tuyến. Chương trình được viết bằng ngôn ngữ C.

3. ```kprobe__sys_clone()```

Đây là hàm eBPF, ```kprobe__sys_clone``` nghĩa là gắn eBPF vào kernel function ```sys_clone```. Khi hệ thống gọi `sys_clone()` để tạo `process/thread` mới, hàm này sẽ chạy

4. ```void *ctx```

`ctx` là tham số, tuy nhiên trong trường hợp này chúng ta chưa sử dụng đến, nên chúng ta chỉ cần ép kiểu nó thành ```void *```

5. `bpf_trace_printk()`



