<h1 align="center">
  <img src="https://media1.giphy.com/media/wvQIqJyNBOCjK/giphy.gif" width="500"/>

Information Security
</h1>

<h2 align="center">
Hê hee heeeeeeeeeeeeee3333
</h2>

---

Lộ trình này được thiết kế thân thiện với người mới bắt đầu, nhằm cung cấp một nền tảng vững chắc về các lĩnh vực khác nhau trong An ninh Máy tính. Nội dung bao gồm các khái niệm cơ bản và ứng dụng trong các chủ đề sau:

- Mạng máy tính và mã hóa  
- Kiến thức cơ bản về MS Windows, Active Directory và Linux  
- Các công cụ tấn công và khai thác hệ thống  
- Giải pháp và công cụ phòng thủ an ninh mạng  

---

## [Section 1: Linux Fundamentals](/Linux_Fundamentals/Linux_Fundamentals.md)
> Phần này cung cấp kiến thức nền tảng về hệ điều hành Linux, từ tổng quan, kiến trúc hệ thống, terminal, shell, hệ thống tệp, quyền truy cập, quản lý người dùng, tiến trình, dịch vụ, gói phần mềm, log cho đến Bash scripting cơ bản. Nội dung được xây dựng theo hướng thực hành, giúp người học làm quen với các lệnh Linux quan trọng, hiểu cách hệ thống hoạt động và áp dụng vào quản trị hệ thống, SOC và an toàn thông tin.

## Nội dung chính

| STT | Nội dung | Mô tả |
|---:|---|---|
| 1 | [Tổng quan về Linux](/Linux_Fundamentals/Linux_Fundamentals.md#1-tổng-quan-về-linux) | Giới thiệu Linux, lịch sử hình thành, vai trò của Linux và triết lý thiết kế mã nguồn mở. |
| 2 | [Cấu trúc và kiến trúc hệ điều hành Linux](/Linux_Fundamentals/Linux_Fundamentals.md#2-cấu-trúc-và-kiến-trúc-hệ-điều-hành-linux) | Trình bày các thành phần chính của Linux, kiến trúc hệ điều hành và cấu trúc hệ thống tệp. |
| 3 | [Terminal, Shell và dòng lệnh](/Linux_Fundamentals/Linux_Fundamentals.md#3-terminal-shell-và-dòng-lệnh) | Giải thích terminal, shell, Bash, prompt và các phím tắt cơ bản khi làm việc với dòng lệnh. |
| 4 | [Làm quen với các lệnh Linux cơ bản](/Linux_Fundamentals/Linux_Fundamentals.md#4-làm-quen-với-các-lệnh-linux-cơ-bản) | Hướng dẫn các lệnh cơ bản như `echo`, `whoami`, `id`, `hostname`, `uname`, `pwd`, `clear` và lịch sử lệnh. |
| 5 | [Tìm kiếm trợ giúp trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#5-tìm-kiếm-trợ-giúp-trong-linux) | Hướng dẫn cách tra cứu tài liệu lệnh bằng `man`, `--help`, `-h`, `apropos` và explainshell. |
| 6 | [Điều hướng trong hệ thống tệp](/Linux_Fundamentals/Linux_Fundamentals.md#6-điều-hướng-trong-hệ-thống-tệp) | Trình bày cách di chuyển trong hệ thống tệp bằng `pwd`, `ls`, `cd`, đường dẫn tuyệt đối/tương đối và phím `TAB`. |
| 7 | [Làm việc với tệp và thư mục](/Linux_Fundamentals/Linux_Fundamentals.md#7-làm-việc-với-tệp-và-thư-mục) | Hướng dẫn tạo, sao chép, di chuyển, đổi tên, xóa tệp/thư mục và kiểm tra loại tệp. |
| 8 | [Xem và chỉnh sửa nội dung tệp](/Linux_Fundamentals/Linux_Fundamentals.md#8-xem-và-chỉnh-sửa-nội-dung-tệp) | Giới thiệu các lệnh xem nội dung tệp như `cat`, `head`, `tail`, `less`, `more` và trình soạn thảo `nano`, `vim`. |
| 9 | [Tìm kiếm tệp và thư mục](/Linux_Fundamentals/Linux_Fundamentals.md#9-tìm-kiếm-tệp-và-thư-mục) | Hướng dẫn tìm chương trình, tệp và thư mục bằng `which`, `find`, `locate` và `updatedb`. |
| 10 | [Bộ mô tả tệp và chuyển hướng dữ liệu](/Linux_Fundamentals/Linux_Fundamentals.md#10-bộ-mô-tả-tệp-và-chuyển-hướng-dữ-liệu) | Giải thích STDIN, STDOUT, STDERR, chuyển hướng dữ liệu với `>`, `>>`, `2>`, `<`, `<< EOF` và pipe `|`. |
| 11 | [Lọc và xử lý nội dung văn bản](/Linux_Fundamentals/Linux_Fundamentals.md#11-lọc-và-xử-lý-nội-dung-văn-bản) | Trình bày các công cụ xử lý văn bản như `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`, `nl`, `diff` và `jq`. |
| 12 | [Biểu thức chính quy trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#12-biểu-thức-chính-quy-trong-linux) | Giới thiệu Regex và cách ứng dụng với `grep`, `sed`, `awk` để tìm kiếm, lọc và xử lý dữ liệu văn bản. |
| 13 | [Quyền truy cập trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#13-quyền-truy-cập-trong-linux) | Giải thích quyền `read`, `write`, `execute`, user/group/others, `chmod`, `chown`, `chgrp` và các rủi ro bảo mật. |
| 14 | [Quản lý người dùng và nhóm](/Linux_Fundamentals/Linux_Fundamentals.md#14-quản-lý-người-dùng-và-nhóm) | Hướng dẫn quản lý user, group, kiểm tra thông tin người dùng, dùng `su`, `sudo`, tạo/xóa user và quản lý nhóm đặc quyền. |
| 15 | [Kết nối và quản trị từ xa](/Linux_Fundamentals/Linux_Fundamentals.md#15-kết-nối-và-quản-trị-từ-xa) | Giới thiệu SSH, cách đăng nhập máy Linux từ xa và truyền tệp an toàn bằng SCP. |
| 16 | [Tải xuống và chia sẻ tệp trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#16-tải-xuống-và-chia-sẻ-tệp-trong-linux) | Hướng dẫn tải tệp bằng `wget`, `curl`, chia sẻ tệp bằng Python HTTP Server và so sánh với `scp`. |
| 17 | [Nén, giải nén và lưu trữ dữ liệu](/Linux_Fundamentals/Linux_Fundamentals.md#17-nén-giải-nén-và-lưu-trữ-dữ-liệu) | Trình bày khái niệm archive/compression và cách dùng `tar`, `gzip`, `gunzip` để nén, giải nén và sao lưu dữ liệu. |
| 18 | [Quản lý tiến trình](/Linux_Fundamentals/Linux_Fundamentals.md#18-quản-lý-tiến-trình) | Giải thích process, PID, cách xem tiến trình bằng `ps`, `top`, kết thúc tiến trình bằng `kill` và quản lý foreground/background. |
| 19 | [Quản lý dịch vụ trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#19-quản-lý-dịch-vụ-trong-linux) | Hướng dẫn quản lý dịch vụ bằng `systemd` và `systemctl`, gồm start, stop, enable, disable, status và ý nghĩa bảo mật. |
| 20 | [Quản lý gói phần mềm](/Linux_Fundamentals/Linux_Fundamentals.md#20-quản-lý-gói-phần-mềm) | Giới thiệu package manager và cách quản lý phần mềm trên Debian/Ubuntu bằng APT. |
| 21 | [Tự động hóa và lập lịch tác vụ](/Linux_Fundamentals/Linux_Fundamentals.md#21-tự-động-hóa-và-lập-lịch-tác-vụ) | Hướng dẫn tự động hóa công việc với `cron`, `crontab`, `at`, `nohup` và ứng dụng trong quản trị hệ thống. |
| 22 | [Log trong Linux](/Linux_Fundamentals/Linux_Fundamentals.md#22-log-trong-linux) | Trình bày khái niệm log, thư mục `/var/log`, các tệp log quan trọng và cách phân tích log phục vụ SOC/điều tra sự cố. |
| 23 | [Bash Scripting cơ bản](/Linux_Fundamentals/Linux_Fundamentals.md#23-bash-scripting-cơ-bản) | Giới thiệu Bash script, shebang, cách chạy script, cấp quyền thực thi, chú thích và gỡ lỗi script. |
| 24 | [Biến và tham số trong Bash](/Linux_Fundamentals/Linux_Fundamentals.md#24-biến-và-tham-số-trong-bash) | Hướng dẫn khai báo biến, sử dụng tham số dòng lệnh, `$0`, `$1`, `$#`, `$@`, `$?` và nhập dữ liệu với `read`. |
| 25 | [Mảng trong Bash](/Linux_Fundamentals/Linux_Fundamentals.md#25-mảng-trong-bash) | Trình bày cách khai báo mảng, truy cập phần tử, in toàn bộ mảng, thay đổi giá trị và xóa phần tử bằng `unset`. |
| 26 | [Câu điều kiện trong Bash](/Linux_Fundamentals/Linux_Fundamentals.md#26-câu-điều-kiện-trong-bash) | Hướng dẫn dùng `if`, `then`, `else`, `fi`, so sánh số, chuỗi, kiểm tra tệp/thư mục và kết hợp nhiều điều kiện. |

---

## [Section 2: Windows Fundamentals and Active Directory Basics](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md)

| STT | Nội dung chính | Mô tả |
|---|---|---|
| 1 | [Tổng quan về hệ điều hành Windows](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#1-tổng-quan-về-hệ-điều-hành-windows) | Giới thiệu khái niệm Windows, vai trò của Windows trong máy tính cá nhân, doanh nghiệp và an toàn thông tin. |
| 2 | [Giao diện Desktop của Windows](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#2-giao-diện-desktop-của-windows) | Trình bày các thành phần cơ bản của giao diện Windows như Desktop, Start Menu, Taskbar và khu vực thông báo. |
| 3 | [Hệ thống tệp trong Windows](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#3-hệ-thống-tệp-trong-windows) | Giải thích các hệ thống tệp phổ biến trong Windows, đặc biệt là NTFS và ý nghĩa bảo mật của quyền truy cập tệp. |
| 4 | [Thư mục hệ thống Windows](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#4-thư-mục-hệ-thống-windows) | Mô tả các thư mục quan trọng như `C:\Windows`, `%windir%`, `System32` và các công cụ hệ thống thường gặp. |
| 5 | [Tài khoản người dùng, hồ sơ và quyền](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#5-tài-khoản-người-dùng-hồ-sơ-và-quyền) | Trình bày tài khoản người dùng, hồ sơ cá nhân, nhóm quyền và nguyên tắc phân quyền trong Windows. |
| 6 | [User Account Control — UAC](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#6-user-account-control--uac) | Giải thích cơ chế UAC, quyền nâng cao, UAC Prompt và vai trò của UAC trong bảo vệ hệ thống. |
| 7 | [Settings và Control Panel](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#7-settings-và-control-panel) | So sánh Windows Settings và Control Panel, đồng thời hướng dẫn khi nào nên sử dụng từng công cụ. |
| 8 | [Task Manager](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#8-task-manager) | Giới thiệu công cụ quản lý tiến trình, theo dõi tài nguyên và xử lý ứng dụng bị treo trong Windows. |
| 9 | [System Configuration — MSConfig](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#9-system-configuration--msconfig) | Trình bày công cụ MSConfig dùng để cấu hình khởi động, dịch vụ và hỗ trợ khắc phục sự cố hệ thống. |
| 10 | [Computer Management](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#10-computer-management) | Tổng hợp các công cụ quản trị như Task Scheduler, Event Viewer, Disk Management, Services và Local Users and Groups. |
| 11 | [Task Scheduler](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#11-task-scheduler) | Giới thiệu cách tạo và quản lý tác vụ tự động, cùng ý nghĩa bảo mật của Scheduled Tasks. |
| 12 | [Event Viewer và Windows Logs](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#12-event-viewer-và-windows-logs) | Trình bày Event Viewer, các loại Windows Logs và vai trò của log trong điều tra sự cố bảo mật. |
| 13 | [System Information](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#13-system-information) | Hướng dẫn xem thông tin phần cứng, phần mềm, môi trường hệ thống và biến môi trường bằng `msinfo32`. |
| 14 | [Resource Monitor](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#14-resource-monitor) | Giới thiệu công cụ theo dõi chi tiết CPU, RAM, Disk, Network và phân tích tiến trình bất thường. |
| 15 | [Command Prompt](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#15-command-prompt) | Trình bày CMD và các lệnh cơ bản như `hostname`, `whoami`, `ipconfig`, `netstat`, `net user`. |
| 16 | [Windows Registry](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#16-windows-registry) | Giải thích Registry, cấu trúc hive/key/value, công cụ `regedit` và ý nghĩa bảo mật của Registry. |
| 17 | [Windows Update](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#17-windows-update) | Trình bày vai trò của Windows Update, bản vá bảo mật, Feature Updates và Patch Tuesday. |
| 18 | [Windows Security](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#18-windows-security) | Giới thiệu trung tâm bảo mật Windows Security và các khu vực bảo vệ chính của hệ thống. |
| 19 | [Virus & Threat Protection](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#19-virus--threat-protection) | Trình bày chức năng quét, phát hiện, cách ly và xử lý virus, malware bằng Microsoft Defender. |
| 20 | [Firewall & Network Protection](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#20-firewall--network-protection) | Giải thích Windows Firewall, network profile và cách kiểm soát kết nối mạng trong Windows. |
| 21 | [App & Browser Control](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#21-app--browser-control) | Trình bày SmartScreen, Exploit Protection và cơ chế bảo vệ khi chạy ứng dụng hoặc truy cập web. |
| 22 | [Device Security](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#22-device-security) | Giới thiệu các tính năng bảo mật thiết bị như TPM, Secure Boot, Core Isolation và Memory Integrity. |
| 23 | [BitLocker](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#23-bitlocker) | Trình bày cơ chế mã hóa ổ đĩa BitLocker và vai trò của nó trong bảo vệ dữ liệu. |
| 24 | [Volume Shadow Copy Service — VSS](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#24-volume-shadow-copy-service--vss) | Giải thích VSS, bản sao bóng và vai trò của VSS trong sao lưu, khôi phục và điều tra bảo mật. |
| 25 | [Tổng quan về Windows Domains](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#25-tổng-quan-về-windows-domains) | Giới thiệu khái niệm Windows Domain và vai trò của domain trong quản lý tập trung doanh nghiệp. |
| 26 | [Active Directory cơ bản](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#26-active-directory-cơ-bản) | Trình bày các khái niệm nền tảng của Active Directory như domain, domain controller, object và directory service. |
| 27 | [Nhóm bảo mật trong Active Directory](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#27-nhóm-bảo-mật-trong-active-directory) | Giải thích security groups và cách sử dụng nhóm để quản lý quyền trong môi trường Active Directory. |
| 28 | [Organizational Units — OUs](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#28-organizational-units--ous) | Trình bày OU và cách tổ chức người dùng, máy tính, nhóm theo cấu trúc quản trị trong domain. |
| 29 | [Quản lý người dùng trong Active Directory](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#29-quản-lý-người-dùng-trong-active-directory) | Hướng dẫn các thao tác cơ bản khi quản lý tài khoản người dùng trong Active Directory. |
| 30 | [Quản lý máy tính trong Active Directory](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#30-quản-lý-máy-tính-trong-active-directory) | Trình bày cách quản lý computer objects và vai trò của máy tính domain trong hệ thống doanh nghiệp. |
| 31 | [Group Policy](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#31-group-policy) | Giới thiệu Group Policy và cách áp dụng chính sách tập trung cho người dùng, máy tính trong domain. |
| 32 | [Triển khai chính sách bảo mật bằng GPO](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#32-triển-khai-chính-sách-bảo-mật-bằng-gpo) | Trình bày cách dùng GPO để triển khai các chính sách bảo mật như mật khẩu, khóa tài khoản và cấu hình hệ thống. |
| 33 | [Phương thức xác thực trong Windows Domain](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#33-phương-thức-xác-thực-trong-windows-domain) | Giới thiệu các phương thức xác thực trong Windows Domain và vai trò của xác thực trong bảo mật doanh nghiệp. |
| 34 | [Kerberos Authentication](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#34-kerberos-authentication) | Giải thích cơ chế xác thực Kerberos, vé xác thực và vai trò của Kerberos trong Active Directory. |
| 35 | [NetNTLM Authentication](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#35-netntlm-authentication) | Trình bày cơ chế NetNTLM, cách hoạt động và các rủi ro bảo mật liên quan đến xác thực NTLM. |
| 36 | [Trees, Forests và Trusts](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#36-trees-forests-và-trusts) | Giải thích các khái niệm tree, forest và trust trong Active Directory để hiểu cấu trúc domain lớn. |
| 37 | [Công cụ quản trị Windows cần nhớ](/Windows_Fundamentals_and_Active_Directory_Basics/Windows_Fundamentals_and_Active_Directory_Basics.md#37-công-cụ-quản-trị-windows-cần-nhớ) | Tổng hợp các công cụ quản trị Windows quan trọng như `control.exe`, `taskmgr.exe`, `eventvwr.msc`, `regedit.exe` và `gpmc.msc`. |



---

## [Section 5: Networking](./5_Networking/)
>Tìm hiểu về mô hình OSI và các tầng mạng TCP/IP. Khám phá các giao thức mạng rõ văn bản và bảo mật mà chúng ta sử dụng hàng ngày.

1. [Networking Concepts](./5_Networking/1_Networking_Concepts.md)
>Tìm hiểu về mô hình OSI của ISO và bộ giao thức TCP/IP.

2. [Networking Essentials](./5_Networking/2_Networking_Essentials.md)  
>Khám phá các giao thức mạng từ cấu hình tự động đến định tuyến gói tin tới đích.

3. [Networking Core Protocols](./5_Networking/3_Networking_Core_Protocols.md)  
>Tìm hiểu về các giao thức lõi của TCP/IP.

4. [Networking Secure Protocols](./5_Networking/4_Networking_Secure_Protocols.md)
>Tìm hiểu cách TLS, SSH và VPN có thể bảo mật lưu lượng mạng của bạn.

5. [Wireshark: The Basics](./5_Networking/5_Wireshark_The_Basics.md)
>Học các kiến thức cơ bản về Wireshark và cách phân tích giao thức cùng các tệp PCAP.

6. [Tcpdump: The Basics](./5_Networking/6_tcpdump_the_basics.md)
>Học cách sử dụng Tcpdump để lưu, lọc và hiển thị các gói tin.

7. [Nmap: The Basics](./5_Networking/7_Nmap_The_Basics.md)  
>Học cách sử dụng Nmap để phát hiện các máy đang hoạt động, tìm cổng mở và xác định phiên bản dịch vụ.

---

## [Section 6: Cryptography](./6_Cryptography/)
>Khám phá các thuật toán mã hóa đối xứng và bất đối xứng khác nhau. Tìm hiểu cách sử dụng các thuật toán băm trong các hệ thống hàng ngày.

1. [Cryptography Basics](./6_Cryptography/1_Cryptography_Basics.md)
>Học các kiến thức cơ bản về mật mã học và mã hóa đối xứng.

2. [Public Key Cryptography Basics](./6_Cryptography/2_Public_Key_Cryptography_Basics.md)
>Khám phá cách thức hoạt động của các thuật toán mã hóa khóa công khai như RSA và tìm hiểu vai trò của chúng trong các ứng dụng như SSH.

3. [Hashing Basics](./6_Cryptography/3_Hashing_Basics.md) 
>Tìm hiểu về các hàm băm và cách chúng được sử dụng trong việc xác minh mật khẩu và kiểm tra tính toàn vẹn của tệp.

4. [John the Ripper: The Basics](./6_Cryptography/4_John_the_Ripper_The_Basics.md)  
>Học cách sử dụng John the Ripper, một công cụ bẻ khóa hash mạnh mẽ và linh hoạt.

---

## [Section 7: Exploitation Basics](./7_Exploitation_Basics/)
>Khám phá nghệ thuật khai thác bằng cách tận dụng một lỗ hổng thực tế. Tiếp theo, tìm hiểu các tính năng khai thác của framework Metasploit.

1. [Moniker Link (CVE-2024-21413)](./7_Exploitation_Basics/1_Moniker_Link.md)  
>Rò rỉ thông tin xác thực của người dùng bằng cách sử dụng CVE-2024-21413 để vượt qua chế độ Protected View của Outlook.

2. [Metasploit: Introduction](./7_Exploitation_Basics/2_Metasploit_Introduction.md) 
>Giới thiệu về các thành phần chính của Metasploit Framework.

3. [Metasploit: Exploitation](./7_Exploitation_Basics/3_Metasploit_Exploitation.md)  
>Sử dụng Metasploit để quét, đánh giá lỗ hổng bảo mật và khai thác.

4. [Metasploit: Meterpreter](./7_Exploitation_Basics/4_Metasploit_Meterpreter.md)  
>Tìm hiểu chuyên sâu về Meterpreter và cách các payload chạy trong bộ nhớ có thể được sử dụng cho các hoạt động hậu khai thác.

5. [Blue](./7_Exploitation_Basics/5_Blue.md)  
>Triển khai và tấn công vào một máy Windows, khai thác các vấn đề cấu hình sai phổ biến.

---

## [Section 8: Web Hacking](./8_Web_Hacking/)
>Tìm hiểu về các ứng dụng web, JavaScript và SQL. Khám phá BurpSuite, một nền tảng kiểm thử bảo mật ứng dụng web, và OWASP Top Ten.

1. [Web Application Basics](./8_Web_Hacking/1_Web_Application_Basics.md)
>Học những kiến thức cơ bản về ứng dụng web: HTTP, URL, phương thức request, mã phản hồi và header.

2. [JavaScript Essentials](./8_Web_Hacking/2_JavaScript_Essentials.md)  
>Học cách sử dụng JavaScript để thêm tính tương tác vào một website và hiểu các lỗ hổng liên quan.

3. [SQL Fundamentals](./8_Web_Hacking/3_SQL_Fundamentals.md)  
>Học cách thực hiện các truy vấn SQL cơ bản để truy xuất và quản lý dữ liệu trong cơ sở dữ liệu.

4. [Burp Suite: The Basics](./8_Web_Hacking/4_Burp_Suite_The_Basics.md)  
>Giới thiệu cách sử dụng Burp Suite cho việc kiểm thử bảo mật ứng dụng web.

- OWASP Top 10 - 2021  
>Tìm hiểu và khai thác từng lỗ hổng trong OWASP Top 10; 10 rủi ro bảo mật web quan trọng nhất.

---

## **Section 9: Offensive Security Tooling**

- Hydra  
- Gobuster: The Basics  
- Shells Overview  
- SQLMap: The Basics  

---

## **Section 10: Defensive Security**

- Defensive Security Intro  
- SOC Fundamentals  
- Digital Forensics Fundamentals  
- Incident Response Fundamentals  
- Logs Fundamentals  

---

## **Section 11: Security Solutions**

- Introduction to SIEM  
- Firewall Fundamentals  
- IDS Fundamentals  
- Vulnerability Scanner Overview  

---

## **Section 12: Defensive Security Tooling**

- CyberChef: The Basics  
- CAPA: The Basics  
- REMnux: Getting Started  
- FlareVM: Arsenal of Tools  

---

## **Section 13: Build Your Cyber Security Career**

- Security Principles  
- Careers in Cyber  
- Training Impact on Teams  
