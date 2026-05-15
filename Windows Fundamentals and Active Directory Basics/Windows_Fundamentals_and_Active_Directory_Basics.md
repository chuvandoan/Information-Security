# Windows Fundamentals and Active Directory Basics

## Mục lục

1. [Tổng quan về hệ điều hành Windows](#1-tổng-quan-về-hệ-điều-hành-windows)



## Nội dung

# 1. Tổng quan về hệ điều hành Windows

## 1.1. Windows là gì?

![](./img/1.1_windows.png)

Windows là một hệ điều hành do Microsoft phát triển, được sử dụng rộng rãi trên máy tính cá nhân, máy tính xách tay, máy trạm và máy chủ trong môi trường doanh nghiệp. Hệ điều hành Windows cung cấp giao diện để người dùng tương tác với phần cứng, phần mềm, tệp tin, thiết bị ngoại vi và các dịch vụ hệ thống.

Windows không chỉ là một môi trường làm việc đồ họa quen thuộc với người dùng phổ thông, mà còn là nền tảng quan trọng trong các hệ thống doanh nghiệp. Trong thực tế, nhiều tổ chức sử dụng Windows để quản lý người dùng, máy tính, tài nguyên mạng, chính sách bảo mật và các dịch vụ nội bộ.

Một hệ điều hành Windows thường bao gồm nhiều thành phần khác nhau như:

- giao diện người dùng đồ họa;
- hệ thống tệp;
- tài khoản người dùng và quyền truy cập;
- công cụ quản trị hệ thống;
- dịch vụ nền;
- cơ chế bảo mật;
- công cụ giám sát và xử lý sự cố.

Vì vậy, để sử dụng và quản trị Windows hiệu quả, người học cần hiểu không chỉ giao diện bên ngoài mà còn cả các thành phần hệ thống bên trong.


## 1.2. Vai trò của Windows trong máy tính cá nhân và doanh nghiệp

Trong máy tính cá nhân, Windows đóng vai trò là môi trường làm việc chính cho người dùng. Người dùng có thể sử dụng Windows để thực hiện các công việc hằng ngày như soạn thảo tài liệu, duyệt web, cài đặt phần mềm, lưu trữ dữ liệu, kết nối mạng và sử dụng các thiết bị ngoại vi.

Trong môi trường doanh nghiệp, vai trò của Windows rộng hơn rất nhiều. Windows thường được sử dụng trên máy trạm của nhân viên, máy chủ nội bộ và các hệ thống quản trị tập trung. Doanh nghiệp có thể sử dụng Windows để quản lý tài khoản người dùng, phân quyền truy cập, triển khai chính sách bảo mật, giám sát hoạt động hệ thống và bảo vệ dữ liệu quan trọng.

Một số vai trò quan trọng của Windows trong doanh nghiệp gồm:

- cung cấp môi trường làm việc cho nhân viên;
- quản lý tài khoản người dùng và nhóm;
- kiểm soát quyền truy cập vào tệp, thư mục và tài nguyên mạng;
- hỗ trợ quản trị tập trung thông qua Windows Server và Active Directory;
- ghi nhận nhật ký sự kiện phục vụ giám sát và điều tra sự cố;
- cung cấp các công cụ bảo mật như Windows Security, Windows Defender Firewall và BitLocker.

Do được sử dụng phổ biến trong doanh nghiệp, Windows cũng trở thành một mục tiêu quan trọng đối với các cuộc tấn công mạng. Vì vậy, hiểu rõ Windows là nền tảng cần thiết đối với quản trị viên hệ thống và chuyên viên an toàn thông tin.


### 1.3. Vì sao cần học Windows trong an toàn thông tin?

Windows là một trong những hệ điều hành phổ biến nhất trong môi trường doanh nghiệp. Nhiều máy trạm, máy chủ, hệ thống xác thực và tài nguyên nội bộ được xây dựng trên nền tảng Windows. Vì vậy, đối với lĩnh vực an toàn thông tin, việc hiểu Windows là điều rất quan trọng.

Người làm an toàn thông tin cần học Windows vì các lý do sau:

- Windows thường là mục tiêu của mã độc, tấn công lừa đảo, leo thang đặc quyền và khai thác cấu hình sai.
- Nhiều sự kiện bảo mật quan trọng được ghi lại trong Windows Event Logs.
- Các cơ chế như User Account Control, NTFS Permissions, Windows Defender Firewall và BitLocker ảnh hưởng trực tiếp đến mức độ an toàn của hệ thống.
- Active Directory, một thành phần quan trọng trong doanh nghiệp, hoạt động dựa trên nền tảng Windows Server.
- Kẻ tấn công thường lợi dụng các công cụ hợp pháp có sẵn trong Windows để ẩn hành vi độc hại.

Đối với một SOC Analyst, kiến thức Windows giúp phân tích log, phát hiện hành vi bất thường, điều tra sự cố và hiểu rõ cách kẻ tấn công di chuyển trong hệ thống. Đối với quản trị viên hệ thống, kiến thức này giúp cấu hình máy tính an toàn hơn, quản lý người dùng hiệu quả hơn và giảm thiểu rủi ro bảo mật.

Nói cách khác, học Windows là bước nền tảng để hiểu cách hệ thống doanh nghiệp vận hành và cách bảo vệ hệ thống đó trước các mối đe dọa mạng.


## 1.4. Lịch sử phát triển của Windows

Windows có lịch sử phát triển lâu dài, bắt đầu từ năm 1985. Qua nhiều phiên bản khác nhau, Windows dần trở thành hệ điều hành phổ biến trong cả môi trường cá nhân và doanh nghiệp.

Một số phiên bản Windows có ảnh hưởng lớn gồm Windows XP, Windows Vista, Windows 7, Windows 8, Windows 10 và Windows 11. Trong đó, Windows XP từng là một phiên bản rất phổ biến và được sử dụng trong thời gian dài. Tuy nhiên, khi Microsoft thông báo kết thúc hỗ trợ Windows XP, nhiều tổ chức phải nhanh chóng chuyển sang các phiên bản mới hơn để đảm bảo khả năng tương thích và an toàn.

Windows Vista là một phiên bản có nhiều thay đổi lớn, nhưng không được người dùng đón nhận tốt. Sau đó, Windows 7 được phát hành và trở thành một phiên bản ổn định, phổ biến trong nhiều năm. Windows 8 và Windows 8.1 xuất hiện sau đó, nhưng không để lại ảnh hưởng lâu dài như Windows 7.

Windows 10 đánh dấu một giai đoạn quan trọng khi Microsoft tập trung nhiều hơn vào bảo mật, cập nhật hệ thống và trải nghiệm người dùng. Sau đó, Windows 11 được giới thiệu với giao diện hiện đại hơn và nhiều yêu cầu bảo mật phần cứng cao hơn.

Qua từng phiên bản, Microsoft liên tục cải thiện Windows về khả năng sử dụng, tính ổn định và bảo mật. Tuy nhiên, do Windows được sử dụng rất rộng rãi, nó vẫn luôn là mục tiêu hấp dẫn đối với tin tặc và phần mềm độc hại.


## 1.5. Các phiên bản Windows phổ biến

Windows có nhiều phiên bản khác nhau, phục vụ các nhóm người dùng và mục đích sử dụng khác nhau. Đối với người dùng cá nhân, các phiên bản thường gặp là Windows Home và Windows Pro. Đối với doanh nghiệp và hệ thống máy chủ, Microsoft cung cấp các phiên bản Windows Server.

Một số phiên bản Windows phổ biến gồm:

| Phiên bản | Mục đích sử dụng chính |
|---|---|
| Windows XP | Phiên bản cũ, từng được sử dụng rất rộng rãi |
| Windows 7 | Phiên bản ổn định, phổ biến trong cá nhân và doanh nghiệp |
| Windows 8 / 8.1 | Phiên bản hướng nhiều hơn đến thiết bị cảm ứng |
| Windows 10 | Phiên bản phổ biến cho máy tính cá nhân và doanh nghiệp |
| Windows 11 | Phiên bản hiện đại hơn, chú trọng giao diện và bảo mật |
| Windows Server | Dùng cho máy chủ và môi trường doanh nghiệp |

Windows dành cho người dùng cuối thường tập trung vào trải nghiệm sử dụng, giao diện đồ họa, ứng dụng văn phòng và các tính năng cá nhân. Trong khi đó, Windows Server tập trung vào quản trị hệ thống, dịch vụ mạng, quản lý người dùng, chia sẻ tài nguyên và triển khai các dịch vụ doanh nghiệp.

Việc phân biệt các phiên bản Windows là cần thiết vì mỗi phiên bản có tính năng, quyền quản trị và khả năng bảo mật khác nhau.


## 1.6. Windows Desktop và Windows Server

Windows Desktop là nhóm hệ điều hành Windows được thiết kế chủ yếu cho người dùng cá nhân, nhân viên văn phòng và máy trạm trong doanh nghiệp. Các phiên bản như Windows 10 hoặc Windows 11 thường thuộc nhóm này. Chúng cung cấp giao diện đồ họa thân thiện, hỗ trợ ứng dụng văn phòng, trình duyệt, phần mềm làm việc và các công cụ cá nhân.

Windows Server là hệ điều hành được thiết kế cho máy chủ. Nó thường được sử dụng để cung cấp dịch vụ cho nhiều người dùng hoặc nhiều máy tính trong mạng. Windows Server có thể đảm nhiệm các vai trò như máy chủ xác thực, máy chủ tệp, máy chủ web, máy chủ DNS, DHCP hoặc Domain Controller trong môi trường Active Directory.

Có thể so sánh ngắn gọn như sau:

| Tiêu chí | Windows Desktop | Windows Server |
|---|---|---|
| Đối tượng sử dụng | Người dùng cá nhân, nhân viên, máy trạm | Doanh nghiệp, quản trị viên, máy chủ |
| Mục đích chính | Làm việc hằng ngày, chạy ứng dụng người dùng | Cung cấp dịch vụ mạng và quản trị tập trung |
| Giao diện | Tối ưu cho người dùng cuối | Tối ưu cho quản trị và dịch vụ |
| Vai trò trong mạng | Máy khách hoặc máy trạm | Máy chủ cung cấp dịch vụ |
| Ví dụ | Windows 10, Windows 11 | Windows Server 2019 |

Trong các hệ thống doanh nghiệp, Windows Desktop và Windows Server thường hoạt động cùng nhau. Máy trạm của người dùng chạy Windows Desktop, còn các dịch vụ trung tâm như Active Directory, DNS, DHCP hoặc File Server thường chạy trên Windows Server.


## 1.7. Sự khác nhau giữa Windows Home và Windows Pro

Windows Home và Windows Pro đều là phiên bản dành cho người dùng cuối, nhưng Windows Pro có nhiều tính năng nâng cao hơn, đặc biệt phù hợp với môi trường doanh nghiệp nhỏ, người dùng kỹ thuật và các hệ thống cần quản lý bảo mật tốt hơn.

Windows Home thường phù hợp với người dùng cá nhân, học tập, giải trí và các nhu cầu cơ bản. Trong khi đó, Windows Pro cung cấp thêm các tính năng quản trị, bảo mật và kết nối doanh nghiệp.

Một số điểm khác nhau chính:

| Tiêu chí | Windows Home | Windows Pro |
|---|---|---|
| Đối tượng sử dụng | Người dùng cá nhân | Người dùng chuyên nghiệp, doanh nghiệp nhỏ |
| BitLocker | Không hỗ trợ đầy đủ | Có hỗ trợ BitLocker |
| Remote Desktop Host | Không hỗ trợ đầy đủ | Có thể dùng để nhận kết nối Remote Desktop |
| Group Policy | Hạn chế | Hỗ trợ tốt hơn |
| Tham gia domain | Không phù hợp | Hỗ trợ tham gia domain |
| Quản trị doanh nghiệp | Ít tính năng hơn | Nhiều tính năng hơn |

Một điểm khác biệt quan trọng là Windows Pro hỗ trợ BitLocker Drive Encryption. Đây là tính năng mã hóa ổ đĩa giúp bảo vệ dữ liệu trong trường hợp thiết bị bị mất, bị đánh cắp hoặc ổ đĩa bị tháo ra khỏi máy.

Vì vậy, trong môi trường cần bảo mật dữ liệu, quản lý người dùng hoặc kết nối vào hệ thống doanh nghiệp, Windows Pro thường phù hợp hơn Windows Home.


## 1.8. Windows Server trong môi trường doanh nghiệp

Windows Server là nền tảng quan trọng trong nhiều hệ thống doanh nghiệp. Khác với Windows Desktop, Windows Server được thiết kế để cung cấp dịch vụ cho nhiều người dùng, nhiều máy tính và nhiều hệ thống khác nhau trong mạng.

Trong môi trường doanh nghiệp, Windows Server có thể đảm nhiệm nhiều vai trò như:

- Domain Controller;
- Active Directory Domain Services;
- DNS Server;
- DHCP Server;
- File Server;
- Print Server;
- Web Server;
- Remote Desktop Services;
- hệ thống quản lý chính sách bảo mật.

Một trong những vai trò quan trọng nhất của Windows Server là triển khai Active Directory. Active Directory cho phép doanh nghiệp quản lý tập trung người dùng, máy tính, nhóm, chính sách bảo mật và quyền truy cập. Thay vì phải cấu hình từng máy tính riêng lẻ, quản trị viên có thể quản lý toàn bộ hệ thống từ một nơi trung tâm.

Windows Server cũng đóng vai trò quan trọng trong bảo mật doanh nghiệp. Thông qua Windows Server và Active Directory, tổ chức có thể áp dụng chính sách mật khẩu, giới hạn quyền người dùng, kiểm soát truy cập tài nguyên, ghi log sự kiện và triển khai các chính sách bảo vệ hệ thống.

Đối với người học an toàn thông tin, Windows Server là nền tảng cần nắm vững vì nhiều cuộc tấn công trong doanh nghiệp thường liên quan đến Active Directory, tài khoản domain, quyền quản trị, dịch vụ mạng và cấu hình sai trên máy chủ Windows.

