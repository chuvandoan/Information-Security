# Windows Fundamentals and Active Directory Basics

## Mục lục

1. [Tổng quan về hệ điều hành Windows](#1-tổng-quan-về-hệ-điều-hành-windows)

2. [Giao diện Desktop của Windows](#2-giao-diện-desktop-của-windows)

3. [Hệ thống tệp trong Windows](#3-hệ-thống-tệp-trong-windows)

4. [Thư mục hệ thống Windows](#4-thư-mục-hệ-thống-windows)

5. [Tài khoản người dùng, hồ sơ và quyền](#5-tài-khoản-người-dùng-hồ-sơ-và-quyền)

6. [User Account Control — UAC](#6-user-account-control--uac)

7. [Settings và Control Panel](#7-settings-và-control-panel)

8. [Task Manager](#8-task-manager)

9. [System Configuration — MSConfig](#9-system-configuration--msconfig)

10. [Computer Management](#10-computer-management)

11. [Task Scheduler](#11-task-scheduler)

12. [Event Viewer và Windows Logs](#12-event-viewer-và-windows-logs)

13. [System Information](#13-system-information)

14. [Resource Monitor](#14-resource-monitor)

15. [Command Prompt](#15-command-prompt)

16. [Windows Registry](#16-windows-registry)

17. [Windows Update](#17-windows-update)

18. [Windows Security](#18-windows-security)

19. [Virus & Threat Protection](#19-virus--threat-protection)

20. [Firewall & Network Protection](#20-firewall--network-protection)

21. [App & Browser Control](#21-app--browser-control)

22. [Device Security](#22-device-security)

23. [BitLocker](#23-bitlocker)

24. [Volume Shadow Copy Service — VSS](#24-volume-shadow-copy-service--vss)

25. [Tổng quan về Windows Domains](#25-tổng-quan-về-windows-domains)

26. [Active Directory cơ bản](#26-active-directory-cơ-bản)

27. [Nhóm bảo mật trong Active Directory](#27-nhóm-bảo-mật-trong-active-directory)

28. [Organizational Units — OUs](#28-organizational-units--ous)

29. [Quản lý người dùng trong Active Directory](#29-quản-lý-người-dùng-trong-active-directory)

30. [Quản lý máy tính trong Active Directory](#30-quản-lý-máy-tính-trong-active-directory)

31. [Group Policy](#31-group-policy)

32. [Triển khai chính sách bảo mật bằng GPO](#32-triển-khai-chính-sách-bảo-mật-bằng-gpo)

33. [Phương thức xác thực trong Windows Domain](#32-triển-khai-chính-sách-bảo-mật-bằng-gpo)

34. [Kerberos Authentication](#34-kerberos-authentication)

35. [NetNTLM Authentication](#35-netntlm-authentication)

36. [Trees, Forests và Trusts](#36-trees-forests-và-trusts)

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


## 1.3. Vì sao cần học Windows trong an toàn thông tin?

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

# 2. Giao diện Desktop của Windows

## 2.1. Windows Desktop là gì?

Windows Desktop là giao diện người dùng đồ họa của hệ điều hành Windows. Đây là màn hình chính xuất hiện sau khi người dùng đăng nhập thành công vào hệ thống.

Thông qua Desktop, người dùng có thể mở chương trình, truy cập tệp tin, thư mục, cài đặt hệ thống và các công cụ quản trị cơ bản. Thay vì phải nhập lệnh thủ công, Windows Desktop cho phép người dùng thao tác với hệ thống bằng chuột, bàn phím, biểu tượng và các cửa sổ đồ họa.

Trong môi trường Windows, Desktop không chỉ là nơi hiển thị hình nền, mà còn là khu vực làm việc trung tâm. Từ đây, người dùng có thể truy cập Start Menu, thanh tác vụ, khu vực thông báo, hộp tìm kiếm và các ứng dụng đang chạy.

Một giao diện Desktop Windows thông thường bao gồm các thành phần chính sau:

![](./img/2.1_windows_desktop.png)

1. màn hình Desktop;

1. Màn hình Desktop  
2. Menu Start  
3. Hộp tìm kiếm (Cortana)  
4. Chế độ xem tác vụ (Task View)  
5. Thanh tác vụ (Taskbar)  
6. Thanh công cụ (Toolbars)  
7. Khu vực thông báo (Notification Area)  

Việc hiểu rõ các thành phần này giúp người dùng thao tác với Windows nhanh hơn, đồng thời hỗ trợ quá trình quản trị và xử lý sự cố cơ bản.


## 2.2. Màn hình Desktop

Màn hình Desktop là khu vực làm việc chính của Windows. Đây là nơi người dùng thường đặt các biểu tượng, shortcut, thư mục hoặc tệp tin cần truy cập nhanh.

Ví dụ, trên Desktop có thể có các shortcut đến trình duyệt web, thư mục tài liệu, ứng dụng văn phòng hoặc các công cụ quản trị hệ thống. Người dùng có thể mở nhanh các đối tượng này bằng cách nhấp đúp chuột vào biểu tượng tương ứng.

Màn hình Desktop có thể được sắp xếp theo nhiều cách khác nhau. Người dùng có thể:

- thay đổi kích thước biểu tượng;
- sắp xếp biểu tượng theo tên, loại, ngày sửa đổi hoặc kích thước;
- tạo thư mục mới;
- tạo shortcut;
- sao chép hoặc dán tệp vào Desktop;
- thay đổi hình nền và giao diện hiển thị.

Khi nhấp chuột phải vào vùng trống trên Desktop, Windows sẽ hiển thị một menu ngữ cảnh. Menu này cho phép người dùng thực hiện nhiều thao tác nhanh như thay đổi cách hiển thị biểu tượng, tạo đối tượng mới, mở Display Settings hoặc mở Personalization.

Menu trên Desktop:

![](./img/2.2_menu.png)


Trong thực tế, Desktop thường được sử dụng để truy cập nhanh các tài nguyên quan trọng. Tuy nhiên, không nên lưu quá nhiều tệp quan trọng trực tiếp trên Desktop vì có thể gây khó quản lý, làm rối giao diện và tăng nguy cơ mất dữ liệu nếu hồ sơ người dùng gặp lỗi.


## 2.3. Start Menu

Start Menu là một trong những thành phần quan trọng nhất của giao diện Windows. Đây là nơi người dùng có thể truy cập ứng dụng, công cụ hệ thống, cài đặt, thư mục cá nhân và các tùy chọn nguồn như tắt máy hoặc khởi động lại.

Trong các phiên bản Windows hiện đại, Start Menu thường được mở bằng cách nhấp vào biểu tượng Windows ở góc dưới bên trái màn hình. Mặc dù giao diện Start Menu đã thay đổi qua từng phiên bản Windows, chức năng chính của nó vẫn là cung cấp điểm truy cập trung tâm đến các chương trình và tính năng của hệ điều hành.

Start Menu thường bao gồm các khu vực chính sau:

![](./img/2.3_menu_start.jpg)

- khu vực tài khoản người dùjpgng;
- lối tắt đến Documents, Pictures và Settings;
- nút Power để tắt máy, khởi động lại hoặc đăng xuất;
- danh sách ứng dụng đã cài đặt;
- khu vực các ô ứng dụng được ghim.

Người dùng có thể tìm kiếm ứng dụng trong Start Menu bằng cách cuộn danh sách ứng dụng hoặc nhập tên ứng dụng vào hộp tìm kiếm. Ngoài ra, có thể ghim các ứng dụng thường dùng vào Start Menu để truy cập nhanh hơn.

Trong quản trị hệ thống, Start Menu cũng là nơi thường dùng để mở các công cụ như Control Panel, Settings, Task Manager, Computer Management, Event Viewer hoặc Command Prompt.


## 2.4. Search Box

Search Box là hộp tìm kiếm trên Windows, thường nằm trên thanh tác vụ hoặc được tích hợp trong Start Menu. Công cụ này giúp người dùng tìm nhanh ứng dụng, tệp tin, thư mục, cài đặt hệ thống và một số nội dung khác trên máy tính.

![](./img/2.4_search_box.png)

Thay vì phải mở từng thư mục hoặc từng menu, người dùng có thể nhập từ khóa trực tiếp vào Search Box. Ví dụ:

- nhập `Control Panel` để mở Bảng điều khiển;
- nhập `Task Manager` để mở trình quản lý tác vụ;
- nhập `wallpaper` để tìm cài đặt hình nền;
- nhập tên ứng dụng để mở nhanh chương trình.

Search Box giúp tiết kiệm thời gian khi người dùng không nhớ chính xác vị trí của một công cụ trong hệ thống. Đây là cách rất hữu ích để truy cập nhanh các thiết lập Windows.

Trong một số trường hợp, người dùng có thể ẩn hoặc thay đổi cách hiển thị Search Box trên thanh tác vụ. Có thể nhấp chuột phải vào Taskbar, chọn phần Search và thay đổi chế độ hiển thị, ví dụ như hiển thị biểu tượng tìm kiếm hoặc ẩn hoàn toàn hộp tìm kiếm.


## 2.5. Task View

Task View là tính năng cho phép người dùng xem nhanh các cửa sổ và ứng dụng đang mở trên hệ thống. Tính năng này giúp chuyển đổi giữa các cửa sổ dễ dàng hơn, đặc biệt khi người dùng đang làm việc với nhiều ứng dụng cùng lúc.

![](./img/2.5_task_view_button.jpg)

Thông qua Task View, người dùng có thể:

- xem toàn bộ cửa sổ đang mở;
- chuyển nhanh sang một ứng dụng khác;
- quản lý nhiều không gian làm việc;
- tạo desktop ảo để tách các nhóm công việc khác nhau.

Ví dụ, người dùng có thể tạo một desktop ảo cho công việc học tập, một desktop khác cho trình duyệt, và một desktop khác cho công cụ quản trị hệ thống. Điều này giúp màn hình làm việc gọn gàng và dễ quản lý hơn.

Nút Task View thường nằm trên Taskbar. Nếu không sử dụng, người dùng có thể ẩn nút này bằng cách nhấp chuột phải vào Taskbar và bỏ chọn tùy chọn hiển thị Task View button.


## 2.6. Taskbar

Taskbar, hay thanh tác vụ, là thanh nằm ở phía dưới màn hình Windows theo mặc định. Đây là nơi hiển thị các ứng dụng đang mở, các ứng dụng được ghim, Start Menu, Search Box, Task View và khu vực thông báo.

![](./img/2.6_taskbar.png)

Taskbar giúp người dùng quản lý các chương trình đang chạy. Khi mở một ứng dụng, biểu tượng của ứng dụng đó sẽ xuất hiện trên Taskbar. Người dùng có thể nhấp vào biểu tượng để chuyển sang cửa sổ tương ứng.

Một số chức năng chính của Taskbar gồm:

- mở Start Menu;
- tìm kiếm ứng dụng và cài đặt;
- hiển thị ứng dụng đang chạy;
- chuyển đổi giữa các cửa sổ;
- ghim ứng dụng thường dùng;
- truy cập nhanh khu vực thông báo;
- mở Task Manager bằng menu chuột phải.

Khi di chuột qua biểu tượng ứng dụng đang mở, Windows có thể hiển thị hình thu nhỏ xem trước của cửa sổ đó. Điều này rất hữu ích khi có nhiều cửa sổ hoặc nhiều phiên bản của cùng một ứng dụng đang chạy.

Người dùng có thể tùy chỉnh Taskbar theo nhu cầu, ví dụ như ẩn Search Box, ẩn Task View, thay đổi vị trí thanh tác vụ hoặc ghim ứng dụng thường dùng để mở nhanh.


## 2.7. Toolbars

Toolbars là các thanh công cụ có thể được hiển thị trên Taskbar để cung cấp quyền truy cập nhanh đến một số vị trí hoặc chức năng cụ thể.

![](./img/2.7_toolbars.png)

Trong Windows, người dùng có thể bật hoặc tắt Toolbars bằng cách nhấp chuột phải vào Taskbar và chọn mục Toolbars. Tùy theo phiên bản Windows, các tùy chọn có thể khác nhau.

Toolbars có thể được dùng để truy cập nhanh vào:

- thư mục cụ thể;
- địa chỉ web;
- liên kết thường dùng;
- một số công cụ hệ thống.

Tuy nhiên, trong thực tế, Toolbars không phải là thành phần được sử dụng thường xuyên bởi mọi người dùng. Nhiều người thường chọn ghim ứng dụng trực tiếp vào Taskbar hoặc sử dụng Start Menu và Search Box để truy cập nhanh hơn.

Dù vậy, Toolbars vẫn là một phần của giao diện Windows và có thể hữu ích trong một số môi trường làm việc cần truy cập nhanh đến thư mục hoặc tài nguyên nhất định.


## 2.8. Notification Area

Notification Area là khu vực thông báo nằm ở góc dưới bên phải của màn hình Windows. Khu vực này thường hiển thị ngày giờ, trạng thái mạng, âm lượng, thông báo hệ thống và một số biểu tượng của ứng dụng chạy nền.

Các biểu tượng thường gặp trong Notification Area gồm:

- đồng hồ hệ thống;
- biểu tượng mạng hoặc Wi-Fi;
- biểu tượng âm lượng;
- biểu tượng pin trên máy tính xách tay;
- Windows Security;
- Action Center;
- biểu tượng của ứng dụng chạy nền.

Notification Area giúp người dùng theo dõi nhanh trạng thái hệ thống. Ví dụ, người dùng có thể kiểm tra máy có kết nối mạng hay không, âm lượng đang bật hay tắt, hệ thống có cảnh báo bảo mật hay có thông báo mới nào không.

Một số biểu tượng trong khu vực này có thể được ẩn hoặc hiển thị tùy theo cài đặt Taskbar. Người dùng có thể vào Taskbar settings để chọn biểu tượng nào được phép hiển thị trong Notification Area.

![](./img/2.8_taskbar_settings.png)

![](./img/2.8_notification_area.png)

Đối với người làm an toàn thông tin, Notification Area cũng có ý nghĩa nhất định vì nó có thể hiển thị trạng thái của Windows Security, phần mềm chống virus, VPN hoặc các công cụ bảo vệ hệ thống khác.


## 2.9. Cá nhân hóa giao diện Windows

Windows cho phép người dùng cá nhân hóa giao diện để phù hợp với sở thích và nhu cầu sử dụng. Việc cá nhân hóa có thể bao gồm thay đổi hình nền, màu sắc, chủ đề, phông chữ, màn hình khóa và cách hiển thị các thành phần giao diện.

Người dùng có thể mở phần cá nhân hóa bằng cách nhấp chuột phải vào Desktop và chọn Personalize. Từ đây, Windows sẽ mở giao diện cài đặt liên quan đến giao diện người dùng.

![](./img/2.9_personalize.png)

![](./img/2.9_personalize_interface.png)

Một số tùy chọn cá nhân hóa phổ biến gồm:

- thay đổi hình nền Desktop;
- thay đổi màu chủ đạo của hệ thống;
- chọn theme;
- cấu hình Lock Screen;
- thay đổi font;
- điều chỉnh Start Menu;
- điều chỉnh Taskbar.

Cá nhân hóa giao diện giúp người dùng làm việc thoải mái hơn. Tuy nhiên, trong môi trường doanh nghiệp, một số tùy chọn cá nhân hóa có thể bị hạn chế bởi chính sách quản trị, đặc biệt khi máy tính tham gia domain hoặc chịu sự quản lý của Group Policy.

Ví dụ, quản trị viên có thể áp dụng chính sách để cố định hình nền công ty, ẩn một số cài đặt hoặc hạn chế người dùng thay đổi giao diện hệ thống.


## 2.10. Display Settings

Display Settings là phần cài đặt liên quan đến màn hình hiển thị của Windows. Người dùng có thể mở Display Settings bằng cách nhấp chuột phải vào Desktop và chọn Display settings.

![](./img/2.10_display_settings.png)

![](./img/2.10_display_setting_interface.png)

Trong Display Settings, người dùng có thể cấu hình các tùy chọn như:

- độ phân giải màn hình;
- tỷ lệ hiển thị;
- hướng màn hình;
- độ sáng;
- nhiều màn hình;
- cách sắp xếp màn hình phụ;
- chế độ hiển thị khi dùng nhiều màn hình.

Độ phân giải màn hình ảnh hưởng trực tiếp đến độ sắc nét và không gian hiển thị. Nếu độ phân giải quá thấp, nội dung có thể bị to và chiếm nhiều diện tích. Nếu độ phân giải phù hợp, giao diện sẽ rõ ràng và dễ làm việc hơn.

Trong trường hợp sử dụng nhiều màn hình, Display Settings cho phép người dùng chọn cách hiển thị như:

- chỉ hiển thị trên một màn hình;
- nhân đôi màn hình;
- mở rộng màn hình;
- chọn màn hình chính.

Lưu ý rằng khi sử dụng Remote Desktop, một số tùy chọn hiển thị có thể bị giới hạn hoặc không thể thay đổi trực tiếp trên máy từ xa.

# 3. Hệ thống tệp trong Windows

## 3.1. Khái niệm hệ thống tệp

Hệ thống tệp là cơ chế mà hệ điều hành sử dụng để tổ chức, lưu trữ, quản lý và truy cập dữ liệu trên thiết bị lưu trữ như ổ cứng, SSD, USB hoặc thẻ nhớ.

![](./img/3.1_new_technology_file_system.png)

Nói đơn giản, hệ thống tệp quyết định cách tệp và thư mục được tạo, đặt tên, lưu trữ, đọc, ghi và bảo vệ trên ổ đĩa. Nếu không có hệ thống tệp, hệ điều hành sẽ không thể biết dữ liệu nằm ở đâu, thuộc về tệp nào và cần được truy cập như thế nào.

Trong Windows, hệ thống tệp có vai trò rất quan trọng vì nó ảnh hưởng trực tiếp đến:

- cách lưu trữ tệp và thư mục;
- giới hạn kích thước tệp;
- quyền truy cập của người dùng;
- khả năng khôi phục khi có lỗi;
- khả năng mã hóa và nén dữ liệu;
- mức độ bảo mật của hệ thống.

Các phiên bản Windows hiện đại chủ yếu sử dụng hệ thống tệp NTFS (New Technology File System). Trước NTFS, Windows từng sử dụng các hệ thống tệp như FAT16, FAT32 và HPFS.


## 3.2. FAT16, FAT32 và HPFS

Trước khi NTFS trở thành hệ thống tệp chính trong Windows hiện đại, Microsoft đã sử dụng một số hệ thống tệp cũ hơn như FAT16, FAT32 và HPFS.

FAT là viết tắt của File Allocation Table. FAT16 và FAT32 từng được sử dụng rộng rãi trên các hệ điều hành cũ và các thiết bị lưu trữ ngoài. Ngày nay, FAT32 vẫn có thể gặp trên USB, thẻ nhớ SD hoặc các thiết bị cần khả năng tương thích với nhiều hệ điều hành khác nhau.

Tuy nhiên, FAT32 có nhiều hạn chế. Một trong những hạn chế phổ biến nhất là không hỗ trợ tệp có dung lượng lớn hơn 4 GB. Ngoài ra, FAT32 không hỗ trợ cơ chế phân quyền chi tiết như NTFS, vì vậy nó không phù hợp cho các hệ thống cần bảo mật dữ liệu tốt.

HPFS, viết tắt của High Performance File System, cũng là một hệ thống tệp từng được sử dụng trước đây. Tuy nhiên, trong các hệ thống Windows hiện đại, HPFS gần như không còn phổ biến.

Có thể tóm tắt như sau:

| Hệ thống tệp | Đặc điểm chính |
|---|---|
| FAT16 | Hệ thống tệp cũ, giới hạn dung lượng thấp |
| FAT32 | Tương thích tốt với USB/thẻ nhớ, nhưng không hỗ trợ tệp trên 4 GB |
| HPFS | Hệ thống tệp hiệu năng cao trước đây, hiện ít phổ biến |
| NTFS | Hệ thống tệp chính của Windows hiện đại, hỗ trợ bảo mật và nhiều tính năng nâng cao |

Trong thực tế, nếu cài đặt Windows trên máy tính cá nhân hoặc máy chủ hiện đại, hệ thống tệp được sử dụng gần như luôn là NTFS.


## 3.3. NTFS là gì?

NTFS là viết tắt của New Technology File System. Đây là hệ thống tệp được sử dụng trong các phiên bản Windows hiện đại.

NTFS được thiết kế để khắc phục nhiều hạn chế của các hệ thống tệp cũ như FAT16 và FAT32. So với FAT32, NTFS mạnh hơn, ổn định hơn và hỗ trợ nhiều tính năng bảo mật hơn.

Một đặc điểm quan trọng của NTFS là đây là hệ thống tệp có cơ chế ghi nhật ký. Điều này có nghĩa là hệ thống có thể lưu lại một số thông tin về thay đổi trên ổ đĩa. Khi xảy ra lỗi, Windows có thể sử dụng thông tin này để hỗ trợ sửa chữa hoặc khôi phục trạng thái của hệ thống tệp.

NTFS cũng cho phép thiết lập quyền truy cập chi tiết trên từng tệp và thư mục. Đây là một điểm rất quan trọng trong môi trường nhiều người dùng hoặc môi trường doanh nghiệp, nơi không phải ai cũng được phép truy cập cùng một dữ liệu.

Ngoài ra, NTFS còn hỗ trợ các tính năng như:

- tệp có kích thước lớn;
- phân quyền tệp và thư mục;
- nén dữ liệu;
- mã hóa dữ liệu;
- ghi nhật ký hệ thống tệp;
- Alternate Data Streams.

Vì vậy, NTFS không chỉ là nơi lưu trữ dữ liệu, mà còn là một thành phần quan trọng trong mô hình bảo mật của Windows.


## 3.4. Ưu điểm của NTFS

NTFS có nhiều ưu điểm so với các hệ thống tệp cũ. Những ưu điểm này giúp NTFS trở thành lựa chọn mặc định cho các phiên bản Windows hiện đại.

Một số ưu điểm quan trọng của NTFS gồm:

- hỗ trợ tệp có dung lượng lớn hơn 4 GB;
- hỗ trợ quyền truy cập riêng biệt cho từng tệp và thư mục;
- hỗ trợ nén tệp và thư mục;
- hỗ trợ mã hóa dữ liệu;
- có cơ chế ghi nhật ký để hỗ trợ phục hồi khi có lỗi;
- phù hợp với môi trường nhiều người dùng;
- phù hợp với hệ thống doanh nghiệp cần kiểm soát quyền truy cập.

Trong FAT32, người dùng không thể thiết lập quyền chi tiết cho từng tệp hoặc thư mục. Điều này khiến FAT32 không phù hợp với hệ thống cần bảo mật cao. Ngược lại, NTFS cho phép quản trị viên xác định rõ ai được đọc, ghi, chỉnh sửa hoặc thực thi một tệp cụ thể.

Ví dụ, trong một doanh nghiệp, thư mục chứa tài liệu kế toán chỉ nên được truy cập bởi bộ phận kế toán và quản lý. Với NTFS, quản trị viên có thể cấu hình quyền để những người dùng khác không thể mở hoặc chỉnh sửa thư mục này.

NTFS cũng hỗ trợ EFS, tức Encrypting File System. Đây là cơ chế mã hóa tệp ở cấp hệ thống tệp, giúp bảo vệ dữ liệu khỏi truy cập trái phép.

Từ góc độ an toàn thông tin, NTFS rất quan trọng vì nó là nền tảng cho việc kiểm soát truy cập dữ liệu trên Windows.


## 3.5. Quyền truy cập trong NTFS

Quyền truy cập trong NTFS cho phép Windows kiểm soát người dùng hoặc nhóm người dùng nào được phép thao tác với tệp và thư mục.

Mỗi tệp hoặc thư mục trên phân vùng NTFS có thể được gán các quyền khác nhau. Các quyền này xác định người dùng có thể đọc, ghi, chỉnh sửa, thực thi hoặc xóa dữ liệu hay không.

Quyền NTFS thường được áp dụng cho:

- người dùng cụ thể;
- nhóm người dùng;
- tài khoản hệ thống;
- tài khoản dịch vụ.

Ví dụ, một thư mục có thể cho phép nhóm Administrators toàn quyền kiểm soát, trong khi nhóm Users chỉ được phép đọc và thực thi. Điều này giúp hệ thống hạn chế người dùng thông thường thay đổi hoặc xóa các tệp quan trọng.

Quyền NTFS có thể được sử dụng để:

- bảo vệ tệp hệ thống;
- giới hạn truy cập vào dữ liệu nhạy cảm;
- phân quyền theo phòng ban;
- ngăn người dùng chỉnh sửa dữ liệu không thuộc phạm vi của họ;
- hỗ trợ điều tra khi có truy cập trái phép.

Trong môi trường doanh nghiệp, quyền NTFS thường được kết hợp với tài khoản người dùng, nhóm bảo mật và Active Directory để quản lý truy cập một cách tập trung và hiệu quả.


## 3.6. Các quyền cơ bản trong NTFS

NTFS cung cấp nhiều loại quyền cơ bản để kiểm soát cách người dùng tương tác với tệp và thư mục. Các quyền này có thể được cấp hoặc từ chối tùy theo yêu cầu bảo mật.

Các quyền cơ bản trong NTFS gồm:

- Full Control;
- Modify;
- Read & Execute;
- List Folder Contents;
- Read;
- Write.

Mỗi quyền có ý nghĩa khác nhau đối với tệp và thư mục. Việc hiểu rõ từng quyền là rất quan trọng để tránh cấu hình sai, đặc biệt trong các hệ thống có nhiều người dùng.


### 3.6.1. Full Control

Full Control là quyền cao nhất trong NTFS. Người dùng có quyền Full Control có thể thực hiện hầu như mọi thao tác đối với tệp hoặc thư mục.

Đối với thư mục, quyền Full Control cho phép người dùng:

- đọc nội dung thư mục;
- tạo tệp và thư mục con;
- chỉnh sửa tệp;
- xóa tệp và thư mục;
- thay đổi quyền truy cập;
- thay đổi chủ sở hữu nếu được phép.

Đối với tệp, quyền Full Control cho phép người dùng:

- đọc tệp;
- ghi vào tệp;
- chỉnh sửa nội dung;
- thực thi tệp nếu đó là tệp chương trình;
- xóa tệp;
- thay đổi quyền của tệp.

Quyền này chỉ nên cấp cho người dùng hoặc nhóm thật sự cần quản trị dữ liệu. Nếu cấp Full Control quá rộng, người dùng có thể vô tình hoặc cố ý xóa, sửa hoặc thay đổi quyền truy cập của dữ liệu quan trọng.


### 3.6.2. Modify

Modify là quyền cho phép người dùng đọc, ghi, chỉnh sửa và xóa tệp hoặc thư mục. Tuy nhiên, quyền này thấp hơn Full Control vì thường không bao gồm quyền thay đổi quyền truy cập hoặc thay đổi chủ sở hữu.

Đối với thư mục, quyền Modify cho phép:

- xem nội dung thư mục;
- tạo tệp mới;
- chỉnh sửa tệp;
- xóa tệp hoặc thư mục con.

Đối với tệp, quyền Modify cho phép:

- đọc nội dung tệp;
- ghi dữ liệu vào tệp;
- chỉnh sửa tệp;
- xóa tệp.

Quyền Modify phù hợp cho người dùng cần làm việc trực tiếp với dữ liệu, ví dụ như nhân viên cần tạo, sửa và xóa tài liệu trong thư mục làm việc của phòng ban.

Tuy nhiên, quyền này vẫn cần được cấp cẩn thận vì người dùng có thể xóa hoặc thay đổi dữ liệu.


### 3.6.3. Read & Execute

Read & Execute là quyền cho phép người dùng đọc nội dung và thực thi tệp chương trình hoặc script.

Đối với thư mục, quyền này cho phép người dùng:

- xem danh sách tệp và thư mục con;
- đọc nội dung;
- thực thi các tệp có thể chạy bên trong thư mục.

Đối với tệp, quyền này cho phép người dùng:

- đọc nội dung tệp;
- chạy tệp nếu đó là tệp thực thi.

Quyền Read & Execute thường được sử dụng cho các thư mục chứa chương trình hoặc script mà người dùng cần chạy nhưng không được phép chỉnh sửa.

Ví dụ, một thư mục chứa công cụ nội bộ của công ty có thể cấp quyền Read & Execute cho nhân viên. Khi đó, nhân viên có thể chạy chương trình nhưng không thể thay đổi hoặc xóa tệp chương trình.


### 3.6.4. List Folder Contents

List Folder Contents là quyền cho phép người dùng xem danh sách các tệp và thư mục con bên trong một thư mục.

Quyền này chủ yếu áp dụng cho thư mục, không áp dụng trực tiếp theo cùng cách đối với tệp. Người dùng có quyền này có thể nhìn thấy những gì có trong thư mục, nhưng không nhất thiết có quyền mở, sửa hoặc xóa nội dung bên trong nếu các quyền khác không được cấp.

Đối với thư mục, quyền List Folder Contents cho phép:

- xem tên tệp;
- xem tên thư mục con;
- điều hướng qua cấu trúc thư mục nếu được cho phép.

Quyền này hữu ích khi người dùng cần biết trong thư mục có những tài nguyên nào, nhưng không cần chỉnh sửa chúng.

Ví dụ, trong một thư mục chia sẻ, người dùng có thể được phép xem danh sách tài liệu nhưng chỉ một số tài liệu nhất định mới cho phép đọc hoặc chỉnh sửa.


### 3.6.5. Read

Read là quyền cho phép người dùng xem nội dung của tệp hoặc thư mục.

Đối với thư mục, quyền Read cho phép:

- xem tên tệp và thư mục con;
- xem thuộc tính của thư mục;
- xem quyền được gán nếu được phép.

Đối với tệp, quyền Read cho phép:

- mở tệp;
- đọc nội dung tệp;
- xem thuộc tính của tệp.

Quyền Read phù hợp với những trường hợp người dùng chỉ cần tham khảo dữ liệu mà không được thay đổi. Ví dụ, một thư mục chứa quy định nội bộ của công ty có thể cấp quyền Read cho toàn bộ nhân viên.

Từ góc độ bảo mật, quyền Read cũng cần được kiểm soát. Với dữ liệu nhạy cảm, chỉ cho phép đọc cũng có thể gây rủi ro nếu người dùng không có thẩm quyền được xem nội dung.


### 3.6.6. Write

Write là quyền cho phép người dùng ghi dữ liệu vào tệp hoặc thêm nội dung vào thư mục.

Đối với thư mục, quyền Write cho phép:

- tạo tệp mới;
- tạo thư mục con;
- ghi dữ liệu vào thư mục.

Đối với tệp, quyền Write cho phép:

- ghi nội dung mới;
- thay đổi nội dung tệp;
- cập nhật dữ liệu trong tệp.

Quyền Write thường được sử dụng khi người dùng cần gửi dữ liệu, tạo tài liệu hoặc lưu kết quả làm việc. Tuy nhiên, nếu chỉ có Write mà không có Read, người dùng có thể ghi dữ liệu nhưng không nhất thiết đọc được nội dung đã có.

Quyền Write cần được cấu hình cẩn thận vì nó có thể cho phép người dùng ghi đè dữ liệu, tạo tệp không mong muốn hoặc đưa nội dung độc hại vào thư mục nếu không có kiểm soát phù hợp.


## 3.7. Cách kiểm tra quyền của tệp và thư mục

Để kiểm tra quyền của một tệp hoặc thư mục trên Windows, người dùng có thể sử dụng giao diện đồ họa.

Các bước cơ bản như sau:

![](./img/3.7.png)

1. Nhấp chuột phải vào tệp hoặc thư mục cần kiểm tra.
2. Chọn **Properties**.
3. Mở tab **Security**.
4. Trong phần **Group or user names**, chọn người dùng hoặc nhóm muốn kiểm tra.
5. Xem các quyền được hiển thị trong phần quyền truy cập.

Trong tab Security, Windows sẽ hiển thị danh sách các nhóm hoặc người dùng có quyền đối với đối tượng đó. Khi chọn một nhóm hoặc người dùng, hệ thống sẽ hiển thị các quyền tương ứng như Read, Write, Modify hoặc Full Control.

Ví dụ, khi kiểm tra thư mục hệ thống `C:\Windows`, ta có thể thấy các nhóm như Administrators, SYSTEM hoặc Users có các quyền khác nhau. Người dùng thông thường thường không có quyền chỉnh sửa sâu trong thư mục hệ thống để tránh gây lỗi hoặc phá hoại hệ điều hành.

Việc kiểm tra quyền thường được dùng trong các tình huống sau:

- xác định ai có quyền truy cập dữ liệu;
- xử lý lỗi không mở được tệp hoặc thư mục;
- kiểm tra cấu hình bảo mật;
- điều tra truy cập trái phép;
- đảm bảo dữ liệu nhạy cảm không bị chia sẻ sai đối tượng.

Trong môi trường doanh nghiệp, kiểm tra quyền NTFS là một kỹ năng quan trọng đối với quản trị viên hệ thống và chuyên viên an toàn thông tin.


## 3.8. Alternate Data Streams — ADS

Alternate Data Streams, viết tắt là ADS, là một tính năng đặc biệt của hệ thống tệp NTFS. ADS cho phép một tệp có thể chứa nhiều luồng dữ liệu khác nhau.

Thông thường, khi người dùng nhìn thấy một tệp trong Windows Explorer, họ chỉ thấy nội dung chính của tệp. Tuy nhiên, trên NTFS, một tệp có thể có thêm các luồng dữ liệu phụ mà Windows Explorer không hiển thị trực tiếp theo mặc định.

Nói đơn giản, ADS cho phép gắn thêm dữ liệu vào một tệp mà không làm thay đổi nội dung chính mà người dùng nhìn thấy. Đây là một tính năng hợp pháp của NTFS và có nhiều mục đích sử dụng khác nhau.

Một ví dụ phổ biến là khi tải tệp từ Internet, Windows có thể thêm thông tin về nguồn gốc của tệp vào một luồng dữ liệu phụ. Thông tin này giúp Windows biết rằng tệp được tải xuống từ Internet và có thể cần cảnh báo người dùng trước khi mở.

Tuy nhiên, vì ADS không dễ thấy trong giao diện thông thường, nó cũng có thể bị lợi dụng để ẩn dữ liệu.

Đặc điểm chính của ADS gồm:

- chỉ có trên NTFS;
- cho phép tệp chứa nhiều luồng dữ liệu;
- không hiển thị rõ ràng trong Windows Explorer mặc định;
- có thể được kiểm tra bằng PowerShell hoặc công cụ chuyên dụng;
- có thể được dùng hợp pháp hoặc bị lạm dụng bởi mã độc.


## 3.9. Ý nghĩa bảo mật của ADS

Từ góc độ bảo mật, Alternate Data Streams là một tính năng cần được quan tâm vì nó có thể bị lợi dụng để ẩn dữ liệu hoặc che giấu hành vi độc hại.

Kẻ tấn công hoặc phần mềm độc hại có thể sử dụng ADS để lưu dữ liệu trong một luồng phụ của tệp. Vì Windows Explorer không hiển thị ADS theo cách thông thường, người dùng có thể không nhận ra rằng một tệp đang chứa thêm dữ liệu ẩn.

ADS có thể bị lợi dụng trong các tình huống như:

- ẩn payload độc hại;
- giấu script hoặc nội dung bất thường;
- che giấu dữ liệu đánh cắp;
- tránh sự chú ý của người dùng thông thường;
- gây khó khăn cho quá trình kiểm tra thủ công.

Tuy nhiên, không phải mọi ADS đều độc hại. Như đã đề cập, Windows cũng có thể dùng ADS để lưu thông tin về nguồn gốc của tệp tải xuống từ Internet. Vì vậy, khi phát hiện ADS, cần phân tích ngữ cảnh trước khi kết luận đó là dấu hiệu tấn công.

Đối với chuyên viên SOC hoặc người làm điều tra số, ADS là một điểm cần chú ý khi phân tích hệ thống Windows. Nếu nghi ngờ có hành vi ẩn dữ liệu, cần sử dụng PowerShell hoặc các công cụ chuyên dụng để kiểm tra các luồng dữ liệu phụ.

Tóm lại, ADS là một tính năng hợp pháp của NTFS, nhưng do khả năng ẩn dữ liệu, nó cũng có thể trở thành kỹ thuật bị lạm dụng trong tấn công mạng.

# 4. Thư mục hệ thống Windows

## 4.1. Thư mục `C:\Windows`

Thư mục `C:\Windows` là thư mục hệ thống chính của hệ điều hành Windows. Đây là nơi lưu trữ nhiều tệp, thư mục con, thư viện, công cụ và thành phần quan trọng giúp Windows có thể khởi động và hoạt động bình thường.

Thông thường, thư mục Windows nằm tại đường dẫn `C:\Windows`. Tuy nhiên, về mặt kỹ thuật, Windows không bắt buộc phải luôn được cài đặt ở ổ `C:`. Trong một số trường hợp, hệ điều hành có thể được cài ở ổ đĩa hoặc thư mục khác.

![](./img/4.1_c_windows.png)

Thư mục `C:\Windows` thường chứa các thành phần như:

- tệp hệ thống của Windows;
- thư viện hệ thống;
- trình điều khiển;
- công cụ quản trị;
- tệp cấu hình;
- thư mục `System32`;
- các thành phần phục vụ cập nhật và bảo trì hệ thống.

Người dùng thông thường không nên chỉnh sửa trực tiếp các tệp trong thư mục này nếu không hiểu rõ chức năng của chúng, vì điều đó có thể làm hệ thống hoạt động không ổn định hoặc gây lỗi nghiêm trọng.


## 4.2. Biến môi trường `%windir%`

`%windir%` là một biến môi trường trong Windows, được dùng để chỉ đường dẫn đến thư mục cài đặt hệ điều hành Windows.

Thông thường, giá trị của biến `%windir%` là `C:\Windows`.

Ví dụ:

- `%windir%` thường tương đương với `C:\Windows`;
- `%windir%\System32` thường tương đương với `C:\Windows\System32`.

Việc sử dụng biến môi trường giúp Windows và các chương trình tham chiếu đến thư mục hệ thống mà không cần viết cố định đường dẫn. Điều này rất hữu ích trong trường hợp Windows được cài đặt ở vị trí khác.

Ngoài `%windir%`, Windows còn có nhiều biến môi trường khác như `%SystemRoot%`, `%TEMP%`, `%USERPROFILE%` và `%ComSpec%`.

Trong quản trị hệ thống, hiểu biến môi trường giúp người dùng đọc script, chạy lệnh và xử lý lỗi đường dẫn chính xác hơn.

Để mở chúng ta nhấn tổ hợp phím Windows + R

![](./img/4.2.png)

## 4.3. Thư mục `System32`

`System32` là một thư mục con rất quan trọng nằm trong thư mục Windows. Đường dẫn phổ biến của thư mục này là `C:\Windows\System32`.

![](./img/4.3_system32.png)

Thư mục này chứa nhiều tệp thực thi, thư viện hệ thống và công cụ quan trọng của Windows. Nhiều chương trình và lệnh hệ thống được gọi trực tiếp từ thư mục này khi người dùng thao tác trong Windows, Command Prompt hoặc PowerShell.

Một số loại tệp thường có trong `System32` gồm:

- tệp `.exe` của các công cụ hệ thống;
- tệp `.dll` chứa thư viện dùng chung;
- công cụ dòng lệnh;
- tiện ích quản trị;
- thành phần mạng;
- thành phần bảo mật;
- tệp cấu hình hệ thống.

Mặc dù có tên là `System32`, thư mục này vẫn rất quan trọng trên cả hệ điều hành Windows 64-bit. Đây là một trong những thư mục cốt lõi của Windows.


## 4.4. Vai trò của `System32`

Thư mục `System32` đóng vai trò trung tâm trong hoạt động của hệ điều hành Windows. Nhiều chức năng quan trọng của hệ thống phụ thuộc vào các tệp nằm trong thư mục này.

Vai trò chính của `System32` gồm:

- lưu trữ các chương trình hệ thống quan trọng;
- chứa thư viện DLL cần thiết cho Windows và ứng dụng;
- cung cấp công cụ quản trị hệ thống;
- hỗ trợ các lệnh trong Command Prompt;
- cung cấp tiện ích mạng;
- hỗ trợ cấu hình, giám sát và xử lý sự cố;
- chứa nhiều thành phần liên quan đến bảo mật.

Ví dụ, khi người dùng mở Command Prompt, Task Manager, Control Panel, System Information hoặc một số công cụ quản trị khác, Windows có thể gọi các tệp nằm trong `System32`.

Đối với quản trị viên hệ thống và người học an toàn thông tin, `System32` là một vị trí cần hiểu rõ vì nó chứa nhiều công cụ hợp pháp của Windows. Các công cụ này có thể được sử dụng cho quản trị, xử lý sự cố, điều tra bảo mật hoặc trong một số trường hợp bị kẻ tấn công lạm dụng.


## 4.5. Vì sao không nên xóa hoặc chỉnh sửa tùy tiện trong `System32`?

Không nên xóa hoặc chỉnh sửa tùy tiện trong `System32` vì đây là thư mục chứa nhiều thành phần cốt lõi của Windows. Nếu xóa nhầm hoặc thay đổi sai tệp trong thư mục này, hệ điều hành có thể gặp lỗi nghiêm trọng.

Một số hậu quả có thể xảy ra gồm:

- Windows hoạt động không ổn định;
- một số công cụ hệ thống không mở được;
- dịch vụ Windows bị lỗi;
- lỗi kết nối mạng;
- lỗi đăng nhập;
- lỗi cập nhật hệ thống;
- hệ điều hành không thể khởi động.

Ngoài ra, việc chỉnh sửa tùy tiện trong `System32` còn có thể tạo ra rủi ro bảo mật. Nếu một tệp hệ thống bị thay thế bằng tệp độc hại, kẻ tấn công có thể lợi dụng nó để duy trì quyền truy cập, leo thang đặc quyền hoặc che giấu hành vi độc hại.

Windows thường áp dụng cơ chế phân quyền để bảo vệ thư mục này. Người dùng thông thường không có toàn quyền chỉnh sửa nhiều tệp trong `System32`, nhằm giảm nguy cơ làm hỏng hệ thống.

Chỉ nên thao tác với `System32` khi:

- hiểu rõ tệp hoặc công cụ đang sử dụng;
- có quyền quản trị phù hợp;
- có hướng dẫn đáng tin cậy;
- đã sao lưu dữ liệu quan trọng;
- thao tác phục vụ mục đích quản trị, sửa lỗi hoặc điều tra hợp lệ.


## 4.6. Các công cụ Windows thường nằm trong `System32`

Nhiều công cụ quan trọng của Windows được lưu trong thư mục `System32`. Các công cụ này có thể được mở từ Start Menu, hộp thoại Run, Command Prompt hoặc PowerShell.

| Công cụ | Lệnh / tệp thực thi | Chức năng chính |
|---|---|---|
| Command Prompt | `cmd.exe` | Mở giao diện dòng lệnh của Windows |
| Control Panel | `control.exe` | Mở Bảng điều khiển |
| Task Manager | `taskmgr.exe` | Quản lý tiến trình và tài nguyên hệ thống |
| System Configuration | `msconfig.exe` | Cấu hình khởi động và dịch vụ |
| Computer Management | `compmgmt.msc` | Quản lý hệ thống tổng hợp |
| Event Viewer | `eventvwr.msc` | Xem nhật ký sự kiện Windows |
| Device Manager | `devmgmt.msc` | Quản lý thiết bị phần cứng |
| Disk Management | `diskmgmt.msc` | Quản lý ổ đĩa và phân vùng |
| Services | `services.msc` | Quản lý dịch vụ Windows |
| System Information | `msinfo32.exe` | Xem thông tin phần cứng và phần mềm |
| Resource Monitor | `resmon.exe` | Theo dõi CPU, RAM, Disk và Network |
| Registry Editor | `regedit.exe` | Xem và chỉnh sửa Windows Registry |
| Windows Defender Firewall | `WF.msc` | Cấu hình tường lửa nâng cao |
| IP Configuration | `ipconfig.exe` | Xem cấu hình mạng |
| Network Statistics | `netstat.exe` | Xem kết nối mạng và thống kê TCP/IP |

Các công cụ này rất hữu ích trong quản trị hệ thống, xử lý sự cố và phân tích bảo mật. Ví dụ, `eventvwr.msc` giúp kiểm tra log sự kiện, `taskmgr.exe` giúp xem tiến trình đang chạy, còn `ipconfig.exe` hỗ trợ kiểm tra cấu hình mạng.


# 5. Tài khoản người dùng, hồ sơ và quyền

## 5.1. Tài khoản người dùng trong Windows

Tài khoản người dùng trong Windows là danh tính được sử dụng để đăng nhập và làm việc trên hệ thống. Mỗi tài khoản đại diện cho một người dùng hoặc một đối tượng có quyền truy cập vào máy tính.

Thông qua tài khoản người dùng, Windows có thể xác định:

- ai đang đăng nhập vào hệ thống;
- người dùng đó được phép làm gì;
- người dùng có thể truy cập tệp hoặc thư mục nào;
- người dùng có quyền thay đổi cài đặt hệ thống hay không;
- hồ sơ cá nhân của người dùng được lưu ở đâu.

Trong Windows, tài khoản người dùng cục bộ thường được chia thành hai loại chính:

- **Administrator Account**;
- **Standard User Account**.

Loại tài khoản quyết định mức quyền của người dùng trên hệ thống. Người dùng có quyền quản trị có thể thay đổi nhiều thiết lập quan trọng, trong khi người dùng tiêu chuẩn bị giới hạn hơn để giảm rủi ro gây lỗi hoặc làm mất an toàn hệ thống.

Trong môi trường doanh nghiệp, tài khoản người dùng có thể được quản lý cục bộ trên từng máy hoặc được quản lý tập trung thông qua Active Directory.


## 5.2. Administrator Account

**Administrator Account** là tài khoản có quyền quản trị trên hệ thống Windows. Người dùng thuộc nhóm Administrator có thể thực hiện các thay đổi quan trọng ảnh hưởng đến toàn bộ máy tính.

Một tài khoản Administrator thường có thể:

- cài đặt và gỡ bỏ phần mềm;
- tạo tài khoản người dùng mới;
- xóa tài khoản người dùng;
- thay đổi loại tài khoản;
- thêm hoặc xóa người dùng khỏi nhóm;
- thay đổi cài đặt hệ thống;
- truy cập nhiều khu vực quản trị;
- thay đổi quyền truy cập của tệp và thư mục;
- chạy chương trình với quyền cao.

Tài khoản Administrator rất quan trọng trong quản trị hệ thống, nhưng cũng tiềm ẩn nhiều rủi ro nếu bị lạm dụng hoặc bị kẻ tấn công chiếm quyền. Nếu mã độc chạy dưới quyền Administrator, nó có thể gây thiệt hại lớn hơn nhiều so với khi chạy dưới quyền người dùng thông thường.

Vì vậy, trong thực tế, không nên sử dụng tài khoản Administrator cho các công việc hằng ngày như duyệt web, đọc email hoặc mở tệp không rõ nguồn gốc. Chỉ nên dùng quyền quản trị khi thật sự cần thiết.


## 5.3. Standard User Account

**Standard User Account** là tài khoản người dùng thông thường trong Windows. Tài khoản này được thiết kế để sử dụng cho các công việc hằng ngày nhưng không có toàn quyền thay đổi hệ thống.

Người dùng Standard User có thể thực hiện các tác vụ cơ bản như:

- đăng nhập vào Windows;
- sử dụng ứng dụng đã được cài đặt;
- tạo và chỉnh sửa tệp trong thư mục cá nhân;
- thay đổi một số thiết lập cá nhân;
- truy cập tài nguyên được cấp quyền.

Tuy nhiên, Standard User thường không thể:

- cài đặt phần mềm cho toàn hệ thống;
- thay đổi cài đặt bảo mật quan trọng;
- tạo hoặc xóa tài khoản người dùng khác;
- thay đổi nhóm người dùng;
- chỉnh sửa tệp hệ thống;
- truy cập dữ liệu của người dùng khác nếu không được cấp quyền.

Loại tài khoản này an toàn hơn cho việc sử dụng hằng ngày vì nó giới hạn quyền của người dùng. Nếu người dùng vô tình chạy một chương trình độc hại, chương trình đó cũng bị giới hạn bởi quyền của tài khoản hiện tại.

Trong an toàn thông tin, việc sử dụng Standard User cho công việc thường ngày là một nguyên tắc quan trọng để giảm nguy cơ leo thang đặc quyền và hạn chế tác động của mã độc.


## 5.4. Sự khác nhau giữa Administrator và Standard User

Administrator và Standard User khác nhau chủ yếu ở mức quyền trên hệ thống.

Administrator có quyền thay đổi các thiết lập cấp hệ thống, trong khi Standard User chỉ có quyền thao tác trong phạm vi cá nhân hoặc các tài nguyên đã được cấp quyền.

| Tiêu chí | Administrator | Standard User |
|---|---|---|
| Quyền cài đặt phần mềm | Có thể cài đặt phần mềm hệ thống | Thường không thể cài đặt nếu cần quyền quản trị |
| Quản lý người dùng | Có thể tạo, xóa, sửa tài khoản | Không thể quản lý tài khoản khác |
| Thay đổi cài đặt hệ thống | Có thể thay đổi | Bị giới hạn |
| Truy cập tệp hệ thống | Có nhiều quyền hơn | Bị hạn chế |
| Mức độ rủi ro khi bị mã độc lợi dụng | Cao hơn | Thấp hơn |
| Phù hợp cho | Quản trị hệ thống | Sử dụng hằng ngày |

Ví dụ, nếu một người dùng Standard User muốn cài đặt phần mềm yêu cầu quyền cao, Windows có thể hiển thị yêu cầu **User Account Control** để yêu cầu xác nhận hoặc nhập thông tin tài khoản quản trị.

Trong môi trường doanh nghiệp, người dùng thông thường nên sử dụng Standard User Account. Quyền Administrator chỉ nên cấp cho quản trị viên hoặc những người thật sự cần thực hiện nhiệm vụ quản trị.


## 5.5. User Profile là gì?

**User Profile** là hồ sơ cá nhân của người dùng trên Windows. Khi một tài khoản người dùng đăng nhập vào hệ thống lần đầu, Windows sẽ tạo một hồ sơ riêng cho tài khoản đó.

User Profile chứa các dữ liệu và thiết lập cá nhân của người dùng, ví dụ:

- Desktop;
- Documents;
- Downloads;
- Pictures;
- Music;
- cấu hình ứng dụng;
- thiết lập giao diện;
- một số dữ liệu cá nhân khác.

![](./img/5.5_user_profile.webp)

Nhờ User Profile, mỗi người dùng có thể có môi trường làm việc riêng trên cùng một máy tính. Ví dụ, mỗi người có Desktop riêng, thư mục tài liệu riêng và một số thiết lập cá nhân riêng.

Khi người dùng đăng nhập lần đầu, Windows sẽ chuẩn bị hồ sơ người dùng. Sau khi hồ sơ được tạo, hệ thống sẽ sử dụng hồ sơ đó cho các lần đăng nhập tiếp theo.

Trong quản trị hệ thống, User Profile rất quan trọng vì nó liên quan đến dữ liệu cá nhân, cấu hình ứng dụng và trải nghiệm làm việc của người dùng.


## 5.6. Thư mục `C:\Users`

`C:\Users` là thư mục mặc định chứa hồ sơ của các người dùng trên Windows.

Mỗi người dùng thường có một thư mục riêng bên trong `C:\Users`. Ví dụ, nếu tài khoản có tên là `Max`, thư mục hồ sơ của người dùng đó thường là:

```text
C:\Users\Max
````

Trong thư mục này, Windows lưu các thư mục và dữ liệu cá nhân của người dùng. Đây là nơi chứa Desktop, Documents, Downloads và nhiều dữ liệu cấu hình liên quan đến tài khoản.

Ví dụ cấu trúc cơ bản có thể như sau:

```text
C:\Users
├── Administrator
├── Public
├── Max
└── User01
```

Thư mục `C:\Users` giúp Windows tách biệt dữ liệu giữa các tài khoản khác nhau. Người dùng này thường không thể truy cập dữ liệu riêng của người dùng khác nếu không có quyền phù hợp.

Từ góc độ bảo mật, thư mục `C:\Users` là nơi quan trọng vì nó thường chứa dữ liệu cá nhân, tài liệu làm việc, tệp tải xuống và có thể cả dữ liệu nhạy cảm.

## 5.7. Các thư mục mặc định trong hồ sơ người dùng

Khi Windows tạo hồ sơ người dùng, hệ thống thường tạo sẵn một số thư mục mặc định để phục vụ việc lưu trữ dữ liệu cá nhân.

Các thư mục thường gặp gồm:

| Thư mục   | Chức năng                                                      |
| --------- | -------------------------------------------------------------- |
| Desktop   | Chứa các biểu tượng, shortcut và tệp nằm trên màn hình Desktop |
| Documents | Lưu trữ tài liệu cá nhân hoặc tài liệu làm việc                |
| Downloads | Lưu các tệp được tải xuống từ Internet                         |
| Pictures  | Lưu trữ hình ảnh                                               |
| Music     | Lưu trữ tệp âm thanh                                           |
| Videos    | Lưu trữ video                                                  |
| AppData   | Chứa dữ liệu cấu hình và dữ liệu ứng dụng của người dùng       |

Ví dụ, nếu người dùng có tên `Max`, thư mục Downloads của người dùng đó thường là:

```text
C:\Users\Max\Downloads
```

Trong điều tra bảo mật, một số thư mục trong User Profile rất đáng chú ý. Ví dụ, thư mục `Downloads` có thể chứa tệp tải từ Internet, thư mục `Desktop` có thể chứa tài liệu người dùng thường mở, còn `AppData` có thể chứa dữ liệu ứng dụng hoặc tệp được phần mềm tạo ra.

Vì vậy, hiểu cấu trúc User Profile giúp quản trị viên và chuyên viên SOC phân tích hoạt động người dùng tốt hơn.

## 5.8. Local Users and Groups

**Local Users and Groups** là công cụ quản lý người dùng và nhóm cục bộ trên một máy Windows. Công cụ này cho phép quản trị viên xem, tạo, sửa, xóa tài khoản người dùng và quản lý tư cách thành viên trong các nhóm cục bộ.

Trong Local Users and Groups, có hai phần chính:

* **Users**;
* **Groups**.

Phần Users chứa danh sách các tài khoản người dùng cục bộ trên máy. Phần Groups chứa các nhóm cục bộ, mỗi nhóm có một tập quyền hoặc vai trò nhất định.

Thông qua công cụ này, quản trị viên có thể:

* xem danh sách người dùng cục bộ;
* tạo người dùng mới;
* đổi mật khẩu;
* vô hiệu hóa tài khoản;
* thêm người dùng vào nhóm;
* xóa người dùng khỏi nhóm;
* kiểm tra mô tả và thuộc tính tài khoản.

Local Users and Groups thường được sử dụng khi quản trị một máy Windows độc lập hoặc khi cần kiểm tra tài khoản cục bộ trên máy trong môi trường domain.

## 5.9. Công cụ `lusrmgr.msc`

`lusrmgr.msc` là lệnh dùng để mở công cụ **Local Users and Groups** trong Windows.

Có thể mở công cụ này bằng cách:

1. Nhấn `Win + R` để mở hộp thoại Run.
2. Nhập lệnh:

```text
lusrmgr.msc
```

3. Nhấn Enter.

![](./img/5.9_lusrmgr.png)

Sau khi mở, cửa sổ Local Users and Groups sẽ hiển thị hai thư mục chính:

* **Users**;
* **Groups**.

Trong **Users**, quản trị viên có thể xem các tài khoản người dùng cục bộ. Trong **Groups**, quản trị viên có thể xem các nhóm cục bộ và thành viên của từng nhóm.

Công cụ `lusrmgr.msc` rất hữu ích khi cần kiểm tra nhanh tài khoản nào đang tồn tại trên máy, người dùng thuộc nhóm nào và có tài khoản lạ nào được tạo bất thường hay không.

Lưu ý rằng công cụ này thường yêu cầu quyền quản trị để thực hiện các thay đổi quan trọng.

## 5.10. Users và Groups

Trong Windows, **Users** là các tài khoản người dùng, còn **Groups** là các nhóm dùng để quản lý quyền cho nhiều người dùng cùng lúc.

Thay vì cấp quyền riêng lẻ cho từng người dùng, Windows cho phép đưa nhiều người dùng vào một nhóm. Sau đó, quyền được cấp cho nhóm sẽ áp dụng cho tất cả thành viên của nhóm đó.

Ví dụ:

* người dùng thuộc nhóm `Administrators` sẽ có quyền quản trị;
* người dùng thuộc nhóm `Users` sẽ có quyền thông thường;
* người dùng thuộc nhóm `Remote Desktop Users` có thể được phép đăng nhập từ xa qua Remote Desktop nếu cấu hình cho phép.

Việc sử dụng nhóm giúp quản lý quyền dễ dàng hơn. Khi một người dùng mới cần quyền giống những người khác, quản trị viên chỉ cần thêm người đó vào nhóm phù hợp.

Một người dùng có thể là thành viên của nhiều nhóm. Khi đó, quyền thực tế của người dùng sẽ phụ thuộc vào các nhóm mà họ thuộc về và các chính sách bảo mật đang áp dụng.

Trong an toàn thông tin, cần kiểm tra kỹ thành viên của các nhóm có quyền cao, đặc biệt là nhóm `Administrators`, vì nếu tài khoản không phù hợp nằm trong nhóm này, hệ thống có thể bị rủi ro nghiêm trọng.

## 5.11. Quyền kế thừa từ nhóm người dùng

Quyền kế thừa từ nhóm người dùng là cơ chế trong đó một người dùng nhận quyền dựa trên nhóm mà họ thuộc về.

Ví dụ, nếu tài khoản `user01` được thêm vào nhóm `Remote Desktop Users`, tài khoản này có thể được cấp quyền đăng nhập từ xa nếu hệ thống cho phép Remote Desktop. Nếu tài khoản được thêm vào nhóm `Administrators`, người dùng sẽ có quyền quản trị trên máy.

Cơ chế này giúp đơn giản hóa việc quản lý quyền. Thay vì cấu hình quyền riêng cho từng người dùng, quản trị viên chỉ cần quản lý tư cách thành viên của các nhóm.

Ví dụ:

```text
Người dùng A → thuộc nhóm Users → có quyền người dùng thông thường
Người dùng B → thuộc nhóm Administrators → có quyền quản trị
Người dùng C → thuộc nhóm Remote Desktop Users → có thể được phép truy cập từ xa
```

Tuy nhiên, quyền kế thừa từ nhóm cũng có thể gây rủi ro nếu quản lý không cẩn thận. Một người dùng bị thêm nhầm vào nhóm có quyền cao có thể thực hiện các thao tác vượt quá phạm vi cần thiết.

Vì vậy, trong quản trị và bảo mật Windows, cần thường xuyên kiểm tra:

* người dùng thuộc những nhóm nào;
* nhóm nào có quyền cao;
* có tài khoản lạ trong nhóm quản trị hay không;
* quyền cấp cho nhóm có phù hợp với công việc thực tế hay không.

Nguyên tắc nên áp dụng là **least privilege**, tức là chỉ cấp quyền tối thiểu cần thiết để người dùng thực hiện công việc.

## 5.12. Các tài khoản tích hợp sẵn trong Windows

Windows có một số tài khoản tích hợp sẵn được tạo mặc định để phục vụ cho hoạt động và quản trị hệ thống. Các tài khoản này có vai trò đặc biệt và cần được quản lý cẩn thận.

Một số tài khoản tích hợp thường gặp gồm:

| Tài khoản       | Ý nghĩa                                               |
| --------------- | ----------------------------------------------------- |
| Administrator   | Tài khoản quản trị tích hợp sẵn                       |
| Guest           | Tài khoản dành cho truy cập khách                     |
| DefaultAccount  | Tài khoản mặc định dùng cho một số chức năng hệ thống |
| SYSTEM          | Tài khoản hệ thống có quyền rất cao                   |
| Local Service   | Tài khoản dịch vụ cục bộ với quyền hạn chế            |
| Network Service | Tài khoản dịch vụ dùng cho một số hoạt động mạng      |

Tài khoản **Administrator** là tài khoản quản trị tích hợp sẵn. Tài khoản này có quyền cao và có thể thực hiện nhiều thay đổi quan trọng trên hệ thống. Vì vậy, cần bảo vệ bằng mật khẩu mạnh và chỉ sử dụng khi cần thiết.

Tài khoản **Guest** được thiết kế cho truy cập khách. Trong nhiều hệ thống hiện đại, tài khoản này thường bị vô hiệu hóa để giảm rủi ro bảo mật.

Các tài khoản như **SYSTEM**, **Local Service** và **Network Service** thường được sử dụng bởi hệ điều hành và các dịch vụ nền. Người dùng thông thường không đăng nhập trực tiếp bằng các tài khoản này.

Từ góc độ bảo mật, các tài khoản tích hợp sẵn cần được kiểm tra định kỳ. Đặc biệt, không nên bật tài khoản Guest nếu không cần thiết và cần hạn chế sử dụng tài khoản Administrator cho các tác vụ hằng ngày.


# 6. User Account Control — UAC

## 6.1. UAC là gì?

**User Account Control**, viết tắt là **UAC**, là một cơ chế bảo mật trong Windows dùng để kiểm soát việc thực thi các tác vụ cần quyền cao trên hệ thống.

UAC giúp ngăn người dùng hoặc chương trình tự ý thực hiện các thay đổi quan trọng mà không có sự xác nhận. Khi một hành động yêu cầu quyền quản trị, Windows sẽ hiển thị thông báo yêu cầu người dùng xác nhận hoặc nhập thông tin tài khoản Administrator.

Ví dụ, UAC có thể xuất hiện khi người dùng:

- cài đặt phần mềm mới;
- thay đổi cài đặt hệ thống;
- chỉnh sửa tệp trong thư mục hệ thống;
- chạy chương trình với quyền Administrator;
- thay đổi cấu hình bảo mật;
- thêm hoặc xóa tài khoản người dùng.

Mục đích chính của UAC là giảm nguy cơ phần mềm độc hại tự động chạy với quyền cao. Nhờ UAC, ngay cả khi người dùng đang đăng nhập bằng tài khoản có quyền quản trị, các chương trình vẫn không tự động có toàn quyền đối với hệ thống nếu chưa được xác nhận.


## 6.2. Vì sao Windows cần UAC?

Windows cần UAC vì nhiều người dùng thường đăng nhập bằng tài khoản có quyền quản trị. Nếu mọi chương trình đều tự động chạy với quyền quản trị, hệ thống sẽ rất dễ bị tấn công.

Khi không có UAC, một chương trình độc hại có thể âm thầm thực hiện các hành động nguy hiểm như:

- cài đặt mã độc;
- thay đổi cấu hình hệ thống;
- chỉnh sửa Registry;
- vô hiệu hóa phần mềm bảo mật;
- tạo tài khoản mới;
- thay đổi quyền truy cập;
- xóa hoặc sửa tệp hệ thống.

UAC giúp giảm rủi ro này bằng cách yêu cầu người dùng xác nhận trước khi một tác vụ có quyền cao được thực hiện.

Nói cách khác, UAC tạo thêm một lớp kiểm soát giữa người dùng, ứng dụng và hệ điều hành. Điều này giúp hạn chế việc mã độc lợi dụng quyền của người dùng đang đăng nhập.

Trong an toàn thông tin, UAC là một cơ chế quan trọng vì nó hỗ trợ nguyên tắc **least privilege**, tức là chỉ sử dụng quyền cao khi thật sự cần thiết.


## 6.3. Cách UAC hoạt động

Khi một người dùng có quyền Administrator đăng nhập vào Windows, phiên làm việc thông thường không tự động chạy với quyền cao nhất. Thay vào đó, Windows sẽ chạy hầu hết tác vụ ở mức quyền tiêu chuẩn.

Khi một chương trình hoặc tác vụ cần quyền quản trị, UAC sẽ can thiệp và hiển thị thông báo xác nhận. Người dùng phải đồng ý hoặc cung cấp thông tin đăng nhập của tài khoản quản trị thì tác vụ mới được tiếp tục.

Quy trình cơ bản của UAC có thể hiểu như sau:

1. Người dùng hoặc chương trình yêu cầu thực hiện một tác vụ cần quyền cao.
2. Windows phát hiện tác vụ này cần quyền Administrator.
3. UAC hiển thị hộp thoại xác nhận.
4. Người dùng xác nhận hoặc nhập thông tin tài khoản quản trị.
5. Nếu được chấp nhận, tác vụ chạy với quyền cao.
6. Nếu bị từ chối, tác vụ không được thực hiện.

Cơ chế này giúp người dùng nhận biết khi có chương trình đang cố gắng thay đổi hệ thống. Nếu UAC xuất hiện bất thường khi người dùng không chủ động thực hiện thao tác nào, đó có thể là dấu hiệu cần kiểm tra kỹ.

Hãy xem xét chương trình trên tài khoản bạn hiện đang đăng nhập. Đối với tài khoản quản trị viên tích hợp sẵn, nhấp chuột phải để xem Properties (Thuộc tính).

Trong tab Security (Bảo mật), bạn có thể thấy danh sách người dùng/nhóm và quyền của họ đối với tệp. Lưu ý rằng người dùng thông thường không được liệt kê ở đây.

![](./img/6.3_how_uac_work.png)

## 6.4. Elevated Privileges

**Elevated Privileges** có nghĩa là quyền được nâng cao, thường là quyền Administrator trong Windows.

Một chương trình chạy với Elevated Privileges có thể thực hiện nhiều thao tác quan trọng hơn so với chương trình chạy dưới quyền người dùng thông thường.

Ví dụ, chương trình chạy với quyền cao có thể:

- ghi vào thư mục hệ thống;
- thay đổi Registry;
- cài đặt driver;
- thay đổi cấu hình bảo mật;
- quản lý dịch vụ Windows;
- thay đổi tài khoản người dùng;
- chỉnh sửa quyền truy cập.

Không phải tác vụ nào cũng cần Elevated Privileges. Các công việc thông thường như duyệt web, soạn thảo văn bản, xem tài liệu hoặc nghe nhạc không cần quyền quản trị.

Việc chỉ sử dụng quyền cao khi cần thiết giúp giảm rủi ro bảo mật. Nếu một ứng dụng độc hại chỉ chạy với quyền người dùng thông thường, thiệt hại có thể bị giới hạn. Nhưng nếu ứng dụng đó chạy với quyền Administrator, nó có thể kiểm soát nhiều phần quan trọng của hệ thống.


## 6.5. Biểu tượng lá chắn UAC

Biểu tượng lá chắn UAC là biểu tượng hình chiếc khiên xuất hiện trên một số chương trình hoặc nút chức năng trong Windows.

Biểu tượng này cho biết thao tác đó cần quyền quản trị để chạy. Khi người dùng nhấp vào chương trình hoặc chức năng có biểu tượng lá chắn, Windows thường sẽ hiển thị UAC Prompt để yêu cầu xác nhận.

Ví dụ, biểu tượng lá chắn có thể xuất hiện khi:

- chạy trình cài đặt phần mềm;
- mở một công cụ quản trị;
- thay đổi cài đặt hệ thống;
- mở chương trình với quyền Administrator;
- thực hiện thao tác ảnh hưởng đến toàn bộ máy tính.

Biểu tượng lá chắn giúp người dùng nhận biết trước rằng hành động sắp thực hiện không phải là thao tác thông thường. Đây là dấu hiệu trực quan để cảnh báo rằng chương trình có thể thay đổi hệ thống.

![](./img/6.5.png)

Nếu một tệp lạ hoặc phần mềm không rõ nguồn gốc có biểu tượng lá chắn và yêu cầu quyền Administrator, người dùng cần kiểm tra cẩn thận trước khi cho phép chạy.

## 6.6. UAC Prompt

**UAC Prompt** là hộp thoại xác nhận xuất hiện khi một chương trình hoặc tác vụ cần quyền cao.

Tùy theo loại tài khoản đang sử dụng, UAC Prompt có thể hoạt động khác nhau:

- Nếu người dùng đang dùng tài khoản Administrator, Windows có thể chỉ yêu cầu xác nhận.
- Nếu người dùng đang dùng tài khoản Standard User, Windows có thể yêu cầu nhập tên người dùng và mật khẩu của tài khoản Administrator.

UAC Prompt thường hiển thị thông tin như:

- tên chương trình muốn chạy;
- nhà phát hành chương trình;
- vị trí hoặc nguồn của chương trình;
- yêu cầu cho phép chương trình thay đổi hệ thống.

Người dùng chỉ nên chọn **Yes** nếu chắc chắn chương trình đáng tin cậy và hành động đó là cần thiết. Nếu không rõ chương trình là gì, hoặc UAC Prompt xuất hiện bất ngờ, nên chọn **No**.

![](./img/6.6_uac_prompt.png)

Trong thực tế, UAC Prompt là một điểm kiểm soát quan trọng giúp người dùng tránh vô tình cấp quyền cao cho mã độc hoặc chương trình không an toàn.


## 6.7. Cài đặt UAC

Windows cho phép người dùng thay đổi mức độ thông báo của UAC thông qua phần **User Account Control Settings**.

Các mức cài đặt UAC thường cho phép điều chỉnh việc Windows sẽ thông báo khi nào. Ví dụ:

- luôn thông báo khi ứng dụng cố gắng cài đặt phần mềm hoặc thay đổi hệ thống;
- chỉ thông báo khi ứng dụng cố gắng thay đổi hệ thống;
- không thông báo trong một số trường hợp nhất định;
- tắt gần như hoàn toàn thông báo UAC.

Mức khuyến nghị thường là giữ UAC ở chế độ mặc định hoặc mức bảo vệ cao hơn. Điều này giúp hệ thống vẫn có cảnh báo khi có chương trình yêu cầu quyền Administrator.

Không nên giảm mức UAC hoặc tắt UAC nếu không có lý do rõ ràng, vì điều đó có thể làm giảm khả năng bảo vệ của Windows trước các chương trình độc hại.


## 6.8. Thay đổi UAC Settings

Có thể mở phần cài đặt UAC bằng nhiều cách khác nhau.

Một cách phổ biến là tìm kiếm trong Start Menu:

1. Mở **Start Menu**.
2. Nhập `UAC`.
3. Chọn **Change User Account Control settings**.
4. Điều chỉnh thanh trượt theo mức mong muốn.
5. Nhấn **OK** để lưu thay đổi.

![](./img/6.8_uac_settings.png)

Ngoài ra, có thể mở nhanh bằng lệnh:

```text
UserAccountControlSettings.exe
```

Trong cửa sổ UAC Settings, Windows hiển thị một thanh trượt cho phép thay đổi mức độ thông báo. Khi di chuyển thanh trượt, Windows sẽ mô tả ý nghĩa của từng mức.

Về mặt bảo mật, nên giữ UAC ở mức mặc định hoặc mức cao hơn. Chỉ nên thay đổi cài đặt này nếu hiểu rõ ảnh hưởng của nó đến hệ thống.

## 6.9. Rủi ro khi tắt UAC

Tắt UAC có thể làm hệ thống dễ bị tấn công hơn. Khi UAC bị tắt hoặc cấu hình quá thấp, các chương trình có thể thực hiện thay đổi quan trọng mà không cần người dùng xác nhận rõ ràng.

Một số rủi ro khi tắt UAC gồm:

* mã độc dễ chạy với quyền cao hơn;
* phần mềm lạ có thể thay đổi hệ thống mà không bị cảnh báo;
* Registry có thể bị chỉnh sửa trái phép;
* dịch vụ bảo mật có thể bị vô hiệu hóa;
* tài khoản người dùng hoặc nhóm có thể bị thay đổi;
* hệ thống khó phát hiện hành vi bất thường hơn.

Trong môi trường doanh nghiệp, việc tắt UAC có thể làm tăng rủi ro bị tấn công, đặc biệt nếu người dùng thường xuyên mở email, tải tệp từ Internet hoặc chạy phần mềm từ nguồn không rõ ràng.

Từ góc độ an toàn thông tin, UAC không phải là cơ chế bảo vệ tuyệt đối, nhưng nó là một lớp phòng thủ quan trọng. Vì vậy, không nên tắt UAC trừ khi có yêu cầu kỹ thuật đặc biệt và đã có biện pháp kiểm soát thay thế phù hợp.

# 7. Settings và Control Panel

## 7.1. Windows Settings

**Windows Settings** là ứng dụng cài đặt hiện đại của Windows, được Microsoft thiết kế để người dùng dễ dàng thay đổi các thiết lập cơ bản của hệ điều hành.

![](./img/7.1_windows_settings.png)

Thông qua Windows Settings, người dùng có thể cấu hình nhiều thành phần như:

- hệ thống hiển thị;
- âm thanh;
- thiết bị;
- mạng và Internet;
- tài khoản người dùng;
- cá nhân hóa giao diện;
- cập nhật Windows;
- quyền riêng tư;
- bảo mật hệ thống.

Windows Settings có giao diện đơn giản, trực quan và phù hợp với người dùng phổ thông. Trong các phiên bản Windows mới như Windows 10 và Windows 11, Microsoft dần chuyển nhiều chức năng từ Control Panel sang Settings.

Một số mục thường gặp trong Windows Settings gồm:

| Nhóm thiết lập | Chức năng chính |
|---|---|
| System | Cài đặt màn hình, âm thanh, thông báo, nguồn điện |
| Devices | Quản lý Bluetooth, máy in, chuột, bàn phím |
| Network & Internet | Cấu hình Wi-Fi, Ethernet, VPN, proxy |
| Personalization | Thay đổi hình nền, màu sắc, theme, Taskbar |
| Apps | Quản lý ứng dụng đã cài đặt |
| Accounts | Quản lý tài khoản người dùng |
| Time & Language | Cấu hình ngày giờ, ngôn ngữ, bàn phím |
| Update & Security | Windows Update, Recovery, Windows Security |

Windows Settings thường được sử dụng cho các thao tác cấu hình cơ bản và nhanh chóng.


## 7.2. Control Panel

**Control Panel** là công cụ cấu hình truyền thống của Windows. Đây là nơi tập trung nhiều thiết lập hệ thống quan trọng, đặc biệt là các thiết lập nâng cao và các công cụ quản trị cũ.

![](./img/7.2_control_panel.png)

Control Panel đã tồn tại trong Windows từ lâu và vẫn được giữ lại trong các phiên bản Windows hiện đại vì nhiều tính năng chưa được chuyển hoàn toàn sang Windows Settings.

Thông qua Control Panel, người dùng có thể cấu hình:

- hệ thống và bảo mật;
- mạng và Internet;
- phần cứng và âm thanh;
- chương trình;
- tài khoản người dùng;
- giao diện;
- đồng hồ và khu vực;
- công cụ trợ năng.

Control Panel thường được sử dụng khi cần truy cập các thiết lập chi tiết hơn, ví dụ như cấu hình adapter mạng, mở Windows Defender Firewall, quản lý thiết bị, gỡ chương trình hoặc thay đổi một số thiết lập hệ thống nâng cao.

Trong quản trị Windows, Control Panel vẫn là công cụ quan trọng vì nhiều hướng dẫn kỹ thuật và công cụ hệ thống vẫn liên quan đến giao diện này.


## 7.3. Sự khác nhau giữa Settings và Control Panel

Windows Settings và Control Panel đều dùng để thay đổi cấu hình hệ thống, nhưng chúng khác nhau về giao diện, mục đích sử dụng và mức độ chi tiết.

| Tiêu chí | Windows Settings | Control Panel |
|---|---|---|
| Giao diện | Hiện đại, đơn giản | Truyền thống, nhiều mục chi tiết |
| Đối tượng phù hợp | Người dùng phổ thông | Người dùng nâng cao, quản trị viên |
| Mức độ thiết lập | Các cài đặt phổ biến | Nhiều cài đặt nâng cao |
| Xu hướng phát triển | Được Microsoft ưu tiên trong Windows mới | Dần được thay thế nhưng vẫn còn quan trọng |
| Ví dụ sử dụng | Đổi hình nền, cấu hình Wi-Fi, Windows Update | Cấu hình adapter mạng, firewall nâng cao, chương trình cũ |

Windows Settings phù hợp khi cần thay đổi nhanh các thiết lập thường dùng. Control Panel phù hợp hơn khi cần truy cập các cấu hình truyền thống hoặc các công cụ quản trị chi tiết.

Trong thực tế, người dùng Windows nên biết sử dụng cả hai vì có những thiết lập chỉ dễ tìm trong Settings, nhưng cũng có những thiết lập vẫn cần mở Control Panel.


## 7.4. Cách mở Settings

Có nhiều cách để mở Windows Settings.

Cách nhanh nhất là sử dụng tổ hợp phím:

```text
Win + I
```

Ngoài ra, có thể mở Settings bằng các cách sau:

1. Nhấn nút **Start**.
2. Chọn biểu tượng **Settings** hình bánh răng.

Hoặc:

1. Nhấn **Start**.
2. Gõ từ khóa `Settings`.
3. Chọn ứng dụng **Settings**.

Cũng có thể mở Settings bằng cách nhấp chuột phải vào một số khu vực của giao diện Windows. Ví dụ:

* nhấp chuột phải trên Desktop rồi chọn **Display settings**;
* nhấp chuột phải trên Desktop rồi chọn **Personalize**;
* nhấp chuột phải vào biểu tượng mạng rồi chọn **Network & Internet settings**.

Windows Settings thường được dùng khi cần truy cập nhanh các thiết lập cơ bản của hệ thống.

## 7.5. Cách mở Control Panel

Có nhiều cách để mở Control Panel trong Windows.

Cách phổ biến nhất là dùng Start Menu:

1. Nhấn **Start**.
2. Nhập từ khóa:

```text
Control Panel
```

3. Chọn **Control Panel** trong kết quả tìm kiếm.

Cách khác là dùng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
```

2. Nhập lệnh:

```text
control
```

3. Nhấn **Enter**.

Ngoài ra, có thể mở Control Panel từ Command Prompt hoặc PowerShell bằng lệnh:

```text
control
```

Khi Control Panel mở ra, người dùng có thể chọn chế độ hiển thị theo **Category**, **Large icons** hoặc **Small icons**. Chế độ **Small icons** thường hữu ích hơn cho người học quản trị hệ thống vì nó hiển thị nhiều công cụ trực tiếp hơn.

## 7.6. Các nhóm thiết lập trong Control Panel

Control Panel chia các thiết lập thành nhiều nhóm khác nhau. Mỗi nhóm chứa các công cụ liên quan đến một lĩnh vực cấu hình của Windows.

Các nhóm thiết lập thường gặp gồm:

| Nhóm thiết lập                 | Chức năng chính                                       |
| ------------------------------ | ----------------------------------------------------- |
| System and Security            | Bảo mật, Windows Defender Firewall, hệ thống, sao lưu |
| Network and Internet           | Cấu hình mạng, chia sẻ, adapter mạng                  |
| Hardware and Sound             | Thiết bị, máy in, âm thanh, nguồn điện                |
| Programs                       | Gỡ cài đặt chương trình, bật/tắt tính năng Windows    |
| User Accounts                  | Quản lý tài khoản người dùng                          |
| Appearance and Personalization | Giao diện, File Explorer Options, font                |
| Clock and Region               | Ngày giờ, khu vực, định dạng ngôn ngữ                 |
| Ease of Access                 | Công cụ hỗ trợ truy cập                               |

Trong chế độ **Small icons**, Control Panel có thể hiển thị trực tiếp nhiều công cụ như:

* Administrative Tools;
* BitLocker Drive Encryption;
* Device Manager;
* File Explorer Options;
* Internet Options;
* Network and Sharing Center;
* Programs and Features;
* System;
* Windows Defender Firewall.

Một điểm cần chú ý là **Windows Defender Firewall** thường nằm trong Control Panel và có thể được mở nhanh khi cần cấu hình tường lửa của Windows.

## 7.7. Network & Internet Settings

**Network & Internet Settings** là phần cài đặt mạng trong Windows Settings. Đây là nơi người dùng có thể xem và cấu hình trạng thái kết nối mạng của máy tính.

Trong Network & Internet Settings, người dùng có thể kiểm tra:

* trạng thái kết nối mạng;
* kết nối Ethernet;
* kết nối Wi-Fi;
* VPN;
* Proxy;
* dữ liệu sử dụng;
* thiết lập chia sẻ mạng;
* các tùy chọn mạng nâng cao.

Ví dụ, khi máy tính không truy cập được Internet, người dùng có thể mở Network & Internet Settings để kiểm tra máy đang kết nối qua Wi-Fi hay Ethernet, có nhận địa chỉ IP hay không, hoặc có đang dùng proxy/VPN không.

Đối với người học an toàn thông tin, phần này rất quan trọng vì cấu hình mạng ảnh hưởng trực tiếp đến khả năng kết nối, giám sát, phân tích log và xử lý sự cố.

Một số tình huống thường cần mở Network & Internet Settings gồm:

* kiểm tra trạng thái mạng;
* thay đổi mạng Wi-Fi;
* cấu hình VPN;
* kiểm tra proxy;
* mở phần cấu hình adapter mạng;
* xử lý lỗi mất kết nối Internet.

## 7.8. Change Adapter Options

**Change Adapter Options** là mục dùng để mở danh sách các card mạng trên Windows. Từ đây, người dùng có thể xem và cấu hình các adapter mạng như Ethernet, Wi-Fi, VPN hoặc adapter ảo.

Để mở Change Adapter Options:

1. Mở **Settings**.
2. Chọn **Network & Internet**.
3. Chọn **Change adapter options** hoặc **Advanced network settings** tùy phiên bản Windows.

![](./img/7.8_change_adapter.png)

Trong cửa sổ Network Connections, người dùng có thể:

* bật hoặc tắt adapter mạng;
* xem trạng thái kết nối;
* đổi tên adapter;
* mở Properties của adapter;
* cấu hình IPv4 hoặc IPv6;
* kiểm tra DNS;
* cấu hình gateway;
* kiểm tra thông tin kết nối mạng.

Ví dụ, để cấu hình địa chỉ IP tĩnh, người dùng có thể:

1. Nhấp chuột phải vào adapter mạng.
2. Chọn **Properties**.
3. Chọn **Internet Protocol Version 4 (TCP/IPv4)**.
4. Nhấn **Properties**.
5. Nhập địa chỉ IP, subnet mask, default gateway và DNS server.

![](./img/7.8_example.png)

Trong môi trường lab an toàn thông tin, Change Adapter Options rất hay được sử dụng để cấu hình địa chỉ IP cho máy ảo, card mạng Host-only, NAT hoặc mạng nội bộ.

## 7.9. Khi nào nên dùng Settings?

Nên dùng Windows Settings khi cần thực hiện các thao tác cấu hình cơ bản, nhanh và phổ biến.

Một số trường hợp nên dùng Settings gồm:

* thay đổi hình nền;
* thay đổi độ phân giải màn hình;
* cấu hình Wi-Fi;
* kiểm tra trạng thái mạng;
* thêm thiết bị Bluetooth;
* quản lý ứng dụng;
* kiểm tra Windows Update;
* cấu hình tài khoản người dùng cơ bản;
* thay đổi ngôn ngữ và thời gian;
* mở Windows Security.

Windows Settings phù hợp với người dùng phổ thông vì giao diện rõ ràng, dễ tìm kiếm và dễ thao tác. Trong Windows 10 và Windows 11, nhiều chức năng mới được Microsoft ưu tiên đưa vào Settings.

Đối với người học cơ bản, nên bắt đầu từ Settings trước vì đây là giao diện đơn giản hơn. Sau đó, khi cần cấu hình sâu hơn, có thể chuyển sang Control Panel hoặc các công cụ quản trị khác.

## 7.10. Khi nào nên dùng Control Panel?

Nên dùng Control Panel khi cần truy cập các thiết lập truyền thống, thiết lập nâng cao hoặc các công cụ quản trị chưa được chuyển hoàn toàn sang Settings.

Một số trường hợp nên dùng Control Panel gồm:

* cấu hình Windows Defender Firewall;
* mở Network and Sharing Center;
* thay đổi thiết lập adapter mạng chi tiết;
* gỡ chương trình bằng Programs and Features;
* cấu hình Power Options nâng cao;
* mở Device Manager;
* cấu hình BitLocker;
* truy cập Administrative Tools;
* thay đổi File Explorer Options;
* cấu hình một số thiết lập hệ thống cũ.

Control Panel đặc biệt hữu ích với quản trị viên hệ thống, người học Windows nâng cao và người làm an toàn thông tin. Nhiều hướng dẫn kỹ thuật, bài lab và công cụ quản trị vẫn sử dụng Control Panel.

Tóm lại, có thể hiểu đơn giản như sau:

* dùng **Settings** cho các cài đặt cơ bản, nhanh và hiện đại;
* dùng **Control Panel** cho các cài đặt chi tiết, truyền thống và nâng cao.

# 8. Task Manager

## 8.1. Task Manager là gì?

**Task Manager** là công cụ quản lý tác vụ của Windows. Công cụ này cho phép người dùng xem các chương trình, tiến trình và dịch vụ đang chạy trên hệ thống.


Thông qua Task Manager, người dùng có thể theo dõi tình trạng sử dụng tài nguyên của máy tính như CPU, RAM, ổ đĩa và mạng. Đây là một công cụ rất quan trọng khi cần kiểm tra hiệu suất hệ thống hoặc xử lý sự cố.

Task Manager thường được dùng để:

- xem ứng dụng nào đang chạy;
- kiểm tra tiến trình đang sử dụng nhiều tài nguyên;
- đóng chương trình bị treo;
- theo dõi CPU, RAM, Disk và Network;
- kiểm tra ứng dụng khởi động cùng Windows;
- xem thông tin người dùng đang đăng nhập;
- hỗ trợ phát hiện tiến trình bất thường.

Đối với người học an toàn thông tin, Task Manager là công cụ cơ bản nhưng rất hữu ích để quan sát hoạt động của hệ thống Windows.


## 8.2. Cách mở Task Manager

Có nhiều cách để mở Task Manager trong Windows.

Cách nhanh nhất là sử dụng tổ hợp phím:

```text
Ctrl + Shift + Esc
````

Ngoài ra, có thể mở Task Manager bằng các cách sau:

1. Nhấn chuột phải vào **Taskbar**.
2. Chọn **Task Manager**.

![](./img/8.2_open_task_manager.png)

Hoặc:

1. Nhấn tổ hợp phím:

```text
Ctrl + Alt + Delete
```

2. Chọn **Task Manager**.

Cũng có thể mở Task Manager từ Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa `Task Manager`.
3. Chọn ứng dụng **Task Manager**.

Trong một số tình huống hệ thống bị chậm hoặc ứng dụng bị treo, tổ hợp phím `Ctrl + Shift + Esc` là cách mở Task Manager nhanh và hiệu quả nhất.

## 8.3. Simple View và More Details

Khi mở Task Manager lần đầu, Windows có thể hiển thị ở dạng đơn giản, gọi là **Simple View**.

![](./img/8.3_task_manager_simple_view.png)

Ở chế độ Simple View, Task Manager chỉ hiển thị danh sách các ứng dụng đang chạy. Người dùng có thể chọn một ứng dụng và nhấn **End task** để đóng ứng dụng đó.

Nếu muốn xem thông tin chi tiết hơn, người dùng có thể nhấn **More details**.

![](./img/8.3_task_manager_more_details.png)

Sau khi chuyển sang chế độ chi tiết, Task Manager sẽ hiển thị nhiều tab hơn, ví dụ:

* Processes;
* Performance;
* App history;
* Startup;
* Users;
* Details;
* Services.

Chế độ **More Details** hữu ích hơn cho quản trị hệ thống và xử lý sự cố vì nó cung cấp thông tin đầy đủ về tiến trình, tài nguyên, hiệu suất và dịch vụ đang chạy.

## 8.4. Tab Processes

Tab **Processes** hiển thị danh sách các ứng dụng và tiến trình đang chạy trên Windows.

![](./img/8.4_tab_processes.png)

Trong tab này, người dùng có thể xem mỗi tiến trình đang sử dụng bao nhiêu tài nguyên hệ thống, bao gồm:

* CPU;
* Memory;
* Disk;
* Network.

Các tiến trình thường được chia thành nhiều nhóm, ví dụ:

* Apps;
* Background processes;
* Windows processes.

**Apps** là các ứng dụng người dùng đang mở, ví dụ như trình duyệt, trình soạn thảo văn bản hoặc File Explorer.

**Background processes** là các tiến trình chạy nền. Chúng có thể thuộc về ứng dụng, dịch vụ hệ thống hoặc phần mềm bảo mật.

**Windows processes** là các tiến trình liên quan trực tiếp đến hoạt động của hệ điều hành Windows.

Tab Processes thường được dùng để xác định chương trình nào đang làm máy tính chậm, chiếm nhiều RAM hoặc sử dụng CPU bất thường.

## 8.5. Tab Performance

Tab **Performance** hiển thị thông tin hiệu suất của hệ thống theo thời gian thực.

![](./img/8.5_tab_performance.png)

Trong tab này, người dùng có thể theo dõi hoạt động của các thành phần phần cứng chính như:

* CPU;
* Memory;
* Disk;
* Ethernet hoặc Wi-Fi;
* GPU nếu hệ thống hỗ trợ.

Thông tin thường được hiển thị dưới dạng biểu đồ, giúp người dùng dễ quan sát mức sử dụng tài nguyên theo thời gian.

Ví dụ, nếu CPU luôn ở mức gần 100%, hệ thống có thể đang chạy một tiến trình nặng hoặc có vấn đề về hiệu suất. Nếu RAM gần đầy, máy tính có thể bị chậm do thiếu bộ nhớ. Nếu Disk hoạt động liên tục ở mức cao, ổ đĩa có thể đang bị quá tải.

Tab Performance rất hữu ích khi cần đánh giá tổng quan tình trạng hoạt động của máy tính.

## 8.6. Theo dõi CPU, RAM, Disk và Network

Task Manager cho phép theo dõi các tài nguyên quan trọng của hệ thống, bao gồm CPU, RAM, Disk và Network.

| Thành phần   | Ý nghĩa                                  |
| ------------ | ---------------------------------------- |
| CPU          | Cho biết mức độ sử dụng bộ xử lý         |
| Memory / RAM | Cho biết lượng bộ nhớ đang được sử dụng  |
| Disk         | Cho biết mức độ đọc/ghi của ổ đĩa        |
| Network      | Cho biết lưu lượng mạng đang gửi và nhận |

Nếu **CPU** sử dụng quá cao trong thời gian dài, máy tính có thể bị chậm, nóng hoặc phản hồi kém.

Nếu **RAM** gần đầy, Windows có thể phải sử dụng bộ nhớ ảo trên ổ đĩa, làm hệ thống chậm hơn.

Nếu **Disk** luôn ở mức cao, máy có thể bị chậm khi mở ứng dụng, sao chép tệp hoặc khởi động hệ thống.

Nếu **Network** có lưu lượng bất thường, có thể có ứng dụng đang tải dữ liệu, đồng bộ dữ liệu hoặc trong một số trường hợp là có tiến trình đáng nghi đang kết nối ra ngoài.

Đối với người làm SOC hoặc điều tra sự cố, việc theo dõi các chỉ số này giúp phát hiện dấu hiệu bất thường ban đầu trên máy tính Windows.

## 8.7. Quản lý ứng dụng đang chạy

Task Manager cho phép người dùng quản lý các ứng dụng và tiến trình đang chạy trên hệ thống.

Một chức năng thường dùng là **End task**. Chức năng này dùng để đóng một ứng dụng hoặc tiến trình khi nó bị treo, không phản hồi hoặc sử dụng quá nhiều tài nguyên.

Các bước đóng một ứng dụng bằng Task Manager:

1. Mở **Task Manager**.
2. Vào tab **Processes**.
3. Chọn ứng dụng hoặc tiến trình cần đóng.
4. Nhấn **End task**.

![](./img/8.7_end_task.png)

Tuy nhiên, cần cẩn thận khi kết thúc tiến trình. Nếu đóng nhầm tiến trình hệ thống quan trọng, Windows có thể hoạt động không ổn định hoặc một số chức năng có thể bị lỗi.

Người dùng nên ưu tiên đóng các ứng dụng thông thường trước, ví dụ như trình duyệt, trình soạn thảo, phần mềm bị treo hoặc chương trình không cần thiết.

Không nên tùy tiện kết thúc các tiến trình thuộc nhóm **Windows processes** nếu không hiểu rõ chức năng của chúng.

## 8.8. Ý nghĩa của Task Manager trong quản trị và xử lý sự cố

Task Manager là một công cụ quan trọng trong quản trị và xử lý sự cố Windows. Công cụ này giúp người dùng nhanh chóng đánh giá tình trạng hoạt động của hệ thống.

Trong quản trị hệ thống, Task Manager có thể được dùng để:

* kiểm tra hiệu suất máy tính;
* xác định ứng dụng gây chậm hệ thống;
* đóng chương trình bị treo;
* theo dõi tài nguyên phần cứng;
* kiểm tra tiến trình chạy nền;
* xem người dùng đang đăng nhập;
* hỗ trợ phân tích sự cố ban đầu.

Trong an toàn thông tin, Task Manager cũng có giá trị nhất định. Nó có thể giúp phát hiện một số dấu hiệu bất thường như:

* tiến trình lạ đang chạy;
* chương trình sử dụng CPU hoặc RAM bất thường;
* lưu lượng mạng bất thường;
* ứng dụng không rõ nguồn gốc;
* tiến trình chạy nền đáng nghi.

Tuy nhiên, Task Manager chỉ là công cụ kiểm tra cơ bản. Trong điều tra bảo mật chuyên sâu, cần kết hợp thêm các công cụ khác như Event Viewer, Resource Monitor, Sysinternals Process Explorer, Windows Defender, EDR hoặc SIEM.

Tóm lại, Task Manager là công cụ đầu tiên nên kiểm tra khi Windows bị chậm, ứng dụng bị treo hoặc hệ thống có dấu hiệu hoạt động bất thường.


# 9. System Configuration — MSConfig

## 9.1. System Configuration là gì?

**System Configuration**, thường được gọi là **MSConfig**, là một công cụ quản trị trong Windows dùng để kiểm tra và thay đổi một số thiết lập liên quan đến quá trình khởi động hệ thống, dịch vụ và công cụ chẩn đoán.

MSConfig thường được sử dụng khi cần khắc phục sự cố Windows, đặc biệt trong các trường hợp máy tính khởi động chậm, dịch vụ gây lỗi hoặc phần mềm nào đó ảnh hưởng đến quá trình hoạt động của hệ thống.

Công cụ này cho phép người dùng quản lý một số thành phần như:

- chế độ khởi động của Windows;
- các dịch vụ đang được bật hoặc tắt;
- tùy chọn khởi động hệ điều hành;
- danh sách công cụ quản trị hệ thống;
- liên kết đến một số tiện ích chẩn đoán khác.

MSConfig không phải là công cụ dùng cho công việc hằng ngày, mà thường được dùng khi cần kiểm tra, phân tích hoặc xử lý lỗi hệ thống.


## 9.2. Cách mở MSConfig

Có nhiều cách để mở công cụ System Configuration trong Windows.

Cách phổ biến nhất là sử dụng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
````

2. Nhập lệnh:

```text
msconfig
```

3. Nhấn **Enter**.

Ngoài ra, có thể mở MSConfig bằng Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
System Configuration
```

3. Chọn ứng dụng **System Configuration**.

Sau khi mở, cửa sổ System Configuration sẽ hiển thị các tab chính như:

* General;
* Boot;
* Services;
* Startup;
* Tools.

Mỗi tab có chức năng riêng và hỗ trợ người dùng kiểm tra các thành phần khác nhau của hệ thống.

## 9.3. Tab General

Tab **General** trong MSConfig cho phép người dùng chọn chế độ khởi động của Windows.

![](./img/9.3_tab_general.png)

Các chế độ thường gặp gồm:

| Chế độ             | Ý nghĩa                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| Normal startup     | Khởi động Windows bình thường với đầy đủ driver, dịch vụ và chương trình |
| Diagnostic startup | Chỉ tải các thiết bị và dịch vụ cơ bản                                   |
| Selective startup  | Cho phép chọn một số thành phần sẽ được tải khi khởi động                |

**Normal startup** là chế độ mặc định. Khi chọn chế độ này, Windows sẽ khởi động đầy đủ các dịch vụ, driver và chương trình như bình thường.

**Diagnostic startup** thường được dùng để kiểm tra lỗi. Khi bật chế độ này, Windows chỉ tải các thành phần cơ bản nhất, giúp xác định xem lỗi có đến từ dịch vụ hoặc chương trình bên thứ ba hay không.

**Selective startup** cho phép người dùng tùy chỉnh các thành phần được tải khi Windows khởi động. Đây là lựa chọn hữu ích khi cần cô lập nguyên nhân gây lỗi nhưng vẫn muốn giữ lại một số dịch vụ cần thiết.

Tab General thường là nơi bắt đầu khi người dùng muốn kiểm tra sự cố liên quan đến quá trình khởi động.

## 9.4. Tab Boot

Tab **Boot** dùng để cấu hình các tùy chọn liên quan đến quá trình khởi động hệ điều hành Windows.

![](./img/9.4_tab_boot.png)

Trong tab này, người dùng có thể xem hệ điều hành đang được cấu hình để khởi động và thay đổi một số tùy chọn nâng cao.

Một số tùy chọn thường gặp trong tab Boot gồm:

| Tùy chọn            | Ý nghĩa                                   |
| ------------------- | ----------------------------------------- |
| Safe boot           | Khởi động Windows ở chế độ an toàn        |
| Minimal             | Chế độ Safe Mode cơ bản                   |
| Alternate shell     | Safe Mode với Command Prompt              |
| Network             | Safe Mode có hỗ trợ mạng                  |
| No GUI boot         | Không hiển thị giao diện khởi động đồ họa |
| Boot log            | Ghi log quá trình khởi động               |
| Base video          | Khởi động với driver đồ họa cơ bản        |
| OS boot information | Hiển thị thông tin driver khi khởi động   |

**Safe boot** là tùy chọn quan trọng khi cần khởi động Windows trong chế độ an toàn để sửa lỗi, gỡ phần mềm hoặc kiểm tra driver.

Ví dụ, nếu Windows bị lỗi sau khi cài một driver mới, người dùng có thể dùng Safe Mode để vào hệ thống và gỡ driver đó.

Tuy nhiên, cần cẩn thận khi thay đổi thiết lập trong tab Boot. Nếu cấu hình sai, Windows có thể khởi động không đúng như mong muốn.

## 9.5. Tab Services

Tab **Services** hiển thị danh sách các dịch vụ trên Windows. Dịch vụ là các chương trình chạy nền để cung cấp chức năng cho hệ điều hành hoặc ứng dụng.

![](./img/9.5_tab_services.png)

Trong tab Services, người dùng có thể:

* xem danh sách dịch vụ;
* kiểm tra dịch vụ đang bật hoặc bị tắt;
* bật hoặc tắt dịch vụ khi khởi động;
* ẩn các dịch vụ của Microsoft;
* kiểm tra dịch vụ bên thứ ba.

Một tùy chọn quan trọng trong tab này là:

```text
Hide all Microsoft services
```

Tùy chọn này giúp ẩn các dịch vụ hệ thống của Microsoft, chỉ hiển thị các dịch vụ của phần mềm bên thứ ba. Đây là cách hữu ích để kiểm tra xem phần mềm bên ngoài có gây lỗi cho Windows hay không.

Ví dụ, nếu máy tính khởi động chậm hoặc thường xuyên bị lỗi, người dùng có thể tạm thời tắt các dịch vụ không thuộc Microsoft để kiểm tra nguyên nhân.

Tuy nhiên, không nên tắt dịch vụ tùy tiện nếu không hiểu chức năng của chúng. Một số dịch vụ có thể liên quan đến phần mềm bảo mật, driver hoặc ứng dụng quan trọng.

## 9.6. Tab Startup

Tab **Startup** từng được dùng để quản lý các chương trình khởi động cùng Windows. Tuy nhiên, trong các phiên bản Windows hiện đại, chức năng quản lý Startup đã được chuyển sang **Task Manager**.

![](./img/9.6_task_startup.png)

Khi mở tab Startup trong MSConfig, Windows thường hiển thị liên kết để mở Task Manager.

Để quản lý chương trình khởi động cùng Windows, người dùng có thể:

1. Mở **Task Manager**.
2. Chọn tab **Startup**.
3. Xem danh sách ứng dụng khởi động cùng hệ thống.
4. Chọn ứng dụng không cần thiết.
5. Nhấn **Disable** để tắt khởi động cùng Windows.

Việc quản lý Startup rất quan trọng vì nhiều chương trình tự động chạy khi Windows khởi động có thể làm máy tính chậm hơn.

Từ góc độ bảo mật, danh sách Startup cũng cần được kiểm tra vì một số mã độc có thể cấu hình để tự chạy khi người dùng đăng nhập vào Windows.

## 9.7. Tab Tools

Tab **Tools** trong MSConfig cung cấp danh sách các công cụ quản trị và chẩn đoán của Windows.

![](./img/9.7_tab_tools.png)

Từ tab này, người dùng có thể chọn một công cụ và nhấn **Launch** để mở nhanh công cụ đó.

Một số công cụ thường có trong tab Tools gồm:

* About Windows;
* Change UAC Settings;
* Security and Maintenance;
* Windows Troubleshooting;
* Computer Management;
* System Information;
* Event Viewer;
* Programs;
* System Properties;
* Internet Options;
* Internet Protocol Configuration;
* Performance Monitor;
* Resource Monitor;
* Task Manager;
* Command Prompt;
* Registry Editor.

Tab Tools rất hữu ích vì nó tập hợp nhiều công cụ quan trọng ở một nơi. Thay vì phải nhớ từng lệnh riêng, người dùng có thể mở MSConfig và chọn công cụ cần dùng.

Trong tab Tools, MSConfig cho phép mở nhanh nhiều công cụ quản trị quan trọng của Windows.

Một số công cụ thường dùng gồm:

| Công cụ             | Chức năng chính                                          |
| ------------------- | -------------------------------------------------------- |
| Change UAC Settings | Thay đổi cài đặt User Account Control                    |
| Computer Management | Quản lý hệ thống, ổ đĩa, người dùng, dịch vụ             |
| System Information  | Xem thông tin phần cứng, phần mềm và môi trường hệ thống |
| Event Viewer        | Xem nhật ký sự kiện Windows                              |
| System Properties   | Xem và thay đổi thuộc tính hệ thống                      |
| Internet Options    | Cấu hình các tùy chọn Internet truyền thống              |
| IP Configuration    | Xem thông tin cấu hình mạng                              |
| Performance Monitor | Theo dõi hiệu suất hệ thống                              |
| Resource Monitor    | Theo dõi CPU, RAM, Disk và Network chi tiết              |
| Task Manager        | Quản lý tiến trình và ứng dụng đang chạy                 |
| Command Prompt      | Mở giao diện dòng lệnh                                   |
| Registry Editor     | Xem và chỉnh sửa Windows Registry                        |

Các công cụ này thường phục vụ cho quản trị, kiểm tra trạng thái hệ thống, xử lý sự cố và phân tích bảo mật.

## 9.8. Vai trò của MSConfig trong khắc phục sự cố

MSConfig có vai trò quan trọng trong quá trình khắc phục sự cố Windows. Công cụ này giúp người dùng kiểm tra xem lỗi có liên quan đến dịch vụ, chương trình khởi động hoặc cấu hình khởi động hay không.

MSConfig thường được sử dụng trong các tình huống như:

* Windows khởi động chậm;
* hệ thống bị lỗi sau khi cài phần mềm;
* nghi ngờ dịch vụ bên thứ ba gây xung đột;
* cần khởi động vào Safe Mode;
* cần tắt tạm thời một số dịch vụ để kiểm tra lỗi;
* cần mở nhanh các công cụ chẩn đoán hệ thống.

Ví dụ, nếu Windows hoạt động bình thường sau khi tắt các dịch vụ bên thứ ba, có thể suy đoán rằng một dịch vụ hoặc phần mềm ngoài Microsoft đang gây ra sự cố.

Trong an toàn thông tin, MSConfig cũng có thể hỗ trợ kiểm tra một số dấu hiệu bất thường, chẳng hạn như dịch vụ lạ, chương trình khởi động đáng nghi hoặc cấu hình hệ thống bị thay đổi.

Tuy nhiên, MSConfig chỉ là công cụ hỗ trợ ban đầu. Khi cần điều tra sâu hơn, nên kết hợp với Task Manager, Event Viewer, Services, Autoruns, Registry Editor và các công cụ bảo mật khác.


# 10. Computer Management

## 10.1. Computer Management là gì?

**Computer Management** là một công cụ quản trị tổng hợp trong Windows. Công cụ này tập hợp nhiều tiện ích quản lý hệ thống vào cùng một giao diện, giúp người dùng và quản trị viên dễ dàng theo dõi, cấu hình và xử lý sự cố trên máy tính.

Thông qua Computer Management, người dùng có thể quản lý nhiều thành phần quan trọng như:

- lịch tác vụ;
- nhật ký sự kiện;
- thư mục chia sẻ;
- người dùng và nhóm cục bộ;
- hiệu suất hệ thống;
- thiết bị phần cứng;
- ổ đĩa và phân vùng;
- dịch vụ Windows;
- WMI Control.

Computer Management đặc biệt hữu ích trong quản trị hệ thống vì thay vì phải mở từng công cụ riêng lẻ, người dùng có thể truy cập nhiều công cụ quan trọng từ một cửa sổ duy nhất.

Trong lĩnh vực an toàn thông tin, Computer Management cũng rất quan trọng vì nó hỗ trợ kiểm tra tài khoản người dùng, nhóm quyền, dịch vụ đang chạy, log sự kiện và các tài nguyên được chia sẻ trên hệ thống.


## 10.2. Cách mở `compmgmt.msc`

Có nhiều cách để mở Computer Management trong Windows.

Cách phổ biến nhất là dùng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
````

2. Nhập lệnh:

```text
compmgmt.msc
```

3. Nhấn **Enter**.

Ngoài ra, có thể mở bằng Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
Computer Management
```

3. Chọn **Computer Management**.

Cũng có thể mở từ menu chuột phải:

1. Nhấp chuột phải vào **This PC** hoặc **Computer**.
2. Chọn **Manage**.

![](./img/10.2_computer_managerment.png)

Sau khi mở, cửa sổ Computer Management thường được chia thành ba nhóm chính:

* **System Tools**;
* **Storage**;
* **Services and Applications**.

## 10.3. System Tools

**System Tools** là nhóm công cụ dùng để quản lý và giám sát các thành phần hệ thống. Đây là phần quan trọng nhất trong Computer Management vì chứa nhiều tiện ích phục vụ quản trị, kiểm tra log và xử lý sự cố.

![](./img/10.3_system_tools.png)

Trong System Tools thường có các công cụ như:

* Task Scheduler;
* Event Viewer;
* Shared Folders;
* Local Users and Groups;
* Performance Monitor;
* Device Manager.

Nhóm System Tools giúp quản trị viên kiểm tra tình trạng hoạt động của Windows, xem sự kiện hệ thống, quản lý tài khoản cục bộ, kiểm tra thiết bị phần cứng và theo dõi hiệu suất.

Đối với người học SOC, System Tools rất cần thiết vì nhiều dữ liệu phục vụ điều tra sự cố ban đầu có thể được tìm thấy tại đây, đặc biệt là trong Event Viewer, Local Users and Groups và Performance Monitor.


### 10.3.1. Task Scheduler

**Task Scheduler** là công cụ dùng để tạo và quản lý các tác vụ tự động trong Windows.

![](./img/10.3.1_task_scheduler.png)

Thông qua Task Scheduler, Windows hoặc người dùng có thể cấu hình một chương trình, script hoặc lệnh chạy tự động theo một điều kiện nhất định.

Ví dụ, một tác vụ có thể được cấu hình để chạy khi:

* hệ thống khởi động;
* người dùng đăng nhập;
* đến một thời điểm cụ thể;
* sau một khoảng thời gian lặp lại;
* một sự kiện nhất định xuất hiện trong log.

Task Scheduler thường được dùng cho các mục đích hợp pháp như:

* chạy script bảo trì;
* tự động sao lưu;
* kiểm tra cập nhật;
* chạy chương trình theo lịch;
* thực hiện tác vụ quản trị định kỳ.

Tuy nhiên, từ góc độ an toàn thông tin, Task Scheduler cũng là nơi cần kiểm tra vì kẻ tấn công có thể tạo scheduled task để duy trì persistence, tức là tự động chạy lại mã độc sau khi máy tính khởi động hoặc người dùng đăng nhập.

### 10.3.2. Event Viewer

**Event Viewer** là công cụ dùng để xem nhật ký sự kiện của Windows. Đây là một trong những công cụ quan trọng nhất khi xử lý sự cố và phân tích bảo mật.

![](./img/10.3.2_event_viewer.png)

Windows ghi lại nhiều loại sự kiện khác nhau trong Event Viewer, ví dụ:

* lỗi ứng dụng;
* lỗi hệ thống;
* cảnh báo;
* thông tin hoạt động;
* đăng nhập thành công;
* đăng nhập thất bại;
* thay đổi chính sách;
* hoạt động của dịch vụ.

Các nhóm log thường gặp gồm:

| Nhóm log         | Ý nghĩa                                                   |
| ---------------- | --------------------------------------------------------- |
| Application      | Ghi sự kiện liên quan đến ứng dụng                        |
| Security         | Ghi sự kiện bảo mật, đăng nhập, kiểm toán                 |
| System           | Ghi sự kiện liên quan đến hệ thống và dịch vụ             |
| Setup            | Ghi sự kiện liên quan đến cài đặt và cập nhật             |
| Forwarded Events | Chứa sự kiện được chuyển tiếp từ máy khác nếu có cấu hình |

Trong quản trị hệ thống, Event Viewer giúp tìm nguyên nhân lỗi hệ thống, lỗi ứng dụng hoặc lỗi dịch vụ.

Trong SOC, Event Viewer rất quan trọng vì nhiều dấu hiệu tấn công có thể được phát hiện qua Windows Logs, đặc biệt là log đăng nhập, tạo tài khoản, thay đổi quyền, chạy dịch vụ hoặc lỗi bất thường.

### 10.3.3. Shared Folders

**Shared Folders** là công cụ dùng để xem và quản lý các thư mục được chia sẻ trên máy tính Windows.

![](./img/10.3.3_share_folders.png)

Thông qua Shared Folders, người dùng có thể kiểm tra:

* các thư mục đang được chia sẻ;
* các phiên kết nối đến thư mục chia sẻ;
* các tệp đang được mở qua mạng.

Shared Folders thường có ba phần chính:

| Mục        | Ý nghĩa                                    |
| ---------- | ------------------------------------------ |
| Shares     | Hiển thị các thư mục đang được chia sẻ     |
| Sessions   | Hiển thị các phiên người dùng đang kết nối |
| Open Files | Hiển thị các tệp đang được mở qua mạng     |

Công cụ này rất hữu ích trong môi trường doanh nghiệp vì nhiều máy Windows có thể chia sẻ thư mục hoặc tài nguyên qua mạng nội bộ.

Từ góc độ bảo mật, cần kiểm tra Shared Folders để phát hiện:

* thư mục bị chia sẻ nhầm;
* quyền truy cập quá rộng;
* người dùng lạ đang kết nối;
* tệp nhạy cảm đang được mở qua mạng;
* chia sẻ ẩn hoặc chia sẻ không cần thiết.

Việc cấu hình sai thư mục chia sẻ có thể dẫn đến rò rỉ dữ liệu hoặc truy cập trái phép.


### 10.3.4. Local Users and Groups

**Local Users and Groups** là công cụ dùng để quản lý tài khoản người dùng và nhóm cục bộ trên máy Windows.

![](./img/10.3.4_local_users_and_groups.png)

Trong công cụ này có hai phần chính:

* **Users**;
* **Groups**.

Phần **Users** hiển thị các tài khoản cục bộ trên máy. Phần **Groups** hiển thị các nhóm cục bộ và thành viên của từng nhóm.

Thông qua Local Users and Groups, quản trị viên có thể:

* tạo tài khoản người dùng mới;
* đổi mật khẩu;
* vô hiệu hóa tài khoản;
* thêm người dùng vào nhóm;
* xóa người dùng khỏi nhóm;
* kiểm tra tài khoản lạ;
* kiểm tra nhóm có quyền cao.

Một nhóm đặc biệt cần chú ý là **Administrators**. Người dùng thuộc nhóm này có quyền quản trị trên hệ thống.

Trong an toàn thông tin, Local Users and Groups thường được kiểm tra để xác định liệu có tài khoản bất thường, tài khoản bị tạo trái phép hoặc người dùng không phù hợp nằm trong nhóm quản trị hay không.

### 10.3.5. Performance Monitor

**Performance Monitor** là công cụ dùng để theo dõi hiệu suất hệ thống Windows một cách chi tiết.

![](./img/10.3.5_performance.png)

Công cụ này cho phép người dùng quan sát nhiều chỉ số hoạt động của hệ thống, ví dụ:

* CPU;
* RAM;
* ổ đĩa;
* mạng;
* tiến trình;
* dịch vụ;
* bộ đếm hiệu suất.

Performance Monitor có thể hiển thị dữ liệu theo thời gian thực hoặc ghi lại dữ liệu để phân tích sau.

So với Task Manager, Performance Monitor chi tiết hơn và phù hợp hơn cho việc theo dõi lâu dài hoặc phân tích hiệu suất chuyên sâu.

Một số tình huống sử dụng Performance Monitor gồm:

* kiểm tra nguyên nhân máy chạy chậm;
* theo dõi mức sử dụng CPU hoặc RAM theo thời gian;
* phân tích nghẽn cổ chai hệ thống;
* giám sát hiệu suất máy chủ;
* thu thập dữ liệu phục vụ báo cáo kỹ thuật.

Trong môi trường doanh nghiệp, Performance Monitor có thể hỗ trợ quản trị viên phát hiện sớm vấn đề về tài nguyên trước khi hệ thống bị gián đoạn.

### 10.3.6. Device Manager

**Device Manager** là công cụ dùng để quản lý thiết bị phần cứng và driver trong Windows.

![](./img/10.3.6_device_manager.png)

Thông qua Device Manager, người dùng có thể xem danh sách các thiết bị được hệ thống nhận diện, chẳng hạn như:

* card mạng;
* card đồ họa;
* ổ đĩa;
* bàn phím;
* chuột;
* màn hình;
* USB controller;
* thiết bị âm thanh;
* thiết bị Bluetooth.

Device Manager cho phép thực hiện các thao tác như:

* kiểm tra trạng thái thiết bị;
* cập nhật driver;
* gỡ driver;
* vô hiệu hóa thiết bị;
* bật lại thiết bị;
* xem thuộc tính phần cứng;
* kiểm tra lỗi driver.

Nếu một thiết bị có vấn đề, Device Manager thường hiển thị biểu tượng cảnh báo màu vàng. Đây là dấu hiệu cho thấy thiết bị có thể bị lỗi driver, không hoạt động đúng hoặc chưa được cài đặt đầy đủ.

Trong an toàn thông tin, Device Manager cũng có thể hỗ trợ kiểm tra các thiết bị lạ, adapter mạng ảo, USB bất thường hoặc phần cứng không được phép kết nối vào hệ thống.


## 10.4. Storage

**Storage** là nhóm công cụ dùng để quản lý thiết bị lưu trữ, ổ đĩa và phân vùng trong Windows.

![](./img/10.4_storage.png)

Thành phần quan trọng nhất trong nhóm Storage là **Disk Management**. Công cụ này cho phép người dùng xem và quản lý các ổ đĩa vật lý, phân vùng, volume và ký tự ổ đĩa.

Thông qua Storage, người dùng có thể:

* xem danh sách ổ đĩa;
* kiểm tra dung lượng ổ đĩa;
* tạo phân vùng mới;
* xóa phân vùng;
* định dạng phân vùng;
* thay đổi ký tự ổ đĩa;
* kiểm tra trạng thái volume;
* quản lý ổ đĩa gắn ngoài.

Trong quản trị hệ thống, Storage rất quan trọng vì lỗi ổ đĩa, thiếu dung lượng hoặc cấu hình phân vùng sai có thể ảnh hưởng trực tiếp đến hoạt động của Windows.

Trong an toàn thông tin, việc kiểm tra Storage cũng có ý nghĩa khi cần phân tích ổ đĩa, xác định phân vùng lạ, kiểm tra thiết bị lưu trữ ngoài hoặc chuẩn bị môi trường điều tra số.

### 10.4.1. Disk Management

**Disk Management** là công cụ dùng để quản lý ổ đĩa, phân vùng và volume trong Windows.

![](./img/10.4.1_disk_managerment.png)

Thông qua Disk Management, người dùng có thể:

* xem ổ đĩa vật lý;
* xem phân vùng;
* tạo volume mới;
* xóa volume;
* định dạng phân vùng;
* thay đổi ký tự ổ đĩa;
* mở rộng hoặc thu nhỏ volume;
* kiểm tra trạng thái ổ đĩa;
* quản lý ổ đĩa gắn ngoài.

Ví dụ, khi cắm một ổ USB hoặc thêm ổ đĩa mới vào máy tính, Disk Management có thể được dùng để kiểm tra ổ đĩa đã được nhận hay chưa và có ký tự ổ đĩa hay chưa.

Cần cẩn thận khi sử dụng Disk Management vì các thao tác như xóa volume hoặc định dạng ổ đĩa có thể làm mất dữ liệu.

Trong điều tra số và an toàn thông tin, Disk Management có thể giúp kiểm tra cấu trúc ổ đĩa, phát hiện phân vùng lạ hoặc xác định các thiết bị lưu trữ đang được kết nối.

## 10.5. Services and Applications

**Services and Applications** là nhóm công cụ dùng để quản lý các dịch vụ và một số thành phần ứng dụng hệ thống.

![](./img/10.5_services_and_applications.png)

Trong nhóm này thường có:

* Services;
* WMI Control.

**Services** cho phép xem và quản lý các dịch vụ đang chạy hoặc được cấu hình trên Windows. **WMI Control** liên quan đến Windows Management Instrumentation, một cơ chế cho phép quản lý và truy vấn thông tin hệ thống.

Nhóm Services and Applications thường được sử dụng khi cần:

* kiểm tra dịch vụ đang chạy;
* khởi động hoặc dừng dịch vụ;
* thay đổi kiểu khởi động của dịch vụ;
* kiểm tra dịch vụ bất thường;
* xem cấu hình WMI;
* xử lý lỗi liên quan đến dịch vụ nền.

Từ góc độ bảo mật, đây là phần cần chú ý vì nhiều mã độc hoặc công cụ tấn công có thể tạo dịch vụ để duy trì quyền truy cập lâu dài trên hệ thống.

### 10.5.1. Services

**Services** là công cụ dùng để quản lý các dịch vụ chạy nền trong Windows.

![](./img/10.6.1_services.png)

Dịch vụ là các chương trình chạy ở chế độ nền để cung cấp chức năng cho hệ điều hành hoặc ứng dụng. Một số dịch vụ khởi động cùng Windows, một số khác chỉ chạy khi cần.

Thông qua Services, người dùng có thể:

* xem danh sách dịch vụ;
* kiểm tra trạng thái dịch vụ;
* khởi động dịch vụ;
* dừng dịch vụ;
* khởi động lại dịch vụ;
* thay đổi kiểu khởi động;
* xem mô tả dịch vụ;
* kiểm tra tài khoản dùng để chạy dịch vụ.

Các kiểu khởi động thường gặp gồm:

| Kiểu khởi động          | Ý nghĩa                                      |
| ----------------------- | -------------------------------------------- |
| Automatic               | Tự động chạy khi Windows khởi động           |
| Automatic Delayed Start | Tự động chạy sau khi hệ thống khởi động xong |
| Manual                  | Chỉ chạy khi được gọi                        |
| Disabled                | Bị vô hiệu hóa                               |

Trong an toàn thông tin, Services là khu vực rất quan trọng vì kẻ tấn công có thể tạo dịch vụ độc hại để duy trì quyền truy cập. Vì vậy, khi điều tra hệ thống Windows, cần kiểm tra các dịch vụ lạ, dịch vụ mới được tạo hoặc dịch vụ chạy từ đường dẫn bất thường.

### 10.5.2. WMI Control

**WMI Control** là công cụ dùng để quản lý và cấu hình **Windows Management Instrumentation**, viết tắt là **WMI**.

![](./img/10.6.2_wmi_control.png)

WMI là một thành phần của Windows cho phép truy vấn thông tin hệ thống, quản lý thiết bị, quản lý dịch vụ và thực hiện một số thao tác quản trị từ xa hoặc cục bộ.

Thông qua WMI, quản trị viên hoặc công cụ quản lý có thể lấy thông tin như:

* tên máy;
* hệ điều hành;
* phần cứng;
* tiến trình;
* dịch vụ;
* ổ đĩa;
* thông tin mạng;
* trạng thái hệ thống.

WMI Control trong Computer Management cho phép kiểm tra thuộc tính, cấu hình và trạng thái của WMI trên máy tính.

Trong quản trị hệ thống, WMI rất hữu ích vì nó hỗ trợ tự động hóa và quản lý nhiều máy tính. Tuy nhiên, trong an toàn thông tin, WMI cũng là một thành phần cần chú ý vì kẻ tấn công có thể lạm dụng WMI để thực thi lệnh, thu thập thông tin hoặc duy trì persistence.

Vì vậy, khi phân tích bảo mật Windows, cần quan tâm đến các hoạt động bất thường liên quan đến WMI, đặc biệt trong môi trường doanh nghiệp hoặc domain.


# 11. Task Scheduler

## 11.1. Task Scheduler là gì?

**Task Scheduler** là công cụ trong Windows dùng để tạo, quản lý và tự động chạy các tác vụ theo điều kiện hoặc thời gian nhất định.

Thông qua Task Scheduler, người dùng hoặc quản trị viên có thể cấu hình để Windows tự động chạy một chương trình, script, lệnh hoặc tác vụ hệ thống mà không cần thao tác thủ công.

Ví dụ, Task Scheduler có thể được dùng để:

- chạy script sao lưu dữ liệu hằng ngày;
- tự động mở một chương trình vào thời điểm nhất định;
- chạy tác vụ bảo trì hệ thống;
- kiểm tra cập nhật;
- xóa tệp tạm theo lịch;
- chạy lệnh khi người dùng đăng nhập;
- thực hiện hành động khi hệ thống khởi động.

Task Scheduler rất hữu ích trong quản trị hệ thống vì nó giúp tự động hóa các công việc lặp lại. Tuy nhiên, từ góc độ an toàn thông tin, đây cũng là một thành phần cần kiểm tra vì kẻ tấn công có thể lợi dụng scheduled task để duy trì quyền truy cập trên hệ thống.


## 11.2. Tác vụ tự động trong Windows

Tác vụ tự động trong Windows là những công việc được cấu hình để chạy mà không cần người dùng trực tiếp khởi động.

Một tác vụ tự động thường bao gồm ba thành phần chính:

- **Trigger**: điều kiện kích hoạt tác vụ;
- **Action**: hành động sẽ được thực hiện;
- **Conditions/Settings**: điều kiện bổ sung và thiết lập nâng cao.

Ví dụ, một tác vụ có thể được cấu hình như sau:

```text
Trigger: chạy mỗi ngày lúc 08:00
Action: chạy file backup.bat
````

Hoặc:

```text
Trigger: khi người dùng đăng nhập
Action: mở một chương trình giám sát hệ thống
```

Trong Windows, nhiều tác vụ hệ thống cũng được tạo sẵn để phục vụ cập nhật, bảo trì, đồng bộ thời gian, kiểm tra bảo mật hoặc thu thập thông tin hệ thống.

Việc hiểu tác vụ tự động giúp người học quản trị Windows biết cách tự động hóa công việc, đồng thời biết kiểm tra các tác vụ bất thường khi phân tích sự cố.

## 11.3. Tạo Basic Task

**Create Basic Task** là chức năng trong Task Scheduler dùng để tạo một tác vụ tự động đơn giản thông qua giao diện hướng dẫn từng bước.

Để tạo Basic Task, có thể thực hiện như sau:

1. Mở **Task Scheduler**.

![](./img/11.3_open_task_scheduler.png)

2. Chọn **Create Basic Task**.

![](./img/11.3_open_create_a_basic_task.png)

3. Nhập tên và mô tả cho tác vụ.

![](./img/11.3_enter_name.png)

4. Chọn **Trigger** để xác định khi nào tác vụ chạy.

![](./img/11.3_select_trigger.png)

5. Chọn **Action** để xác định hành động cần thực hiện.

![](./img/11.3_select_action.png)

6. Chọn chương trình cần chạy 

![](./img/11.3_select_program.png)

7. Nhấn **Finish** để hoàn tất.

![](./img/11.3_finish.png)

## 11.4. Trigger trong Task Scheduler

**Trigger** là điều kiện dùng để kích hoạt một tác vụ trong Task Scheduler.

Nói cách khác, Trigger trả lời câu hỏi: **khi nào tác vụ sẽ chạy?**

Một số loại Trigger thường gặp gồm:

| Trigger                         | Ý nghĩa                                               |
| ------------------------------- | ----------------------------------------------------- |
| Daily                           | Chạy hằng ngày                                        |
| Weekly                          | Chạy hằng tuần                                        |
| Monthly                         | Chạy hằng tháng                                       |
| One time                        | Chạy một lần tại thời điểm cụ thể                     |
| When the computer starts        | Chạy khi máy tính khởi động                           |
| When I log on                   | Chạy khi người dùng đăng nhập                         |
| When a specific event is logged | Chạy khi một sự kiện cụ thể xuất hiện trong Event Log |

Ví dụ, nếu muốn chạy script kiểm tra hệ thống mỗi sáng, có thể chọn Trigger là **Daily** và đặt thời gian là `08:00`.

Nếu muốn chạy chương trình khi người dùng đăng nhập vào Windows, có thể chọn Trigger là **When I log on**.

Trigger rất quan trọng vì nếu cấu hình sai, tác vụ có thể không chạy đúng thời điểm hoặc chạy quá thường xuyên, gây ảnh hưởng đến hiệu suất hệ thống.

## 11.5. Action trong Task Scheduler

**Action** là hành động mà Task Scheduler sẽ thực hiện khi Trigger được kích hoạt.

Nói cách khác, Action trả lời câu hỏi: **tác vụ sẽ làm gì?**

Action phổ biến nhất là:

```text
Start a program
```

Với Action này, Task Scheduler có thể chạy:

* một chương trình `.exe`;
* một script `.bat`;
* một script PowerShell `.ps1`;
* một lệnh hệ thống;
* một công cụ quản trị;
* một file thực thi do người dùng chỉ định.

Ví dụ:

```text
Action: Start a program
Program/script: powershell.exe
Arguments: -File C:\Scripts\check_logs.ps1
```

Hoặc:

```text
Action: Start a program
Program/script: C:\Scripts\backup.bat
```

Khi cấu hình Action, cần kiểm tra kỹ đường dẫn đến chương trình hoặc script. Nếu đường dẫn sai, tác vụ sẽ không chạy thành công.

Từ góc độ bảo mật, phần Action rất quan trọng vì nó cho biết tác vụ đang chạy chương trình hoặc lệnh nào. Khi điều tra hệ thống, nếu thấy một scheduled task chạy file lạ trong thư mục tạm, thư mục người dùng hoặc đường dẫn bất thường, cần kiểm tra kỹ.

## 11.6. Ứng dụng Task Scheduler trong quản trị hệ thống

Task Scheduler được sử dụng rất nhiều trong quản trị hệ thống vì nó giúp tự động hóa các công việc lặp lại.

Một số ứng dụng phổ biến gồm:

* tự động sao lưu dữ liệu;
* chạy script kiểm tra hệ thống;
* xóa file tạm định kỳ;
* thu thập log;
* kiểm tra dung lượng ổ đĩa;
* khởi động lại dịch vụ theo lịch;
* gửi báo cáo hệ thống;
* chạy tác vụ bảo trì ngoài giờ làm việc.

Ví dụ, quản trị viên có thể tạo một scheduled task để chạy script kiểm tra dung lượng ổ đĩa mỗi ngày. Nếu dung lượng còn quá thấp, script có thể ghi log hoặc gửi cảnh báo.

Một ví dụ khác là tự động chạy script thu thập log từ máy trạm vào cuối ngày để phục vụ giám sát bảo mật.

Task Scheduler giúp giảm thao tác thủ công, giảm sai sót và đảm bảo các công việc quan trọng được thực hiện đúng lịch.

Tuy nhiên, cần quản lý Task Scheduler cẩn thận. Nếu có quá nhiều tác vụ không cần thiết, hệ thống có thể bị chậm hoặc khó kiểm soát.

## 11.7. Ý nghĩa bảo mật của Scheduled Tasks

Từ góc độ an toàn thông tin, **Scheduled Tasks** là một khu vực rất quan trọng cần kiểm tra trong Windows.

Kẻ tấn công có thể lợi dụng Task Scheduler để duy trì **persistence**, tức là giữ khả năng tự động chạy lại mã độc sau khi máy tính khởi động hoặc sau khi người dùng đăng nhập.

Ví dụ, một mã độc có thể tạo scheduled task để:

* chạy file độc hại khi Windows khởi động;
* chạy script PowerShell khi người dùng đăng nhập;
* kết nối ra máy chủ điều khiển theo lịch;
* tải thêm payload từ Internet;
* khôi phục lại mã độc nếu bị xóa;
* thực hiện lệnh định kỳ mà người dùng không biết.

Khi phân tích bảo mật, cần kiểm tra các yếu tố sau:

* tên tác vụ có bất thường không;
* tác vụ được tạo khi nào;
* tác vụ chạy bằng tài khoản nào;
* Trigger của tác vụ là gì;
* Action của tác vụ chạy file hoặc lệnh nào;
* đường dẫn chương trình có đáng tin cậy không;
* tác vụ có chạy từ thư mục tạm hoặc thư mục người dùng không;
* tác vụ có dùng PowerShell, cmd.exe hoặc script lạ không.

Một số dấu hiệu đáng nghi gồm:

* tên tác vụ giống hệ thống nhưng viết sai hoặc lạ;
* tác vụ chạy file trong `AppData`, `Temp` hoặc `Downloads`;
* tác vụ chạy PowerShell với tham số khó hiểu;
* tác vụ mới được tạo gần thời điểm xảy ra sự cố;
* tác vụ chạy bằng tài khoản có quyền cao;
* tác vụ không có mô tả rõ ràng.

Vì vậy, trong điều tra sự cố Windows, Task Scheduler là một trong những nơi cần kiểm tra sớm. Nó giúp phát hiện các cơ chế tự động chạy chương trình, cả hợp pháp lẫn độc hại.

# 12. Event Viewer và Windows Logs

## 12.1. Event Viewer là gì?

**Event Viewer** là công cụ trong Windows dùng để xem và phân tích các sự kiện được hệ điều hành, ứng dụng và dịch vụ ghi lại trong quá trình hoạt động.

Trong Windows, nhiều hành động quan trọng đều có thể được ghi thành log, ví dụ:

- ứng dụng bị lỗi;
- dịch vụ khởi động hoặc dừng;
- hệ thống gặp lỗi phần cứng hoặc driver;
- người dùng đăng nhập thành công;
- người dùng đăng nhập thất bại;
- thay đổi chính sách bảo mật;
- thay đổi tài khoản hoặc quyền truy cập.

Event Viewer giúp người dùng và quản trị viên xem lại những gì đã xảy ra trên hệ thống. Đây là công cụ rất quan trọng khi cần xử lý sự cố, kiểm tra lỗi hoặc điều tra các dấu hiệu bất thường.

Có thể mở Event Viewer bằng lệnh:

```text
eventvwr.msc
````

Hoặc mở thông qua:

```text
Computer Management → System Tools → Event Viewer
```
![](./img/12.1_event_viewer.png)

## 12.2. Vai trò của Event Viewer trong điều tra sự cố

Event Viewer có vai trò quan trọng trong điều tra sự cố vì nó lưu lại nhiều thông tin về hoạt động của hệ thống Windows.

Khi máy tính gặp lỗi, người dùng thường chỉ nhìn thấy biểu hiện bên ngoài như máy chậm, ứng dụng bị treo, dịch vụ không chạy hoặc không đăng nhập được. Tuy nhiên, Event Viewer có thể cung cấp thông tin chi tiết hơn về nguyên nhân.

Ví dụ, Event Viewer có thể giúp xác định:

* ứng dụng nào bị lỗi;
* dịch vụ nào không khởi động được;
* driver nào gây lỗi;
* thời điểm xảy ra sự cố;
* người dùng nào đã đăng nhập;
* có bao nhiêu lần đăng nhập thất bại;
* hệ thống có bị tắt bất thường hay không;
* có thay đổi bảo mật nào xảy ra hay không.

Trong quá trình điều tra, quản trị viên thường dùng Event Viewer để đối chiếu thời gian xảy ra sự cố với các sự kiện được ghi lại trong log.

Ví dụ, nếu người dùng báo rằng máy bị lỗi lúc 09:30, quản trị viên có thể mở Event Viewer và kiểm tra các sự kiện gần thời điểm đó để tìm nguyên nhân.

## 12.3. Các loại sự kiện trong Windows

Windows phân loại sự kiện theo mức độ và mục đích ghi log. Mỗi loại sự kiện cho biết tính chất của thông tin được ghi lại.

Các loại sự kiện thường gặp gồm:

* Error;
* Warning;
* Information;
* Success Audit;
* Failure Audit.

### 12.3.1. Error

**Error** là loại sự kiện cho biết đã xảy ra lỗi nghiêm trọng hoặc một thành phần nào đó không hoạt động đúng.

![](./img/12.3_error.png)

Ví dụ về Error:

* ứng dụng bị crash;
* dịch vụ không khởi động được;
* driver bị lỗi;
* hệ thống không đọc được một thành phần cần thiết;
* lỗi liên quan đến ổ đĩa hoặc phần cứng.

Sự kiện Error thường cần được kiểm tra kỹ, đặc biệt nếu nó xuất hiện lặp lại nhiều lần hoặc xảy ra gần thời điểm hệ thống gặp sự cố.

Trong điều tra sự cố, Error là một trong những loại log được kiểm tra đầu tiên.

### 12.3.2. Warning

**Warning** là loại sự kiện cảnh báo rằng có vấn đề tiềm ẩn, nhưng chưa chắc đã gây lỗi nghiêm trọng ngay lập tức.

![](./img/12.3_warning.png)

Ví dụ về Warning:

* dịch vụ phản hồi chậm;
* ổ đĩa gần đầy;
* kết nối mạng không ổn định;
* cấu hình có khả năng gây lỗi;
* một thành phần hệ thống hoạt động không như mong đợi.

Warning không phải lúc nào cũng nguy hiểm, nhưng nếu xuất hiện thường xuyên, nó có thể là dấu hiệu cho thấy hệ thống đang có vấn đề.

Trong quản trị hệ thống, Warning giúp phát hiện sớm sự cố trước khi nó trở thành lỗi nghiêm trọng.

### 12.3.3. Information

**Information** là loại sự kiện ghi lại các hoạt động bình thường của hệ thống, ứng dụng hoặc dịch vụ.

![](./img/12.3_information.png)

Ví dụ về Information:

* dịch vụ đã khởi động thành công;
* ứng dụng đã hoàn thành một tác vụ;
* hệ thống đã cài đặt cập nhật;
* một thành phần Windows hoạt động bình thường;
* chương trình ghi nhận trạng thái hoạt động.

Information thường không phải là dấu hiệu lỗi. Tuy nhiên, nó vẫn hữu ích khi cần dựng lại chuỗi sự kiện trong quá trình điều tra.

Ví dụ, khi phân tích một sự cố, log Information có thể giúp xác định dịch vụ nào đã chạy trước khi lỗi xảy ra.

### 12.3.4. Success Audit

**Success Audit** là sự kiện ghi lại một hành động bảo mật đã thực hiện thành công.

![](./img/12.3_succes_audit.png)

Ví dụ về Success Audit:

* đăng nhập thành công;
* truy cập tài nguyên thành công;
* thay đổi chính sách thành công;
* thao tác quản trị được thực hiện thành công;
* kiểm toán một hành động bảo mật thành công.

Loại sự kiện này thường xuất hiện trong **Security Log**.

Trong SOC, Success Audit rất quan trọng vì nó giúp xác định tài khoản nào đã đăng nhập, đăng nhập vào thời điểm nào và thực hiện hành động gì trên hệ thống.

### 12.3.5. Failure Audit

**Failure Audit** là sự kiện ghi lại một hành động bảo mật không thành công.

![](./img/12.3_failure_audit.png)

Ví dụ về Failure Audit:

* đăng nhập thất bại;
* nhập sai mật khẩu;
* truy cập tài nguyên bị từ chối;
* thao tác quản trị không được phép;
* cố gắng sử dụng quyền không hợp lệ.

Failure Audit rất quan trọng trong phát hiện tấn công. Nhiều lần đăng nhập thất bại trong thời gian ngắn có thể là dấu hiệu của brute-force attack hoặc credential guessing.

Trong điều tra bảo mật, Failure Audit giúp xác định các hành vi truy cập trái phép hoặc cố gắng vượt qua cơ chế xác thực.

## 12.4. Windows Logs

**Windows Logs** là nhóm log chính trong Event Viewer, nơi Windows lưu lại các sự kiện quan trọng của hệ thống, ứng dụng và bảo mật.

![](./img/12.4_windows_logs.png)

Các log thường gặp gồm:

* Application;
* Security;
* System;
* Setup;
* Forwarded Events;
* Custom Logs nếu có cấu hình riêng.

Trong đó, Application, Security và System là ba nhóm log thường được sử dụng nhiều nhất khi xử lý sự cố và điều tra bảo mật.

### 12.4.1. Application Log

**Application Log** ghi lại các sự kiện liên quan đến ứng dụng chạy trên Windows.

![](./img/12.4_application_logs.png)

Các sự kiện trong Application Log có thể bao gồm:

* ứng dụng bị lỗi;
* ứng dụng crash;
* ứng dụng không khởi động được;
* phần mềm ghi nhận trạng thái hoạt động;
* lỗi liên quan đến dịch vụ ứng dụng.

Ví dụ, nếu một phần mềm văn phòng hoặc phần mềm nghiệp vụ bị lỗi, thông tin lỗi có thể được ghi trong Application Log.

Application Log hữu ích khi cần xác định nguyên nhân lỗi ở tầng ứng dụng.

### 12.4.2. Security Log

**Security Log** ghi lại các sự kiện liên quan đến bảo mật và kiểm toán trong Windows.

![](./img/12.4_security_logs.png)

Đây là một trong những log quan trọng nhất đối với SOC và điều tra sự cố bảo mật.

Security Log có thể chứa các sự kiện như:

* đăng nhập thành công;
* đăng nhập thất bại;
* đăng xuất;
* thay đổi tài khoản người dùng;
* thay đổi nhóm;
* thay đổi chính sách bảo mật;
* truy cập tài nguyên;
* sử dụng quyền đặc biệt.

Ví dụ, nếu có nhiều lần đăng nhập thất bại vào một tài khoản trong thời gian ngắn, Security Log có thể giúp phát hiện dấu hiệu tấn công mật khẩu.

Security Log thường được thu thập bởi SIEM hoặc EDR để phân tích tập trung trong môi trường doanh nghiệp.

### 12.4.3. System Log

**System Log** ghi lại các sự kiện liên quan đến hệ điều hành Windows và các thành phần hệ thống.

![](./img/12.4_system_logs.png)

System Log có thể bao gồm:

* lỗi driver;
* lỗi dịch vụ hệ thống;
* sự kiện khởi động hoặc tắt máy;
* lỗi phần cứng;
* lỗi ổ đĩa;
* lỗi mạng;
* trạng thái của các dịch vụ Windows.

Ví dụ, nếu một dịch vụ Windows không khởi động được, sự kiện liên quan có thể xuất hiện trong System Log.

System Log rất quan trọng khi xử lý các lỗi liên quan đến hệ điều hành, phần cứng hoặc dịch vụ nền.

### 12.4.4. Custom Logs

**Custom Logs** là các log tùy chỉnh hoặc log riêng do ứng dụng, dịch vụ hoặc cấu hình quản trị tạo ra.

Không giống các log mặc định như Application, Security và System, Custom Logs phụ thuộc vào phần mềm hoặc chính sách được cài đặt trên hệ thống.

Ví dụ, một số ứng dụng doanh nghiệp, phần mềm bảo mật hoặc công cụ giám sát có thể tạo log riêng trong Event Viewer.

Custom Logs có thể hữu ích khi cần phân tích một ứng dụng cụ thể hoặc theo dõi một nhóm sự kiện chuyên biệt.

Trong môi trường doanh nghiệp, Custom Logs có thể được dùng để phục vụ giám sát, kiểm toán hoặc tích hợp với hệ thống SIEM.

## 12.5. Ý nghĩa của Event Logs trong SOC

Trong SOC, **Event Logs** là một trong những nguồn dữ liệu quan trọng nhất để phát hiện, phân tích và điều tra sự cố bảo mật.

Event Logs giúp SOC Analyst trả lời các câu hỏi quan trọng như:

* ai đã đăng nhập vào hệ thống;
* đăng nhập xảy ra khi nào;
* đăng nhập thành công hay thất bại;
* tài khoản nào có hành vi bất thường;
* dịch vụ nào được tạo hoặc thay đổi;
* có tiến trình hoặc ứng dụng nào gặp lỗi bất thường;
* có thay đổi chính sách hoặc quyền truy cập hay không;
* sự kiện xảy ra theo trình tự như thế nào.

Trong môi trường doanh nghiệp, log từ nhiều máy Windows thường được gửi về SIEM để phân tích tập trung. Nhờ đó, SOC có thể phát hiện các mẫu hành vi bất thường trên nhiều máy cùng lúc.

Ví dụ, nếu cùng một tài khoản đăng nhập thất bại trên nhiều máy trong thời gian ngắn, SIEM có thể cảnh báo về khả năng brute-force hoặc password spraying.

Event Logs không chỉ giúp phát hiện tấn công mà còn hỗ trợ điều tra sau sự cố, dựng lại timeline và xác định phạm vi ảnh hưởng.

## 12.6. Event Viewer trong phát hiện và điều tra tấn công

Event Viewer có thể hỗ trợ phát hiện và điều tra nhiều loại tấn công trên Windows, đặc biệt khi kiểm tra Security Log, System Log và Application Log.

Một số dấu hiệu đáng chú ý trong Event Viewer gồm:

* nhiều lần đăng nhập thất bại;
* đăng nhập thành công vào thời điểm bất thường;
* tài khoản mới được tạo;
* người dùng được thêm vào nhóm Administrators;
* dịch vụ mới được cài đặt;
* scheduled task bất thường;
* lỗi liên tục từ một ứng dụng hoặc dịch vụ;
* hệ thống bị tắt hoặc khởi động lại bất thường;
* thay đổi chính sách bảo mật;
* truy cập trái phép vào tài nguyên.

Khi điều tra tấn công, cần chú ý đến các yếu tố sau:

* thời điểm xảy ra sự kiện;
* tài khoản liên quan;
* máy nguồn và máy đích;
* loại log;
* Event ID;
* mô tả sự kiện;
* hành động thành công hay thất bại;
* sự kiện trước và sau thời điểm nghi ngờ.

Ví dụ, nếu phát hiện nhiều Failure Audit liên quan đến đăng nhập thất bại, sau đó có một Success Audit từ cùng một nguồn, có thể nghi ngờ rằng kẻ tấn công đã đoán đúng mật khẩu.

Event Viewer là công cụ rất hữu ích cho phân tích ban đầu. Tuy nhiên, trong điều tra chuyên sâu, cần kết hợp thêm các nguồn dữ liệu khác như Sysmon logs, PowerShell logs, firewall logs, EDR alerts và SIEM correlation rules.

# 13. System Information

## 13.1. System Information là gì?

**System Information** là công cụ trong Windows dùng để xem thông tin chi tiết về phần cứng, phần mềm, thành phần hệ thống và môi trường hoạt động của máy tính.

Công cụ này giúp người dùng và quản trị viên nhanh chóng kiểm tra cấu hình hệ thống mà không cần cài thêm phần mềm bên ngoài.

System Information có thể hiển thị các thông tin như:

- phiên bản hệ điều hành;
- tên máy tính;
- nhà sản xuất hệ thống;
- model máy;
- loại CPU;
- dung lượng RAM;
- BIOS/UEFI;
- thiết bị phần cứng;
- driver;
- dịch vụ;
- chương trình khởi động;
- biến môi trường.

Trong quản trị hệ thống, System Information rất hữu ích khi cần kiểm tra cấu hình máy, xác định thông tin phần cứng, kiểm tra môi trường phần mềm hoặc hỗ trợ xử lý sự cố.

Trong an toàn thông tin, công cụ này có thể giúp thu thập thông tin ban đầu về hệ thống trước khi phân tích sâu hơn.


## 13.2. Cách mở `msinfo32.exe`

Có nhiều cách để mở System Information trong Windows.

Cách phổ biến nhất là sử dụng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
````

2. Nhập lệnh:

```text
msinfo32.exe
```

3. Nhấn **Enter**.

Ngoài ra, có thể mở bằng Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
System Information
```

3. Chọn ứng dụng **System Information**.

Cũng có thể mở từ Command Prompt hoặc PowerShell bằng lệnh:

```text
msinfo32
```

Sau khi mở, cửa sổ System Information sẽ hiển thị nhiều nhóm thông tin khác nhau, trong đó các nhóm chính gồm:

* **System Summary**;
* **Hardware Resources**;
* **Components**;
* **Software Environment**.

![](./img/13.2_open_system_info.png)

## 13.3. System Summary

**System Summary** là phần tóm tắt thông tin tổng quan của hệ thống. Đây là phần đầu tiên được hiển thị khi mở System Information.

System Summary thường cung cấp các thông tin như:

| Thông tin                 | Ý nghĩa                                |
| ------------------------- | -------------------------------------- |
| OS Name                   | Tên hệ điều hành Windows               |
| Version                   | Phiên bản hệ điều hành                 |
| System Name               | Tên máy tính                           |
| System Manufacturer       | Nhà sản xuất thiết bị                  |
| System Model              | Model máy                              |
| System Type               | Kiến trúc hệ thống, ví dụ x64-based PC |
| Processor                 | Thông tin CPU                          |
| BIOS Version/Date         | Phiên bản và ngày phát hành BIOS       |
| Installed Physical Memory | Dung lượng RAM được cài đặt            |
| Total Physical Memory     | Tổng bộ nhớ vật lý khả dụng            |
| Available Physical Memory | Bộ nhớ còn trống                       |
| Time Zone                 | Múi giờ hệ thống                       |

Phần System Summary rất hữu ích khi cần kiểm tra nhanh thông tin cơ bản của máy tính.

Ví dụ, khi cài phần mềm hoặc driver, người dùng có thể cần biết máy đang dùng Windows phiên bản nào, kiến trúc 32-bit hay 64-bit, CPU gì và dung lượng RAM bao nhiêu.

Trong môi trường doanh nghiệp, System Summary cũng giúp quản trị viên kiểm kê tài sản, kiểm tra cấu hình máy trạm và xác định thiết bị có đáp ứng yêu cầu kỹ thuật hay không.

## 13.4. Hardware Resources

**Hardware Resources** là nhóm thông tin liên quan đến tài nguyên phần cứng của hệ thống.

![](./img/13.4_hardware_resources.png)

Phần này thường bao gồm các mục như:

* Conflicts/Sharing;
* DMA;
* Forced Hardware;
* I/O;
* IRQs;
* Memory.

Hardware Resources giúp người dùng xem cách Windows phân bổ tài nguyên phần cứng cho các thiết bị.

Ví dụ, hệ thống có thể hiển thị thông tin về:

* vùng bộ nhớ phần cứng;
* ngắt IRQ;
* địa chỉ I/O;
* tài nguyên đang được chia sẻ giữa các thiết bị;
* xung đột phần cứng nếu có.

Đối với người dùng thông thường, phần này có thể khá khó hiểu. Tuy nhiên, với quản trị viên hệ thống hoặc kỹ thuật viên, Hardware Resources có thể hữu ích khi xử lý lỗi phần cứng, driver hoặc xung đột thiết bị.

Trong thực tế hiện nay, Windows thường tự động quản lý phần lớn tài nguyên phần cứng, nên người dùng hiếm khi cần chỉnh sửa trực tiếp các thông tin này.

## 13.5. Components

**Components** là nhóm thông tin hiển thị các thành phần phần cứng và thiết bị được Windows nhận diện.

![](./img/13.5_components.png)

Phần này có thể chứa thông tin về:

* Multimedia;
* Display;
* Infrared;
* Input;
* Modem;
* Network;
* Ports;
* Storage;
* Printing;
* Problem Devices;
* USB.

Ví dụ, trong mục **Display**, người dùng có thể xem thông tin về card đồ họa, driver màn hình và độ phân giải. Trong mục **Network**, có thể xem thông tin về card mạng. Trong mục **Storage**, có thể xem thông tin liên quan đến ổ đĩa.

Một mục rất hữu ích là **Problem Devices**. Mục này hiển thị các thiết bị đang gặp vấn đề hoặc chưa được hệ thống nhận diện đúng.

Components thường được dùng khi cần:

* kiểm tra thiết bị phần cứng;
* xác định driver đang sử dụng;
* xem thông tin card mạng;
* kiểm tra thiết bị lưu trữ;
* phát hiện thiết bị lỗi;
* hỗ trợ xử lý sự cố phần cứng.

Trong điều tra bảo mật, phần Components cũng có thể hỗ trợ kiểm tra các thiết bị bất thường, adapter mạng lạ hoặc thiết bị USB được hệ thống nhận diện.

## 13.6. Software Environment

**Software Environment** là nhóm thông tin liên quan đến môi trường phần mềm của Windows.

![](./img/13.6_software_environment.png)

Phần này có thể hiển thị thông tin về:

* System Drivers;
* Environment Variables;
* Print Jobs;
* Network Connections;
* Running Tasks;
* Loaded Modules;
* Services;
* Program Groups;
* Startup Programs;
* OLE Registration;
* Windows Error Reporting.

Software Environment giúp người dùng xem nhiều thông tin quan trọng về các thành phần phần mềm đang hoạt động trên hệ thống.

Ví dụ:

* **Running Tasks** cho biết các tác vụ đang chạy;
* **Services** cho biết các dịch vụ trên hệ thống;
* **Startup Programs** cho biết các chương trình khởi động cùng Windows;
* **Environment Variables** cho biết các biến môi trường;
* **System Drivers** cho biết driver hệ thống.

Trong quản trị hệ thống, Software Environment rất hữu ích khi cần kiểm tra phần mềm, dịch vụ, driver hoặc chương trình tự khởi động.

Trong an toàn thông tin, đây là nơi có thể hỗ trợ phát hiện dấu hiệu bất thường như chương trình khởi động lạ, dịch vụ đáng nghi hoặc driver không rõ nguồn gốc.

## 13.7. Environment Variables

**Environment Variables**, hay biến môi trường, là các giá trị được Windows và chương trình sử dụng để xác định đường dẫn, cấu hình hoặc thông tin môi trường hệ thống.

![](./img/13.7_enviroment_variables.png)

Biến môi trường giúp hệ điều hành và ứng dụng hoạt động linh hoạt hơn. Thay vì phải ghi cố định một đường dẫn, chương trình có thể dùng biến môi trường để tham chiếu đến vị trí tương ứng trên từng máy.

Ví dụ:

| Biến môi trường | Ý nghĩa                                                  |
| --------------- | -------------------------------------------------------- |
| `WINDIR`        | Chỉ đến thư mục cài đặt Windows                          |
| `SystemRoot`    | Chỉ đến thư mục hệ thống Windows                         |
| `TEMP`          | Chỉ đến thư mục tạm                                      |
| `TMP`           | Chỉ đến thư mục tạm                                      |
| `USERPROFILE`   | Chỉ đến thư mục hồ sơ người dùng hiện tại                |
| `PATH`          | Danh sách thư mục dùng để tìm chương trình khi chạy lệnh |
| `ComSpec`       | Chỉ đến chương trình Command Prompt                      |

Biến môi trường rất quan trọng khi chạy lệnh, viết script hoặc xử lý lỗi đường dẫn.

Ví dụ, thay vì viết trực tiếp:

```text
C:\Windows
```

có thể dùng:

```text
%WINDIR%
```

Điều này giúp lệnh hoặc script hoạt động linh hoạt hơn trên nhiều máy khác nhau.

## 13.8. Biến môi trường `WINDIR`

`WINDIR` là biến môi trường dùng để chỉ đường dẫn đến thư mục cài đặt Windows.

Thông thường, giá trị của `WINDIR` là:

```text
C:\Windows
```

Ví dụ, khi cần tham chiếu đến thư mục System32, có thể dùng:

```text
%WINDIR%\System32
```

Thông thường, đường dẫn này tương đương với:

```text
C:\Windows\System32
```

Biến `WINDIR` hữu ích vì không phải hệ thống Windows nào cũng bắt buộc được cài trong `C:\Windows`. Nếu Windows được cài ở vị trí khác, biến môi trường vẫn giúp chương trình tìm đúng thư mục hệ thống.

Trong quản trị Windows, `WINDIR` thường xuất hiện trong script, lệnh hệ thống, cấu hình phần mềm và một số tài liệu kỹ thuật.

Ví dụ:

```cmd
echo %WINDIR%
```

![](./img/13.8_windir.png)

Lệnh trên dùng để hiển thị giá trị hiện tại của biến `WINDIR` trong Command Prompt.

## 13.9. Biến môi trường `ComSpec`

`ComSpec` là biến môi trường dùng để chỉ đường dẫn đến chương trình Command Prompt của Windows.

Thông thường, giá trị của `ComSpec` là:

```text
%SystemRoot%\system32\cmd.exe
```

Hoặc tương đương với:

```text
C:\Windows\System32\cmd.exe
```

Biến này cho biết Windows sẽ sử dụng chương trình nào làm trình thông dịch lệnh mặc định cho Command Prompt.

Có thể kiểm tra giá trị của `ComSpec` bằng lệnh:

```cmd
echo %ComSpec%
```

Kết quả thường là:

```text
C:\Windows\system32\cmd.exe
```

![](./img/13.9_comspec.png)

Trong thực tế, `ComSpec` có thể được sử dụng bởi script, chương trình cài đặt hoặc một số ứng dụng cần gọi Command Prompt để chạy lệnh.

Từ góc độ bảo mật, nếu giá trị `ComSpec` bị thay đổi bất thường, đó có thể là dấu hiệu cần kiểm tra kỹ, vì nó liên quan đến chương trình thực thi lệnh của hệ thống.

## 13.10. Tìm kiếm thông tin trong System Information

System Information có chức năng tìm kiếm giúp người dùng nhanh chóng tìm thông tin cần thiết trong toàn bộ dữ liệu hệ thống.

Ở phía dưới cửa sổ System Information thường có ô **Find what**. Người dùng có thể nhập từ khóa cần tìm, sau đó nhấn **Find** để tìm thông tin liên quan.

Ví dụ, có thể tìm các từ khóa như:

```text
WINDIR
```

```text
ComSpec
```

```text
Processor
```

```text
BIOS
```

```text
Startup
```

Chức năng tìm kiếm rất hữu ích vì System Information chứa nhiều nhóm thông tin khác nhau. Nếu không dùng tìm kiếm, người dùng có thể mất thời gian để mở từng mục thủ công.

Trong quản trị và xử lý sự cố, tìm kiếm trong System Information giúp nhanh chóng xác định:

* biến môi trường;
* thông tin CPU;
* phiên bản BIOS;
* driver;
* chương trình khởi động;
* dịch vụ;
* thiết bị có vấn đề.

# 14. Resource Monitor

## 14.1. Resource Monitor là gì?

**Resource Monitor** là công cụ trong Windows dùng để theo dõi chi tiết việc sử dụng tài nguyên hệ thống theo thời gian thực.

Công cụ này cho phép người dùng quan sát các thành phần chính của hệ thống như:

- CPU;
- Memory;
- Disk;
- Network.

So với Task Manager, Resource Monitor cung cấp thông tin chi tiết hơn về từng tiến trình và mức độ sử dụng tài nguyên của chúng. Vì vậy, công cụ này rất hữu ích khi cần phân tích nguyên nhân máy tính bị chậm, ứng dụng bị treo, ổ đĩa hoạt động bất thường hoặc mạng có lưu lượng đáng nghi.

Resource Monitor thường được sử dụng trong các tình huống như:

- kiểm tra tiến trình sử dụng nhiều CPU;
- xác định chương trình chiếm nhiều RAM;
- theo dõi tiến trình đang đọc/ghi ổ đĩa;
- kiểm tra kết nối mạng của từng tiến trình;
- phát hiện hoạt động bất thường trên hệ thống;
- hỗ trợ xử lý sự cố hiệu suất.


## 14.2. Cách mở `resmon.exe`

Có nhiều cách để mở Resource Monitor trong Windows.

Cách phổ biến nhất là sử dụng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
````

2. Nhập lệnh:

```text
resmon.exe
```

3. Nhấn **Enter**.

Ngoài ra, có thể mở bằng Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
Resource Monitor
```

3. Chọn ứng dụng **Resource Monitor**.

Cũng có thể mở Resource Monitor từ Task Manager:

1. Mở **Task Manager**.
2. Chọn tab **Performance**.
3. Chọn **Open Resource Monitor**.

Sau khi mở, Resource Monitor sẽ hiển thị các tab chính gồm:

* Overview;
* CPU;
* Memory;
* Disk;
* Network.

## 14.3. Overview

Tab **Overview** cung cấp cái nhìn tổng quan về tình trạng sử dụng tài nguyên của hệ thống.

![](./img/14.3_overview_resmon.png)

Trong tab này, người dùng có thể xem nhanh hoạt động của:

* CPU;
* Disk;
* Network;
* Memory.

Overview giúp người dùng nhanh chóng xác định tài nguyên nào đang có dấu hiệu bất thường. Ví dụ, nếu máy tính bị chậm, có thể mở Overview để xem CPU, RAM, Disk hay Network đang bị sử dụng nhiều nhất.

Tab Overview thường hiển thị danh sách các tiến trình đang hoạt động cùng với mức độ sử dụng tài nguyên của chúng. Điều này giúp người dùng có cái nhìn ban đầu trước khi chuyển sang các tab chi tiết hơn.

Ví dụ:

* nếu CPU cao, chuyển sang tab **CPU**;
* nếu RAM gần đầy, chuyển sang tab **Memory**;
* nếu ổ đĩa hoạt động liên tục, chuyển sang tab **Disk**;
* nếu có lưu lượng mạng bất thường, chuyển sang tab **Network**.

Overview là nơi phù hợp để bắt đầu quá trình phân tích hiệu suất hệ thống.

## 14.4. CPU Monitoring

Tab **CPU** trong Resource Monitor cho phép theo dõi chi tiết hoạt động của bộ xử lý và các tiến trình đang sử dụng CPU.

![](./img/14.4_cpu_monitoring.png)

Trong tab này, người dùng có thể xem:

* tiến trình nào đang sử dụng CPU;
* mức sử dụng CPU của từng tiến trình;
* số luồng đang chạy;
* dịch vụ liên quan đến tiến trình;
* module hoặc handle liên quan.

Thông tin CPU rất hữu ích khi máy tính bị chậm, quạt chạy mạnh hoặc hệ thống phản hồi kém.

Ví dụ, nếu một tiến trình sử dụng CPU ở mức cao trong thời gian dài, có thể tiến trình đó đang xử lý tác vụ nặng, bị lỗi hoặc có hành vi bất thường.

Một số tình huống cần kiểm tra CPU gồm:

* máy tính chạy chậm;
* ứng dụng không phản hồi;
* CPU luôn gần 100%;
* tiến trình lạ sử dụng nhiều CPU;
* dịch vụ nền gây quá tải hệ thống.

Trong điều tra bảo mật, tiến trình sử dụng CPU bất thường cũng có thể là dấu hiệu của mã độc, script đào tiền ảo hoặc chương trình chạy nền không mong muốn.

## 14.5. Memory Monitoring

Tab **Memory** dùng để theo dõi việc sử dụng bộ nhớ RAM của hệ thống.

![](./img/14.5_memory_monitoring.png)

Trong tab này, người dùng có thể xem:

* tiến trình nào đang sử dụng nhiều RAM;
* tổng lượng RAM đang được sử dụng;
* lượng RAM còn trống;
* bộ nhớ đang ở trạng thái Standby;
* bộ nhớ bị chiếm bởi tiến trình cụ thể;
* tình trạng paging nếu hệ thống thiếu RAM.

Memory Monitoring rất quan trọng vì khi RAM bị sử dụng quá nhiều, Windows có thể phải dùng bộ nhớ ảo trên ổ đĩa. Điều này làm hệ thống chậm hơn đáng kể.

Một số dấu hiệu cần kiểm tra trong tab Memory gồm:

* RAM gần đầy;
* một tiến trình chiếm RAM bất thường;
* ứng dụng tăng RAM liên tục theo thời gian;
* hệ thống bị chậm khi mở nhiều chương trình;
* máy thường xuyên bị treo hoặc phản hồi chậm.

Trong xử lý sự cố, tab Memory giúp xác định ứng dụng nào đang gây thiếu bộ nhớ. Trong một số trường hợp, tiến trình sử dụng RAM tăng liên tục có thể là dấu hiệu của memory leak.

Từ góc độ bảo mật, tiến trình lạ sử dụng nhiều RAM cũng cần được kiểm tra, đặc biệt nếu nó không có tên rõ ràng hoặc chạy từ đường dẫn bất thường.

## 14.6. Disk Monitoring

Tab **Disk** cho phép theo dõi hoạt động đọc và ghi dữ liệu trên ổ đĩa.

![](./img/14.6_disk_monitoring.png)

Trong tab này, người dùng có thể xem:

* tiến trình nào đang đọc/ghi dữ liệu;
* tệp nào đang được truy cập;
* tốc độ đọc dữ liệu;
* tốc độ ghi dữ liệu;
* thời gian phản hồi của ổ đĩa;
* mức độ hoạt động của từng ổ đĩa.

Disk Monitoring rất hữu ích khi máy tính bị chậm do ổ đĩa hoạt động liên tục. Trong nhiều trường hợp, Disk sử dụng cao có thể làm toàn bộ hệ thống phản hồi chậm, dù CPU và RAM không quá tải.

Một số tình huống cần kiểm tra Disk gồm:

* ổ đĩa luôn hoạt động ở mức cao;
* máy chậm khi mở ứng dụng;
* hệ thống khởi động lâu;
* phần mềm ghi dữ liệu liên tục;
* nghi ngờ có tiến trình đang đọc nhiều tệp;
* nghi ngờ mã độc đang mã hóa hoặc sao chép dữ liệu.

Trong an toàn thông tin, Disk Monitoring có thể hỗ trợ phát hiện hành vi bất thường như:

* tiến trình đọc nhiều tệp trong thời gian ngắn;
* ghi dữ liệu vào thư mục lạ;
* truy cập nhiều tệp người dùng;
* hoạt động giống ransomware;
* tạo hoặc sửa nhiều tệp bất thường.

## 14.7. Network Monitoring

Tab **Network** cho phép theo dõi hoạt động mạng của hệ thống theo từng tiến trình.

![](./img/14.7_network_monitoring.png)

Trong tab này, người dùng có thể xem:

* tiến trình nào đang sử dụng mạng;
* địa chỉ IP từ xa đang kết nối;
* cổng mạng đang sử dụng;
* lưu lượng gửi và nhận;
* kết nối TCP đang mở;
* cổng đang lắng nghe.

Network Monitoring rất hữu ích khi cần kiểm tra ứng dụng nào đang truy cập Internet hoặc kết nối đến máy chủ bên ngoài.

Một số tình huống cần kiểm tra Network gồm:

* mạng chậm bất thường;
* có lưu lượng mạng cao dù người dùng không làm gì;
* tiến trình lạ kết nối ra ngoài;
* ứng dụng kết nối đến IP không rõ;
* nghi ngờ máy bị mã độc điều khiển từ xa;
* cần kiểm tra chương trình nào đang mở cổng lắng nghe.

Trong điều tra bảo mật, tab Network rất quan trọng vì nhiều mã độc cần kết nối ra ngoài để nhận lệnh, gửi dữ liệu hoặc tải thêm payload.

Khi phát hiện một tiến trình lạ có kết nối mạng, cần kiểm tra thêm:

* tên tiến trình;
* đường dẫn file thực thi;
* địa chỉ IP từ xa;
* cổng kết nối;
* thời điểm kết nối;
* tài khoản đang chạy tiến trình.

## 14.8. Phân tích tiến trình bằng Resource Monitor

Resource Monitor cho phép phân tích tiến trình chi tiết hơn so với Task Manager.

Khi kiểm tra một tiến trình, người dùng có thể xem tiến trình đó đang sử dụng tài nguyên nào, ví dụ:

* dùng bao nhiêu CPU;
* chiếm bao nhiêu RAM;
* đang đọc hoặc ghi tệp nào;
* đang kết nối đến địa chỉ IP nào;
* đang sử dụng dịch vụ hoặc handle nào.

Quy trình phân tích cơ bản có thể thực hiện như sau:

1. Mở **Resource Monitor**.
2. Vào tab **Overview** để xác định tài nguyên bị sử dụng nhiều.
3. Chuyển sang tab tương ứng: **CPU**, **Memory**, **Disk** hoặc **Network**.
4. Tìm tiến trình có mức sử dụng bất thường.
5. Kiểm tra tên tiến trình, PID và tài nguyên đang sử dụng.
6. Nếu cần, đối chiếu với Task Manager, Event Viewer hoặc công cụ bảo mật khác.

Một số dấu hiệu tiến trình đáng nghi gồm:

* tên tiến trình lạ;
* chạy từ thư mục `Temp`, `AppData` hoặc `Downloads`;
* sử dụng CPU cao bất thường;
* đọc/ghi nhiều tệp trong thời gian ngắn;
* kết nối đến IP lạ;
* không có mô tả rõ ràng;
* chạy dưới quyền người dùng không phù hợp.

Resource Monitor không thay thế các công cụ điều tra chuyên sâu, nhưng nó rất hữu ích trong bước kiểm tra ban đầu.

## 14.9. Ứng dụng Resource Monitor trong xử lý sự cố

Resource Monitor là công cụ rất hữu ích trong xử lý sự cố Windows, đặc biệt là các sự cố liên quan đến hiệu suất và tài nguyên hệ thống.

Một số ứng dụng phổ biến gồm:

* xác định nguyên nhân máy tính chạy chậm;
* kiểm tra tiến trình sử dụng CPU cao;
* phát hiện ứng dụng chiếm nhiều RAM;
* kiểm tra ổ đĩa bị quá tải;
* xác định chương trình đang sử dụng mạng;
* kiểm tra kết nối TCP đáng nghi;
* hỗ trợ phân tích tiến trình bất thường;
* hỗ trợ điều tra ban đầu khi nghi ngờ mã độc.

Ví dụ, nếu người dùng báo rằng máy tính rất chậm, quản trị viên có thể mở Resource Monitor để kiểm tra:

* CPU có bị sử dụng quá cao không;
* RAM có gần đầy không;
* Disk có hoạt động liên tục không;
* Network có lưu lượng bất thường không.

Nếu phát hiện một tiến trình chiếm nhiều tài nguyên, cần kiểm tra thêm tiến trình đó là gì, nằm ở đâu và có hợp pháp hay không.

Trong SOC, Resource Monitor có thể hỗ trợ phân tích nhanh trên máy cục bộ. Tuy nhiên, để điều tra đầy đủ, cần kết hợp thêm các nguồn dữ liệu khác như Event Viewer, Sysmon, Windows Defender, EDR, firewall logs và SIEM.

Tóm lại, Resource Monitor là công cụ quan trọng giúp người học Windows hiểu hệ thống đang sử dụng tài nguyên như thế nào và hỗ trợ phát hiện các dấu hiệu bất thường ban đầu.

# 15. Command Prompt

## 15.1. Command Prompt là gì?

**Command Prompt**, thường gọi là **CMD**, là giao diện dòng lệnh truyền thống của Windows. Thay vì thao tác bằng giao diện đồ họa, người dùng có thể nhập lệnh để thực hiện các tác vụ quản trị, kiểm tra hệ thống, cấu hình mạng và xử lý sự cố.

Command Prompt cho phép người dùng làm việc với Windows bằng các câu lệnh như:

- xem tên máy tính;
- kiểm tra tài khoản đang đăng nhập;
- kiểm tra cấu hình mạng;
- xem kết nối mạng;
- quản lý người dùng cục bộ;
- quản lý nhóm cục bộ;
- mở công cụ hệ thống;
- chạy script hoặc chương trình.

## 15.2. Cách mở CMD

Có nhiều cách để mở Command Prompt trong Windows.

Cách phổ biến nhất là mở từ Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
cmd
````

3. Chọn **Command Prompt**.

Có thể mở CMD bằng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
```

2. Nhập:

```text
cmd
```

3. Nhấn **Enter**.

![](./img/15.2_open_cmd.png)

Nếu cần chạy CMD với quyền quản trị, có thể:

1. Nhấn **Start**.
2. Gõ `cmd`.
3. Nhấp chuột phải vào **Command Prompt**.
4. Chọn **Run as administrator**.

Khi chạy CMD với quyền quản trị, người dùng có thể thực hiện nhiều lệnh yêu cầu quyền cao hơn, ví dụ như thay đổi cấu hình hệ thống hoặc quản lý tài khoản người dùng.

## 15.3. Cú pháp lệnh trong CMD

Một lệnh trong CMD thường có cấu trúc cơ bản như sau:

```cmd
command [option] [argument]
```

Trong đó:

| Thành phần | Ý nghĩa                       |
| ---------- | ----------------------------- |
| `command`  | Tên lệnh cần chạy             |
| `option`   | Tùy chọn hoặc tham số bổ sung |
| `argument` | Đối tượng mà lệnh sẽ tác động |

Ví dụ:

```cmd
ipconfig /all
```

Trong lệnh trên:

* `ipconfig` là tên lệnh;
* `/all` là tùy chọn để hiển thị thông tin chi tiết hơn.

Một ví dụ khác:

```cmd
net user
```

Trong lệnh này:

* `net` là lệnh chính;
* `user` là tham số dùng để làm việc với tài khoản người dùng.

CMD thường sử dụng dấu `/` cho các tùy chọn, ví dụ:

```cmd
ipconfig /all
net user /?
```

Để dùng CMD hiệu quả, cần hiểu tên lệnh, tham số và cách xem trợ giúp của từng lệnh.

## 15.4. Lệnh `hostname`

Lệnh `hostname` dùng để hiển thị tên máy tính hiện tại.

Cú pháp:

```cmd
hostname
```

![](./img/15.4_hostname.png)

Tên máy tính rất quan trọng trong quản trị hệ thống và điều tra sự cố. Khi làm việc trong mạng doanh nghiệp, mỗi máy tính thường có một hostname riêng để phân biệt với các thiết bị khác.

Lệnh này thường được dùng khi cần:

* xác định đang làm việc trên máy nào;
* ghi nhận thông tin máy trong báo cáo;
* kiểm tra máy trong môi trường domain;
* đối chiếu với log hoặc cảnh báo bảo mật.

## 15.5. Lệnh `whoami`

Lệnh `whoami` dùng để hiển thị tài khoản người dùng hiện tại đang đăng nhập trong phiên CMD.

Cú pháp:

```cmd
whoami
```

![](./img/15.5_whoami.png)

Nếu máy tính thuộc domain, kết quả có thể có dạng:

```text
company\user01
```

Lệnh này giúp xác định người dùng hiện tại đang chạy lệnh là ai. Đây là thông tin quan trọng khi kiểm tra quyền, phân tích log hoặc xử lý sự cố.

Một số tình huống sử dụng `whoami`:

* kiểm tra tài khoản đang đăng nhập;
* xác định đang dùng tài khoản local hay domain;
* kiểm tra ngữ cảnh người dùng khi chạy script;
* hỗ trợ điều tra hoạt động đáng nghi.

Trong an toàn thông tin, `whoami` thường được dùng trong giai đoạn thu thập thông tin ban đầu trên hệ thống Windows.

## 15.6. Lệnh `ipconfig`

Lệnh `ipconfig` dùng để hiển thị thông tin cấu hình mạng cơ bản của máy tính Windows.

Cú pháp:

```cmd
ipconfig
```

Lệnh này thường hiển thị các thông tin như:

* địa chỉ IPv4;
* subnet mask;
* default gateway;
* adapter mạng đang sử dụng;
* trạng thái kết nối mạng.

![](./img/15.6_ipconfig.png)

Lệnh `ipconfig` rất hữu ích khi cần kiểm tra nhanh máy tính có nhận địa chỉ IP hay không.

Một số tình huống thường dùng:

* máy không vào được mạng;
* cần kiểm tra địa chỉ IP;
* cần xác định default gateway;
* kiểm tra adapter mạng;
* kiểm tra cấu hình trong môi trường lab.

## 15.7. Lệnh `ipconfig /all`

Lệnh `ipconfig /all` hiển thị thông tin cấu hình mạng chi tiết hơn so với `ipconfig`.

Cú pháp:

```cmd
ipconfig /all
```

Lệnh này có thể hiển thị thêm các thông tin như:

* hostname;
* DNS suffix;
* địa chỉ MAC;
* DHCP enabled;
* DHCP server;
* DNS server;
* lease obtained;
* lease expires;
* thông tin chi tiết của từng adapter mạng.

Ví dụ, để xem địa chỉ MAC của card mạng, có thể dùng:

```cmd
ipconfig /all
```

Sau đó tìm dòng:

```text
Physical Address
```

![](./img/15.7_ipconfig_all.png)

Trong quản trị hệ thống, `ipconfig /all` thường được dùng khi cần kiểm tra chi tiết cấu hình mạng của một máy.

Trong SOC hoặc điều tra sự cố, thông tin từ `ipconfig /all` có thể giúp xác định:

* máy đang dùng DNS nào;
* địa chỉ MAC của thiết bị;
* máy có nhận IP từ DHCP hay không;
* adapter mạng nào đang hoạt động;
* có adapter ảo hoặc cấu hình mạng bất thường hay không.

## 15.8. Lệnh `netstat`

Lệnh `netstat` dùng để hiển thị thông tin về các kết nối mạng, cổng đang lắng nghe và thống kê mạng trên Windows.

Cú pháp cơ bản:

```cmd
netstat
```

![](./img/15.8_netstat.png)

Một số tùy chọn thường dùng:

```cmd
netstat -ano
```

![](./img/15.8_netstat_ano.png)

Ý nghĩa thường gặp:

| Tùy chọn | Ý nghĩa                                        |
| -------- | ---------------------------------------------- |
| `-a`     | Hiển thị tất cả kết nối và cổng đang lắng nghe |
| `-n`     | Hiển thị địa chỉ và cổng dưới dạng số          |
| `-o`     | Hiển thị PID của tiến trình liên quan          |



Lệnh này giúp xem tiến trình nào đang mở kết nối mạng hoặc lắng nghe trên cổng nào.

Thông tin thường có trong kết quả `netstat`:

* protocol;
* local address;
* foreign address;
* state;
* PID.

Một số trạng thái kết nối thường gặp:

| Trạng thái  | Ý nghĩa                             |
| ----------- | ----------------------------------- |
| LISTENING   | Đang lắng nghe kết nối              |
| ESTABLISHED | Kết nối đã được thiết lập           |
| TIME_WAIT   | Kết nối đang chờ đóng               |
| CLOSE_WAIT  | Kết nối đang chờ phía ứng dụng đóng |

Trong an toàn thông tin, `netstat` rất hữu ích để kiểm tra kết nối đáng nghi, ví dụ một tiến trình lạ đang kết nối ra địa chỉ IP bên ngoài.

## 15.9. Lệnh `net`

Lệnh `net` là một nhóm lệnh dùng để quản lý nhiều thành phần trong Windows, đặc biệt là người dùng, nhóm, dịch vụ, chia sẻ mạng và phiên kết nối.

Cú pháp chung:

```cmd
net [subcommand]
```

Một số lệnh `net` thường gặp:

| Lệnh             | Chức năng                        |
| ---------------- | -------------------------------- |
| `net user`       | Quản lý tài khoản người dùng     |
| `net localgroup` | Quản lý nhóm cục bộ              |
| `net share`      | Xem hoặc quản lý thư mục chia sẻ |
| `net use`        | Kết nối tài nguyên mạng          |
| `net session`    | Xem phiên kết nối đến máy        |
| `net start`      | Xem hoặc khởi động dịch vụ       |
| `net stop`       | Dừng dịch vụ                     |

Lệnh `net` rất quan trọng trong quản trị Windows vì có thể thực hiện nhiều thao tác nhanh trực tiếp từ CMD.

### 15.9.1. Lệnh `net user`

Lệnh `net user` dùng để xem và quản lý tài khoản người dùng trên Windows.

Cú pháp xem danh sách người dùng:

```cmd
net user
```

![](./img/15.9_net_user.png)

Cú pháp xem thông tin một người dùng cụ thể:

```cmd
net user username
```
![](./img/15.9_net_user_ad.png)

Lệnh này có thể hiển thị các thông tin như:

* tên tài khoản;
* tài khoản đang bật hay bị khóa;
* thời điểm đặt mật khẩu gần nhất;
* thời điểm mật khẩu hết hạn;
* nhóm mà người dùng thuộc về;
* thời gian đăng nhập được phép.

Với quyền quản trị, `net user` cũng có thể được dùng để tạo hoặc chỉnh sửa tài khoản.

Ví dụ tạo người dùng mới:

```cmd
net user testuser Password123 /add
```

![](./img/15.9_net_create_user.png)

Tuy nhiên, khi dùng trong môi trường học tập hoặc lab, cần cẩn thận và chỉ thực hiện trên hệ thống được phép.

Trong điều tra bảo mật, `net user` giúp kiểm tra có tài khoản lạ nào được tạo trên máy hay không.

### 15.9.2. Lệnh `net localgroup`

Lệnh `net localgroup` dùng để xem và quản lý các nhóm cục bộ trên Windows.

Cú pháp xem danh sách nhóm cục bộ:

```cmd
net localgroup
```

![](./img/15.9_net_localgroup.png)

Cú pháp xem thành viên của một nhóm:

```cmd
net localgroup groupname
```

Ví dụ kiểm tra nhóm Administrators:

```cmd
net localgroup Administrators
```

![](./img/15.9_net_localgroup_ad.png)

Lệnh này giúp xác định tài khoản nào đang thuộc nhóm có quyền cao.

Với quyền quản trị, có thể thêm người dùng vào nhóm:

```cmd
net localgroup Administrators testuser /add
```

![](./img/15.9_net_add_user_to_group.png)

Hoặc xóa người dùng khỏi nhóm:

```cmd
net localgroup Administrators testuser /delete
```

![](./img/15.9_net_delete_user_from_group.png)

Trong an toàn thông tin, `net localgroup Administrators` là lệnh rất quan trọng vì nó giúp kiểm tra xem có tài khoản bất thường nào đang có quyền quản trị trên máy hay không.

## 15.10. Xem trợ giúp lệnh với `/?`

Trong CMD, có thể xem hướng dẫn sử dụng của nhiều lệnh bằng cách thêm tham số:

```cmd
/?
```

Ví dụ:

```cmd
ipconfig /?
```

![](./img/15.10.png)

Lệnh này hiển thị các tùy chọn có thể sử dụng với `ipconfig`.

Một ví dụ khác:

```cmd
net user /?
```

Kết quả sẽ hiển thị cú pháp và các tham số liên quan đến lệnh `net user`.

Việc sử dụng `/?` rất hữu ích khi người dùng không nhớ chính xác cú pháp lệnh hoặc muốn tìm thêm tùy chọn nâng cao.

Một số ví dụ:

```cmd
hostname /?
whoami /?
netstat /?
net /?
```

Không phải mọi lệnh đều hỗ trợ cùng một kiểu trợ giúp, nhưng `/?` là cách phổ biến trong CMD.

## 15.11. Xem trợ giúp lệnh `net help`

Đối với nhóm lệnh `net`, Windows cung cấp cơ chế trợ giúp riêng là `net help`.

Cú pháp:

```cmd
net help
```

![](./img/15.11_net_help.png)

Lệnh này hiển thị danh sách các lệnh con có thể dùng với `net`.

Để xem trợ giúp cho một lệnh cụ thể, có thể dùng:

```cmd
net help user
```

![](./img/15.11_net_help_user.png)

Hoặc:

```cmd
net help localgroup
```

![](./img/15.11_net_help_localgroup.png)

`net help` rất hữu ích vì nhóm lệnh `net` có nhiều chức năng khác nhau. Khi không nhớ cú pháp, người dùng nên kiểm tra trợ giúp trước khi chạy lệnh có thể thay đổi hệ thống.

## 15.12. Xóa màn hình với `cls`

Lệnh `cls` dùng để xóa nội dung đang hiển thị trên cửa sổ Command Prompt.

Cú pháp:

```cmd
cls
```

Sau khi chạy lệnh này, màn hình CMD sẽ được làm sạch, nhưng các lệnh đã chạy trước đó không bị hủy. Đây chỉ là thao tác xóa phần hiển thị để cửa sổ dòng lệnh gọn hơn.

Lệnh `cls` thường được dùng khi:

* màn hình CMD có quá nhiều kết quả;
* cần trình bày lại lệnh cho dễ nhìn;
* muốn bắt đầu một phần làm việc mới;
* chụp màn hình kết quả lệnh rõ ràng hơn.

Ví dụ:

```cmd
ipconfig
cls
whoami
```

Trong ví dụ trên, sau khi chạy `cls`, nội dung hiển thị trước đó sẽ được xóa khỏi cửa sổ CMD.

## 15.13. Vai trò của CMD trong quản trị và bảo mật

Command Prompt có vai trò quan trọng trong quản trị hệ thống Windows và an toàn thông tin.

Trong quản trị hệ thống, CMD giúp thực hiện nhanh nhiều thao tác như:

* kiểm tra tên máy;
* kiểm tra tài khoản hiện tại;
* xem cấu hình mạng;
* kiểm tra kết nối;
* quản lý người dùng;
* quản lý nhóm;
* kiểm tra dịch vụ;
* chạy script;
* mở công cụ hệ thống.

Trong bảo mật và SOC, CMD hỗ trợ thu thập thông tin ban đầu khi phân tích một máy Windows.

Một số lệnh thường dùng trong kiểm tra bảo mật cơ bản gồm:

| Lệnh                            | Mục đích                          |
| ------------------------------- | --------------------------------- |
| `hostname`                      | Xác định tên máy                  |
| `whoami`                        | Xác định tài khoản hiện tại       |
| `ipconfig /all`                 | Kiểm tra cấu hình mạng chi tiết   |
| `netstat -ano`                  | Kiểm tra kết nối mạng và PID      |
| `net user`                      | Xem tài khoản người dùng          |
| `net localgroup Administrators` | Kiểm tra thành viên nhóm quản trị |
| `cls`                           | Xóa màn hình CMD                  |

Tuy nhiên, CMD cũng có thể bị kẻ tấn công lạm dụng. Nhiều kỹ thuật tấn công sử dụng các công cụ hợp pháp có sẵn trong Windows để thu thập thông tin, tạo tài khoản, thay đổi nhóm quyền hoặc kết nối mạng.

Vì vậy, trong giám sát bảo mật, việc phát hiện các lệnh CMD bất thường cũng rất quan trọng. Đặc biệt cần chú ý khi CMD được chạy bởi tiến trình lạ, chạy với quyền Administrator hoặc thực hiện các lệnh liên quan đến tài khoản, nhóm, mạng và dịch vụ.

# 16. Windows Registry

## 16.1. Windows Registry là gì?

**Windows Registry** là cơ sở dữ liệu trung tâm của hệ điều hành Windows. Registry lưu trữ các thiết lập cấu hình quan trọng của hệ thống, phần cứng, phần mềm, tài khoản người dùng và nhiều thành phần khác.

Nói đơn giản, Registry giống như một nơi lưu trữ thông tin cấu hình mà Windows và các chương trình đã cài đặt sử dụng để hoạt động đúng.

Registry có thể chứa thông tin về:

- cấu hình hệ điều hành;
- thiết lập phần mềm;
- thông tin phần cứng;
- driver;
- tài khoản người dùng;
- dịch vụ hệ thống;
- chương trình khởi động cùng Windows;
- thiết lập giao diện;
- chính sách bảo mật.

Registry là một thành phần rất quan trọng trong Windows. Nếu Registry bị lỗi hoặc bị chỉnh sửa sai, hệ thống có thể hoạt động không ổn định, một số chương trình có thể không chạy được hoặc Windows có thể gặp lỗi nghiêm trọng.


## 16.2. Vai trò của Registry trong Windows

Registry đóng vai trò lưu trữ và quản lý cấu hình của Windows. Khi hệ điều hành hoặc một chương trình cần đọc thiết lập nào đó, nó có thể truy cập Registry để lấy thông tin.

Ví dụ, Registry có thể được dùng để lưu:

- chương trình nào sẽ chạy khi Windows khởi động;
- loại file nào được mở bằng ứng dụng nào;
- thiết lập của người dùng;
- cấu hình của dịch vụ Windows;
- thông tin về driver;
- thiết lập bảo mật;
- chính sách hệ thống.

Khi người dùng thay đổi một số cài đặt trong giao diện Windows, thay đổi đó có thể được ghi vào Registry. Ví dụ, khi thay đổi cấu hình phần mềm, thay đổi tùy chọn hệ thống hoặc cài đặt ứng dụng mới, Registry có thể được cập nhật.

Registry giúp Windows quản lý cấu hình một cách tập trung. Thay vì mỗi thành phần lưu cấu hình ở một nơi riêng biệt, nhiều thông tin quan trọng được lưu trong một cấu trúc thống nhất.

Trong quản trị hệ thống, Registry rất quan trọng vì nhiều thiết lập nâng cao của Windows chỉ có thể kiểm tra hoặc chỉnh sửa thông qua Registry.


## 16.3. Cấu trúc phân cấp của Registry

Windows Registry có cấu trúc phân cấp giống như cây thư mục. Trong Registry có các nhánh chính, bên trong mỗi nhánh có các khóa con và giá trị cấu hình.

Các thành phần chính trong Registry gồm:

| Thành phần | Ý nghĩa |
|---|---|
| Hive | Nhánh lớn trong Registry |
| Key | Khóa Registry, giống như thư mục |
| Subkey | Khóa con nằm trong một key |
| Value | Giá trị cấu hình được lưu trong key |
| Data | Dữ liệu cụ thể của một value |

Một số hive chính thường gặp trong Registry gồm:

| Hive | Ý nghĩa |
|---|---|
| `HKEY_CLASSES_ROOT` | Lưu thông tin về loại file, liên kết file và COM objects |
| `HKEY_CURRENT_USER` | Lưu cấu hình của người dùng hiện tại |
| `HKEY_LOCAL_MACHINE` | Lưu cấu hình chung của máy tính |
| `HKEY_USERS` | Lưu cấu hình của tất cả người dùng |
| `HKEY_CURRENT_CONFIG` | Lưu thông tin cấu hình phần cứng hiện tại |

Ví dụ một đường dẫn Registry có thể có dạng:

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
```

Trong đó:

* `HKEY_LOCAL_MACHINE` là hive;
* `SOFTWARE` là key;
* `Microsoft`, `Windows`, `CurrentVersion` là các subkey.

Cấu trúc phân cấp này giúp Registry tổ chức dữ liệu cấu hình theo từng nhóm rõ ràng.

## 16.4. Registry Editor

**Registry Editor** là công cụ dùng để xem và chỉnh sửa Windows Registry. Công cụ này cho phép người dùng truy cập vào các hive, key, subkey và value trong Registry.

Registry Editor thường được sử dụng bởi:

* quản trị viên hệ thống;
* kỹ thuật viên hỗ trợ;
* người phân tích bảo mật;
* người dùng nâng cao;
* phần mềm hoặc tài liệu kỹ thuật cần chỉnh cấu hình sâu.

Thông qua Registry Editor, người dùng có thể:

* xem cấu hình hệ thống;
* tìm kiếm key hoặc value;
* tạo key mới;
* sửa giá trị Registry;
* xóa key hoặc value;
* xuất Registry ra file `.reg`;
* nhập cấu hình từ file `.reg`.

Tuy nhiên, Registry Editor là công cụ nhạy cảm. Việc chỉnh sửa sai có thể làm Windows hoặc ứng dụng hoạt động không đúng. Vì vậy, chỉ nên thay đổi Registry khi hiểu rõ mục đích và có hướng dẫn đáng tin cậy.

## 16.5. Cách mở `regedit`

Có thể mở Registry Editor bằng lệnh `regedit`.

Cách mở bằng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
```

2. Nhập lệnh:

```text
regedit
```

3. Nhấn **Enter**.

Nếu hệ thống hiển thị UAC Prompt, cần chọn **Yes** để cho phép mở Registry Editor với quyền phù hợp.

Ngoài ra, có thể mở bằng Start Menu:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
regedit
```

3. Chọn **Registry Editor**.

Sau khi mở, giao diện Registry Editor sẽ hiển thị cây thư mục Registry ở bên trái và các giá trị tương ứng ở bên phải.

![](./img/16.5_regedit.png)

## 16.6. Cách mở `regedt32.exe`

`regedt32.exe` là một cách khác để mở Registry Editor trong Windows.

Có thể mở bằng hộp thoại Run:

1. Nhấn:

```text
Win + R
```

2. Nhập:

```text
regedt32.exe
```

3. Nhấn **Enter**.

Trong các phiên bản Windows hiện đại, `regedt32.exe` thường mở cùng công cụ Registry Editor như `regedit`.

Trước đây, `regedt32.exe` và `regedit.exe` từng có một số khác biệt. Tuy nhiên, trong các phiên bản Windows mới, người dùng thông thường chỉ cần nhớ rằng cả hai đều có thể dùng để mở Registry Editor.

Trong thực tế, lệnh được sử dụng phổ biến hơn là:

```text
regedit
```

## 16.7. Những thông tin được lưu trong Registry

Registry lưu trữ rất nhiều thông tin cấu hình của Windows và phần mềm. Đây là lý do Registry được xem là một trong những thành phần quan trọng nhất của hệ điều hành.

Một số loại thông tin thường được lưu trong Registry gồm:

| Loại thông tin         | Ví dụ                                                         |
| ---------------------- | ------------------------------------------------------------- |
| Cấu hình hệ điều hành  | Thiết lập hệ thống, giao diện, dịch vụ                        |
| Cấu hình phần mềm      | Tùy chọn của chương trình đã cài đặt                          |
| Thông tin phần cứng    | Driver, thiết bị, cấu hình phần cứng                          |
| Tài khoản người dùng   | Một số thiết lập liên quan đến người dùng                     |
| Chương trình khởi động | Ứng dụng chạy khi Windows khởi động hoặc người dùng đăng nhập |
| Chính sách hệ thống    | Một số thiết lập bảo mật và quản trị                          |
| Liên kết file          | File `.txt`, `.pdf`, `.docx` mở bằng chương trình nào         |
| Dịch vụ Windows        | Cấu hình và trạng thái của dịch vụ                            |

Ví dụ, Registry có thể lưu thông tin về chương trình nào được phép tự động chạy khi người dùng đăng nhập vào Windows.

Một số đường dẫn Registry thường được quan tâm trong bảo mật là các vị trí liên quan đến startup, dịch vụ, policy và cấu hình phần mềm.

## 16.8. Rủi ro khi chỉnh sửa Registry

Chỉnh sửa Registry có thể gây rủi ro nếu người dùng không hiểu rõ ý nghĩa của key hoặc value đang thay đổi.

Một số rủi ro khi chỉnh sửa Registry sai gồm:

* Windows hoạt động không ổn định;
* phần mềm không mở được;
* dịch vụ Windows bị lỗi;
* thiết bị hoặc driver hoạt động sai;
* mất cấu hình người dùng;
* lỗi đăng nhập;
* hệ thống khởi động không bình thường;
* giảm mức độ bảo mật của hệ thống.

Ví dụ, nếu xóa nhầm key liên quan đến một dịch vụ quan trọng, dịch vụ đó có thể không khởi động được. Nếu thay đổi sai cấu hình đăng nhập hoặc startup, Windows có thể gặp lỗi khi người dùng đăng nhập.

Trước khi chỉnh sửa Registry, nên:

* hiểu rõ key/value cần thay đổi;
* sao lưu Registry hoặc key liên quan;
* tạo restore point nếu cần;
* làm theo tài liệu đáng tin cậy;
* không xóa key lạ nếu chưa biết chức năng;
* không chạy file `.reg` từ nguồn không rõ ràng.

Trong môi trường doanh nghiệp, việc chỉnh sửa Registry nên được kiểm soát cẩn thận, đặc biệt trên máy chủ hoặc máy tính quan trọng.

## 16.9. Ý nghĩa bảo mật của Registry

Registry có ý nghĩa rất quan trọng trong an toàn thông tin Windows vì nhiều cấu hình bảo mật và hành vi hệ thống được lưu tại đây.

Kẻ tấn công có thể lợi dụng Registry để:

* duy trì persistence;
* cấu hình chương trình tự khởi động;
* thay đổi thiết lập bảo mật;
* vô hiệu hóa công cụ bảo vệ;
* ẩn cấu hình độc hại;
* thay đổi hành vi của hệ thống;
* lưu dữ liệu hoặc cấu hình cho mã độc.

Một số dấu hiệu đáng nghi trong Registry gồm:

* key startup lạ;
* chương trình chạy từ `AppData`, `Temp` hoặc `Downloads`;
* value có tên giống hệ thống nhưng đường dẫn bất thường;
* cấu hình bị thay đổi gần thời điểm xảy ra sự cố;
* chính sách bảo mật bị tắt hoặc bị sửa;
* dịch vụ lạ được đăng ký trong Registry.

Trong điều tra sự cố, Registry thường được kiểm tra để tìm dấu vết về:

* chương trình tự khởi động;
* phần mềm đã cài đặt;
* dịch vụ độc hại;
* cấu hình persistence;
* thay đổi chính sách hệ thống;
* thông tin người dùng và môi trường hệ thống.

Tuy nhiên, cần phân tích Registry cẩn thận vì không phải mọi key lạ đều là độc hại. Một số phần mềm hợp pháp cũng tạo nhiều key và value trong Registry.

Tóm lại, Registry là cơ sở dữ liệu cấu hình trung tâm của Windows. Đối với quản trị viên và SOC Analyst, hiểu Registry giúp kiểm tra hệ thống sâu hơn, phát hiện cấu hình bất thường và hỗ trợ điều tra bảo mật.

# 17. Windows Update

## 17.1. Windows Update là gì?

**Windows Update** là dịch vụ cập nhật của Microsoft dành cho hệ điều hành Windows. Dịch vụ này cho phép Windows tải xuống và cài đặt các bản cập nhật cần thiết để cải thiện bảo mật, sửa lỗi và bổ sung tính năng mới cho hệ thống.

Windows Update có thể cung cấp nhiều loại cập nhật khác nhau, ví dụ:

- bản vá bảo mật;
- bản sửa lỗi hệ thống;
- bản cập nhật tính năng;
- bản cập nhật driver;
- bản cập nhật cho Microsoft Defender;
- bản cập nhật chất lượng hệ thống.

Trong các phiên bản Windows hiện đại, Windows Update thường hoạt động tự động. Hệ thống sẽ kiểm tra, tải xuống và cài đặt các bản cập nhật khi có sẵn. Tuy nhiên, trong một số trường hợp, người dùng vẫn cần khởi động lại máy để hoàn tất quá trình cập nhật.

Windows Update là một thành phần quan trọng giúp hệ điều hành hoạt động ổn định, an toàn và tương thích tốt hơn với phần mềm, phần cứng mới.


## 17.2. Vai trò của Windows Update trong bảo mật

Windows Update có vai trò rất quan trọng trong bảo mật hệ thống. Nhiều cuộc tấn công mạng khai thác các lỗ hổng đã biết trong hệ điều hành, dịch vụ hoặc thành phần phần mềm. Nếu hệ thống không được cập nhật, các lỗ hổng này có thể bị kẻ tấn công lợi dụng.

Vai trò bảo mật của Windows Update gồm:

- vá các lỗ hổng bảo mật đã được phát hiện;
- giảm nguy cơ bị khai thác bởi mã độc;
- cập nhật cơ chế bảo vệ của Windows;
- cải thiện khả năng chống lại các kỹ thuật tấn công mới;
- cập nhật Microsoft Defender và các thành phần bảo mật;
- tăng độ ổn định của hệ thống.

Ví dụ, nếu một lỗ hổng nghiêm trọng trong Windows được công bố, Microsoft có thể phát hành bản vá thông qua Windows Update. Nếu người dùng không cài đặt bản vá, máy tính vẫn có thể bị tấn công qua lỗ hổng đó.

Trong môi trường doanh nghiệp, việc quản lý cập nhật là một phần quan trọng của chiến lược bảo mật. Máy tính không được cập nhật thường xuyên có thể trở thành điểm yếu trong toàn bộ hệ thống mạng.


## 17.3. Security Updates

**Security Updates** là các bản cập nhật bảo mật dùng để vá lỗ hổng trong Windows hoặc các thành phần liên quan.

Các bản cập nhật này thường được phát hành khi Microsoft phát hiện hoặc xác nhận một vấn đề bảo mật có thể ảnh hưởng đến người dùng. Mục tiêu chính của Security Updates là giảm nguy cơ hệ thống bị khai thác.

Security Updates có thể khắc phục các vấn đề như:

- lỗ hổng thực thi mã từ xa;
- lỗ hổng leo thang đặc quyền;
- lỗ hổng bỏ qua cơ chế bảo mật;
- lỗi trong dịch vụ hệ thống;
- lỗi trong giao thức mạng;
- lỗi trong thành phần xác thực;
- lỗ hổng trong trình điều khiển hoặc thư viện hệ thống.

Từ góc độ an toàn thông tin, Security Updates là loại cập nhật quan trọng nhất. Nếu không cài đặt các bản vá bảo mật kịp thời, hệ thống có thể bị tấn công ngay cả khi người dùng không trực tiếp thực hiện hành động nguy hiểm.

Vì vậy, người dùng cá nhân và doanh nghiệp cần ưu tiên cài đặt Security Updates, đặc biệt là các bản vá cho lỗ hổng nghiêm trọng.


## 17.4. Feature Updates

**Feature Updates** là các bản cập nhật tính năng của Windows. Khác với Security Updates, Feature Updates thường bổ sung chức năng mới, cải thiện giao diện hoặc thay đổi một số thành phần lớn của hệ điều hành.

Feature Updates có thể bao gồm:

- tính năng mới của Windows;
- thay đổi giao diện người dùng;
- cải thiện hiệu suất;
- cải thiện khả năng tương thích;
- cập nhật công cụ hệ thống;
- thay đổi trong Windows Security;
- bổ sung chức năng quản trị mới.

Các bản cập nhật tính năng thường có dung lượng lớn hơn và thời gian cài đặt lâu hơn so với bản cập nhật bảo mật thông thường.

Trong môi trường doanh nghiệp, Feature Updates cần được kiểm tra kỹ trước khi triển khai rộng rãi. Lý do là một số tính năng mới có thể ảnh hưởng đến phần mềm nội bộ, driver, chính sách hệ thống hoặc quy trình làm việc của người dùng.

Vì vậy, doanh nghiệp thường triển khai Feature Updates theo kế hoạch, thử nghiệm trên một nhóm máy trước khi áp dụng cho toàn bộ tổ chức.


## 17.5. Patch Tuesday

**Patch Tuesday** là thuật ngữ dùng để chỉ ngày Microsoft thường phát hành các bản vá định kỳ hằng tháng.

Thông thường, Patch Tuesday diễn ra vào **thứ Ba của tuần thứ hai trong tháng**. Vào thời điểm này, Microsoft có thể phát hành các bản vá bảo mật, bản sửa lỗi và các cập nhật liên quan cho Windows và sản phẩm Microsoft khác.

Patch Tuesday quan trọng vì đây là thời điểm quản trị viên hệ thống thường theo dõi các bản vá mới, đánh giá mức độ nghiêm trọng và lập kế hoạch triển khai cập nhật.

Trong môi trường doanh nghiệp, quy trình sau Patch Tuesday thường gồm:

1. Theo dõi danh sách bản vá mới.
2. Xác định bản vá nào quan trọng hoặc nghiêm trọng.
3. Kiểm tra ảnh hưởng đến hệ thống hiện tại.
4. Thử nghiệm trên một nhóm máy nhỏ.
5. Triển khai cho toàn bộ hệ thống.
6. Theo dõi lỗi sau cập nhật.

Từ góc độ bảo mật, Patch Tuesday giúp doanh nghiệp duy trì lịch cập nhật định kỳ và giảm nguy cơ tồn tại lỗ hổng chưa được vá trong hệ thống.


## 17.6. Cách mở Windows Update

Có nhiều cách để mở Windows Update trong Windows.

Cách phổ biến nhất là mở qua Windows Settings:

1. Nhấn **Start**.
2. Chọn **Settings**.
3. Chọn **Update & Security**.
4. Chọn **Windows Update**.

Trong Windows 11, đường dẫn có thể là:

```text
Settings → Windows Update
````

Ngoài ra, có thể mở nhanh bằng cách:

1. Nhấn **Start**.
2. Gõ từ khóa:

```text
Windows Update
```

3. Chọn **Windows Update settings**.

Trong giao diện Windows Update, người dùng có thể:

* kiểm tra bản cập nhật mới;
* xem trạng thái cập nhật;
* tải xuống bản cập nhật;
* cài đặt bản cập nhật;
* xem lịch sử cập nhật;
* tạm dừng cập nhật;
* cấu hình giờ hoạt động;
* kiểm tra yêu cầu khởi động lại.


Có thể mở Windows Update bằng lệnh trong hộp thoại Run, Command Prompt hoặc PowerShell.

Một lệnh thường dùng là:

```cmd
control /name Microsoft.WindowsUpdate
```

Cách thực hiện:

1. Nhấn tổ hợp phím:

```text
Win + R
```

2. Nhập lệnh:

```cmd
control /name Microsoft.WindowsUpdate
```

3. Nhấn **Enter**.

Lệnh này giúp mở nhanh giao diện Windows Update mà không cần đi qua nhiều bước trong Settings.

Ngoài ra, người dùng có thể tìm kiếm trực tiếp bằng Start Menu với từ khóa:

```text
Windows Update
```

![](./img/17.6_windows_update.png)

Trong quản trị hệ thống, việc biết lệnh mở nhanh Windows Update giúp tiết kiệm thời gian khi cần kiểm tra trạng thái cập nhật trên nhiều máy.

## 17.7. Restart Required

**Restart Required** nghĩa là hệ thống cần được khởi động lại để hoàn tất quá trình cài đặt bản cập nhật.

Một số bản cập nhật có thể được cài đặt khi Windows đang chạy. Tuy nhiên, các bản cập nhật liên quan đến kernel, driver, dịch vụ hệ thống hoặc tệp đang được sử dụng thường cần khởi động lại để áp dụng hoàn toàn.

Khi Windows Update hiển thị trạng thái Restart Required, người dùng nên lưu lại công việc đang làm và khởi động lại máy vào thời điểm phù hợp.

Nếu không khởi động lại, bản cập nhật có thể chưa được áp dụng đầy đủ. Điều này có thể khiến hệ thống vẫn còn tồn tại lỗi hoặc lỗ hổng bảo mật.

Trong môi trường doanh nghiệp, việc khởi động lại sau cập nhật cần được quản lý cẩn thận để tránh gián đoạn công việc. Quản trị viên thường cấu hình thời gian cập nhật và khởi động lại ngoài giờ làm việc.

# 18. Windows Security

## 18.1. Windows Security là gì?

**Windows Security** là trung tâm bảo mật tích hợp sẵn trong Windows. Đây là nơi người dùng có thể kiểm tra trạng thái bảo vệ của hệ thống và quản lý các tính năng bảo mật quan trọng.

![](./img/18.1_windows_security.png)

Windows Security giúp bảo vệ máy tính khỏi nhiều rủi ro như:

- virus;
- malware;
- ransomware;
- truy cập trái phép;
- ứng dụng không an toàn;
- website độc hại;
- cấu hình bảo mật yếu;
- vấn đề liên quan đến thiết bị và phần cứng.

Trong các phiên bản Windows hiện đại, Windows Security được tích hợp trực tiếp vào hệ điều hành. Người dùng không cần cài đặt thêm phần mềm bên ngoài để có các chức năng bảo vệ cơ bản.

Windows Security thường bao gồm nhiều khu vực bảo vệ khác nhau, ví dụ như:

- Virus & Threat Protection;
- Firewall & Network Protection;
- App & Browser Control;
- Device Security.

Đối với người dùng cá nhân, Windows Security giúp kiểm tra nhanh máy tính có đang được bảo vệ hay không. Đối với người học an toàn thông tin, đây là công cụ cơ bản để hiểu các lớp bảo vệ mặc định của Windows.


## 18.2. Protection Areas

**Protection Areas** là các khu vực bảo vệ chính trong Windows Security. Mỗi khu vực phụ trách một nhóm chức năng bảo mật riêng.

Các Protection Areas quan trọng gồm:

| Protection Area | Chức năng chính |
|---|---|
| Virus & Threat Protection | Bảo vệ hệ thống khỏi virus, malware và các mối đe dọa khác |
| Firewall & Network Protection | Quản lý tường lửa và bảo vệ kết nối mạng |
| App & Browser Control | Bảo vệ khi chạy ứng dụng và truy cập web |
| Device Security | Kiểm tra các tính năng bảo mật phần cứng và bảo mật lõi hệ thống |

Ngoài ra, tùy phiên bản Windows và cấu hình hệ thống, Windows Security có thể hiển thị thêm một số khu vực khác như:

- Account Protection;
- Device Performance & Health;
- Family Options.

Các Protection Areas giúp người dùng kiểm tra tình trạng bảo mật theo từng nhóm rõ ràng. Nếu có vấn đề, Windows Security thường hiển thị cảnh báo để người dùng xử lý.


## 18.3. Ý nghĩa biểu tượng trạng thái bảo mật

Windows Security sử dụng các biểu tượng trạng thái để cho biết tình trạng bảo mật của từng khu vực.

Các màu thường gặp gồm:

- màu xanh lá cây;
- màu vàng;
- màu đỏ.

Nhờ các biểu tượng này, người dùng có thể nhanh chóng biết hệ thống đang an toàn, cần chú ý hay đang có vấn đề nghiêm trọng.


### 18.3.1. Màu xanh lá cây

Biểu tượng **màu xanh lá cây** thường cho biết trạng thái bảo mật đang tốt.

![](./img/18.3_green.png)

Điều này có nghĩa là khu vực bảo vệ đó đang hoạt động bình thường và không có hành động khẩn cấp nào cần thực hiện.

Ví dụ:

- antivirus đang bật;
- không phát hiện mối đe dọa;
- firewall đang hoạt động;
- thiết bị không có cảnh báo bảo mật quan trọng;
- các thiết lập bảo vệ chính đang được bật.

Khi thấy biểu tượng màu xanh lá cây, người dùng có thể hiểu rằng Windows Security chưa phát hiện vấn đề nghiêm trọng ở khu vực đó.


### 18.3.2. Màu vàng

Biểu tượng **màu vàng** thường cho biết có vấn đề cần chú ý hoặc cần người dùng kiểm tra thêm.

![](./img/18.3_yellow.png)

Trạng thái này không nhất thiết có nghĩa là hệ thống đang bị tấn công, nhưng cho thấy có một thiết lập hoặc cảnh báo cần được xem xét.

Ví dụ:

- cần bật một tính năng bảo vệ;
- cần kiểm tra cảnh báo bảo mật;
- có khuyến nghị từ Windows Security;
- cần cập nhật hoặc quét hệ thống;
- có thiết lập chưa tối ưu.

Khi thấy biểu tượng màu vàng, người dùng nên mở khu vực đó để xem Windows đề xuất hành động gì.


### 18.3.3. Màu đỏ

Biểu tượng **màu đỏ** thường cho biết có vấn đề nghiêm trọng cần xử lý ngay.

![](./img/18.3_red.png)

Ví dụ:

- antivirus bị tắt;
- firewall bị tắt;
- phát hiện mối đe dọa;
- hệ thống có nguy cơ cao;
- một thành phần bảo vệ quan trọng không hoạt động.

Khi thấy biểu tượng màu đỏ, người dùng không nên bỏ qua. Cần mở Windows Security, kiểm tra nguyên nhân và thực hiện hành động khắc phục càng sớm càng tốt.

Trong môi trường doanh nghiệp, trạng thái màu đỏ trên máy trạm có thể là dấu hiệu cần gửi cảnh báo cho quản trị viên hoặc SOC.


## 18.4. Virus & Threat Protection

**Virus & Threat Protection** là khu vực trong Windows Security dùng để bảo vệ hệ thống khỏi virus, malware và các mối đe dọa khác.

![](./img/18.4_virus_and_threat_protection.png)

Khu vực này thường liên quan đến Microsoft Defender Antivirus, công cụ chống mã độc tích hợp sẵn trong Windows.

Trong Virus & Threat Protection, người dùng có thể:

- kiểm tra trạng thái bảo vệ hiện tại;
- xem lịch sử mối đe dọa;
- chạy quét nhanh;
- chạy quét đầy đủ;
- chạy quét tùy chỉnh;
- cấu hình bảo vệ thời gian thực;
- bật bảo vệ dựa trên đám mây;
- quản lý exclusions;
- kiểm tra ransomware protection.

Một số loại quét thường gặp gồm:

| Loại quét | Ý nghĩa |
|---|---|
| Quick scan | Quét nhanh các khu vực thường bị mã độc lợi dụng |
| Full scan | Quét toàn bộ hệ thống |
| Custom scan | Quét tệp hoặc thư mục do người dùng chọn |
| Microsoft Defender Offline scan | Quét ngoại tuyến để xử lý một số mã độc khó loại bỏ |

Virus & Threat Protection rất quan trọng vì malware có thể gây nhiều hậu quả như đánh cắp dữ liệu, mã hóa tệp, theo dõi người dùng hoặc mở cửa hậu cho kẻ tấn công.

Đối với người học SOC, khu vực này giúp hiểu cách Windows phát hiện, cách ly và xử lý các mối đe dọa cơ bản trên endpoint.


## 18.5. Firewall & Network Protection

**Firewall & Network Protection** là khu vực dùng để quản lý tường lửa và bảo vệ kết nối mạng của Windows.

![](./img/18.5_firewall_network_protection.png)

Windows Firewall giúp kiểm soát lưu lượng mạng vào và ra khỏi máy tính. Nó có thể cho phép hoặc chặn kết nối dựa trên hồ sơ mạng, ứng dụng, cổng hoặc quy tắc tường lửa.

Trong Firewall & Network Protection, thường có ba loại network profile:

| Network Profile | Ý nghĩa |
|---|---|
| Domain network | Dùng khi máy tính tham gia domain trong doanh nghiệp |
| Private network | Dùng cho mạng riêng đáng tin cậy, ví dụ mạng gia đình hoặc nội bộ |
| Public network | Dùng cho mạng công cộng, ví dụ Wi-Fi ở quán cà phê, sân bay |

Public network thường có mức bảo vệ nghiêm ngặt hơn vì đây là môi trường ít đáng tin cậy hơn.

Trong khu vực này, người dùng có thể:

- kiểm tra firewall đang bật hay tắt;
- xem trạng thái từng network profile;
- cho phép ứng dụng đi qua firewall;
- mở Advanced settings;
- cấu hình quy tắc inbound và outbound;
- khôi phục firewall về mặc định.

Từ góc độ bảo mật, firewall là lớp phòng thủ quan trọng giúp giảm nguy cơ truy cập trái phép vào máy tính qua mạng.


## 18.6. App & Browser Control

**App & Browser Control** là khu vực trong Windows Security dùng để bảo vệ người dùng khi chạy ứng dụng và truy cập nội dung trên web.

![](./img/18.6_app_browser_control.png)

Khu vực này liên quan đến các cơ chế như Microsoft Defender SmartScreen và Exploit Protection.

App & Browser Control có thể giúp bảo vệ khỏi:

- ứng dụng không rõ nguồn gốc;
- tệp tải xuống đáng ngờ;
- website độc hại;
- nội dung lừa đảo;
- khai thác lỗ hổng trong ứng dụng;
- phần mềm có hành vi không an toàn.

Một số chức năng thường gặp gồm:

| Chức năng | Ý nghĩa |
|---|---|
| Check apps and files | Kiểm tra ứng dụng và tệp tải xuống |
| SmartScreen for Microsoft Edge | Bảo vệ khi duyệt web bằng Microsoft Edge |
| Potentially unwanted app blocking | Chặn ứng dụng không mong muốn |
| Exploit Protection | Giảm rủi ro từ các kỹ thuật khai thác lỗ hổng |

Khi người dùng tải hoặc chạy một tệp không rõ nguồn gốc, SmartScreen có thể hiển thị cảnh báo nếu tệp đó có dấu hiệu đáng ngờ.

Đối với an toàn thông tin, App & Browser Control rất quan trọng vì nhiều cuộc tấn công bắt đầu từ việc người dùng tải tệp độc hại hoặc truy cập website giả mạo.


## 18.7. Device Security

**Device Security** là khu vực trong Windows Security dùng để kiểm tra và quản lý các tính năng bảo mật liên quan đến phần cứng và bảo vệ lõi hệ thống.

![](./img/18.7_device_security.png)

Khu vực này thường hiển thị các tính năng như:

- Core Isolation;
- Memory Integrity;
- Security Processor;
- TPM;
- Secure Boot nếu thiết bị hỗ trợ.

Một số thành phần quan trọng:

| Thành phần | Ý nghĩa |
|---|---|
| Core Isolation | Cô lập các tiến trình quan trọng của hệ thống để tăng bảo mật |
| Memory Integrity | Giúp ngăn mã độc can thiệp vào vùng nhớ quan trọng |
| Security Processor | Liên quan đến TPM và bảo vệ khóa mã hóa |
| TPM | Chip hoặc mô-đun bảo mật dùng cho các chức năng như BitLocker |
| Secure Boot | Giúp ngăn mã độc can thiệp vào quá trình khởi động |

Device Security phụ thuộc vào phần cứng của máy tính. Nếu thiết bị không hỗ trợ một số tính năng, Windows có thể không hiển thị đầy đủ các mục này.

Trong môi trường doanh nghiệp, Device Security giúp nâng cao mức bảo vệ của endpoint, đặc biệt khi kết hợp với BitLocker, Secure Boot và các chính sách bảo mật tập trung.


## 18.8. Windows Security trong Windows Server

Trong Windows Server, các chức năng bảo mật cũng rất quan trọng, nhưng cách quản lý có thể khác so với Windows Desktop.

Windows Server thường được dùng để cung cấp dịch vụ cho nhiều người dùng hoặc nhiều hệ thống khác nhau. Vì vậy, bảo mật trên Windows Server cần được cấu hình cẩn thận hơn, đặc biệt đối với các máy chủ như:

- Domain Controller;
- File Server;
- DNS Server;
- DHCP Server;
- Web Server;
- Remote Desktop Server.

Trên Windows Server, quản trị viên cần quan tâm đến:

- cập nhật bảo mật;
- firewall;
- antivirus hoặc Microsoft Defender;
- quyền truy cập;
- chính sách đăng nhập;
- dịch vụ đang chạy;
- cấu hình mạng;
- Event Logs;
- tài khoản quản trị;
- bảo vệ dữ liệu.

Windows Security trên máy chủ có thể không được sử dụng theo cách giống hoàn toàn với máy tính cá nhân. Trong doanh nghiệp, bảo mật máy chủ thường được quản lý kết hợp với Group Policy, Windows Defender for Endpoint, SIEM, EDR và các công cụ quản trị tập trung khác.

# 19. Virus & Threat Protection

## 19.1. Current Threats

**Current Threats** là khu vực hiển thị tình trạng mối đe dọa hiện tại trên hệ thống Windows. Đây là nơi người dùng có thể kiểm tra xem Windows Security có phát hiện virus, malware hoặc hành vi đáng nghi nào hay không.

![](./img/19.1_current_threats.png)

Trong phần Current Threats, Windows thường hiển thị các thông tin như:

- trạng thái bảo vệ hiện tại;
- thời gian quét gần nhất;
- số lượng tệp đã được quét;
- mối đe dọa được phát hiện nếu có;
- hành động cần thực hiện;
- trạng thái xử lý mối đe dọa.

Nếu hệ thống không phát hiện vấn đề, Windows Security thường hiển thị trạng thái an toàn. Nếu phát hiện mối đe dọa, người dùng có thể thấy cảnh báo và các tùy chọn xử lý như cách ly, xóa hoặc cho phép.

Current Threats rất quan trọng vì nó giúp người dùng nhanh chóng biết máy tính có đang gặp nguy cơ bảo mật hay không.


## 19.2. Scan Options

**Scan Options** là phần cho phép người dùng chọn kiểu quét malware trên hệ thống.

![](./img/19.2_scan_options.png)

Windows Security cung cấp nhiều loại quét khác nhau tùy theo nhu cầu. Nếu cần kiểm tra nhanh, có thể dùng Quick Scan. Nếu cần kiểm tra toàn bộ hệ thống, có thể dùng Full Scan. Nếu chỉ muốn kiểm tra một thư mục hoặc tệp cụ thể, có thể dùng Custom Scan.

Các tùy chọn quét thường gặp gồm:

| Loại quét | Mục đích |
|---|---|
| Quick Scan | Quét nhanh các khu vực thường bị malware lợi dụng |
| Full Scan | Quét toàn bộ hệ thống |
| Custom Scan | Quét tệp hoặc thư mục do người dùng chọn |
| Microsoft Defender Offline Scan | Quét ngoại tuyến để xử lý một số malware khó loại bỏ |

Việc chọn đúng loại quét giúp tiết kiệm thời gian và tăng hiệu quả phát hiện mối đe dọa.


### 19.2.1. Quick Scan

**Quick Scan** là chế độ quét nhanh của Windows Security.

Chế độ này thường kiểm tra các khu vực quan trọng và thường bị malware lợi dụng, ví dụ:

- thư mục hệ thống;
- tiến trình đang chạy;
- vị trí khởi động cùng Windows;
- một số khu vực nhạy cảm trong hệ điều hành.

Quick Scan có thời gian thực hiện ngắn hơn Full Scan, nên phù hợp để kiểm tra nhanh tình trạng hệ thống.

Nên dùng Quick Scan khi:

- muốn kiểm tra nhanh máy tính;
- vừa tải tệp từ Internet;
- nghi ngờ máy có dấu hiệu bất thường nhẹ;
- cần kiểm tra định kỳ hằng ngày hoặc hằng tuần.

Tuy nhiên, Quick Scan không kiểm tra toàn bộ tệp trên hệ thống, vì vậy nếu nghi ngờ máy bị nhiễm malware nghiêm trọng, nên dùng Full Scan hoặc Microsoft Defender Offline Scan.


### 19.2.2. Full Scan

**Full Scan** là chế độ quét toàn bộ hệ thống.

Chế độ này kiểm tra tất cả tệp và chương trình đang chạy trên ổ đĩa. Vì phạm vi quét rộng hơn nên Full Scan thường mất nhiều thời gian hơn Quick Scan.

Full Scan phù hợp trong các trường hợp:

- nghi ngờ máy tính bị nhiễm malware;
- hệ thống có hành vi bất thường;
- máy chạy chậm không rõ nguyên nhân;
- sau khi phát hiện mối đe dọa;
- cần kiểm tra kỹ toàn bộ hệ thống.

Ưu điểm của Full Scan là kiểm tra sâu hơn và toàn diện hơn. Tuy nhiên, quá trình quét có thể làm máy tính chậm hơn trong lúc đang chạy, đặc biệt trên máy có ổ đĩa lớn hoặc nhiều tệp.

Trong môi trường doanh nghiệp, Full Scan thường được lên lịch vào thời điểm ít ảnh hưởng đến người dùng, ví dụ ngoài giờ làm việc.


### 19.2.3. Custom Scan

**Custom Scan** là chế độ quét tùy chỉnh, cho phép người dùng chọn tệp, thư mục hoặc ổ đĩa cụ thể để kiểm tra.

Custom Scan phù hợp khi người dùng muốn kiểm tra một khu vực nhất định, ví dụ:

- thư mục Downloads;
- USB vừa cắm vào máy;
- thư mục chứa file nghi ngờ;
- file cài đặt vừa tải về;
- thư mục chia sẻ;
- ổ đĩa ngoài.

Ví dụ, nếu người dùng tải một file lạ từ Internet, có thể dùng Custom Scan để quét riêng file hoặc thư mục đó trước khi mở.

Custom Scan giúp tiết kiệm thời gian vì không cần quét toàn bộ hệ thống. Tuy nhiên, nó chỉ kiểm tra khu vực được chọn, nên không thay thế hoàn toàn cho Full Scan trong trường hợp cần kiểm tra toàn diện.


## 19.3. Threat History

**Threat History** là phần hiển thị lịch sử các mối đe dọa mà Windows Security đã phát hiện hoặc xử lý.

![](./img/19.3_threat_history.png)

Trong Threat History, người dùng có thể xem lại:

- mối đe dọa đã phát hiện;
- thời điểm phát hiện;
- mức độ nghiêm trọng;
- hành động đã thực hiện;
- tệp hoặc vị trí liên quan;
- trạng thái hiện tại của mối đe dọa.

Threat History rất hữu ích khi cần kiểm tra xem trước đó hệ thống đã từng phát hiện malware hay chưa.

Trong điều tra bảo mật, Threat History giúp trả lời các câu hỏi như:

- malware được phát hiện khi nào;
- tệp độc hại nằm ở đâu;
- Windows đã xử lý mối đe dọa như thế nào;
- mối đe dọa đã bị xóa hay vẫn còn tồn tại;
- người dùng có cho phép mối đe dọa nào chạy hay không.


## 19.4. Quarantined Threats

**Quarantined Threats** là các mối đe dọa đã bị Windows Security cách ly.

Khi một tệp hoặc chương trình bị cách ly, nó không bị xóa ngay lập tức nhưng bị đưa vào trạng thái không thể hoạt động bình thường. Điều này giúp ngăn mối đe dọa tiếp tục gây hại cho hệ thống.

Cách ly thường được sử dụng khi Windows Security phát hiện:

- virus;
- trojan;
- spyware;
- ransomware;
- file thực thi đáng nghi;
- script độc hại;
- phần mềm có hành vi nguy hiểm.

Trong phần Quarantined Threats, người dùng có thể xem các mối đe dọa đã bị cách ly và chọn hành động tiếp theo, ví dụ:

- xóa khỏi hệ thống;
- khôi phục nếu đó là nhận diện nhầm;
- xem thêm thông tin chi tiết.

Không nên khôi phục tệp bị cách ly nếu không chắc chắn rằng tệp đó an toàn. Nếu cần khôi phục, nên kiểm tra kỹ nguồn gốc tệp và có thể quét lại bằng công cụ bảo mật khác.


## 19.5. Allowed Threats

**Allowed Threats** là danh sách các mối đe dọa hoặc tệp đáng nghi mà người dùng đã cho phép chạy trên hệ thống.

![](./img/19.5_allowed_threats.png)

Khi một tệp bị Windows Security phát hiện là nguy hiểm hoặc đáng nghi, người dùng có thể chọn cho phép nếu tin rằng đó là nhận diện nhầm. Khi đó, tệp có thể xuất hiện trong danh sách Allowed Threats.

Tuy nhiên, đây là khu vực cần đặc biệt cẩn thận. Nếu người dùng cho phép nhầm một tệp độc hại, Windows Security có thể không tiếp tục chặn tệp đó.

Allowed Threats có thể tạo rủi ro nếu:

- người dùng không hiểu rõ tệp đã cho phép;
- malware bị nhận diện nhưng vẫn được cho chạy;
- kẻ tấn công lừa người dùng thêm tệp độc hại vào danh sách cho phép;
- phần mềm nguy hiểm bị bỏ qua trong các lần quét sau.

Trong kiểm tra bảo mật, cần xem lại danh sách Allowed Threats để đảm bảo không có tệp độc hại hoặc tệp không rõ nguồn gốc được cho phép nhầm.


## 19.6. Virus & Threat Protection Settings

**Virus & Threat Protection Settings** là phần cài đặt bảo vệ chống virus và mối đe dọa trong Windows Security.

![](./img/19.6_virus_and_threat_protection_settings.png)

Tại đây, người dùng có thể cấu hình các tính năng bảo vệ quan trọng như:

- Real-Time Protection;
- Cloud-Delivered Protection;
- Automatic Sample Submission;
- Controlled Folder Access;
- Exclusions;
- Notifications;
- Ransomware Protection.

Các thiết lập này ảnh hưởng trực tiếp đến khả năng phát hiện và ngăn chặn malware của Windows Security.

Trong hầu hết trường hợp, người dùng nên giữ các tính năng bảo vệ chính ở trạng thái bật. Việc tắt hoặc cấu hình sai có thể làm giảm khả năng bảo vệ của hệ thống.

Trong môi trường doanh nghiệp, các thiết lập này thường được quản lý tập trung bằng Group Policy, Microsoft Intune, Microsoft Defender for Endpoint hoặc các giải pháp quản lý endpoint khác.


### 19.6.1. Real-Time Protection

**Real-Time Protection** là tính năng bảo vệ thời gian thực của Microsoft Defender Antivirus.

![](./img/19.6_realtime_protection.png)

Khi tính năng này được bật, Windows Security sẽ liên tục giám sát hệ thống để phát hiện hoạt động đáng nghi hoặc tệp độc hại.

Real-Time Protection có thể kiểm tra:

- file khi được mở;
- file khi được tải xuống;
- chương trình khi được chạy;
- script đáng nghi;
- tiến trình có hành vi bất thường;
- một số thay đổi nguy hiểm trên hệ thống.

Đây là một trong những lớp bảo vệ quan trọng nhất của Windows Security. Nếu tắt Real-Time Protection, malware có thể có cơ hội chạy mà không bị phát hiện kịp thời.

Chỉ nên tắt Real-Time Protection trong trường hợp đặc biệt, ví dụ khi kiểm thử trong môi trường lab an toàn hoặc khi có yêu cầu kỹ thuật rõ ràng. Sau đó cần bật lại ngay.


### 19.6.2. Cloud-Delivered Protection

**Cloud-Delivered Protection** là tính năng bảo vệ dựa trên đám mây của Microsoft Defender.

![](./img/19.6_cloud_delivered_protection.png)

Khi bật tính năng này, Windows Security có thể sử dụng dữ liệu từ dịch vụ đám mây của Microsoft để phát hiện mối đe dọa nhanh hơn, đặc biệt là các malware mới hoặc chưa phổ biến.

Cloud-Delivered Protection giúp:

- cải thiện khả năng phát hiện malware mới;
- phản hồi nhanh hơn trước mối đe dọa;
- sử dụng thông tin bảo mật cập nhật từ Microsoft;
- hỗ trợ phân tích các tệp đáng nghi;
- tăng hiệu quả của Microsoft Defender Antivirus.

Tính năng này đặc biệt hữu ích vì nhiều malware hiện đại thay đổi rất nhanh. Nếu chỉ dựa vào chữ ký cục bộ trên máy, hệ thống có thể phản ứng chậm hơn.

Trong môi trường doanh nghiệp, Cloud-Delivered Protection thường được khuyến nghị bật nếu chính sách bảo mật và quyền riêng tư cho phép.


### 19.6.3. Automatic Sample Submission

**Automatic Sample Submission** là tính năng cho phép Windows Security tự động gửi mẫu tệp đáng nghi đến Microsoft để phân tích.

![](./img/19.6_automatic_sample_submision.png)

Khi Microsoft Defender phát hiện một tệp có dấu hiệu đáng ngờ nhưng chưa đủ thông tin để kết luận, hệ thống có thể gửi mẫu đó để kiểm tra thêm.

Tính năng này giúp:

- cải thiện khả năng phát hiện malware;
- hỗ trợ Microsoft phân tích mối đe dọa mới;
- tăng tốc độ cập nhật nhận diện;
- bảo vệ người dùng khác khỏi malware tương tự.

Tuy nhiên, trong một số môi trường doanh nghiệp, việc gửi mẫu tự động có thể liên quan đến chính sách bảo mật dữ liệu. Vì vậy, tổ chức cần cấu hình tính năng này phù hợp với yêu cầu nội bộ.

Đối với người dùng cá nhân, nên bật Automatic Sample Submission để tăng khả năng bảo vệ, trừ khi có lý do riêng về quyền riêng tư hoặc dữ liệu nhạy cảm.


### 19.6.4. Controlled Folder Access

**Controlled Folder Access** là tính năng giúp bảo vệ các thư mục quan trọng khỏi việc bị thay đổi trái phép bởi ứng dụng không đáng tin cậy.

![](./img/19.6_controlled_folder_access.png)

Tính năng này đặc biệt hữu ích trong việc chống ransomware. Ransomware thường cố gắng mã hóa tài liệu, hình ảnh, dữ liệu cá nhân hoặc thư mục làm việc của người dùng. Controlled Folder Access giúp ngăn các ứng dụng không được phép thay đổi những thư mục được bảo vệ.

Các thư mục thường cần bảo vệ gồm:

- Documents;
- Pictures;
- Desktop;
- Downloads;
- thư mục dữ liệu công việc;
- thư mục chứa tài liệu quan trọng.

Khi Controlled Folder Access được bật, chỉ các ứng dụng được tin cậy mới có thể thay đổi nội dung trong thư mục được bảo vệ.

Nếu một ứng dụng hợp pháp bị chặn nhầm, người dùng có thể thêm ứng dụng đó vào danh sách cho phép. Tuy nhiên, cần kiểm tra kỹ trước khi cho phép ứng dụng truy cập thư mục được bảo vệ.


### 19.6.5. Exclusions

**Exclusions** là danh sách loại trừ trong Windows Security. Các tệp, thư mục, tiến trình hoặc loại file được thêm vào Exclusions sẽ không bị Microsoft Defender quét hoặc giám sát theo cách thông thường.

![](./img/19.6_exclusions.png)

Exclusions có thể được sử dụng trong một số trường hợp hợp pháp, ví dụ:

- phần mềm nội bộ bị nhận diện nhầm;
- thư mục chứa file lab bảo mật;
- môi trường phát triển phần mềm;
- công cụ kiểm thử được phép sử dụng;
- thư mục có nhiều file tạm gây ảnh hưởng hiệu suất.

Tuy nhiên, Exclusions là khu vực có rủi ro cao. Nếu thêm sai thư mục hoặc file vào danh sách loại trừ, malware có thể lợi dụng vị trí đó để ẩn khỏi antivirus.

Không nên thêm các thư mục sau vào Exclusions nếu không có lý do rõ ràng:

- `C:\Users\<user>\Downloads`;
- `C:\Users\<user>\AppData`;
- `C:\Windows`;
- `C:\Windows\System32`;
- toàn bộ ổ `C:\`.

Trong điều tra bảo mật, cần kiểm tra danh sách Exclusions vì kẻ tấn công có thể cố gắng thêm đường dẫn độc hại vào đây để tránh bị phát hiện.


### 19.6.6. Notifications

**Notifications** là phần cài đặt thông báo của Windows Security.

![](./img/19.6_notifications.png)

Thông báo giúp người dùng biết khi có vấn đề bảo mật xảy ra, ví dụ:

- phát hiện malware;
- đã cách ly mối đe dọa;
- cần quét hệ thống;
- tính năng bảo vệ bị tắt;
- firewall có vấn đề;
- cần thực hiện hành động bảo mật.

Thông báo bảo mật rất quan trọng vì nếu người dùng không nhìn thấy cảnh báo, họ có thể không biết hệ thống đang gặp rủi ro.

Trong môi trường cá nhân, nên bật thông báo quan trọng của Windows Security để kịp thời xử lý khi có mối đe dọa.

Trong môi trường doanh nghiệp, thông báo trên máy người dùng có thể được kết hợp với cảnh báo tập trung gửi về hệ thống quản lý bảo mật, EDR hoặc SIEM.


## 19.7. Ransomware Protection

**Ransomware Protection** là nhóm tính năng giúp bảo vệ dữ liệu khỏi ransomware.

![](./img/19.7_ransomware_protection.png)

Ransomware là loại malware mã hóa tệp của nạn nhân và yêu cầu tiền chuộc để khôi phục dữ liệu. Đây là một trong những mối đe dọa nghiêm trọng đối với cả người dùng cá nhân và doanh nghiệp.

Trong Windows Security, Ransomware Protection thường liên quan đến:

- Controlled Folder Access;
- bảo vệ thư mục quan trọng;
- quản lý ứng dụng được phép truy cập thư mục;
- khôi phục dữ liệu nếu có tích hợp với dịch vụ sao lưu phù hợp.

Để tăng khả năng chống ransomware, nên:

- bật Controlled Folder Access nếu phù hợp;
- không mở file đính kèm đáng nghi;
- không chạy phần mềm không rõ nguồn gốc;
- cập nhật Windows thường xuyên;
- sao lưu dữ liệu quan trọng;
- không lưu bản sao lưu duy nhất trên cùng máy;
- kiểm tra cảnh báo từ Windows Security.

Ransomware Protection không thay thế hoàn toàn việc sao lưu dữ liệu. Sao lưu ngoại tuyến hoặc sao lưu trên hệ thống được bảo vệ vẫn là biện pháp rất quan trọng.


# 20. Firewall & Network Protection

## 20.1. Windows Defender Firewall là gì?

**Windows Defender Firewall** là tường lửa tích hợp sẵn trong Windows. Công cụ này giúp kiểm soát lưu lượng mạng đi vào và đi ra khỏi máy tính.

Firewall hoạt động như một lớp bảo vệ giữa máy tính và mạng bên ngoài. Nó có thể cho phép hoặc chặn kết nối dựa trên các quy tắc bảo mật đã được cấu hình.

Windows Defender Firewall có thể kiểm soát:

- ứng dụng nào được phép kết nối mạng;
- cổng mạng nào được mở;
- kết nối nào được phép đi vào máy;
- kết nối nào bị chặn;
- quy tắc mạng theo từng loại mạng khác nhau.

Trong Windows Security, phần quản lý firewall nằm tại:

```text
Windows Security → Firewall & network protection
```

## 20.2. Vai trò của firewall

Firewall có vai trò kiểm soát và lọc lưu lượng mạng để bảo vệ hệ thống khỏi các kết nối không mong muốn hoặc nguy hiểm.

Một firewall giúp:

* ngăn truy cập trái phép từ bên ngoài;
* giảm nguy cơ bị khai thác qua cổng mạng;
* kiểm soát ứng dụng nào được phép giao tiếp qua mạng;
* bảo vệ máy tính khi kết nối mạng công cộng;
* giới hạn bề mặt tấn công của hệ thống;
* hỗ trợ phát hiện và điều tra một số hành vi bất thường.

Ví dụ, nếu một dịch vụ trên máy tính đang lắng nghe trên một cổng mạng, firewall có thể chặn kết nối từ bên ngoài vào dịch vụ đó. Điều này giúp giảm nguy cơ kẻ tấn công truy cập trái phép.

Trong môi trường doanh nghiệp, firewall trên từng máy trạm là một lớp bảo vệ quan trọng bên cạnh firewall mạng, IDS/IPS, EDR và SIEM.

## 20.3. Firewall Profiles

Windows Defender Firewall sử dụng các **Firewall Profiles** để áp dụng mức bảo vệ khác nhau tùy theo loại mạng mà máy tính đang kết nối.

![](./img/20.3_firewall_profile.png)

Có ba profile chính:

* Domain Profile;
* Private Profile;
* Public Profile.

Mỗi profile có mục đích sử dụng khác nhau. Khi máy tính kết nối vào một mạng, Windows sẽ xác định loại mạng và áp dụng profile tương ứng.

### 20.3.1. Domain Profile

**Domain Profile** được sử dụng khi máy tính tham gia vào domain của doanh nghiệp và kết nối với mạng domain.

![](./img/20.3_domain.png)

Profile này thường áp dụng cho các máy tính trong môi trường tổ chức, nơi có Active Directory, Domain Controller và các chính sách quản lý tập trung.

Trong Domain Profile, quản trị viên có thể cấu hình firewall thông qua Group Policy để đảm bảo tất cả máy tính trong domain tuân thủ cùng một chính sách bảo mật.

Ví dụ, doanh nghiệp có thể cấu hình:

* cho phép một số dịch vụ nội bộ;
* chặn kết nối không cần thiết;
* cho phép quản trị từ xa từ máy quản trị;
* áp dụng quy tắc firewall thống nhất cho toàn bộ máy trạm.

Domain Profile thường được kiểm soát bởi quản trị viên hệ thống.

### 20.3.2. Private Profile

**Private Profile** được sử dụng khi máy tính kết nối vào mạng riêng đáng tin cậy, ví dụ như mạng gia đình hoặc mạng nội bộ nhỏ.

![](./img/20.3_private.png)

Mạng Private thường được xem là an toàn hơn mạng công cộng. Vì vậy, Windows có thể cho phép một số chức năng chia sẻ hoặc phát hiện thiết bị trong mạng nội bộ.

Private Profile thường phù hợp với:

* mạng gia đình;
* mạng văn phòng nhỏ;
* mạng nội bộ đáng tin cậy;
* môi trường lab cá nhân.

Tuy nhiên, dù là mạng riêng, vẫn cần bật firewall để bảo vệ máy tính khỏi các thiết bị khác trong cùng mạng nếu chúng bị nhiễm malware hoặc bị kiểm soát bởi kẻ tấn công.

### 20.3.3. Public Profile

**Public Profile** được sử dụng khi máy tính kết nối vào mạng công cộng hoặc mạng không đáng tin cậy.

![](./img/20.3_public.png)

Ví dụ:

* Wi-Fi ở quán cà phê;
* Wi-Fi sân bay;
* Wi-Fi khách sạn;
* mạng công cộng ở trường học;
* mạng không rõ chủ sở hữu.

Public Profile thường có mức bảo vệ nghiêm ngặt hơn Private Profile. Windows sẽ hạn chế khả năng chia sẻ và chặn nhiều kết nối đi vào hơn để giảm rủi ro bị tấn công.

Khi sử dụng mạng công cộng, nên để firewall bật và tránh bật các chức năng chia sẻ tệp nếu không cần thiết.

Từ góc độ bảo mật, Public Profile là profile cần được bảo vệ chặt chẽ nhất.

## 20.4. Bật và tắt Firewall

Người dùng có thể bật hoặc tắt Windows Defender Firewall trong phần Firewall & network protection.

Các bước cơ bản:

1. Mở **Windows Security**.
2. Chọn **Firewall & network protection**.
3. Chọn profile cần cấu hình: Domain, Private hoặc Public.
4. Bật hoặc tắt **Microsoft Defender Firewall**.

Tuy nhiên, không nên tắt firewall nếu không có lý do rõ ràng. Khi firewall bị tắt, máy tính có thể dễ bị truy cập trái phép hơn qua mạng.

Một số trường hợp người dùng tạm thời tắt firewall để kiểm tra lỗi kết nối hoặc kiểm thử trong lab. Sau khi kiểm tra xong, nên bật lại ngay.

Trong môi trường doanh nghiệp, người dùng thông thường thường không được phép tự ý tắt firewall. Thiết lập này có thể được quản lý tập trung bằng Group Policy hoặc công cụ quản lý endpoint.

## 20.5. Block All Incoming Connections

**Block All Incoming Connections** là tùy chọn dùng để chặn tất cả kết nối đi vào máy tính, kể cả các kết nối có thể đã nằm trong danh sách được cho phép.

Tùy chọn này thường được dùng khi cần tăng mức bảo vệ, đặc biệt khi máy tính đang kết nối vào mạng không đáng tin cậy.

Khi bật Block All Incoming Connections:

* các kết nối từ bên ngoài vào máy sẽ bị chặn;
* ứng dụng khác khó truy cập dịch vụ trên máy;
* giảm nguy cơ bị dò quét hoặc khai thác từ mạng;
* một số chức năng chia sẻ mạng có thể không hoạt động.

Tùy chọn này phù hợp khi:

* dùng Wi-Fi công cộng;
* nghi ngờ mạng đang không an toàn;
* cần tạm thời khóa các kết nối vào máy;
* muốn giảm tối đa bề mặt tấn công.

Tuy nhiên, nếu bật tùy chọn này trong mạng doanh nghiệp, một số dịch vụ hợp pháp như chia sẻ file, quản trị từ xa hoặc ứng dụng nội bộ có thể bị ảnh hưởng.

## 20.6. Allow an App Through Firewall

**Allow an App Through Firewall** là chức năng cho phép người dùng cấu hình ứng dụng nào được phép giao tiếp qua Windows Defender Firewall.

![](./img/20.6_allow_an_app_through_firewall.png)

Một số ứng dụng cần kết nối mạng để hoạt động, ví dụ:

* trình duyệt web;
* ứng dụng chat;
* phần mềm họp trực tuyến;
* game online;
* dịch vụ chia sẻ file;
* công cụ quản trị từ xa;
* ứng dụng nội bộ doanh nghiệp.

Để cho phép một ứng dụng đi qua firewall:

1. Mở **Windows Security**.
2. Chọn **Firewall & network protection**.
3. Chọn **Allow an app through firewall**.
4. Nhấn **Change settings** nếu cần quyền chỉnh sửa.
5. Chọn ứng dụng cần cho phép.
6. Chọn profile tương ứng: Private hoặc Public.
7. Nhấn **OK**.

Cần cẩn thận khi cho phép ứng dụng qua firewall. Không nên cho phép ứng dụng lạ hoặc không rõ nguồn gốc, đặc biệt trên Public Network.

Trong kiểm tra bảo mật, danh sách ứng dụng được cho phép qua firewall cần được rà soát định kỳ để phát hiện ứng dụng không cần thiết hoặc đáng nghi.

## 20.7. Advanced Firewall Settings

**Advanced Firewall Settings** là phần cấu hình nâng cao của Windows Defender Firewall.

![](./img/20.7_advanced_firewall_settings.png)

Tại đây, người dùng hoặc quản trị viên có thể tạo và quản lý các quy tắc firewall chi tiết hơn.

Các loại quy tắc chính gồm:

| Loại quy tắc              | Ý nghĩa                                              |
| ------------------------- | ---------------------------------------------------- |
| Inbound Rules             | Kiểm soát kết nối đi vào máy tính                    |
| Outbound Rules            | Kiểm soát kết nối đi ra khỏi máy tính                |
| Connection Security Rules | Cấu hình quy tắc bảo mật kết nối                     |
| Monitoring                | Theo dõi trạng thái firewall và quy tắc đang áp dụng |

Trong Advanced Firewall Settings, có thể tạo rule dựa trên:

* chương trình;
* cổng mạng;
* giao thức TCP hoặc UDP;
* địa chỉ IP;
* profile mạng;
* dịch vụ;
* hành động Allow hoặc Block.

Ví dụ, quản trị viên có thể tạo rule để:

* chặn kết nối đến một cổng cụ thể;
* chỉ cho phép Remote Desktop từ một địa chỉ IP quản trị;
* chặn ứng dụng không được kết nối Internet;
* cho phép dịch vụ nội bộ trong Domain Profile;
* chặn lưu lượng không cần thiết trên Public Profile.

Advanced Firewall Settings rất quan trọng trong môi trường doanh nghiệp vì nó cho phép kiểm soát kết nối mạng chi tiết và phù hợp với chính sách bảo mật.

**Công cụ `WF.msc`**

`WF.msc` là lệnh dùng để mở nhanh giao diện **Windows Defender Firewall with Advanced Security**.

Có thể mở bằng hộp thoại Run:

1. Nhấn tổ hợp phím:

```text
Win + R
```

2. Nhập lệnh:

```text
WF.msc
```

3. Nhấn **Enter**.

Công cụ này cho phép quản lý firewall ở mức nâng cao, bao gồm:

* Inbound Rules;
* Outbound Rules;
* Connection Security Rules;
* Monitoring;
* cấu hình profile Domain, Private và Public;
* tạo rule cho chương trình, cổng, giao thức hoặc địa chỉ IP.

`WF.msc` thường được sử dụng bởi quản trị viên hệ thống, người học Windows nâng cao và người làm an toàn thông tin.

Trong thực tế, khi cần cấu hình firewall chi tiết hơn phần Windows Security thông thường, `WF.msc` là công cụ nên sử dụng.


# 21. App & Browser Control

## 21.1. App & Browser Control là gì?

**App & Browser Control** là một khu vực trong Windows Security dùng để bảo vệ người dùng khi mở ứng dụng, chạy tệp tải xuống và truy cập các nội dung trên Internet.

Tính năng này giúp giảm nguy cơ người dùng chạy phải phần mềm độc hại, ứng dụng không rõ nguồn gốc hoặc truy cập vào website nguy hiểm.

App & Browser Control thường liên quan đến các cơ chế bảo vệ như:

- Microsoft Defender SmartScreen;
- kiểm tra ứng dụng và tệp tải xuống;
- cảnh báo website độc hại;
- bảo vệ khỏi ứng dụng không an toàn;
- Exploit Protection.

Có thể mở App & Browser Control theo đường dẫn:

```text
Windows Security → App & browser control
```

Đối với người dùng thông thường, đây là lớp bảo vệ quan trọng khi tải file từ Internet hoặc mở phần mềm chưa rõ nguồn gốc. Đối với người học an toàn thông tin, App & Browser Control giúp hiểu cách Windows giảm rủi ro từ ứng dụng và trình duyệt.

## 21.2. Microsoft Defender SmartScreen

**Microsoft Defender SmartScreen** là tính năng bảo mật của Windows dùng để kiểm tra ứng dụng, tệp tải xuống và website có dấu hiệu nguy hiểm.

![](./img/21.2_microsoft_defender_smartscreen.png)

SmartScreen có thể cảnh báo người dùng khi:

* mở một ứng dụng không rõ nguồn gốc;
* chạy file tải xuống từ Internet;
* truy cập website giả mạo;
* truy cập trang web có nội dung độc hại;
* mở tệp có mức độ tin cậy thấp;
* sử dụng ứng dụng chưa được nhận diện là an toàn.

Khi SmartScreen phát hiện rủi ro, Windows có thể hiển thị cảnh báo để người dùng cân nhắc trước khi tiếp tục. Điều này giúp ngăn người dùng vô tình chạy phần mềm độc hại hoặc truy cập trang web lừa đảo.

Ví dụ, nếu người dùng tải một file `.exe` từ một website không đáng tin cậy, SmartScreen có thể cảnh báo rằng file này có thể gây hại cho hệ thống.

SmartScreen không thay thế hoàn toàn antivirus, nhưng nó là một lớp bảo vệ bổ sung rất quan trọng, đặc biệt trong các tình huống liên quan đến Internet và tệp tải xuống.

## 21.3. Check Apps and Files

**Check Apps and Files** là tính năng kiểm tra ứng dụng và tệp trong App & Browser Control.

![](./img/21.2_check_app_and_files.png)

Tính năng này giúp Windows đánh giá độ an toàn của các ứng dụng và file mà người dùng chuẩn bị chạy. Nếu một file có nguồn gốc không rõ ràng hoặc có dấu hiệu đáng ngờ, Windows có thể hiển thị cảnh báo.

Check Apps and Files có thể giúp bảo vệ khỏi:

* file thực thi độc hại;
* chương trình không rõ nguồn gốc;
* phần mềm giả mạo;
* tệp tải xuống từ website không đáng tin cậy;
* ứng dụng có hành vi bất thường.

Các trạng thái cấu hình thường gặp có thể gồm:

| Trạng thái | Ý nghĩa                            |
| ---------- | ---------------------------------- |
| Block      | Chặn ứng dụng hoặc file đáng ngờ   |
| Warn       | Cảnh báo người dùng trước khi chạy |
| Off        | Tắt kiểm tra ứng dụng và file      |

Về mặt bảo mật, nên để tính năng này ở chế độ **Warn** hoặc **Block**. Không nên tắt nếu không có lý do rõ ràng, vì điều đó có thể làm tăng nguy cơ người dùng chạy phải phần mềm độc hại.

## 21.4. Bảo vệ khỏi website độc hại

App & Browser Control giúp bảo vệ người dùng khỏi các website độc hại thông qua Microsoft Defender SmartScreen và các cơ chế kiểm tra nội dung web.

Website độc hại có thể được dùng để:

* đánh cắp tài khoản;
* phát tán malware;
* lừa người dùng tải phần mềm giả mạo;
* giả mạo trang đăng nhập;
* khai thác lỗ hổng trình duyệt;
* thu thập thông tin cá nhân.

Khi người dùng truy cập một website có dấu hiệu nguy hiểm, SmartScreen có thể hiển thị cảnh báo. Cảnh báo này giúp người dùng dừng lại trước khi nhập thông tin nhạy cảm hoặc tải file độc hại.

Ví dụ, một website giả mạo trang đăng nhập ngân hàng hoặc email có thể bị SmartScreen chặn nếu nó đã được nhận diện là nguy hiểm.

Đối với người dùng cá nhân, tính năng này giúp giảm nguy cơ bị phishing. Đối với doanh nghiệp, nó giúp hạn chế nguy cơ nhân viên truy cập nhầm các website độc hại trong quá trình làm việc.

## 21.5. Bảo vệ khỏi ứng dụng không an toàn

App & Browser Control cũng giúp bảo vệ hệ thống khỏi các ứng dụng không an toàn hoặc không đáng tin cậy.

Ứng dụng không an toàn có thể bao gồm:

* phần mềm không rõ nguồn gốc;
* phần mềm giả mạo;
* phần mềm bị chỉnh sửa;
* công cụ có hành vi đáng ngờ;
* ứng dụng có khả năng gây hại;
* phần mềm không mong muốn.

Khi người dùng chạy một ứng dụng đáng nghi, Windows có thể hiển thị cảnh báo để người dùng quyết định có tiếp tục hay không.

Một số dấu hiệu của ứng dụng không an toàn gồm:

* tải từ website lạ;
* không có nhà phát hành rõ ràng;
* yêu cầu quyền Administrator không hợp lý;
* bị nhiều công cụ bảo mật cảnh báo;
* tên file giống phần mềm nổi tiếng nhưng nguồn tải không chính thức;
* nằm trong thư mục tạm hoặc thư mục tải xuống.

Trong an toàn thông tin, người dùng nên chỉ cài đặt phần mềm từ nguồn đáng tin cậy. Không nên bỏ qua cảnh báo của SmartScreen nếu không hiểu rõ file hoặc ứng dụng đó.

## 21.6. Exploit Protection

**Exploit Protection** là tính năng trong Windows dùng để giảm nguy cơ bị khai thác lỗ hổng trong ứng dụng hoặc hệ điều hành.

![](./img/21.6_exploit_protection.png)

Exploit là kỹ thuật lợi dụng lỗ hổng phần mềm để thực hiện hành vi trái phép, ví dụ như chạy mã độc, chiếm quyền điều khiển hoặc vượt qua cơ chế bảo vệ.

Exploit Protection giúp áp dụng một số cơ chế giảm thiểu rủi ro, ví dụ:

* ngăn một số hành vi khai thác bộ nhớ;
* hạn chế kỹ thuật tấn công vào tiến trình;
* áp dụng chính sách bảo vệ cho toàn hệ thống;
* cấu hình bảo vệ riêng cho từng chương trình;
* giảm khả năng khai thác lỗ hổng chưa được vá.

Trong Windows Security, Exploit Protection thường có hai nhóm cấu hình chính:

| Nhóm cấu hình    | Ý nghĩa                                    |
| ---------------- | ------------------------------------------ |
| System settings  | Áp dụng thiết lập bảo vệ cho toàn hệ thống |
| Program settings | Cấu hình bảo vệ riêng cho từng ứng dụng    |

Thông thường, người dùng phổ thông nên giữ cấu hình mặc định của Exploit Protection. Việc thay đổi tùy tiện có thể làm một số ứng dụng hoạt động không ổn định.

Đối với quản trị viên và chuyên viên bảo mật, Exploit Protection có thể được sử dụng để tăng cường bảo vệ cho các ứng dụng quan trọng hoặc ứng dụng có nguy cơ cao.

## 21.7. Cấu hình mặc định và khuyến nghị bảo mật

Trong hầu hết trường hợp, người dùng nên giữ cấu hình mặc định của App & Browser Control, vì đây là cấu hình đã được Windows thiết kế để cân bằng giữa bảo mật và khả năng sử dụng.

Một số khuyến nghị bảo mật gồm:

* bật Microsoft Defender SmartScreen;
* không tắt Check Apps and Files;
* không bỏ qua cảnh báo khi chạy file lạ;
* chỉ tải phần mềm từ nguồn chính thức;
* không chạy file `.exe`, `.bat`, `.cmd`, `.ps1` từ nguồn không rõ;
* giữ Exploit Protection ở cấu hình mặc định nếu không có yêu cầu đặc biệt;
* kiểm tra kỹ ứng dụng yêu cầu quyền Administrator;
* cập nhật Windows và trình duyệt thường xuyên.

Trong môi trường doanh nghiệp, App & Browser Control nên được quản lý bằng chính sách tập trung để đảm bảo người dùng không tự ý tắt các cơ chế bảo vệ quan trọng.

Từ góc độ SOC, cần chú ý các dấu hiệu như:

* SmartScreen bị tắt;
* người dùng thường xuyên bỏ qua cảnh báo;
* nhiều file không rõ nguồn gốc được tải xuống;
* ứng dụng lạ yêu cầu quyền cao;
* Exploit Protection bị thay đổi bất thường;
* trình duyệt truy cập nhiều website bị cảnh báo.

Tóm lại, App & Browser Control là một lớp bảo vệ quan trọng của Windows. Nó giúp giảm nguy cơ từ website độc hại, phần mềm không an toàn và các kỹ thuật khai thác lỗ hổng.


# 22. Device Security

## 22.1. Device Security là gì?

**Device Security** là khu vực trong Windows Security dùng để kiểm tra và quản lý các tính năng bảo mật liên quan đến phần cứng, firmware và các cơ chế bảo vệ lõi của hệ điều hành.

Khác với Virus & Threat Protection tập trung vào chống malware, Device Security tập trung nhiều hơn vào việc bảo vệ hệ thống ở mức thấp hơn, gần với phần cứng và quá trình khởi động.

Device Security có thể bao gồm các thành phần như:

- Core Isolation;
- Memory Integrity;
- Security Processor;
- TPM;
- Secure Boot;
- các tính năng bảo mật dựa trên ảo hóa.

Các tính năng này giúp bảo vệ Windows khỏi những kỹ thuật tấn công nâng cao, ví dụ như can thiệp vào bộ nhớ, tấn công vào quá trình khởi động hoặc cố gắng đánh cắp khóa mã hóa.

Tùy vào phần cứng của máy tính, Device Security có thể hiển thị đầy đủ hoặc chỉ hiển thị một số mục nhất định. Nếu thiết bị không hỗ trợ TPM, Secure Boot hoặc tính năng ảo hóa, một số tùy chọn có thể không xuất hiện.


## 22.2. Core Isolation

**Core Isolation** là tính năng bảo mật dùng để cô lập các tiến trình và thành phần quan trọng của Windows khỏi phần còn lại của hệ thống.

![](./img/22.2_core_isolation.png)

Cơ chế này sử dụng công nghệ bảo mật dựa trên ảo hóa để tạo ra một vùng bảo vệ riêng cho các thành phần nhạy cảm. Nhờ đó, nếu một tiến trình độc hại chạy trên hệ thống, nó sẽ khó can thiệp trực tiếp vào các phần quan trọng của Windows hơn.

Core Isolation giúp:

- bảo vệ các tiến trình hệ thống quan trọng;
- giảm nguy cơ mã độc can thiệp vào kernel;
- tăng khả năng chống khai thác lỗ hổng;
- hỗ trợ bảo vệ thông tin xác thực và dữ liệu nhạy cảm;
- tăng cường bảo mật cho hệ điều hành.

Trong môi trường doanh nghiệp, Core Isolation là một tính năng quan trọng vì nó giúp bảo vệ endpoint trước các kỹ thuật tấn công nâng cao.

Tuy nhiên, tính năng này phụ thuộc vào phần cứng và driver. Nếu driver cũ hoặc không tương thích, Windows có thể không cho bật một số tính năng trong Core Isolation.


## 22.3. Memory Integrity

**Memory Integrity** là một tính năng nằm trong Core Isolation. Tính năng này giúp ngăn mã độc chèn hoặc thay đổi mã trong các tiến trình bảo mật cao của Windows.

![](./img/22.3_memory_intefrity.png)

Memory Integrity còn có thể được hiểu là một cơ chế bảo vệ tính toàn vẹn của bộ nhớ. Nó giúp đảm bảo rằng các thành phần quan trọng trong bộ nhớ không bị can thiệp trái phép.

Memory Integrity có vai trò:

- ngăn mã độc can thiệp vào vùng nhớ quan trọng;
- giảm nguy cơ tấn công vào kernel;
- bảo vệ hệ thống khỏi driver độc hại;
- tăng mức độ an toàn cho Windows;
- hỗ trợ chống lại một số kỹ thuật khai thác nâng cao.

Nếu Memory Integrity bị tắt, hệ thống có thể mất đi một lớp bảo vệ quan trọng. Tuy nhiên, trong một số trường hợp, tính năng này có thể không bật được do driver không tương thích.

Khi cấu hình Memory Integrity, cần chú ý:

- nên bật nếu thiết bị hỗ trợ;
- kiểm tra driver không tương thích nếu bật không thành công;
- cập nhật driver từ nguồn chính thức;
- không cài driver không rõ nguồn gốc;
- không tắt tính năng này nếu không có lý do kỹ thuật rõ ràng.

Từ góc độ bảo mật, Memory Integrity rất quan trọng vì nhiều tấn công nâng cao cố gắng can thiệp vào bộ nhớ hoặc kernel để tránh bị phát hiện.


## 22.4. Security Processor

**Security Processor** là phần trong Device Security liên quan đến bộ xử lý bảo mật của thiết bị, thường là TPM.

Security Processor giúp Windows thực hiện các chức năng bảo mật phần cứng, đặc biệt là các chức năng liên quan đến lưu trữ khóa, mã hóa và xác minh tính toàn vẹn của hệ thống.

Trong mục Security Processor, người dùng có thể xem các thông tin như:

- thiết bị có TPM hay không;
- phiên bản TPM;
- trạng thái hoạt động của TPM;
- thông tin nhà sản xuất;
- trạng thái sẵn sàng của Security Processor;
- tùy chọn xử lý sự cố liên quan đến TPM.

Security Processor thường được sử dụng bởi các tính năng như:

- BitLocker;
- Windows Hello;
- Secure Boot;
- Credential Guard;
- các cơ chế bảo vệ khóa mã hóa.

Nếu Security Processor gặp lỗi, một số tính năng bảo mật của Windows có thể không hoạt động đúng. Ví dụ, BitLocker có thể yêu cầu khóa khôi phục hoặc Windows Hello có thể gặp vấn đề khi xác thực.


## 22.5. TPM là gì?

**TPM** là viết tắt của **Trusted Platform Module**. Đây là một thành phần bảo mật phần cứng dùng để lưu trữ và bảo vệ các khóa mã hóa, thông tin xác thực và dữ liệu nhạy cảm khác.

TPM có thể tồn tại dưới dạng:

- chip phần cứng riêng trên bo mạch chủ;
- firmware TPM được tích hợp trong CPU hoặc nền tảng phần cứng.

TPM không phải là nơi lưu trữ toàn bộ dữ liệu người dùng. Thay vào đó, nó chủ yếu được dùng để bảo vệ khóa và hỗ trợ các cơ chế xác thực an toàn.

Một số chức năng phổ biến của TPM gồm:

- lưu trữ khóa mã hóa;
- hỗ trợ BitLocker;
- hỗ trợ Secure Boot;
- bảo vệ thông tin xác thực;
- kiểm tra tính toàn vẹn của quá trình khởi động;
- hỗ trợ Windows Hello;
- giảm nguy cơ khóa mã hóa bị đánh cắp.

Ví dụ, khi dùng BitLocker để mã hóa ổ đĩa, TPM có thể lưu trữ khóa bảo vệ và chỉ giải phóng khóa khi hệ thống khởi động trong trạng thái tin cậy.

Trong các phiên bản Windows hiện đại, TPM là một thành phần rất quan trọng đối với bảo mật thiết bị.

# 23. BitLocker

## 23.1. BitLocker là gì?

**BitLocker** là tính năng mã hóa ổ đĩa được tích hợp trong Windows. Tính năng này giúp bảo vệ dữ liệu bằng cách mã hóa toàn bộ ổ đĩa hoặc phân vùng.

Khi BitLocker được bật, dữ liệu trên ổ đĩa sẽ được mã hóa. Nếu người khác tháo ổ đĩa ra khỏi máy tính hoặc cố gắng truy cập dữ liệu từ môi trường khác, họ sẽ không thể đọc được dữ liệu nếu không có khóa giải mã phù hợp.

BitLocker thường được sử dụng để bảo vệ:

- ổ đĩa hệ thống;
- ổ dữ liệu;
- máy tính xách tay;
- máy tính doanh nghiệp;
- thiết bị lưu trữ ngoài;
- USB hoặc ổ cứng di động.

BitLocker đặc biệt quan trọng trong trường hợp thiết bị bị mất hoặc bị đánh cắp. Ngay cả khi kẻ tấn công có được ổ đĩa vật lý, dữ liệu vẫn được bảo vệ bằng mã hóa.


## 23.2. BitLocker Drive Encryption

**BitLocker Drive Encryption** là chức năng mã hóa ổ đĩa của BitLocker. Nó cho phép mã hóa toàn bộ volume thay vì chỉ mã hóa từng tệp riêng lẻ.

BitLocker Drive Encryption có thể được áp dụng cho:

- ổ đĩa chứa hệ điều hành Windows;
- ổ dữ liệu bên trong máy;
- ổ cứng gắn ngoài;
- USB nếu dùng BitLocker To Go.

Khi mã hóa ổ hệ thống, BitLocker sẽ bảo vệ các tệp hệ điều hành, tệp người dùng, chương trình và dữ liệu khác nằm trên ổ đó.

Một hệ thống sử dụng BitLocker thường yêu cầu người dùng có một trong các yếu tố sau để mở khóa ổ đĩa:

- TPM;
- PIN;
- Startup Key;
- Recovery Key;
- mật khẩu đối với ổ dữ liệu hoặc thiết bị di động.

BitLocker Drive Encryption giúp đảm bảo rằng dữ liệu không thể bị đọc trực tiếp nếu ổ đĩa bị truy cập ngoài hệ điều hành Windows hợp lệ.


## 23.3. Vai trò của BitLocker trong bảo vệ dữ liệu

BitLocker có vai trò quan trọng trong bảo vệ dữ liệu, đặc biệt là dữ liệu trên máy tính xách tay và thiết bị doanh nghiệp.

Nếu máy tính không được mã hóa, kẻ tấn công có thể tháo ổ cứng ra và gắn vào máy khác để đọc dữ liệu. Trong trường hợp dùng BitLocker, dữ liệu trên ổ đĩa đã được mã hóa nên không thể đọc được nếu không có khóa giải mã.

BitLocker giúp bảo vệ dữ liệu trong các tình huống như:

- máy tính bị mất;
- máy tính bị đánh cắp;
- ổ cứng bị tháo ra khỏi máy;
- người không có quyền cố gắng truy cập dữ liệu;
- thiết bị lưu trữ ngoài bị thất lạc;
- dữ liệu doanh nghiệp nằm trên máy cá nhân hoặc laptop.

Trong môi trường doanh nghiệp, BitLocker thường được dùng để bảo vệ dữ liệu nhạy cảm như:

- tài liệu nội bộ;
- thông tin khách hàng;
- dữ liệu tài chính;
- thông tin xác thực;
- dữ liệu dự án;
- tài liệu pháp lý.

BitLocker không ngăn được mọi loại tấn công, nhưng nó là lớp bảo vệ rất quan trọng đối với dữ liệu khi thiết bị không còn nằm trong sự kiểm soát của người dùng.


## 23.4. BitLocker và TPM

BitLocker thường hoạt động kết hợp với **TPM** để tăng cường bảo mật.

**TPM** là viết tắt của **Trusted Platform Module**. Đây là thành phần bảo mật phần cứng dùng để lưu trữ khóa mã hóa và kiểm tra trạng thái tin cậy của hệ thống khi khởi động.

Khi BitLocker sử dụng TPM, khóa mã hóa ổ đĩa được bảo vệ bởi TPM. TPM chỉ giải phóng khóa nếu quá trình khởi động của hệ thống không có dấu hiệu bị thay đổi bất thường.

Ví dụ, nếu kẻ tấn công cố gắng thay đổi bootloader hoặc can thiệp vào quá trình khởi động, TPM có thể không giải phóng khóa mã hóa. Khi đó, hệ thống có thể yêu cầu Recovery Key.

Lợi ích khi BitLocker kết hợp với TPM:

- bảo vệ khóa mã hóa tốt hơn;
- giảm nguy cơ ổ đĩa bị giải mã trái phép;
- kiểm tra tính toàn vẹn của quá trình khởi động;
- hỗ trợ mở khóa tự động khi hệ thống ở trạng thái tin cậy;
- tăng mức độ bảo mật cho máy tính xách tay và endpoint doanh nghiệp.

Trong các máy tính hiện đại, BitLocker thường được khuyến nghị sử dụng cùng TPM để đạt mức bảo vệ tốt hơn.


## 23.5. BitLocker trên hệ thống không có TPM

BitLocker vẫn có thể được sử dụng trên hệ thống không có TPM, nhưng cần cấu hình bổ sung.

Khi không có TPM, Windows không thể dùng phần cứng để bảo vệ khóa mã hóa theo cách thông thường. Vì vậy, hệ thống cần một phương thức khác để mở khóa ổ đĩa khi khởi động.

Một cách phổ biến là sử dụng **Startup Key** được lưu trên USB.

Trong trường hợp này, khi máy tính khởi động, người dùng cần cắm USB chứa Startup Key để BitLocker có thể mở khóa ổ đĩa hệ thống.

BitLocker không có TPM vẫn có thể bảo vệ dữ liệu, nhưng thường kém tiện lợi hơn và phụ thuộc nhiều hơn vào việc người dùng bảo quản khóa bên ngoài.

Một số lưu ý khi dùng BitLocker không có TPM:

- cần cấu hình chính sách cho phép BitLocker chạy không cần TPM;
- cần bảo quản Startup Key cẩn thận;
- không nên để USB chứa Startup Key cùng với máy tính;
- cần lưu Recovery Key ở nơi an toàn;
- nếu mất khóa, có thể không truy cập được dữ liệu.

Trong môi trường doanh nghiệp, nên ưu tiên thiết bị có TPM để triển khai BitLocker hiệu quả và an toàn hơn.


## 23.6. Startup Key

**Startup Key** là khóa khởi động được dùng để mở khóa ổ đĩa BitLocker trong quá trình khởi động hệ thống.

Startup Key thường được lưu trên USB. Khi máy tính bật lên, người dùng cần cắm USB chứa Startup Key để Windows có thể giải mã ổ đĩa và tiếp tục khởi động.

Startup Key thường được dùng trong trường hợp:

- máy tính không có TPM;
- tổ chức muốn thêm một lớp xác thực khi khởi động;
- cần bảo vệ ổ hệ thống bằng khóa ngoài;
- yêu cầu chính sách bảo mật cao hơn.

Startup Key có vai trò giống như một yếu tố vật lý. Nếu không có USB chứa khóa, ổ đĩa sẽ không được mở khóa.

Tuy nhiên, cần bảo quản Startup Key rất cẩn thận. Nếu để USB chứa khóa cùng với máy tính, khi máy bị đánh cắp, kẻ tấn công cũng có thể có luôn khóa để mở ổ đĩa.

Khuyến nghị bảo mật:

- không cắm Startup Key thường xuyên khi không cần;
- không để Startup Key trong cùng túi với laptop;
- tạo bản sao dự phòng nếu chính sách cho phép;
- lưu Recovery Key riêng biệt;
- kiểm soát ai được giữ Startup Key.


## 23.7. Recovery Key

**Recovery Key** là khóa khôi phục BitLocker. Đây là chuỗi khóa dùng để mở khóa ổ đĩa trong trường hợp BitLocker không thể mở khóa theo cách thông thường.

Recovery Key rất quan trọng vì nếu mất Recovery Key, người dùng có thể không thể truy cập dữ liệu đã mã hóa.

BitLocker có thể yêu cầu Recovery Key trong các trường hợp như:

- TPM phát hiện thay đổi bất thường trong quá trình khởi động;
- BIOS/UEFI bị thay đổi;
- bootloader bị thay đổi;
- phần cứng quan trọng bị thay đổi;
- người dùng quên PIN;
- mất Startup Key;
- ổ đĩa được gắn sang máy khác;
- cấu hình BitLocker bị lỗi.

Recovery Key có thể được lưu ở nhiều nơi tùy cấu hình, ví dụ:

- tài khoản Microsoft;
- file văn bản;
- bản in giấy;
- USB;
- Active Directory;
- Azure AD hoặc Microsoft Entra ID;
- hệ thống quản lý endpoint của doanh nghiệp.

Trong môi trường doanh nghiệp, Recovery Key nên được lưu tập trung và quản lý bởi bộ phận IT. Không nên để người dùng lưu Recovery Key ở nơi dễ mất hoặc dễ bị truy cập trái phép.


## 23.8. BitLocker To Go

**BitLocker To Go** là tính năng dùng để mã hóa thiết bị lưu trữ di động như USB hoặc ổ cứng ngoài.

Khác với BitLocker Drive Encryption thường dùng cho ổ đĩa bên trong máy, BitLocker To Go tập trung bảo vệ dữ liệu trên thiết bị có thể tháo rời.

BitLocker To Go hữu ích trong các tình huống:

- USB chứa tài liệu quan trọng;
- ổ cứng ngoài lưu dữ liệu sao lưu;
- thiết bị di động dùng để chuyển dữ liệu giữa các máy;
- nhân viên mang dữ liệu ra ngoài văn phòng;
- cần bảo vệ dữ liệu khi thiết bị bị mất.

Khi bật BitLocker To Go, người dùng thường cần đặt mật khẩu để mở khóa thiết bị. Nếu nhập đúng mật khẩu, Windows sẽ cho phép truy cập dữ liệu. Nếu không có mật khẩu hoặc Recovery Key, dữ liệu trên thiết bị sẽ không thể đọc được.

Trong doanh nghiệp, BitLocker To Go giúp giảm nguy cơ rò rỉ dữ liệu qua USB hoặc ổ đĩa di động bị thất lạc.


## 23.9. Sự khác nhau giữa BitLocker và EFS

BitLocker và EFS đều là cơ chế mã hóa dữ liệu trong Windows, nhưng chúng hoạt động ở cấp độ khác nhau.

| Tiêu chí | BitLocker | EFS |
|---|---|---|
| Tên đầy đủ | BitLocker Drive Encryption | Encrypting File System |
| Cấp độ mã hóa | Mã hóa toàn bộ ổ đĩa hoặc volume | Mã hóa từng tệp hoặc thư mục |
| Mục đích chính | Bảo vệ dữ liệu khi thiết bị hoặc ổ đĩa bị mất | Bảo vệ tệp khỏi người dùng khác trên cùng hệ thống |
| Phạm vi bảo vệ | Toàn bộ ổ đĩa | Tệp/thư mục được chọn |
| Phụ thuộc TPM | Có thể dùng TPM để tăng bảo mật | Không dùng TPM theo cách BitLocker |
| Phù hợp cho | Laptop, ổ hệ thống, ổ dữ liệu, USB | Tệp hoặc thư mục nhạy cảm riêng lẻ |
| Quản lý doanh nghiệp | Thường quản lý tập trung qua chính sách | Có thể quản lý qua chứng chỉ và chính sách |

Ví dụ:

- Nếu muốn bảo vệ toàn bộ laptop khi bị mất, nên dùng BitLocker.
- Nếu chỉ muốn mã hóa một thư mục tài liệu riêng, có thể dùng EFS.

Trong thực tế, BitLocker thường được ưu tiên trong doanh nghiệp vì nó bảo vệ toàn bộ ổ đĩa và giảm nguy cơ dữ liệu bị đọc khi thiết bị bị đánh cắp.

EFS vẫn có ích trong một số trường hợp, nhưng nếu người dùng mất chứng chỉ mã hóa hoặc cấu hình sai, có thể gặp khó khăn khi khôi phục dữ liệu.


## 23.10. Ý nghĩa bảo mật của mã hóa ổ đĩa

Mã hóa ổ đĩa là một biện pháp bảo mật quan trọng để bảo vệ dữ liệu khi thiết bị rơi vào tay người không có quyền.

Nếu không có mã hóa ổ đĩa, kẻ tấn công có thể:

- tháo ổ cứng và đọc dữ liệu trên máy khác;
- dùng hệ điều hành ngoài để truy cập tệp;
- sao chép dữ liệu nhạy cảm;
- khai thác dữ liệu từ máy bị mất;
- truy cập tài liệu doanh nghiệp mà không cần đăng nhập Windows.

Khi ổ đĩa được mã hóa bằng BitLocker, dữ liệu sẽ không thể đọc được nếu không có khóa giải mã phù hợp.

Mã hóa ổ đĩa đặc biệt quan trọng đối với:

- laptop doanh nghiệp;
- thiết bị chứa dữ liệu khách hàng;
- máy tính của nhân viên làm việc từ xa;
- ổ đĩa sao lưu;
- USB chứa dữ liệu nhạy cảm;
- hệ thống có yêu cầu tuân thủ bảo mật.

Tuy nhiên, mã hóa ổ đĩa không thay thế các biện pháp bảo mật khác. Nếu người dùng đã đăng nhập vào Windows và mã độc chạy trong phiên làm việc đó, dữ liệu đã mở khóa vẫn có thể bị truy cập. Vì vậy, BitLocker cần được kết hợp với các biện pháp khác như:

- mật khẩu mạnh;
- MFA nếu có;
- antivirus;
- cập nhật hệ thống;
- kiểm soát quyền truy cập;
- sao lưu dữ liệu;
- giám sát bảo mật.

Tóm lại, BitLocker là công cụ quan trọng giúp bảo vệ dữ liệu ở cấp ổ đĩa. Đối với Windows trong môi trường doanh nghiệp, mã hóa ổ đĩa là một lớp phòng thủ cần thiết để giảm rủi ro rò rỉ dữ liệu khi thiết bị bị mất hoặc bị đánh cắp.


# 24. Volume Shadow Copy Service — VSS

## 24.1. VSS là gì?

**VSS** là viết tắt của **Volume Shadow Copy Service**. Đây là một dịch vụ trong Windows dùng để tạo các bản sao tại một thời điểm cụ thể của dữ liệu trên ổ đĩa.

![](./img/24.1_vss.png)

Các bản sao này thường được gọi là:

- Shadow Copy;
- Volume Shadow Copy;
- Snapshot;
- bản sao bóng của ổ đĩa.

VSS cho phép Windows hoặc phần mềm sao lưu tạo bản sao dữ liệu ngay cả khi một số tệp đang được sử dụng. Điều này rất quan trọng vì trong thực tế, nhiều tệp hệ thống, cơ sở dữ liệu hoặc tài liệu có thể đang mở trong lúc quá trình sao lưu diễn ra.

Mục đích chính của VSS là hỗ trợ:

- sao lưu dữ liệu;
- tạo điểm khôi phục hệ thống;
- khôi phục phiên bản cũ của tệp;
- hỗ trợ phần mềm backup;
- phục hồi hệ thống sau lỗi cấu hình hoặc lỗi phần mềm.

Nói đơn giản, VSS giúp Windows tạo một “ảnh chụp” trạng thái dữ liệu tại một thời điểm nhất định để có thể dùng cho khôi phục hoặc sao lưu.


## 24.2. Shadow Copy là gì?

**Shadow Copy** là bản sao bóng của dữ liệu được tạo bởi Volume Shadow Copy Service.

Shadow Copy không nhất thiết là một bản sao đầy đủ theo cách người dùng sao chép thủ công toàn bộ thư mục. Thay vào đó, nó lưu trạng thái của dữ liệu tại một thời điểm cụ thể để hỗ trợ khôi phục khi cần.

Shadow Copy có thể được dùng để:

- khôi phục tệp về phiên bản trước đó;
- hỗ trợ System Restore;
- hỗ trợ phần mềm backup;
- giảm rủi ro mất dữ liệu khi có lỗi hệ thống;
- phục hồi một số thay đổi không mong muốn.

Ví dụ, nếu một tệp bị sửa nhầm hoặc bị xóa, trong một số trường hợp người dùng có thể khôi phục phiên bản trước của tệp nếu Shadow Copy còn tồn tại.

Tuy nhiên, Shadow Copy không nên được xem là phương án backup duy nhất. Nếu ổ đĩa bị hỏng, máy bị ransomware hoặc Shadow Copies bị xóa, người dùng vẫn có thể mất dữ liệu.


## 24.3. System Restore Point

**System Restore Point** là điểm khôi phục hệ thống. Nó lưu lại trạng thái quan trọng của Windows tại một thời điểm nhất định.

Restore Point thường bao gồm các thông tin như:

- một số tệp hệ thống;
- Registry;
- driver;
- cấu hình hệ thống;
- một số thiết lập quan trọng của Windows.

System Restore Point thường được tạo trước hoặc sau các thay đổi lớn, ví dụ:

- cài đặt driver mới;
- cài đặt phần mềm quan trọng;
- cập nhật hệ thống;
- thay đổi cấu hình Windows;
- thao tác thử nghiệm có thể ảnh hưởng đến hệ thống.

Khi hệ thống gặp lỗi sau một thay đổi, người dùng có thể sử dụng Restore Point để đưa Windows về trạng thái trước đó.

Cần lưu ý rằng System Restore không phải là công cụ sao lưu dữ liệu cá nhân đầy đủ. Nó chủ yếu phục vụ việc khôi phục cấu hình hệ thống, không thay thế backup tài liệu cá nhân.


## 24.4. System Volume Information

**System Volume Information** là thư mục hệ thống đặc biệt trên mỗi ổ đĩa Windows.

Thư mục này có thể chứa các dữ liệu liên quan đến:

- Volume Shadow Copies;
- System Restore Points;
- thông tin chỉ mục hệ thống;
- dữ liệu phục vụ khôi phục và bảo vệ hệ thống.

Thông thường, người dùng không thể truy cập trực tiếp thư mục này bằng quyền thông thường. Windows bảo vệ thư mục này vì nó chứa dữ liệu hệ thống nhạy cảm.

Đường dẫn thường gặp có dạng:

```text
C:\System Volume Information
```

Trên mỗi ổ đĩa có bật System Protection, Windows có thể tạo và lưu dữ liệu khôi phục trong thư mục System Volume Information.

Không nên tự ý xóa hoặc chỉnh sửa thư mục này. Nếu cần xóa Restore Points hoặc quản lý dung lượng, nên thực hiện thông qua giao diện System Protection của Windows.

## 24.5. Tạo điểm khôi phục

Người dùng có thể tạo **Restore Point** thủ công trước khi thực hiện các thay đổi quan trọng trên hệ thống.

Nên tạo điểm khôi phục trước khi:

* cài driver mới;
* cài phần mềm lạ;
* thay đổi Registry;
* chỉnh cấu hình hệ thống quan trọng;
* thử nghiệm trong môi trường lab;
* cập nhật phần mềm có rủi ro gây lỗi.

Các bước tạo Restore Point:

1. Mở **Start Menu**.
2. Tìm kiếm:

```text
Create a restore point
```

3. Mở cửa sổ **System Properties**.
4. Chọn tab **System Protection**.
5. Chọn ổ đĩa hệ thống, thường là ổ `C:`.
6. Nhấn **Create**.
7. Đặt tên cho điểm khôi phục.
8. Nhấn **Create** để bắt đầu.

Ví dụ tên Restore Point có thể là:

```text
Before installing new driver
```

Đặt tên rõ ràng giúp người dùng dễ nhận biết lý do tạo điểm khôi phục khi cần phục hồi hệ thống sau này.

## 24.6. Khôi phục hệ thống

**System Restore** cho phép đưa hệ thống về trạng thái đã được lưu trong Restore Point trước đó.

Tính năng này hữu ích khi Windows gặp lỗi sau khi:

* cài đặt driver;
* cài phần mềm;
* cập nhật hệ thống;
* thay đổi Registry;
* chỉnh sai cấu hình;
* hệ thống hoạt động không ổn định.

Các bước khôi phục hệ thống:

1. Mở **Start Menu**.
2. Tìm kiếm:

```text
Create a restore point
```

3. Mở tab **System Protection**.
4. Chọn **System Restore**.
5. Chọn Restore Point phù hợp.
6. Xác nhận quá trình khôi phục.
7. Khởi động lại máy nếu Windows yêu cầu.

Sau khi khôi phục, Windows sẽ quay lại trạng thái hệ thống tại thời điểm Restore Point được tạo.

Cần lưu ý:

* System Restore có thể gỡ bỏ một số phần mềm hoặc driver được cài sau thời điểm tạo Restore Point;
* System Restore không phải là công cụ khôi phục toàn bộ dữ liệu cá nhân;
* nên sao lưu dữ liệu quan trọng trước khi thực hiện khôi phục;
* không nên tắt máy đột ngột trong quá trình System Restore.

## 24.7. Cấu hình System Protection

**System Protection** là tính năng quản lý Restore Points và Shadow Copies cho từng ổ đĩa.

Trong System Protection, người dùng có thể:

* bật hoặc tắt bảo vệ hệ thống cho ổ đĩa;
* tạo Restore Point;
* thực hiện System Restore;
* cấu hình dung lượng dùng cho Restore Points;
* xóa các Restore Points cũ.

Các bước mở System Protection:

1. Mở **Start Menu**.
2. Tìm kiếm:

```text
Create a restore point
```

3. Chọn tab **System Protection**.

Nếu System Protection chưa được bật, người dùng có thể chọn ổ đĩa và nhấn **Configure** để bật.

Một số tùy chọn thường gặp:

| Tùy chọn                  | Ý nghĩa                                     |
| ------------------------- | ------------------------------------------- |
| Turn on system protection | Bật bảo vệ hệ thống                         |
| Disable system protection | Tắt bảo vệ hệ thống                         |
| Max Usage                 | Giới hạn dung lượng dùng cho restore points |
| Delete                    | Xóa các restore points hiện có              |

Nếu dung lượng dành cho System Protection quá thấp, Windows có thể chỉ lưu được ít Restore Points. Nếu dung lượng quá cao, nó có thể chiếm nhiều không gian ổ đĩa.

## 24.8. VSS trong sao lưu dữ liệu

VSS có vai trò quan trọng trong quá trình sao lưu dữ liệu trên Windows.

Khi phần mềm backup cần sao lưu dữ liệu, VSS có thể tạo snapshot để đảm bảo dữ liệu được sao lưu ở trạng thái nhất quán. Điều này đặc biệt quan trọng với các tệp đang được mở hoặc đang được hệ thống sử dụng.

VSS thường được sử dụng bởi:

* Windows Backup;
* phần mềm backup của bên thứ ba;
* phần mềm sao lưu máy chủ;
* phần mềm sao lưu cơ sở dữ liệu;
* hệ thống backup trong doanh nghiệp.

Lợi ích của VSS trong backup:

* sao lưu được tệp đang sử dụng;
* tạo bản sao dữ liệu nhất quán;
* giảm rủi ro backup bị lỗi;
* hỗ trợ khôi phục phiên bản trước;
* giúp quá trình sao lưu ít ảnh hưởng đến người dùng hơn.

Ví dụ, nếu một file đang mở trong lúc backup, VSS có thể giúp phần mềm backup lấy bản snapshot ổn định thay vì cố sao chép trực tiếp file đang thay đổi.

Tuy nhiên, VSS chỉ là một thành phần hỗ trợ backup. Nó không thay thế hoàn toàn chiến lược backup đầy đủ.

## 24.9. VSS và rủi ro ransomware

VSS có ý nghĩa bảo mật quan trọng, đặc biệt trong bối cảnh ransomware.

Ransomware là loại malware mã hóa dữ liệu của nạn nhân và yêu cầu tiền chuộc. Vì Shadow Copies có thể được dùng để khôi phục dữ liệu, nhiều ransomware cố gắng xóa Shadow Copies trước hoặc sau khi mã hóa tệp.

Nếu ransomware xóa được Shadow Copies, người dùng sẽ khó khôi phục dữ liệu bằng các công cụ có sẵn của Windows.

Một số hành vi đáng nghi liên quan đến ransomware gồm:

* xóa Shadow Copies;
* tắt System Protection;
* thay đổi cấu hình VSS;
* chạy lệnh xóa restore points;
* xóa dữ liệu trong System Volume Information;
* vô hiệu hóa dịch vụ backup;
* mã hóa nhiều tệp trong thời gian ngắn.

Trong điều tra bảo mật, việc kiểm tra VSS có thể giúp xác định:

* Shadow Copies có còn tồn tại không;
* Restore Points có bị xóa bất thường không;
* thời điểm Shadow Copies bị xóa;
* tiến trình nào đã thực hiện thao tác đáng nghi;
* có dấu hiệu ransomware hay không.

Một số lệnh thường được ransomware lạm dụng trong thực tế có thể liên quan đến việc xóa shadow copies. Vì vậy, SOC cần chú ý các sự kiện hoặc cảnh báo liên quan đến thao tác này.

VSS có thể hỗ trợ khôi phục, nhưng không nên phụ thuộc hoàn toàn vào VSS để chống ransomware.

## 24.10. Ý nghĩa của backup ngoại tuyến

**Backup ngoại tuyến** là bản sao lưu được lưu tách biệt khỏi hệ thống chính và không luôn kết nối trực tiếp với máy tính hoặc mạng nội bộ.

Backup ngoại tuyến rất quan trọng vì ransomware có thể mã hóa hoặc xóa cả dữ liệu gốc lẫn các bản sao lưu đang kết nối với hệ thống.

Ví dụ backup ngoại tuyến gồm:

* ổ cứng ngoài chỉ cắm khi sao lưu;
* bản sao lưu lưu ở vị trí vật lý khác;
* backup trên hệ thống không truy cập trực tiếp từ máy người dùng;
* bản sao lưu immutable;
* bản sao lưu được cô lập khỏi mạng chính.

Backup ngoại tuyến giúp bảo vệ dữ liệu trong các tình huống:

* ransomware xóa Shadow Copies;
* máy tính bị mã hóa toàn bộ;
* tài khoản bị chiếm quyền;
* ổ đĩa chính bị hỏng;
* hệ thống backup online bị tấn công;
* dữ liệu bị xóa nhầm hoặc phá hoại.

Một nguyên tắc backup thường được nhắc đến là quy tắc **3-2-1**:

| Thành phần                     | Ý nghĩa                                                  |
| ------------------------------ | -------------------------------------------------------- |
| 3 bản sao dữ liệu              | Có ít nhất 3 bản dữ liệu                                 |
| 2 loại phương tiện lưu trữ     | Lưu trên ít nhất 2 loại thiết bị hoặc nền tảng khác nhau |
| 1 bản sao ngoài hệ thống chính | Có ít nhất 1 bản sao ngoại tuyến hoặc ngoài vị trí chính |

Từ góc độ bảo mật, backup ngoại tuyến là lớp phòng thủ cuối cùng khi các biện pháp bảo vệ khác thất bại.

Tóm lại, VSS và Shadow Copies rất hữu ích trong khôi phục hệ thống và hỗ trợ backup. Tuy nhiên, trong bối cảnh ransomware, người dùng và doanh nghiệp không nên chỉ dựa vào VSS. Cần có chiến lược backup ngoại tuyến, kiểm tra khả năng khôi phục định kỳ và bảo vệ hệ thống backup khỏi truy cập trái phép.


# 25. Tổng quan về Windows Domains

## 25.1. Windows Domain là gì?

**Windows Domain** là một mô hình mạng trong đó người dùng, máy tính và tài nguyên được quản lý tập trung dưới sự kiểm soát của một tổ chức hoặc doanh nghiệp.

Nói đơn giản, Windows Domain là một nhóm các máy tính và tài khoản người dùng được quản lý chung. Thay vì mỗi máy tính có danh sách tài khoản và cấu hình riêng, doanh nghiệp có thể quản lý tất cả thông qua một hệ thống trung tâm.

Trong Windows Domain, các thành phần thường gặp gồm:

- người dùng;
- máy tính;
- nhóm người dùng;
- máy chủ;
- máy in;
- thư mục chia sẻ;
- chính sách bảo mật;
- tài nguyên mạng.

Windows Domain giúp doanh nghiệp quản lý hệ thống Windows dễ dàng hơn, đặc biệt khi số lượng máy tính và người dùng tăng lên.

Ví dụ, trong một công ty có 300 nhân viên và 150 máy tính, nếu không có domain, quản trị viên phải tạo tài khoản và cấu hình từng máy riêng lẻ. Điều này rất mất thời gian và khó kiểm soát. Khi sử dụng Windows Domain, các tài khoản và chính sách có thể được quản lý tập trung.


## 25.2. Vì sao doanh nghiệp cần Windows Domain?

Doanh nghiệp cần Windows Domain vì việc quản lý từng máy tính riêng lẻ không còn hiệu quả khi hệ thống phát triển lớn.

Nếu doanh nghiệp chỉ có vài máy tính, quản trị viên có thể cấu hình thủ công từng máy. Tuy nhiên, khi có hàng trăm máy tính và người dùng ở nhiều phòng ban hoặc nhiều văn phòng khác nhau, cách quản lý thủ công sẽ gây nhiều vấn đề.

Windows Domain giúp doanh nghiệp:

- quản lý người dùng tập trung;
- quản lý máy tính tập trung;
- áp dụng chính sách bảo mật đồng nhất;
- kiểm soát quyền truy cập tài nguyên;
- đơn giản hóa quá trình đăng nhập;
- giảm lỗi cấu hình thủ công;
- dễ dàng thu hồi quyền khi nhân viên nghỉ việc;
- hỗ trợ giám sát và điều tra bảo mật.

Ví dụ, khi một nhân viên mới vào công ty, quản trị viên chỉ cần tạo tài khoản trong domain. Nhân viên đó có thể đăng nhập vào các máy tính được phép sử dụng và truy cập tài nguyên theo quyền được cấp.

Ngược lại, khi nhân viên nghỉ việc, quản trị viên chỉ cần vô hiệu hóa tài khoản domain. Khi đó, người này sẽ không thể đăng nhập vào hệ thống hoặc truy cập tài nguyên doanh nghiệp nữa.


## 25.3. Quản lý tập trung người dùng và máy tính

Một lợi ích quan trọng của Windows Domain là khả năng quản lý tập trung người dùng và máy tính.

Trong môi trường không có domain, tài khoản người dùng thường được tạo cục bộ trên từng máy. Điều này gây khó khăn khi cần thay đổi mật khẩu, cấp quyền hoặc thu hồi quyền truy cập.

Trong môi trường domain, thông tin người dùng được lưu trữ tập trung trong Active Directory. Người dùng có thể dùng một tài khoản domain để đăng nhập vào nhiều máy tính khác nhau trong mạng doanh nghiệp.

Quản lý tập trung giúp quản trị viên thực hiện các công việc như:

- tạo tài khoản người dùng mới;
- đặt lại mật khẩu;
- vô hiệu hóa tài khoản;
- phân quyền theo nhóm;
- quản lý máy tính tham gia domain;
- kiểm tra tài khoản nào thuộc nhóm nào;
- quản lý tài nguyên theo phòng ban hoặc vai trò.

Ví dụ, thay vì tạo tài khoản `nguyen.van.a` trên từng máy, quản trị viên chỉ cần tạo một tài khoản domain. Sau đó, tài khoản này có thể được sử dụng trong toàn bộ hệ thống domain theo quyền được cấp.

Điều này giúp tiết kiệm thời gian, giảm sai sót và tăng khả năng kiểm soát hệ thống.


## 25.4. Quản lý chính sách bảo mật tập trung

Windows Domain cho phép doanh nghiệp quản lý chính sách bảo mật tập trung thông qua Active Directory và Group Policy.

Thay vì cấu hình từng máy riêng lẻ, quản trị viên có thể tạo chính sách và áp dụng cho nhiều người dùng hoặc máy tính cùng lúc.

Một số chính sách bảo mật thường được quản lý tập trung gồm:

- độ dài tối thiểu của mật khẩu;
- thời gian hết hạn mật khẩu;
- khóa tài khoản sau nhiều lần đăng nhập sai;
- hạn chế truy cập Control Panel;
- cấu hình Windows Firewall;
- cấu hình Windows Update;
- chặn thiết bị USB;
- cấu hình màn hình khóa;
- triển khai script đăng nhập;
- giới hạn quyền của người dùng.

Ví dụ, doanh nghiệp có thể đặt chính sách yêu cầu mật khẩu tối thiểu 10 ký tự cho toàn bộ người dùng trong domain. Khi chính sách được áp dụng, tất cả tài khoản thuộc phạm vi đó phải tuân thủ quy định này.

Từ góc độ bảo mật, quản lý chính sách tập trung giúp đảm bảo hệ thống có cấu hình đồng nhất và giảm rủi ro do người dùng hoặc quản trị viên cấu hình sai trên từng máy riêng lẻ.


## 25.5. Active Directory trong Windows Domain

**Active Directory** là thành phần trung tâm của Windows Domain. Đây là nơi lưu trữ và quản lý thông tin về các đối tượng trong mạng doanh nghiệp.

Các đối tượng trong Active Directory có thể bao gồm:

- người dùng;
- máy tính;
- nhóm;
- máy in;
- thư mục chia sẻ;
- tài khoản dịch vụ;
- đơn vị tổ chức;
- chính sách.

Active Directory giúp domain hoạt động như một hệ thống quản lý tập trung. Khi người dùng đăng nhập bằng tài khoản domain, hệ thống sẽ kiểm tra thông tin xác thực trong Active Directory.

Active Directory cũng cho phép quản trị viên tổ chức tài nguyên theo cấu trúc rõ ràng. Ví dụ, có thể chia người dùng và máy tính theo phòng ban như:

- IT;
- HR;
- Accounting;
- Sales;
- Security;
- Students;
- Servers;
- Workstations.

Trong môi trường doanh nghiệp, Active Directory không chỉ là nơi lưu tài khoản. Nó còn là nền tảng cho xác thực, phân quyền, chính sách bảo mật và quản lý tài nguyên.


## 25.6. Domain Controller là gì?

**Domain Controller**, viết tắt là **DC**, là máy chủ chịu trách nhiệm vận hành dịch vụ Active Directory trong Windows Domain.

Domain Controller lưu trữ cơ sở dữ liệu Active Directory và xử lý các yêu cầu xác thực của người dùng, máy tính trong domain.

Khi người dùng đăng nhập bằng tài khoản domain, máy tính sẽ gửi yêu cầu xác thực đến Domain Controller. Domain Controller kiểm tra thông tin đăng nhập và quyết định người dùng có được phép đăng nhập hay không.

Domain Controller thường đảm nhiệm các nhiệm vụ như:

- xác thực người dùng;
- xác thực máy tính;
- lưu trữ dữ liệu Active Directory;
- xử lý đăng nhập domain;
- áp dụng Group Policy;
- quản lý quyền truy cập;
- đồng bộ thông tin trong domain.

Trong doanh nghiệp, Domain Controller là thành phần rất quan trọng. Nếu Domain Controller gặp lỗi, người dùng có thể gặp khó khăn khi đăng nhập hoặc truy cập tài nguyên domain.

Vì vậy, doanh nghiệp thường triển khai nhiều Domain Controller để tăng tính sẵn sàng và giảm rủi ro gián đoạn hệ thống.


## 25.7. Ví dụ thực tế về Windows Domain

Một ví dụ dễ hiểu về Windows Domain là hệ thống máy tính trong trường học, đại học hoặc công ty.

Ví dụ, trong một trường đại học, sinh viên được cấp một tài khoản như:

```text
student01
```

Sinh viên có thể dùng tài khoản này để đăng nhập vào nhiều máy tính khác nhau trong phòng lab. Thông tin tài khoản không cần được tạo riêng trên từng máy, vì quá trình xác thực được thực hiện thông qua Active Directory.

Khi sinh viên nhập username và password, máy tính sẽ gửi thông tin này đến Domain Controller để kiểm tra. Nếu thông tin hợp lệ, sinh viên được đăng nhập vào máy.

Ngoài đăng nhập, domain còn có thể áp dụng các chính sách như:

* không cho sinh viên truy cập Control Panel;
* không cho cài phần mềm;
* giới hạn quyền Administrator;
* tự động kết nối máy in;
* ánh xạ thư mục mạng;
* áp dụng cấu hình bảo mật chung.

Trong công ty, Windows Domain cũng hoạt động tương tự. Nhân viên có thể dùng tài khoản domain để đăng nhập vào máy tính công ty và truy cập tài nguyên như file server, printer, email hoặc ứng dụng nội bộ.

## 25.8. Đăng nhập miền bằng tài khoản domain

Khi máy tính đã tham gia Windows Domain, người dùng có thể đăng nhập bằng tài khoản domain thay vì tài khoản cục bộ.

Tài khoản domain thường có dạng:

```text
DOMAIN\username
```

Ví dụ:

```text
COMPANY\nguyen.van.a
```

Hoặc có thể dùng dạng giống địa chỉ email:

```text
username@domain.local
```

Ví dụ:

```text
nguyen.van.a@company.local
```

Khi người dùng đăng nhập bằng tài khoản domain, quá trình cơ bản diễn ra như sau:

1. Người dùng nhập username và password.
2. Máy tính gửi yêu cầu xác thực đến Domain Controller.
3. Domain Controller kiểm tra thông tin trong Active Directory.
4. Nếu thông tin đúng, người dùng được đăng nhập.
5. Chính sách bảo mật và quyền truy cập được áp dụng theo tài khoản đó.

Đăng nhập bằng tài khoản domain có nhiều lợi ích:

* dùng một tài khoản cho nhiều máy trong doanh nghiệp;
* dễ quản lý mật khẩu;
* dễ thu hồi quyền;
* áp dụng chính sách bảo mật tập trung;
* kiểm soát quyền truy cập tài nguyên;
* hỗ trợ ghi log và điều tra bảo mật.

# 26. Active Directory cơ bản

## 26.1. Active Directory là gì?

**Active Directory**, thường viết tắt là **AD**, là dịch vụ thư mục của Microsoft dùng trong môi trường Windows Domain.

Active Directory cho phép doanh nghiệp quản lý tập trung các đối tượng trong hệ thống mạng như:

- người dùng;
- máy tính;
- nhóm;
- máy in;
- thư mục chia sẻ;
- tài khoản dịch vụ;
- chính sách bảo mật;
- tài nguyên mạng.

Nói đơn giản, Active Directory là nơi lưu trữ thông tin về các thành phần trong mạng doanh nghiệp. Khi người dùng đăng nhập, truy cập thư mục chia sẻ hoặc sử dụng tài nguyên mạng, Active Directory có thể tham gia vào quá trình xác thực và phân quyền.

Trong môi trường doanh nghiệp, Active Directory là thành phần rất quan trọng vì nó giúp quản trị viên kiểm soát danh tính, thiết bị và quyền truy cập theo cách tập trung.


## 26.2. Active Directory Domain Services — AD DS

**Active Directory Domain Services**, viết tắt là **AD DS**, là dịch vụ cốt lõi của Active Directory trong Windows Domain.

AD DS hoạt động như một danh mục trung tâm chứa thông tin về các đối tượng trong miền. Các đối tượng này có thể là người dùng, máy tính, nhóm, máy in, thư mục chia sẻ và nhiều tài nguyên khác.

AD DS cung cấp các chức năng quan trọng như:

- lưu trữ thông tin người dùng và máy tính;
- xác thực đăng nhập domain;
- phân quyền truy cập tài nguyên;
- quản lý nhóm bảo mật;
- áp dụng Group Policy;
- tổ chức tài nguyên theo OU;
- hỗ trợ quản trị tập trung trong doanh nghiệp.

Khi một máy tính hoặc người dùng tham gia domain, thông tin của họ sẽ được quản lý trong AD DS. Vì vậy, AD DS có thể được xem là nền tảng chính của Windows Domain.

Trong thực tế, máy chủ chạy AD DS thường được gọi là **Domain Controller**.


## 26.3. Đối tượng trong Active Directory

Trong Active Directory, mọi thành phần được quản lý thường được biểu diễn dưới dạng **object** — tức là đối tượng.

Một số đối tượng phổ biến trong AD gồm:

| Đối tượng | Ý nghĩa |
|---|---|
| User | Đại diện cho người dùng hoặc tài khoản dịch vụ |
| Computer | Đại diện cho máy tính tham gia domain |
| Group | Dùng để gom người dùng hoặc máy tính nhằm cấp quyền |
| Printer | Đại diện cho máy in trong mạng |
| Shared Folder | Đại diện cho tài nguyên chia sẻ |
| Organizational Unit | Container dùng để tổ chức người dùng, máy tính và áp dụng chính sách |
| Service Account | Tài khoản dùng để chạy dịch vụ hoặc ứng dụng |

Mỗi đối tượng có các thuộc tính riêng. Ví dụ, một user object có thể có tên đăng nhập, họ tên, email, phòng ban và nhóm thành viên. Một computer object có thể có tên máy, hệ điều hành và vị trí trong domain.

Việc quản lý các đối tượng này giúp doanh nghiệp kiểm soát hệ thống rõ ràng hơn.


## 26.4. Security Principals

**Security Principals** là các đối tượng có thể được xác thực và có thể được cấp quyền truy cập tài nguyên trong mạng.

Nói cách khác, security principal là đối tượng có thể “hành động” trên tài nguyên. Ví dụ, một người dùng có thể đăng nhập và truy cập thư mục chia sẻ. Một máy tính cũng có thể xác thực với domain để nhận chính sách và giao tiếp với các dịch vụ khác.

Các security principals phổ biến trong Active Directory gồm:

- Users;
- Computers;
- Security Groups;
- Service Accounts.

Security principals rất quan trọng vì chúng liên quan trực tiếp đến xác thực và phân quyền.

Ví dụ:

- user `alice` có quyền đọc thư mục `Finance`;
- nhóm `IT Support` có quyền reset mật khẩu người dùng;
- máy tính `PC01$` có thể xác thực với domain;
- service account `svc_sql` được dùng để chạy dịch vụ cơ sở dữ liệu.

Từ góc độ bảo mật, quản lý security principals đúng cách là nền tảng của kiểm soát truy cập trong Active Directory.


## 26.5. Users

**Users** là một trong những loại đối tượng phổ biến nhất trong Active Directory.

User object thường đại diện cho người dùng thật trong tổ chức, ví dụ:

- nhân viên;
- sinh viên;
- quản trị viên;
- nhân sự hỗ trợ kỹ thuật;
- người dùng thuộc các phòng ban khác nhau.

Một user trong AD thường có các thông tin như:

- username;
- họ tên;
- mật khẩu;
- email;
- phòng ban;
- trạng thái tài khoản;
- nhóm mà người dùng thuộc về;
- quyền truy cập tài nguyên.

Người dùng domain có thể sử dụng tài khoản của mình để đăng nhập vào máy tính đã tham gia domain và truy cập tài nguyên được cấp quyền.

Ví dụ tài khoản domain có thể có dạng:

```text
COMPANY\nguyen.van.a
```

Hoặc:

```text
nguyen.van.a@company.local
```

Trong quản trị bảo mật, cần kiểm soát chặt chẽ tài khoản người dùng, đặc biệt là tài khoản có quyền cao như Domain Admins hoặc Account Operators.

## 26.6. Service Accounts

**Service Accounts** là tài khoản được dùng để chạy dịch vụ hoặc ứng dụng trong môi trường Windows Domain.

Khác với tài khoản người dùng thông thường, service account thường không đại diện cho một con người cụ thể. Nó được dùng cho các dịch vụ như:

* IIS;
* MSSQL;
* ứng dụng nội bộ;
* dịch vụ backup;
* dịch vụ giám sát;
* tác vụ tự động;
* phần mềm quản lý hệ thống.

Ví dụ, một dịch vụ cơ sở dữ liệu có thể chạy bằng tài khoản:

```text
COMPANY\svc_sql
```

Service account nên được cấp đúng quyền cần thiết để chạy dịch vụ, không nên cấp quyền quá rộng.

Một số nguyên tắc bảo mật khi dùng service account:

* không dùng tài khoản Domain Admin để chạy dịch vụ;
* đặt tên rõ ràng, ví dụ `svc_backup`, `svc_sql`;
* chỉ cấp quyền tối thiểu cần thiết;
* theo dõi đăng nhập và hoạt động của service account;
* thay đổi hoặc quản lý mật khẩu theo chính sách;
* vô hiệu hóa service account không còn sử dụng.

Service Accounts là mục tiêu hấp dẫn với kẻ tấn công vì nhiều tài khoản dịch vụ có quyền truy cập tài nguyên quan trọng.

## 26.7. Computers

**Computers** là các đối tượng đại diện cho máy tính đã tham gia vào domain Active Directory.

Khi một máy tính được join vào domain, Active Directory sẽ tạo một computer object tương ứng.

Computer object có thể đại diện cho:

* máy trạm của nhân viên;
* laptop doanh nghiệp;
* máy chủ;
* máy ảo;
* Domain Controller;
* thiết bị Windows tham gia domain.

Việc quản lý computer objects giúp quản trị viên:

* biết máy nào thuộc domain;
* áp dụng chính sách cho từng nhóm máy;
* phân loại máy trạm và máy chủ;
* kiểm soát thiết bị được phép truy cập domain;
* theo dõi thiết bị không còn sử dụng;
* tổ chức máy theo OU.

Ví dụ, doanh nghiệp có thể tạo các OU riêng như:

```text
Workstations
Servers
Domain Controllers
```

Sau đó đưa máy tính vào đúng OU để áp dụng chính sách phù hợp.

## 26.8. Machine Accounts

**Machine Account** là tài khoản máy tính trong Active Directory. Khi một máy tính tham gia domain, nó sẽ có một tài khoản riêng giống như người dùng, nhưng dành cho máy tính.

Tên machine account thường có dạng:

```text
ComputerName$
```

Ví dụ, nếu máy tính tên là:

```text
DC01
```

Thì tài khoản máy tính sẽ là:

```text
DC01$
```

Machine account được dùng để máy tính xác thực với domain. Nhờ đó, máy tính có thể:

* nhận Group Policy;
* giao tiếp an toàn với Domain Controller;
* truy cập một số dịch vụ domain;
* chứng minh danh tính của nó trong mạng;
* tham gia vào cơ chế xác thực domain.

Mật khẩu của machine account thường được Windows tự động quản lý và thay đổi định kỳ. Người dùng thông thường không cần biết hoặc sử dụng mật khẩu này.

Từ góc độ bảo mật, machine account cũng cần được quản lý cẩn thận. Máy tính không còn sử dụng nên được vô hiệu hóa hoặc xóa khỏi AD để tránh rủi ro.

## 26.9. Security Groups

**Security Groups** là nhóm bảo mật trong Active Directory. Chúng được dùng để gom nhiều người dùng, máy tính hoặc nhóm khác lại với nhau nhằm quản lý quyền truy cập dễ hơn.

Thay vì cấp quyền cho từng người dùng riêng lẻ, quản trị viên có thể cấp quyền cho một nhóm. Sau đó, người dùng nào thuộc nhóm sẽ tự động có quyền tương ứng.

Ví dụ:

* nhóm `HR` có quyền truy cập thư mục nhân sự;
* nhóm `IT Support` có quyền hỗ trợ người dùng;
* nhóm `Domain Admins` có quyền quản trị toàn miền;
* nhóm `Backup Operators` có quyền phục vụ sao lưu dữ liệu.

Một số security groups mặc định quan trọng gồm:

| Security Group     | Ý nghĩa                                                   |
| ------------------ | --------------------------------------------------------- |
| Domain Admins      | Có quyền quản trị toàn bộ domain                          |
| Server Operators   | Có thể quản trị Domain Controllers ở một số mức nhất định |
| Backup Operators   | Có quyền phục vụ sao lưu dữ liệu                          |
| Account Operators  | Có thể tạo hoặc sửa đổi tài khoản trong domain            |
| Domain Users       | Bao gồm các tài khoản người dùng trong domain             |
| Domain Computers   | Bao gồm các máy tính trong domain                         |
| Domain Controllers | Bao gồm các Domain Controllers trong domain               |

Security Groups là công cụ quan trọng để thực hiện phân quyền theo vai trò. Trong bảo mật, cần thường xuyên kiểm tra thành viên của các nhóm có quyền cao.

## 26.10. Shared Resources

**Shared Resources** là các tài nguyên được chia sẻ trong mạng domain để người dùng hoặc máy tính có thể truy cập theo quyền được cấp.

Các shared resources phổ biến gồm:

* thư mục chia sẻ;
* máy in mạng;
* file server;
* ứng dụng nội bộ;
* cơ sở dữ liệu;
* tài nguyên trên máy chủ.

Active Directory giúp quản lý quyền truy cập tới các tài nguyên này thông qua người dùng và nhóm bảo mật.

Ví dụ, doanh nghiệp có thư mục chia sẻ:

```text
\\FILE-SERVER\Accounting
```

Quản trị viên có thể cấp quyền truy cập thư mục này cho nhóm:

```text
Accounting
```

Khi một nhân viên mới vào phòng kế toán, chỉ cần thêm tài khoản của nhân viên đó vào nhóm `Accounting`, người đó sẽ có quyền truy cập tài nguyên tương ứng.

Cách quản lý này giúp hệ thống dễ kiểm soát hơn và giảm sai sót so với việc cấp quyền thủ công cho từng người dùng.

## 26.11. Active Directory Users and Computers

**Active Directory Users and Computers**, thường viết tắt là **ADUC**, là công cụ quản trị dùng để quản lý người dùng, máy tính, nhóm và OU trong Active Directory.

Thông qua ADUC, quản trị viên có thể thực hiện nhiều tác vụ như:

* tạo người dùng mới;
* xóa người dùng;
* chỉnh sửa thông tin người dùng;
* reset mật khẩu;
* tạo nhóm bảo mật;
* thêm người dùng vào nhóm;
* tạo OU;
* di chuyển người dùng hoặc máy tính vào OU;
* quản lý computer objects;
* xem cấu trúc domain.

ADUC thường được sử dụng trực tiếp trên Domain Controller hoặc trên máy quản trị đã cài công cụ RSAT.

Trong môi trường học lab, ADUC là công cụ rất quan trọng để quan sát cấu trúc Active Directory và thực hành quản lý đối tượng.

## 26.12. Công cụ ADUC

Công cụ **ADUC** có thể được mở từ Start Menu trên Domain Controller bằng cách tìm:

```text
Active Directory Users and Computers
```

Ngoài ra, trong nhiều hệ thống, có thể mở bằng lệnh:

```text
dsa.msc
```

Giao diện ADUC thường hiển thị cấu trúc cây của domain. Bên trong domain có thể có:

* OU do quản trị viên tạo;
* container mặc định;
* users;
* groups;
* computers;
* domain controllers.

Một số container mặc định thường gặp gồm:

| Container / OU           | Ý nghĩa                                            |
| ------------------------ | -------------------------------------------------- |
| Builtin                  | Chứa các nhóm mặc định có sẵn                      |
| Computers                | Nơi máy tính mới join domain được đưa vào mặc định |
| Domain Controllers       | OU mặc định chứa các Domain Controllers            |
| Users                    | Chứa người dùng và nhóm mặc định của domain        |
| Managed Service Accounts | Chứa tài khoản dịch vụ được quản lý                |

Trong ADUC, quản trị viên có thể nhấp chuột phải vào OU hoặc đối tượng để thực hiện thao tác như tạo mới, đổi tên, xóa, di chuyển, reset mật khẩu hoặc chỉnh sửa thuộc tính.

Từ góc độ bảo mật, ADUC cần được sử dụng cẩn thận vì thao tác sai có thể ảnh hưởng đến toàn bộ domain. Đặc biệt cần chú ý khi chỉnh sửa:

* nhóm Domain Admins;
* tài khoản service account;
* OU chứa Domain Controllers;
* tài khoản người dùng có quyền cao;
* computer objects của máy chủ quan trọng.

Tóm lại, ADUC là công cụ cơ bản nhưng rất quan trọng trong quản trị Active Directory. Người học Windows Domain cần nắm được cách dùng ADUC để hiểu cách AD tổ chức và quản lý người dùng, máy tính, nhóm và tài nguyên.


# 27. Nhóm bảo mật trong Active Directory

## 27.1. Security Group là gì?

**Security Group** là nhóm bảo mật trong Active Directory dùng để gom nhiều đối tượng lại với nhau nhằm quản lý quyền truy cập dễ hơn.

Các đối tượng có thể là thành viên của Security Group gồm:

- người dùng;
- máy tính;
- nhóm khác;
- tài khoản dịch vụ.

Security Group được xem là một loại **security principal**, nghĩa là nó có thể được cấp quyền truy cập vào tài nguyên trong mạng.

Ví dụ, thay vì cấp quyền truy cập thư mục cho từng người dùng, quản trị viên có thể tạo một nhóm tên là `Accounting`, sau đó cấp quyền cho nhóm này. Người dùng nào được thêm vào nhóm `Accounting` sẽ tự động có quyền tương ứng.

Security Group giúp việc quản trị quyền trong doanh nghiệp trở nên đơn giản, rõ ràng và dễ kiểm soát hơn.


## 27.2. Vai trò của nhóm trong cấp quyền

Vai trò quan trọng nhất của nhóm bảo mật là **cấp quyền theo nhóm thay vì cấp quyền trực tiếp cho từng người dùng**.

Ví dụ, doanh nghiệp có thư mục chia sẻ:

```text
\\FILE-SERVER\HR
```

Thay vì cấp quyền cho từng nhân viên phòng nhân sự, quản trị viên có thể:

1. Tạo nhóm `HR`.
2. Thêm nhân viên phòng nhân sự vào nhóm `HR`.
3. Cấp quyền truy cập thư mục `\\FILE-SERVER\HR` cho nhóm `HR`.

Cách này có nhiều lợi ích:

* dễ thêm người dùng mới;
* dễ xóa quyền khi nhân viên chuyển bộ phận;
* giảm lỗi khi phân quyền thủ công;
* quản lý quyền theo vai trò;
* dễ kiểm tra ai có quyền truy cập tài nguyên;
* phù hợp với nguyên tắc least privilege.

Security Group thường được dùng để cấp quyền cho:

* thư mục chia sẻ;
* máy in mạng;
* ứng dụng nội bộ;
* cơ sở dữ liệu;
* máy chủ;
* quyền quản trị;
* quyền sao lưu;
* quyền hỗ trợ người dùng.

Trong bảo mật Active Directory, cần đặc biệt chú ý đến các nhóm có quyền cao vì nếu tài khoản trong các nhóm này bị chiếm quyền, toàn bộ domain có thể bị ảnh hưởng.

## 27.3. Domain Admins

**Domain Admins** là một trong những nhóm quyền cao nhất trong Active Directory Domain.

Người dùng thuộc nhóm này có quyền quản trị trên toàn bộ domain. Theo mặc định, thành viên của Domain Admins có thể quản trị hầu hết các máy tính trong domain, bao gồm cả Domain Controllers.

Domain Admins có thể thực hiện các tác vụ như:

* quản lý toàn bộ người dùng trong domain;
* tạo, sửa hoặc xóa tài khoản;
* thêm người dùng vào nhóm quyền cao;
* quản lý Domain Controllers;
* cấu hình Group Policy;
* truy cập nhiều hệ thống trong domain;
* thay đổi chính sách bảo mật;
* quản lý tài nguyên quan trọng.

Đây là nhóm rất nhạy cảm về mặt bảo mật. Chỉ những tài khoản thật sự cần quyền quản trị toàn domain mới nên thuộc nhóm này.

Một số khuyến nghị bảo mật với Domain Admins:

* giới hạn số lượng thành viên;
* không dùng tài khoản Domain Admin cho công việc hằng ngày;
* sử dụng tài khoản quản trị riêng;
* bật MFA nếu môi trường hỗ trợ;
* giám sát mọi thay đổi thành viên nhóm;
* kiểm tra log đăng nhập của tài khoản Domain Admin;
* không đăng nhập Domain Admin vào máy trạm thông thường.

Nếu một tài khoản Domain Admin bị chiếm quyền, kẻ tấn công có thể kiểm soát toàn bộ domain.

## 27.4. Server Operators

**Server Operators** là nhóm cho phép thành viên thực hiện một số tác vụ quản trị trên Domain Controllers.

Người dùng trong nhóm này có thể có quyền quản lý máy chủ ở mức nhất định, ví dụ như khởi động hoặc dừng dịch vụ, sao lưu hệ thống hoặc thực hiện một số tác vụ vận hành máy chủ.

Tuy nhiên, Server Operators không có toàn quyền giống Domain Admins. Theo nội dung tài liệu, nhóm này không thể thay đổi tư cách thành viên của các nhóm quản trị.

Server Operators có thể phù hợp trong trường hợp doanh nghiệp muốn giao một số nhiệm vụ vận hành máy chủ cho nhân viên IT mà không cấp toàn quyền quản trị domain.

Tuy nhiên, đây vẫn là nhóm nhạy cảm vì nó liên quan đến Domain Controllers. Cần kiểm soát chặt chẽ thành viên của nhóm này.

Khuyến nghị bảo mật:

* chỉ thêm người dùng thật sự cần quyền;
* không dùng cho tài khoản thông thường;
* theo dõi thay đổi thành viên nhóm;
* kiểm tra hoạt động quản trị trên Domain Controllers;
* tránh cấp quyền này nếu không có nhu cầu rõ ràng.

## 27.5. Backup Operators

**Backup Operators** là nhóm dùng cho các tài khoản cần thực hiện nhiệm vụ sao lưu dữ liệu.

Thành viên của nhóm này có thể truy cập tệp để phục vụ quá trình backup, kể cả trong một số trường hợp quyền thông thường không cho phép truy cập.

Nhóm này thường được dùng cho:

* nhân viên phụ trách sao lưu;
* tài khoản dịch vụ backup;
* phần mềm sao lưu;
* hệ thống khôi phục dữ liệu.

Backup Operators rất quan trọng trong vận hành hệ thống, nhưng cũng có rủi ro bảo mật cao. Lý do là tài khoản có quyền sao lưu có thể đọc nhiều dữ liệu nhạy cảm trong hệ thống.

Nếu tài khoản thuộc Backup Operators bị chiếm quyền, kẻ tấn công có thể lợi dụng quyền này để truy cập hoặc sao chép dữ liệu quan trọng.

Khuyến nghị bảo mật:

* chỉ cấp quyền cho tài khoản backup cần thiết;
* không dùng tài khoản cá nhân nếu không cần;
* theo dõi hoạt động sao lưu;
* kiểm soát nơi lưu bản backup;
* bảo vệ mật khẩu của tài khoản backup;
* kiểm tra định kỳ thành viên nhóm Backup Operators.

Trong SOC, hoạt động truy cập dữ liệu lớn bất thường bởi tài khoản backup cần được giám sát.

## 27.6. Account Operators

**Account Operators** là nhóm cho phép thành viên tạo hoặc sửa đổi các tài khoản trong domain.

Nhóm này thường được dùng để ủy quyền cho nhân viên IT hoặc bộ phận hỗ trợ người dùng thực hiện một số tác vụ liên quan đến tài khoản.

Thành viên của Account Operators có thể thực hiện các tác vụ như:

* tạo tài khoản người dùng;
* chỉnh sửa thông tin tài khoản;
* reset mật khẩu;
* vô hiệu hóa tài khoản;
* quản lý một số nhóm hoặc người dùng theo phạm vi được phép.

Tuy nhiên, Account Operators là nhóm cần được kiểm soát cẩn thận. Nếu bị lạm dụng, tài khoản trong nhóm này có thể tạo tài khoản mới hoặc thay đổi tài khoản hiện có để phục vụ mục đích trái phép.

Rủi ro có thể bao gồm:

* tạo tài khoản ẩn;
* reset mật khẩu trái phép;
* kích hoạt tài khoản đã bị vô hiệu hóa;
* thay đổi thông tin tài khoản;
* hỗ trợ leo thang đặc quyền nếu kết hợp với cấu hình sai khác.

Khuyến nghị bảo mật:

* giới hạn thành viên nhóm;
* sử dụng delegation theo OU nếu có thể;
* không cấp quyền rộng hơn nhu cầu;
* giám sát sự kiện tạo tài khoản mới;
* giám sát reset mật khẩu;
* rà soát tài khoản được tạo gần đây.

Trong môi trường doanh nghiệp, không nên thêm quá nhiều người vào Account Operators nếu chỉ cần quyền hỗ trợ ở một OU cụ thể.

## 27.7. Domain Users

**Domain Users** là nhóm mặc định bao gồm các tài khoản người dùng trong domain.

Khi một tài khoản người dùng domain được tạo, tài khoản đó thường thuộc nhóm Domain Users theo mặc định.

Domain Users thường đại diện cho nhóm người dùng thông thường trong doanh nghiệp, ví dụ:

* nhân viên;
* sinh viên;
* người dùng văn phòng;
* tài khoản người dùng tiêu chuẩn.

Nhóm này thường được dùng để cấp các quyền cơ bản cho toàn bộ người dùng domain, ví dụ:

* đăng nhập vào máy trạm;
* truy cập tài nguyên chung;
* sử dụng máy in mạng;
* truy cập một số thư mục chia sẻ chung;
* nhận chính sách người dùng thông thường.

Tuy nhiên, cần cẩn thận khi cấp quyền cho Domain Users. Vì nhóm này có phạm vi rất rộng, nếu cấp quyền quá cao cho Domain Users, gần như toàn bộ người dùng trong domain sẽ có quyền đó.

Khuyến nghị bảo mật:

* không cấp quyền quản trị cho Domain Users;
* không cấp quyền ghi vào thư mục nhạy cảm;
* không dùng Domain Users để cấp quyền cho dữ liệu quan trọng;
* tạo nhóm riêng theo phòng ban hoặc vai trò;
* áp dụng nguyên tắc least privilege.

Ví dụ, thay vì cấp quyền truy cập thư mục kế toán cho Domain Users, nên tạo nhóm riêng như `Accounting Users` và chỉ thêm nhân viên kế toán vào nhóm đó.

## 27.8. Domain Computers

**Domain Computers** là nhóm mặc định bao gồm các máy tính hiện có trong domain.

Khi một máy tính được join vào domain, tài khoản máy tính của nó thường thuộc nhóm Domain Computers.

Domain Computers đại diện cho các thiết bị đã tham gia domain, ví dụ:

* máy trạm;
* laptop doanh nghiệp;
* máy ảo;
* một số máy chủ thành viên domain.

Nhóm này có thể được dùng trong một số chính sách hoặc cấu hình liên quan đến máy tính. Ví dụ, quản trị viên có thể áp dụng chính sách cho các máy tính domain hoặc kiểm soát quyền truy cập dựa trên tài khoản máy.

Từ góc độ bảo mật, Domain Computers giúp xác định thiết bị nào thuộc domain và có thể xác thực với Domain Controller.

Một số lưu ý bảo mật:

* kiểm tra các máy tính không còn sử dụng;
* vô hiệu hóa hoặc xóa computer object cũ;
* không để máy lạ join domain tùy tiện;
* phân loại máy tính vào OU phù hợp;
* áp dụng chính sách khác nhau cho máy trạm và máy chủ;
* giám sát việc tạo computer account mới.

Nếu domain có nhiều computer account cũ không được quản lý, kẻ tấn công có thể lợi dụng chúng trong một số tình huống nhất định.

## 27.9. Domain Controllers

**Domain Controllers** là nhóm bao gồm tất cả các Domain Controllers hiện có trong domain.

Domain Controller là máy chủ chạy dịch vụ Active Directory Domain Services. Đây là thành phần trung tâm của Windows Domain, chịu trách nhiệm xác thực người dùng, quản lý AD DS và áp dụng nhiều chính sách quan trọng.

Nhóm Domain Controllers thường liên quan đến các máy chủ có vai trò đặc biệt trong domain.

Domain Controllers rất nhạy cảm vì chúng chứa hoặc xử lý nhiều dữ liệu quan trọng như:

* thông tin người dùng;
* thông tin máy tính;
* nhóm bảo mật;
* chính sách domain;
* dữ liệu xác thực;
* mật khẩu băm của tài khoản domain.

Nếu một Domain Controller bị chiếm quyền, toàn bộ domain có thể bị kiểm soát.

Một số khuyến nghị bảo mật đối với Domain Controllers:

* không sử dụng Domain Controller như máy trạm thông thường;
* hạn chế đăng nhập trực tiếp;
* chỉ quản trị viên được phép truy cập;
* cập nhật bảo mật thường xuyên;
* giám sát log đăng nhập và thay đổi AD;
* bảo vệ vật lý và mạng cho Domain Controllers;
* không cài phần mềm không cần thiết;
* sao lưu System State định kỳ;
* kiểm tra thành viên nhóm Domain Admins thường xuyên.

Trong SOC, Domain Controllers là nguồn log cực kỳ quan trọng. Các sự kiện đăng nhập, thay đổi tài khoản, thay đổi nhóm quyền cao và hoạt động xác thực đều cần được giám sát chặt chẽ.

Tóm lại, nhóm bảo mật trong Active Directory giúp quản lý quyền truy cập theo cách tập trung và hiệu quả. Tuy nhiên, các nhóm có quyền cao như Domain Admins, Server Operators, Backup Operators và Account Operators cần được kiểm soát đặc biệt để tránh rủi ro leo thang đặc quyền và mất quyền kiểm soát domain.

# 28. Organizational Units — OUs

## 28.1. OU là gì?

**OU** là viết tắt của **Organizational Unit**, nghĩa là **Đơn vị tổ chức** trong Active Directory.

OU là một loại container dùng để chứa và sắp xếp các đối tượng trong Active Directory, ví dụ:

- người dùng;
- máy tính;
- nhóm;
- tài khoản dịch vụ;
- OU con.

Có thể hiểu OU giống như một thư mục dùng để tổ chức các đối tượng trong domain theo cấu trúc rõ ràng hơn.

Ví dụ, trong một công ty, có thể tạo các OU theo phòng ban:

```text
IT
HR
Accounting
Sales
Marketing
Management
```

Hoặc tạo OU theo loại thiết bị:

```text
Workstations
Servers
Domain Controllers
```

OU giúp Active Directory dễ quản lý hơn, đặc biệt trong môi trường doanh nghiệp có nhiều người dùng, nhiều máy tính và nhiều chính sách khác nhau.

## 28.2. Vai trò của OU trong Active Directory

Vai trò chính của OU là **tổ chức đối tượng** và **áp dụng chính sách quản trị**.

Trong Active Directory, nếu tất cả người dùng và máy tính nằm chung một vị trí, việc quản lý sẽ rất khó khăn. OU giúp chia nhỏ hệ thống thành các nhóm logic, phù hợp với cơ cấu tổ chức hoặc mục đích quản trị.

OU thường được dùng để:

* phân loại người dùng theo phòng ban;
* phân loại máy tính theo loại thiết bị;
* áp dụng Group Policy cho từng nhóm đối tượng;
* ủy quyền quản trị cho một bộ phận cụ thể;
* quản lý người dùng và máy tính dễ hơn;
* giảm nhầm lẫn trong hệ thống lớn.

Ví dụ, người dùng phòng IT có thể cần chính sách khác với người dùng phòng Sales. Khi đó, quản trị viên có thể tạo hai OU riêng:

```text
IT
Sales
```

Sau đó áp dụng chính sách khác nhau cho từng OU.

## 28.3. OU và phòng ban doanh nghiệp

Trong nhiều doanh nghiệp, OU thường được thiết kế dựa trên cơ cấu phòng ban.

Ví dụ, một công ty có các phòng ban sau:

* IT;
* HR;
* Accounting;
* Sales;
* Marketing;
* Management.

Khi đó, Active Directory có thể được tổ chức như sau:

```text
company.local
├── IT
├── HR
├── Accounting
├── Sales
├── Marketing
└── Management
```

Mỗi OU sẽ chứa các tài khoản người dùng thuộc phòng ban tương ứng.

Ví dụ:

```text
Sales
├── user01
├── user02
└── user03
```

Cách tổ chức này có lợi vì mỗi phòng ban có thể có yêu cầu chính sách khác nhau.

Ví dụ:

| OU         | Chính sách có thể áp dụng                           |
| ---------- | --------------------------------------------------- |
| IT         | Cho phép truy cập công cụ quản trị                  |
| Sales      | Hạn chế cài đặt phần mềm                            |
| HR         | Bảo vệ dữ liệu nhân sự                              |
| Accounting | Giới hạn truy cập tài nguyên tài chính              |
| Marketing  | Cho phép một số phần mềm thiết kế hoặc truyền thông |

Tuy nhiên, OU không bắt buộc phải luôn tương ứng với phòng ban. Doanh nghiệp cũng có thể thiết kế OU theo vị trí địa lý, loại thiết bị, mức độ bảo mật hoặc yêu cầu vận hành.

## 28.4. Container mặc định trong Active Directory

Khi tạo domain Active Directory, Windows tự động tạo một số container và OU mặc định.

Các container này giúp lưu trữ các đối tượng quan trọng của domain ngay từ đầu.

Một số container mặc định thường gặp gồm:

* Builtin;
* Computers;
* Domain Controllers;
* Users;
* Managed Service Accounts.

Các container mặc định này có vai trò khác nhau và không nên xóa tùy tiện.

### 28.4.1. Builtin

**Builtin** là container chứa các nhóm mặc định có sẵn trong Windows Server và Active Directory.

Các nhóm trong Builtin thường được dùng cho các quyền quản trị hoặc vận hành cơ bản.

Ví dụ, trong Builtin có thể có các nhóm như:

* Administrators;
* Backup Operators;
* Remote Desktop Users;
* Server Operators;
* Account Operators.

Những nhóm này có thể có quyền đặc biệt trên hệ thống, vì vậy cần kiểm soát cẩn thận thành viên của chúng.

Từ góc độ bảo mật, không nên thêm người dùng vào các nhóm trong Builtin nếu không hiểu rõ quyền mà nhóm đó cung cấp.

### 28.4.2. Computers

**Computers** là container mặc định dùng để chứa các máy tính mới tham gia domain.

Khi một máy tính được join vào domain, nếu quản trị viên không chỉ định OU khác, computer object thường sẽ được đưa vào container Computers.

Ví dụ:

```text
Computers
├── PC01
├── PC02
└── LAPTOP01
```

Tuy nhiên, trong môi trường doanh nghiệp, không nên để tất cả máy tính nằm lâu dài trong container Computers. Nên di chuyển chúng vào các OU phù hợp để áp dụng chính sách tốt hơn.

Ví dụ:

```text
Workstations
Servers
```

Lý do là máy trạm và máy chủ thường cần các chính sách khác nhau.

### 28.4.3. Domain Controllers

**Domain Controllers** là OU mặc định chứa các Domain Controller trong domain.

Domain Controller là máy chủ rất quan trọng vì nó vận hành Active Directory Domain Services và xử lý xác thực trong domain.

OU Domain Controllers thường được áp dụng các chính sách bảo mật đặc biệt, ví dụ:

* Default Domain Controllers Policy;
* chính sách đăng nhập quản trị;
* chính sách audit;
* cấu hình bảo mật nâng cao;
* hạn chế quyền truy cập.

Không nên di chuyển Domain Controller sang OU khác nếu không có lý do rõ ràng. Việc cấu hình sai chính sách cho Domain Controller có thể ảnh hưởng nghiêm trọng đến toàn bộ domain.

### 28.4.4. Users

**Users** là container mặc định chứa một số người dùng và nhóm mặc định của domain.

Trong container này có thể có:

* tài khoản Administrator;
* tài khoản Guest;
* một số nhóm mặc định;
* một số tài khoản người dùng được tạo ban đầu.

Tuy nhiên, trong môi trường doanh nghiệp, không nên để toàn bộ người dùng mới trong container Users nếu cần áp dụng chính sách theo phòng ban.

Thay vào đó, nên tạo các OU riêng như:

```text
IT
HR
Accounting
Sales
```

Sau đó đưa người dùng vào OU tương ứng.

Điều này giúp áp dụng Group Policy rõ ràng hơn và quản lý người dùng dễ hơn.

### 28.4.5. Managed Service Accounts

**Managed Service Accounts** là container chứa các tài khoản dịch vụ được quản lý trong domain.

Managed Service Account là loại tài khoản được thiết kế để chạy dịch vụ hoặc ứng dụng một cách an toàn hơn so với tài khoản người dùng thông thường.

Container này có thể chứa:

* Managed Service Accounts;
* Group Managed Service Accounts;
* tài khoản dùng cho dịch vụ trong domain.

Các tài khoản dịch vụ thường được dùng cho:

* SQL Server;
* IIS;
* dịch vụ backup;
* ứng dụng nội bộ;
* dịch vụ giám sát;
* tác vụ tự động.

Từ góc độ bảo mật, tài khoản dịch vụ cần được quản lý cẩn thận vì chúng có thể có quyền truy cập vào hệ thống hoặc dữ liệu quan trọng.

## 28.5. So sánh OU và Security Group

OU và Security Group đều giúp phân loại đối tượng trong Active Directory, nhưng mục đích sử dụng của chúng khác nhau.

| Tiêu chí                     | OU                                               | Security Group                                     |
| ---------------------------- | ------------------------------------------------ | -------------------------------------------------- |
| Tên đầy đủ                   | Organizational Unit                              | Security Group                                     |
| Mục đích chính               | Tổ chức đối tượng và áp dụng chính sách          | Cấp quyền truy cập tài nguyên                      |
| Dùng cho                     | User, computer, group, OU con                    | User, computer, service account, group khác        |
| Áp dụng Group Policy         | Có                                               | Không trực tiếp theo cách OU                       |
| Cấp quyền thư mục/máy in     | Không phải mục đích chính                        | Có                                                 |
| Một user thuộc bao nhiêu OU? | Thường chỉ nằm trong một OU tại một thời điểm    | Có thể thuộc nhiều nhóm                            |
| Ví dụ                        | OU `Sales` để áp dụng chính sách cho phòng Sales | Group `Sales_Users` để cấp quyền vào thư mục Sales |

Ví dụ dễ hiểu:

* OU trả lời câu hỏi: **người dùng hoặc máy tính này nằm ở đâu trong cấu trúc quản trị?**
* Security Group trả lời câu hỏi: **người dùng hoặc máy tính này được quyền truy cập tài nguyên nào?**

Vì vậy, không nên dùng OU để thay thế Security Group và cũng không nên dùng Security Group để thay thế OU.

## 28.6. OU dùng để áp dụng chính sách

OU thường được dùng để áp dụng **Group Policy Object — GPO**.

GPO là tập hợp các cấu hình có thể áp dụng cho người dùng hoặc máy tính trong Active Directory.

Ví dụ, có thể áp dụng chính sách cho OU `Sales` như:

* chặn truy cập Control Panel;
* không cho cài phần mềm;
* tự động khóa màn hình sau 5 phút;
* cấu hình Windows Firewall;
* cấu hình mật khẩu;
* cấu hình proxy;
* triển khai script đăng nhập.

Ví dụ cấu trúc:

```text
company.local
├── Sales
│   ├── user01
│   └── user02
├── IT
│   ├── admin01
│   └── admin02
└── Workstations
    ├── PC01
    └── PC02
```

Nếu liên kết một GPO vào OU `Sales`, chính sách đó sẽ áp dụng cho các đối tượng phù hợp trong OU `Sales`.

Một điểm quan trọng là GPO có thể được kế thừa xuống các OU con. Vì vậy, khi thiết kế OU, cần tính đến việc chính sách sẽ ảnh hưởng đến những đối tượng nào.

Ví dụ:

```text
Sales
└── Interns
```

Nếu GPO được áp dụng cho OU `Sales`, OU con `Interns` cũng có thể bị ảnh hưởng bởi chính sách đó.

Từ góc độ bảo mật, OU giúp triển khai chính sách nhất quán cho từng nhóm người dùng hoặc máy tính.

## 28.7. Security Group dùng để cấp quyền tài nguyên

**Security Group** được dùng để cấp quyền truy cập tài nguyên.

Các tài nguyên có thể bao gồm:

* thư mục chia sẻ;
* máy in mạng;
* file server;
* ứng dụng nội bộ;
* database;
* hệ thống quản trị;
* tài nguyên trên máy chủ.

Ví dụ, công ty có thư mục chia sẻ:

```text
\\FILE-SERVER\Sales
```

Thay vì cấp quyền trực tiếp cho từng người dùng, quản trị viên nên tạo nhóm:

```text
Sales_Users
```

Sau đó:

1. Thêm người dùng phòng Sales vào nhóm `Sales_Users`.
2. Cấp quyền truy cập thư mục `\\FILE-SERVER\Sales` cho nhóm `Sales_Users`.

Cách này giúp quản lý quyền dễ hơn.

Khi nhân viên mới vào phòng Sales, chỉ cần thêm người đó vào nhóm `Sales_Users`.

Khi nhân viên chuyển phòng hoặc nghỉ việc, chỉ cần xóa người đó khỏi nhóm.

Ví dụ:

```text
Sales_Users
├── user01
├── user02
└── user03
```

Security Group đặc biệt quan trọng trong bảo mật vì nó giúp thực hiện nguyên tắc **least privilege** — chỉ cấp quyền vừa đủ cho đúng người cần truy cập.

Tóm lại:

* **OU** dùng để tổ chức đối tượng và áp dụng chính sách.
* **Security Group** dùng để cấp quyền truy cập tài nguyên.

Hiểu rõ sự khác nhau giữa OU và Security Group là nền tảng quan trọng khi học Active Directory và bảo mật Windows Domain.

# 29. Quản lý người dùng trong Active Directory

## 29.1. Tạo người dùng trong AD

Trong Active Directory, người dùng được quản lý dưới dạng **User Object**. Mỗi tài khoản người dùng đại diện cho một cá nhân hoặc một tài khoản dùng để đăng nhập, truy cập tài nguyên và nhận chính sách trong domain.

Có thể tạo người dùng bằng công cụ **Active Directory Users and Computers — ADUC**.

Các bước tạo người dùng trong ADUC:

1. Mở **Active Directory Users and Computers**.
2. Chọn OU nơi muốn tạo người dùng.
3. Nhấp chuột phải vào OU.
4. Chọn **New → User**.
5. Nhập thông tin người dùng.
6. Đặt username đăng nhập.
7. Thiết lập mật khẩu ban đầu.
8. Chọn các tùy chọn mật khẩu phù hợp.
9. Nhấn **Finish**.

Ví dụ, nếu công ty có OU `Sales`, người dùng thuộc phòng kinh doanh nên được tạo trong OU này:

```text
company.local
└── Sales
    └── user01
```

Khi tạo người dùng, cần đặt thông tin rõ ràng như:

- họ tên;
- username;
- phòng ban;
- email;
- chức vụ;
- mô tả tài khoản nếu cần.

Trong môi trường doanh nghiệp, không nên tạo tất cả người dùng trong container `Users` mặc định. Nên đưa người dùng vào đúng OU để dễ áp dụng chính sách và quản lý.


## 29.2. Xóa người dùng trong AD

Xóa người dùng trong Active Directory là thao tác loại bỏ tài khoản khỏi domain.

Có thể xóa người dùng trong ADUC bằng cách:

1. Mở **Active Directory Users and Computers**.
2. Tìm đến OU chứa người dùng.
3. Nhấp chuột phải vào tài khoản người dùng.
4. Chọn **Delete**.
5. Xác nhận thao tác xóa.

Tuy nhiên, trong thực tế doanh nghiệp, không nên xóa tài khoản ngay lập tức nếu chưa chắc chắn. Thay vào đó, nên **Disable Account** trước.

Lý do nên vô hiệu hóa trước khi xóa:

- tránh xóa nhầm tài khoản;
- giữ lại thông tin để điều tra nếu cần;
- giữ lịch sử liên quan đến log;
- có thể khôi phục nếu người dùng quay lại;
- tránh ảnh hưởng đến quyền sở hữu tệp hoặc hệ thống liên quan.

Quy trình an toàn hơn khi nhân viên nghỉ việc:

1. Disable tài khoản.
2. Đổi mật khẩu nếu cần.
3. Thu hồi quyền nhóm.
4. Kiểm tra quyền truy cập tài nguyên.
5. Lưu lại thông tin theo chính sách nội bộ.
6. Xóa tài khoản sau thời gian lưu trữ nếu được phép.


## 29.3. Chỉnh sửa thông tin người dùng

Trong ADUC, quản trị viên có thể chỉnh sửa thông tin của tài khoản người dùng thông qua phần **Properties**.

Các bước chỉnh sửa:

1. Mở **Active Directory Users and Computers**.
2. Tìm tài khoản người dùng.
3. Nhấp chuột phải vào tài khoản.
4. Chọn **Properties**.
5. Chỉnh sửa thông tin cần thiết.
6. Nhấn **Apply** hoặc **OK**.

Một số thông tin thường được chỉnh sửa gồm:

| Thuộc tính | Ý nghĩa |
|---|---|
| First name | Tên |
| Last name | Họ |
| Display name | Tên hiển thị |
| User logon name | Tên đăng nhập |
| Email | Địa chỉ email |
| Department | Phòng ban |
| Title | Chức vụ |
| Office | Văn phòng |
| Telephone number | Số điện thoại |
| Member Of | Nhóm mà người dùng thuộc về |

Việc cập nhật thông tin người dùng giúp Active Directory phản ánh đúng cơ cấu tổ chức và hỗ trợ quản trị tốt hơn.

Từ góc độ bảo mật, cần đặc biệt chú ý tab **Member Of**, vì đây là nơi cho biết người dùng đang thuộc những nhóm nào. Nếu người dùng bị thêm nhầm vào nhóm quyền cao, họ có thể có quyền vượt quá nhu cầu công việc.


## 29.4. Đặt lại mật khẩu người dùng

Đặt lại mật khẩu là một tác vụ quản trị phổ biến trong Active Directory, đặc biệt đối với bộ phận IT Support hoặc Helpdesk.

Có thể đặt lại mật khẩu bằng ADUC:

1. Mở **Active Directory Users and Computers**.
2. Tìm tài khoản người dùng.
3. Nhấp chuột phải vào tài khoản.
4. Chọn **Reset Password**.
5. Nhập mật khẩu mới.
6. Xác nhận mật khẩu.
7. Chọn tùy chọn phù hợp nếu cần.
8. Nhấn **OK**.

Tùy chọn thường dùng khi reset password là:

```text
User must change password at next logon
```

Tùy chọn này giúp đảm bảo người dùng không tiếp tục sử dụng mật khẩu tạm thời do quản trị viên đặt.

Khi đặt lại mật khẩu, cần lưu ý:

- không gửi mật khẩu qua kênh không an toàn;
- không dùng mật khẩu quá đơn giản;
- không dùng lại mật khẩu cũ;
- xác minh danh tính người yêu cầu reset;
- ghi nhận thao tác reset nếu tổ chức yêu cầu;
- buộc người dùng đổi mật khẩu khi đăng nhập lần tiếp theo.


## 29.5. Buộc người dùng đổi mật khẩu khi đăng nhập

Tùy chọn **User must change password at next logon** dùng để buộc người dùng đổi mật khẩu khi đăng nhập lần tiếp theo.

Tùy chọn này thường được sử dụng trong các trường hợp:

- tài khoản mới được tạo;
- mật khẩu được reset bởi IT Support;
- nghi ngờ mật khẩu đã bị lộ;
- người dùng quên mật khẩu;
- tài khoản được khôi phục sau khi bị khóa.

Cách bật tùy chọn này trong ADUC:

1. Mở **Active Directory Users and Computers**.
2. Tìm tài khoản người dùng.
3. Nhấp chuột phải → **Properties**.
4. Mở tab **Account**.
5. Chọn:

```text
User must change password at next logon
```

6. Nhấn **Apply** hoặc **OK**.

Ý nghĩa bảo mật của tùy chọn này là người dùng sẽ không tiếp tục dùng mật khẩu tạm thời do quản trị viên biết. Sau khi đăng nhập, người dùng phải tạo mật khẩu mới của riêng mình.

Trong môi trường doanh nghiệp, đây là thực hành bảo mật nên áp dụng khi cấp mật khẩu ban đầu hoặc reset mật khẩu.


## 29.6. Xóa OU dư thừa

Trong Active Directory, đôi khi có các OU không còn cần thiết, ví dụ phòng ban đã giải thể hoặc cấu trúc tổ chức đã thay đổi.

Có thể xóa OU trong ADUC bằng cách:

1. Mở **Active Directory Users and Computers**.
2. Tìm OU cần xóa.
3. Nhấp chuột phải vào OU.
4. Chọn **Delete**.
5. Xác nhận thao tác.

Tuy nhiên, trong nhiều trường hợp, Windows sẽ không cho xóa OU ngay vì OU được bảo vệ khỏi việc xóa nhầm.

Khi xóa OU, cần rất cẩn thận vì:

- người dùng bên trong OU có thể bị xóa;
- nhóm bên trong OU có thể bị xóa;
- OU con cũng có thể bị xóa;
- chính sách liên quan có thể bị ảnh hưởng;
- có thể làm sai cấu trúc quản trị AD.

Trước khi xóa OU, nên kiểm tra:

- OU có còn người dùng không;
- OU có chứa máy tính không;
- OU có OU con không;
- OU có GPO đang liên kết không;
- có tài khoản dịch vụ hoặc tài khoản quan trọng bên trong không.

Trong thực tế, nên di chuyển hoặc backup thông tin trước khi xóa OU quan trọng.


## 29.7. Advanced Features trong ADUC

**Advanced Features** là tùy chọn trong ADUC giúp hiển thị thêm các thành phần và tab nâng cao.

Để bật Advanced Features:

1. Mở **Active Directory Users and Computers**.
2. Trên thanh menu, chọn **View**.
3. Chọn **Advanced Features**.

Khi bật Advanced Features, ADUC sẽ hiển thị thêm một số thông tin và tùy chọn nâng cao, ví dụ:

- tab **Object** trong Properties;
- một số container hệ thống;
- thông tin thuộc tính chi tiết hơn;
- tùy chọn bảo vệ đối tượng khỏi xóa nhầm;
- khả năng kiểm tra một số cấu hình nâng cao.

Advanced Features thường cần dùng khi muốn xóa một OU đang được bảo vệ khỏi xóa nhầm.

Ví dụ, để bỏ bảo vệ xóa nhầm cho OU:

1. Bật **Advanced Features**.
2. Nhấp chuột phải vào OU.
3. Chọn **Properties**.
4. Mở tab **Object**.
5. Bỏ chọn:

```text
Protect object from accidental deletion
```

6. Nhấn **OK**.


## 29.8. Bảo vệ OU khỏi xóa nhầm

Active Directory có cơ chế bảo vệ OU khỏi việc xóa nhầm. Tùy chọn này thường có tên:

```text
Protect object from accidental deletion
```

Khi tùy chọn này được bật, quản trị viên không thể xóa OU một cách trực tiếp nếu chưa tắt bảo vệ.

Mục đích của tính năng này là giảm rủi ro xóa nhầm các đối tượng quan trọng trong AD.

Tính năng này đặc biệt hữu ích với các OU chứa:

- người dùng quan trọng;
- máy chủ;
- máy trạm doanh nghiệp;
- Domain Controllers;
- tài khoản dịch vụ;
- cấu trúc phòng ban lớn.

Không nên tắt tính năng bảo vệ này nếu không có lý do rõ ràng.

Nếu cần xóa OU thật sự, cần:

1. Bật **Advanced Features**.
2. Mở **Properties** của OU.
3. Vào tab **Object**.
4. Bỏ chọn **Protect object from accidental deletion**.
5. Xác nhận thay đổi.
6. Thực hiện xóa OU.

Từ góc độ bảo mật và quản trị, bảo vệ OU khỏi xóa nhầm giúp giảm rủi ro lỗi thao tác của con người.


## 29.9. Delegation là gì?

**Delegation** trong Active Directory là quá trình ủy quyền một số quyền quản trị nhất định cho người dùng hoặc nhóm mà không cần cấp quyền Domain Admin.

Nói đơn giản, Delegation cho phép một người dùng thực hiện một số tác vụ quản trị trong phạm vi nhất định.

Ví dụ:

- IT Support được reset mật khẩu cho người dùng phòng Sales;
- trưởng bộ phận được chỉnh sửa thông tin người dùng trong OU của mình;
- Helpdesk được unlock account;
- nhóm quản trị máy trạm được quản lý OU Workstations.

Delegation giúp phân chia công việc quản trị mà không cần cấp quyền quá cao.

Lợi ích của Delegation:

- giảm phụ thuộc vào Domain Admin;
- áp dụng nguyên tắc least privilege;
- giới hạn quyền theo OU;
- phân quyền rõ ràng theo vai trò;
- giảm rủi ro lạm dụng quyền;
- hỗ trợ bộ phận Helpdesk làm việc hiệu quả hơn.

Delegation rất quan trọng trong doanh nghiệp vì không phải tác vụ nào cũng cần quyền quản trị toàn domain.


## 29.10. Delegate Control

**Delegate Control** là chức năng trong ADUC dùng để ủy quyền quản trị cho một user hoặc group trên một OU cụ thể.

Cách mở Delegate Control:

1. Mở **Active Directory Users and Computers**.
2. Tìm OU cần ủy quyền.
3. Nhấp chuột phải vào OU.
4. Chọn **Delegate Control**.
5. Chọn user hoặc group được ủy quyền.
6. Chọn tác vụ muốn ủy quyền.
7. Hoàn tất wizard.

Các quyền thường được ủy quyền gồm:

- reset password;
- force password change at next logon;
- read user information;
- create, delete, and manage user accounts;
- modify membership of a group;
- manage computer accounts.

Ví dụ, có thể ủy quyền cho nhóm `Helpdesk` quyền reset mật khẩu trong OU `Sales`.

Cấu trúc ví dụ:

```text
company.local
└── Sales
    ├── user01
    ├── user02
    └── user03
```

Nếu Delegate Control được áp dụng cho OU `Sales`, người được ủy quyền chỉ có quyền trong phạm vi OU này, không có quyền quản trị toàn domain.

Đây là cách quản lý an toàn hơn so với việc thêm Helpdesk vào nhóm Domain Admins.


## 29.11. Ủy quyền đặt lại mật khẩu

Một trường hợp sử dụng phổ biến của Delegation là ủy quyền cho IT Support hoặc Helpdesk đặt lại mật khẩu người dùng.

Ví dụ, công ty muốn tài khoản `phillip` có thể reset mật khẩu cho người dùng trong OU `Sales`.

Các bước thực hiện trong ADUC:

1. Mở **Active Directory Users and Computers**.
2. Nhấp chuột phải vào OU `Sales`.
3. Chọn **Delegate Control**.
4. Nhấn **Next**.
5. Thêm user hoặc group cần ủy quyền, ví dụ `phillip`.
6. Chọn tác vụ:

```text
Reset user passwords and force password change at next logon
```

7. Nhấn **Next**.
8. Nhấn **Finish**.

Sau khi cấu hình, người được ủy quyền có thể reset mật khẩu cho người dùng trong OU đó.

Điểm quan trọng là người được ủy quyền không nhất thiết có quyền Domain Admin. Họ chỉ có quyền thực hiện tác vụ đã được cấp trong phạm vi OU.

Khuyến nghị bảo mật:

- nên ủy quyền cho group thay vì user cá nhân;
- đặt tên group rõ ràng, ví dụ `Helpdesk_ResetPassword_Sales`;
- chỉ cấp đúng quyền cần thiết;
- thường xuyên kiểm tra quyền đã delegate;
- ghi log thao tác reset mật khẩu;
- không ủy quyền quá rộng trên toàn domain nếu không cần.


## 29.12. Quản lý người dùng AD bằng PowerShell

Ngoài ADUC, quản trị viên có thể quản lý người dùng Active Directory bằng PowerShell.

PowerShell rất hữu ích khi cần:

- tạo nhiều người dùng;
- reset mật khẩu nhanh;
- chỉnh sửa thuộc tính hàng loạt;
- xuất danh sách người dùng;
- kiểm tra trạng thái tài khoản;
- tự động hóa tác vụ quản trị.

Để dùng các lệnh AD trong PowerShell, thường cần module Active Directory:

```powershell
Import-Module ActiveDirectory
```

Một số lệnh PowerShell thường dùng:

| Lệnh | Ý nghĩa |
|---|---|
| `Get-ADUser` | Xem thông tin người dùng |
| `New-ADUser` | Tạo người dùng mới |
| `Set-ADUser` | Chỉnh sửa thuộc tính người dùng |
| `Remove-ADUser` | Xóa người dùng |
| `Disable-ADAccount` | Vô hiệu hóa tài khoản |
| `Enable-ADAccount` | Kích hoạt tài khoản |
| `Unlock-ADAccount` | Mở khóa tài khoản |
| `Set-ADAccountPassword` | Đặt lại mật khẩu |

Ví dụ xem thông tin người dùng:

```powershell
Get-ADUser -Identity sophie
```

Ví dụ đặt lại mật khẩu:

```powershell
Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString "New Password")
```

Ví dụ buộc người dùng đổi mật khẩu khi đăng nhập lần tiếp theo:

```powershell
Set-ADUser sophie -ChangePasswordAtLogon $true
```

Ví dụ vô hiệu hóa tài khoản:

```powershell
Disable-ADAccount -Identity sophie
```

Ví dụ tạo người dùng mới:

```powershell
New-ADUser `
  -Name "Nguyen Van A" `
  -GivenName "A" `
  -Surname "Nguyen Van" `
  -SamAccountName "nguyen.van.a" `
  -UserPrincipalName "nguyen.van.a@company.local" `
  -Path "OU=Sales,DC=company,DC=local" `
  -AccountPassword (Read-Host -AsSecureString "Initial Password") `
  -Enabled $true
```

Khi dùng PowerShell để quản lý AD, cần cẩn thận vì lệnh có thể thay đổi nhiều tài khoản rất nhanh. Trước khi chạy lệnh hàng loạt, nên kiểm tra kỹ phạm vi bằng các lệnh như `Get-ADUser`.

Từ góc độ bảo mật, cần giám sát các thao tác PowerShell liên quan đến AD, đặc biệt là:

- tạo tài khoản mới;
- reset mật khẩu;
- thêm user vào nhóm quyền cao;
- thay đổi thuộc tính tài khoản;
- vô hiệu hóa hoặc kích hoạt tài khoản;
- xóa người dùng hoặc OU.

Tóm lại, quản lý người dùng trong Active Directory là nhiệm vụ cơ bản nhưng rất quan trọng. Quản trị viên cần biết cách tạo, chỉnh sửa, reset mật khẩu, xóa tài khoản, ủy quyền quản trị và sử dụng PowerShell một cách an toàn.


# 30. Quản lý máy tính trong Active Directory

## 30.1. Computer Objects trong AD

Trong Active Directory, **Computer Object** là đối tượng đại diện cho một máy tính đã tham gia vào domain.

Khi một máy tính được join vào domain, Active Directory sẽ tạo một đối tượng máy tính tương ứng. Đối tượng này giúp domain nhận diện, xác thực và quản lý máy tính đó trong hệ thống.

Computer Object có thể đại diện cho:

- máy trạm của người dùng;
- laptop doanh nghiệp;
- máy chủ;
- máy ảo;
- Domain Controller;
- thiết bị Windows tham gia domain.

Ví dụ, nếu một máy tính có tên là:

```text
PC01
````

thì trong Active Directory sẽ có một Computer Object tên là:

```text
PC01
```

Computer Object rất quan trọng vì nó cho phép máy tính:

* xác thực với Domain Controller;
* nhận Group Policy;
* được quản lý tập trung;
* truy cập tài nguyên domain nếu được cấp quyền;
* được phân loại theo OU;
* được áp dụng chính sách bảo mật phù hợp.

Từ góc độ bảo mật, cần quản lý Computer Objects cẩn thận vì mỗi máy tính trong domain đều là một điểm truy cập vào hệ thống doanh nghiệp.

## 30.2. Container Computers mặc định

Khi một máy tính mới tham gia domain, nếu quản trị viên không chỉ định vị trí khác, Computer Object thường được đưa vào container mặc định có tên là **Computers**.

Container này có thể có dạng:

```text
domain.local
└── Computers
    ├── PC01
    ├── PC02
    └── LAPTOP01
```

Container **Computers** giúp lưu trữ các máy tính mới join domain, nhưng trong môi trường doanh nghiệp, không nên để toàn bộ máy tính ở đây lâu dài.

Lý do là container Computers không phù hợp để tổ chức chính sách chi tiết theo từng loại thiết bị. Máy trạm, máy chủ và các thiết bị quan trọng thường cần chính sách khác nhau.

Ví dụ:

* máy trạm cần chính sách khóa màn hình, hạn chế Control Panel;
* máy chủ cần chính sách bảo mật nghiêm ngặt hơn;
* Domain Controller cần chính sách riêng;
* laptop có thể cần BitLocker và chính sách firewall khác.

Vì vậy, sau khi máy tính join domain, quản trị viên nên di chuyển chúng vào OU phù hợp.

## 30.3. Vì sao cần phân loại máy tính trong AD?

Cần phân loại máy tính trong Active Directory để quản lý và áp dụng chính sách chính xác hơn.

Nếu tất cả máy tính đều nằm chung một container, rất khó áp dụng chính sách khác nhau cho từng nhóm thiết bị. Trong thực tế, không phải máy tính nào cũng có cùng vai trò và mức độ nhạy cảm.

Ví dụ:

| Loại thiết bị      | Yêu cầu quản lý                                      |
| ------------------ | ---------------------------------------------------- |
| Workstations       | Máy người dùng, cần chính sách sử dụng hằng ngày     |
| Servers            | Máy cung cấp dịch vụ, cần bảo mật và ổn định cao hơn |
| Domain Controllers | Máy quản lý domain, cần bảo vệ đặc biệt              |

Việc phân loại máy tính giúp:

* áp dụng Group Policy phù hợp;
* dễ quản lý máy trạm và máy chủ;
* giảm rủi ro cấu hình sai;
* phân quyền quản trị rõ ràng;
* dễ kiểm kê tài sản;
* hỗ trợ điều tra sự cố;
* tăng mức độ bảo mật của domain.

Ví dụ, quản trị viên có thể tạo các OU riêng:

```text
Workstations
Servers
Domain Controllers
```

Sau đó di chuyển máy tính vào đúng OU để áp dụng chính sách phù hợp.

Đây là cách quản lý tốt hơn so với để tất cả máy tính trong container Computers mặc định.

## 30.4. Workstations

**Workstations** là các máy trạm được người dùng sử dụng để làm việc hằng ngày.

Workstations thường là:

* máy tính để bàn của nhân viên;
* laptop công ty;
* máy trong phòng lab;
* máy của sinh viên hoặc nhân viên văn phòng;
* máy người dùng đăng nhập bằng tài khoản domain.

Máy trạm là loại thiết bị phổ biến nhất trong domain. Người dùng domain thường đăng nhập vào các máy này để làm việc, truy cập tài liệu, sử dụng ứng dụng nội bộ và kết nối tài nguyên mạng.

Các chính sách thường áp dụng cho Workstations gồm:

* khóa màn hình tự động;
* hạn chế quyền Administrator cục bộ;
* bật Windows Defender Firewall;
* bật antivirus;
* cấu hình Windows Update;
* chặn truy cập Control Panel nếu cần;
* cấu hình BitLocker cho laptop;
* giới hạn cài đặt phần mềm;
* thu thập log bảo mật.

Từ góc độ bảo mật, Workstations là mục tiêu phổ biến của tấn công vì người dùng thường mở email, tải tệp và truy cập web trên các máy này.

Do đó, không nên đăng nhập tài khoản có quyền cao như Domain Admin vào máy trạm thông thường, trừ khi thật sự cần thiết và có kiểm soát.

## 30.5. Servers

**Servers** là các máy chủ trong domain, dùng để cung cấp dịch vụ cho người dùng hoặc các hệ thống khác.

Máy chủ có thể đảm nhiệm nhiều vai trò như:

* File Server;
* Web Server;
* Database Server;
* DNS Server;
* DHCP Server;
* Application Server;
* Backup Server;
* Remote Desktop Server.

Servers thường quan trọng hơn máy trạm vì chúng lưu trữ dữ liệu, cung cấp dịch vụ hoặc xử lý chức năng trọng yếu của doanh nghiệp.

Các chính sách thường áp dụng cho Servers gồm:

* hạn chế đăng nhập cục bộ;
* chỉ cho phép quản trị viên được truy cập;
* bật firewall với rule chặt chẽ;
* giới hạn phần mềm được cài đặt;
* bật audit logging;
* cấu hình backup;
* cập nhật bảo mật theo kế hoạch;
* giám sát dịch vụ quan trọng;
* bảo vệ tài khoản dịch vụ.

Không nên áp dụng chính sách giống hệt máy trạm cho máy chủ nếu chính sách đó có thể làm gián đoạn dịch vụ.

Ví dụ, chính sách tự động restart sau cập nhật có thể phù hợp với máy trạm, nhưng với máy chủ cần được lập lịch cẩn thận để tránh ảnh hưởng đến người dùng.

## 30.6. Domain Controllers

**Domain Controllers** là các máy chủ đặc biệt trong domain. Chúng chạy dịch vụ **Active Directory Domain Services — AD DS** và chịu trách nhiệm xác thực người dùng, máy tính, quản lý dữ liệu AD và phân phối chính sách.

Domain Controllers là thành phần nhạy cảm nhất trong Windows Domain vì chúng liên quan trực tiếp đến:

* xác thực người dùng;
* xác thực máy tính;
* dữ liệu Active Directory;
* tài khoản domain;
* nhóm bảo mật;
* Group Policy;
* mật khẩu băm;
* quyền truy cập trong domain.

Trong Active Directory, Domain Controllers thường nằm trong OU mặc định:

```text
Domain Controllers
```

OU này thường được áp dụng chính sách riêng, ví dụ:

```text
Default Domain Controllers Policy
```

Không nên di chuyển Domain Controllers sang OU khác nếu không có lý do rõ ràng.

Một số nguyên tắc bảo mật với Domain Controllers:

* không dùng Domain Controller như máy trạm;
* không cài phần mềm không cần thiết;
* hạn chế đăng nhập trực tiếp;
* chỉ quản trị viên được phép truy cập;
* bật audit logging;
* cập nhật bảo mật định kỳ;
* sao lưu System State;
* giám sát thay đổi AD;
* bảo vệ vật lý và mạng.

Nếu Domain Controller bị chiếm quyền, toàn bộ domain có thể bị kiểm soát.

## 30.7. Tạo OU cho Workstations

Để quản lý máy trạm tốt hơn, nên tạo OU riêng cho Workstations.

Các bước tạo OU trong ADUC:

1. Mở **Active Directory Users and Computers**.
2. Nhấp chuột phải vào domain.
3. Chọn **New → Organizational Unit**.
4. Nhập tên OU:

```text
Workstations
```

5. Nhấn **OK**.

Sau khi tạo, cấu trúc có thể như sau:

```text
domain.local
└── Workstations
```

OU Workstations sẽ được dùng để chứa các máy trạm của người dùng.

Ví dụ:

```text
Workstations
├── PC01
├── PC02
├── LAPTOP01
└── LAPTOP02
```

Khi các máy trạm nằm trong OU này, quản trị viên có thể áp dụng GPO riêng cho máy trạm, ví dụ:

* tự động khóa màn hình sau 5 phút;
* bật Windows Firewall;
* cấu hình Windows Update;
* chặn người dùng cài phần mềm;
* cấu hình audit policy;
* triển khai script quản trị.

Việc tạo OU riêng cho Workstations giúp chính sách rõ ràng và dễ kiểm soát hơn.

## 30.8. Tạo OU cho Servers

Tương tự Workstations, nên tạo OU riêng cho Servers để quản lý máy chủ.

Các bước tạo OU Servers:

1. Mở **Active Directory Users and Computers**.
2. Nhấp chuột phải vào domain.
3. Chọn **New → Organizational Unit**.
4. Nhập tên OU:

```text
Servers
```

5. Nhấn **OK**.

Cấu trúc ví dụ:

```text
domain.local
└── Servers
```

Bên trong OU Servers có thể chứa các máy chủ như:

```text
Servers
├── FILE-SERVER01
├── WEB-SERVER01
├── DB-SERVER01
└── BACKUP-SERVER01
```

Trong môi trường lớn hơn, có thể chia OU Servers thành các OU con:

```text
Servers
├── File Servers
├── Web Servers
├── Database Servers
└── Backup Servers
```

Cách chia này giúp áp dụng chính sách riêng cho từng nhóm máy chủ.

Ví dụ:

* File Servers cần chính sách audit truy cập file;
* Web Servers cần cấu hình firewall theo cổng web;
* Database Servers cần bảo vệ quyền truy cập cơ sở dữ liệu;
* Backup Servers cần chính sách bảo vệ dữ liệu sao lưu.

Việc tạo OU Servers giúp giảm nguy cơ áp dụng nhầm chính sách của máy trạm lên máy chủ.

## 30.9. Di chuyển máy tính vào OU phù hợp

Sau khi tạo OU, cần di chuyển các Computer Objects vào đúng OU.

Các bước di chuyển máy tính trong ADUC:

1. Mở **Active Directory Users and Computers**.
2. Mở container **Computers** hoặc OU hiện tại.
3. Chọn máy tính cần di chuyển.
4. Nhấp chuột phải vào máy tính.
5. Chọn **Move**.
6. Chọn OU đích, ví dụ `Workstations` hoặc `Servers`.
7. Nhấn **OK**.

Ví dụ, có thể di chuyển:

```text
PC01 → Workstations
FILE-SERVER01 → Servers
```

Sau khi di chuyển, cấu trúc có thể là:

```text
domain.local
├── Workstations
│   ├── PC01
│   └── PC02
└── Servers
    ├── FILE-SERVER01
    └── WEB-SERVER01
```

Việc di chuyển máy tính vào đúng OU giúp máy nhận đúng Group Policy.

Nếu một máy không nhận chính sách ngay, có thể chạy lệnh trên máy đó:

```cmd
gpupdate /force
```

Sau đó kiểm tra lại chính sách đã áp dụng hay chưa.

Trong thực tế, cần có quy trình rõ ràng sau khi join domain: máy mới không nên nằm lâu trong container Computers mà nên được đưa vào OU phù hợp.

## 30.10. Nguyên tắc bảo mật khi quản lý máy trạm và máy chủ

Khi quản lý máy tính trong Active Directory, cần áp dụng các nguyên tắc bảo mật phù hợp cho từng loại thiết bị.

Đối với **Workstations**, nên chú ý:

* không cho người dùng thông thường có quyền Administrator cục bộ;
* bật Windows Defender hoặc antivirus;
* bật Windows Defender Firewall;
* cập nhật hệ thống định kỳ;
* cấu hình khóa màn hình tự động;
* hạn chế chạy phần mềm không rõ nguồn gốc;
* bật BitLocker cho laptop;
* thu thập log bảo mật;
* không đăng nhập tài khoản Domain Admin vào máy trạm thông thường.

Đối với **Servers**, nên chú ý:

* chỉ cài dịch vụ cần thiết;
* hạn chế số người được đăng nhập;
* bật audit logging;
* cấu hình firewall chặt chẽ;
* cập nhật bảo mật theo kế hoạch;
* sao lưu dữ liệu quan trọng;
* giám sát dịch vụ đang chạy;
* bảo vệ tài khoản dịch vụ;
* không dùng máy chủ cho công việc cá nhân.

Đối với **Domain Controllers**, cần bảo vệ nghiêm ngặt hơn:

* chỉ quản trị viên được phép truy cập;
* không cài phần mềm không cần thiết;
* không dùng làm file server hoặc máy trạm;
* giám sát log xác thực;
* giám sát thay đổi nhóm quyền cao;
* sao lưu System State;
* kiểm tra thành viên Domain Admins;
* bảo vệ khỏi truy cập vật lý trái phép.

Một số nguyên tắc chung:

* phân loại máy tính theo OU rõ ràng;
* áp dụng GPO phù hợp từng nhóm;
* xóa hoặc disable computer objects không còn sử dụng;
* đặt tên máy theo quy ước dễ hiểu;
* kiểm tra máy lạ mới join domain;
* theo dõi thay đổi trong AD;
* áp dụng nguyên tắc least privilege;
* không dùng chung chính sách cho mọi loại thiết bị nếu nhu cầu khác nhau.

Tóm lại, quản lý máy tính trong Active Directory không chỉ là việc đưa máy vào domain. Quan trọng hơn là phải phân loại đúng, áp dụng chính sách phù hợp và bảo vệ từng nhóm thiết bị theo mức độ rủi ro của chúng.


# 31. Group Policy

## 31.1. Group Policy là gì?

**Group Policy** là cơ chế trong Active Directory dùng để quản lý tập trung các thiết lập cho người dùng và máy tính trong domain.

Thay vì cấu hình từng máy tính riêng lẻ, quản trị viên có thể tạo chính sách và áp dụng cho nhiều đối tượng cùng lúc.

Group Policy có thể dùng để cấu hình:

- mật khẩu;
- khóa tài khoản;
- quyền truy cập Control Panel;
- Windows Firewall;
- Windows Update;
- màn hình khóa;
- script đăng nhập;
- cấu hình bảo mật;
- thiết lập cho người dùng;
- thiết lập cho máy tính.

Ví dụ, doanh nghiệp có thể tạo chính sách yêu cầu tất cả người dùng phải dùng mật khẩu tối thiểu 10 ký tự. Khi chính sách được áp dụng, người dùng trong phạm vi đó phải tuân theo yêu cầu này.

Group Policy là một thành phần rất quan trọng trong quản trị Windows Domain vì nó giúp đảm bảo cấu hình hệ thống đồng nhất và giảm rủi ro do cấu hình thủ công.


## 31.2. Group Policy Object — GPO

**GPO** là viết tắt của **Group Policy Object**. Đây là đối tượng chứa các thiết lập chính sách trong Active Directory.

Có thể hiểu GPO là một “gói cấu hình” dùng để áp dụng cho người dùng hoặc máy tính.

Một GPO có thể chứa các thiết lập như:

- chính sách mật khẩu;
- chính sách khóa tài khoản;
- chặn truy cập Control Panel;
- cấu hình Windows Firewall;
- cấu hình màn hình khóa;
- chạy script khi đăng nhập;
- cấu hình trình duyệt;
- cấu hình bảo mật hệ thống.

Ví dụ, có thể tạo một GPO tên là:

```text
Restrict Control Panel
```

Sau đó cấu hình GPO này để chặn người dùng mở Control Panel.

Một GPO chỉ có hiệu lực khi nó được liên kết với phạm vi phù hợp, ví dụ domain, site hoặc OU.

## 31.3. Vai trò của GPO trong quản trị miền

GPO có vai trò quan trọng trong quản trị miền vì nó cho phép quản trị viên áp dụng cấu hình tập trung cho nhiều người dùng và máy tính.

Nếu không có GPO, quản trị viên phải cấu hình từng máy riêng lẻ. Điều này rất mất thời gian và dễ gây sai sót.

GPO giúp doanh nghiệp:

* áp dụng chính sách bảo mật đồng nhất;
* giảm cấu hình thủ công;
* quản lý người dùng theo phòng ban;
* quản lý máy tính theo loại thiết bị;
* hạn chế quyền người dùng;
* triển khai thiết lập bảo mật;
* kiểm soát môi trường làm việc;
* hỗ trợ tuân thủ chính sách nội bộ.

Ví dụ:

| Nhu cầu quản trị    | Có thể dùng GPO để làm gì                    |
| ------------------- | -------------------------------------------- |
| Bảo vệ tài khoản    | Cấu hình password policy và account lockout  |
| Bảo vệ máy trạm     | Bật firewall, khóa màn hình tự động          |
| Giới hạn người dùng | Chặn Control Panel hoặc hạn chế cài phần mềm |
| Quản lý máy chủ     | Cấu hình audit policy và quyền đăng nhập     |
| Chuẩn hóa hệ thống  | Áp dụng cấu hình giống nhau cho nhiều máy    |

Từ góc độ bảo mật, GPO giúp giảm rủi ro do người dùng tự ý thay đổi cấu hình hoặc máy tính có thiết lập không đồng nhất.

## 31.4. Group Policy Management

**Group Policy Management** là công cụ dùng để tạo, chỉnh sửa, liên kết và quản lý GPO trong Active Directory.

Công cụ này thường được mở trên Domain Controller hoặc máy quản trị đã cài RSAT.

Có thể mở bằng Start Menu bằng cách tìm:

```text
Group Policy Management
```

Hoặc mở bằng lệnh:

```text
gpmc.msc
```

Trong Group Policy Management, quản trị viên có thể xem:

* cấu trúc domain;
* các OU;
* các GPO đã tạo;
* GPO đang liên kết với domain hoặc OU;
* phạm vi áp dụng của GPO;
* Security Filtering;
* trạng thái kế thừa chính sách;
* kết quả áp dụng chính sách.

Công cụ này rất quan trọng vì nó cho phép quản trị viên quản lý chính sách một cách trực quan và tập trung.

## 31.5. Tạo GPO

Để tạo một GPO mới, quản trị viên có thể sử dụng công cụ **Group Policy Management**.

Các bước cơ bản:

1. Mở **Group Policy Management**.
2. Mở domain cần quản lý.
3. Nhấp chuột phải vào **Group Policy Objects**.
4. Chọn **New**.
5. Nhập tên GPO.
6. Nhấn **OK**.

Ví dụ tên GPO:

```text
Lock Screen Policy
```

Sau khi tạo, GPO mới chưa tự động áp dụng cho người dùng hoặc máy tính. Cần liên kết GPO đó với domain hoặc OU phù hợp.

Sau khi tạo GPO, quản trị viên có thể nhấp chuột phải vào GPO và chọn **Edit** để chỉnh sửa nội dung chính sách.

Ví dụ, trong GPO có thể cấu hình:

* khóa màn hình sau 5 phút;
* chặn Control Panel;
* cấu hình password policy;
* bật firewall;
* chạy script đăng nhập.

## 31.6. Liên kết GPO với OU

Một GPO cần được **link** với OU, domain hoặc site để có hiệu lực.

Trong thực tế, GPO thường được liên kết với OU để áp dụng chính sách cho nhóm người dùng hoặc máy tính cụ thể.

Các bước liên kết GPO với OU:

1. Mở **Group Policy Management**.
2. Chọn OU cần áp dụng chính sách.
3. Nhấp chuột phải vào OU.
4. Chọn **Link an Existing GPO**.
5. Chọn GPO muốn liên kết.
6. Nhấn **OK**.

Ví dụ, nếu muốn áp dụng chính sách khóa màn hình cho máy trạm, có thể link GPO vào OU:

```text
Workstations
```

Cấu trúc ví dụ:

```text
company.local
└── Workstations
    ├── PC01
    └── PC02
```

Khi GPO được liên kết với OU `Workstations`, các máy tính trong OU đó sẽ nhận chính sách nếu chúng thuộc phạm vi áp dụng của GPO.

Theo tài liệu, GPO liên kết với một OU có thể áp dụng cho OU đó và các OU con bên dưới nó. 

## 31.7. GPO Scope

**GPO Scope** là phạm vi mà GPO được áp dụng trong Active Directory.

Scope cho biết GPO đang được liên kết ở đâu và đối tượng nào có thể nhận chính sách đó.

Một GPO có thể được liên kết với:

* site;
* domain;
* OU.

Ví dụ:

```text
company.local
├── Sales
├── IT
└── Workstations
```

Nếu GPO được link vào OU `Sales`, chính sách sẽ áp dụng cho các đối tượng phù hợp trong OU `Sales`.

Nếu GPO được link ở cấp domain, chính sách có thể ảnh hưởng đến phạm vi rộng hơn, thậm chí nhiều OU bên dưới.

Khi kiểm tra một GPO trong Group Policy Management, tab **Scope** cho biết:

* GPO được link ở đâu;
* Security Filtering;
* WMI Filtering nếu có;
* đối tượng nào có thể nhận chính sách.

Hiểu đúng GPO Scope rất quan trọng để tránh áp dụng chính sách sai phạm vi.

## 31.8. Security Filtering

**Security Filtering** là cơ chế dùng để giới hạn đối tượng nào được áp dụng GPO.

Theo mặc định, nhiều GPO áp dụng cho nhóm **Authenticated Users**, tức là bao gồm người dùng và máy tính đã xác thực trong domain. 

Tuy nhiên, trong thực tế có thể cần áp dụng GPO cho một nhóm cụ thể thay vì toàn bộ người dùng hoặc máy tính trong OU.

Ví dụ, trong OU `Sales`, chỉ muốn GPO áp dụng cho nhóm:

```text
Sales_Users
```

Khi đó, có thể dùng Security Filtering để giới hạn phạm vi.

Security Filtering hữu ích trong các trường hợp:

* chỉ áp dụng chính sách cho một nhóm người dùng;
* loại trừ một số tài khoản đặc biệt;
* áp dụng chính sách cho nhóm máy tính cụ thể;
* triển khai thử nghiệm GPO cho một nhóm nhỏ;
* giảm rủi ro áp dụng nhầm chính sách.

Cần cấu hình Security Filtering cẩn thận. Nếu bỏ sai nhóm hoặc thiếu quyền đọc và áp dụng chính sách, GPO có thể không hoạt động như mong muốn.

## 31.9. Computer Configuration

**Computer Configuration** là phần trong GPO chứa các thiết lập áp dụng cho máy tính.

Các thiết lập trong Computer Configuration được áp dụng dựa trên Computer Object, không phụ thuộc trực tiếp vào người dùng nào đăng nhập.

Computer Configuration thường dùng để cấu hình:

* chính sách bảo mật máy tính;
* Windows Firewall;
* Windows Update;
* dịch vụ hệ thống;
* script khởi động hoặc tắt máy;
* audit policy;
* thiết lập Registry ở cấp máy;
* quyền đăng nhập cục bộ;
* cấu hình phần mềm cho máy tính.

Ví dụ, nếu muốn bật firewall cho tất cả máy trạm trong OU `Workstations`, nên cấu hình trong Computer Configuration.

Một số tình huống dùng Computer Configuration:

| Tình huống        | Ví dụ                                 |
| ----------------- | ------------------------------------- |
| Cấu hình máy trạm | Bật firewall, bật audit logging       |
| Cấu hình máy chủ  | Hạn chế đăng nhập cục bộ              |
| Bảo mật hệ thống  | Cấu hình quyền user rights assignment |
| Cập nhật          | Thiết lập Windows Update              |
| Khởi động máy     | Chạy startup script                   |

Computer Configuration rất quan trọng trong bảo mật vì nó cho phép áp dụng chính sách ổn định cho thiết bị, kể cả khi người dùng khác nhau đăng nhập vào máy.

## 31.10. User Configuration

**User Configuration** là phần trong GPO chứa các thiết lập áp dụng cho người dùng.

Các thiết lập này đi theo tài khoản người dùng. Khi người dùng đăng nhập vào máy tính trong domain, chính sách liên quan đến user có thể được áp dụng.

User Configuration thường dùng để cấu hình:

* Start Menu;
* Desktop;
* Control Panel;
* script đăng nhập hoặc đăng xuất;
* giới hạn ứng dụng;
* cấu hình trình duyệt;
* ổ đĩa mạng;
* máy in;
* thiết lập môi trường người dùng;
* chính sách giao diện.

Ví dụ, nếu muốn chặn người dùng phòng Sales mở Control Panel, có thể cấu hình GPO trong User Configuration và link GPO với OU chứa user phòng Sales.

Một số tình huống dùng User Configuration:

| Tình huống           | Ví dụ                             |
| -------------------- | --------------------------------- |
| Giới hạn người dùng  | Chặn Control Panel                |
| Thiết lập môi trường | Map network drive                 |
| Quản lý giao diện    | Cấu hình desktop hoặc Start Menu  |
| Tự động hóa          | Chạy logon script                 |
| Bảo mật người dùng   | Hạn chế truy cập công cụ hệ thống |

User Configuration giúp quản trị viên kiểm soát trải nghiệm và quyền hạn của người dùng trong môi trường domain.

## 31.11. Default Domain Policy

**Default Domain Policy** là GPO mặc định được tạo khi domain Active Directory được thiết lập.

GPO này thường được liên kết với toàn bộ domain. Theo tài liệu, Default Domain Policy là một trong các GPO có sẵn và được liên kết với toàn bộ miền. 

Default Domain Policy thường chứa các chính sách cơ bản áp dụng cho toàn domain, đặc biệt là:

* Password Policy;
* Account Lockout Policy;
* Kerberos Policy;
* một số thiết lập bảo mật cơ bản.

Trong thực tế, Default Domain Policy nên được sử dụng cẩn thận. Không nên đưa quá nhiều cấu hình không liên quan vào GPO này vì nó có thể ảnh hưởng đến toàn bộ domain.

Khuyến nghị:

* giữ Default Domain Policy cho các chính sách cấp domain quan trọng;
* không chỉnh sửa tùy tiện;
* sao lưu trước khi thay đổi lớn;
* ghi lại mọi thay đổi;
* không dùng để cấu hình tất cả thiết lập cho mọi OU;
* tạo GPO riêng cho từng mục đích cụ thể nếu cần.

Ví dụ, chính sách mật khẩu toàn domain có thể nằm trong Default Domain Policy.

## 31.12. Default Domain Controllers Policy

**Default Domain Controllers Policy** là GPO mặc định được áp dụng cho OU **Domain Controllers**.

Theo tài liệu, Default Domain Controllers Policy được liên kết với OU Domain Controllers. 

GPO này chứa các thiết lập dành riêng cho Domain Controllers. Vì Domain Controllers là thành phần rất nhạy cảm trong domain, chính sách áp dụng cho chúng cần được kiểm soát chặt chẽ.

Default Domain Controllers Policy có thể liên quan đến:

* audit policy;
* user rights assignment;
* quyền đăng nhập;
* cấu hình bảo mật cho Domain Controllers;
* thiết lập hệ thống quan trọng.

Không nên chỉnh sửa GPO này nếu không hiểu rõ tác động, vì cấu hình sai có thể ảnh hưởng đến khả năng xác thực và hoạt động của toàn bộ domain.

Khuyến nghị:

* chỉ quản trị viên có kinh nghiệm mới nên chỉnh sửa;
* ghi lại mọi thay đổi;
* kiểm tra trong môi trường lab nếu có thể;
* không áp dụng chính sách máy trạm cho Domain Controllers;
* thường xuyên kiểm tra cấu hình bảo mật của Domain Controllers.

## 31.13. Password Policy

**Password Policy** là chính sách quy định yêu cầu đối với mật khẩu của tài khoản trong domain.

Chính sách này thường nằm trong Default Domain Policy và áp dụng ở cấp domain.

Password Policy có thể bao gồm:

* độ dài tối thiểu của mật khẩu;
* độ phức tạp của mật khẩu;
* thời gian hết hạn mật khẩu;
* lịch sử mật khẩu;
* tuổi tối thiểu của mật khẩu;
* quy định người dùng có được dùng lại mật khẩu cũ hay không.

Ví dụ, tài liệu đề cập đến cấu hình mật khẩu tối thiểu 10 ký tự trong Group Policy. 

Một chính sách mật khẩu tốt giúp giảm nguy cơ:

* đoán mật khẩu;
* brute-force;
* password spraying;
* dùng mật khẩu quá yếu;
* dùng lại mật khẩu cũ.

Ví dụ cấu hình khuyến nghị cơ bản:

| Thiết lập                                  | Ý nghĩa                                        |
| ------------------------------------------ | ---------------------------------------------- |
| Minimum password length                    | Độ dài tối thiểu của mật khẩu                  |
| Password must meet complexity requirements | Yêu cầu độ phức tạp                            |
| Enforce password history                   | Không cho dùng lại mật khẩu gần đây            |
| Maximum password age                       | Thời gian tối đa được dùng một mật khẩu        |
| Minimum password age                       | Thời gian tối thiểu trước khi đổi lại mật khẩu |

Trong doanh nghiệp, Password Policy cần cân bằng giữa bảo mật và khả năng sử dụng. Mật khẩu quá yếu gây rủi ro, nhưng chính sách quá khó dùng có thể khiến người dùng ghi mật khẩu ra nơi không an toàn.

## 31.14. Account Lockout Policy

**Account Lockout Policy** là chính sách khóa tài khoản sau một số lần đăng nhập sai.

Chính sách này giúp giảm nguy cơ brute-force mật khẩu trong domain.

Account Lockout Policy thường gồm các thiết lập:

| Thiết lập                           | Ý nghĩa                                          |
| ----------------------------------- | ------------------------------------------------ |
| Account lockout threshold           | Số lần đăng nhập sai trước khi tài khoản bị khóa |
| Account lockout duration            | Thời gian tài khoản bị khóa                      |
| Reset account lockout counter after | Thời gian đặt lại bộ đếm đăng nhập sai           |

Ví dụ, doanh nghiệp có thể cấu hình:

```text
Account lockout threshold: 5 invalid attempts
Account lockout duration: 15 minutes
Reset account lockout counter after: 15 minutes
```

Khi đó, nếu người dùng nhập sai mật khẩu 5 lần, tài khoản sẽ bị khóa trong 15 phút.

Account Lockout Policy giúp bảo vệ tài khoản, nhưng cần cấu hình hợp lý. Nếu ngưỡng quá thấp, người dùng có thể bị khóa tài khoản thường xuyên. Nếu ngưỡng quá cao, chính sách có thể không đủ hiệu quả chống brute-force.

Từ góc độ SOC, nhiều tài khoản bị lockout trong thời gian ngắn có thể là dấu hiệu của:

* brute-force;
* password spraying;
* người dùng nhập sai mật khẩu hàng loạt;
* hệ thống hoặc dịch vụ đang dùng mật khẩu cũ;
* tấn công vào tài khoản domain.

## 31.15. Kế thừa GPO

**Kế thừa GPO** nghĩa là GPO được áp dụng từ cấp cao xuống cấp thấp trong cấu trúc Active Directory.

Nếu một GPO được liên kết với domain hoặc OU cha, các OU con bên dưới có thể cũng bị ảnh hưởng.

Ví dụ:

```text
company.local
└── Sales
    └── Interns
```

Nếu GPO được link vào OU `Sales`, OU con `Interns` cũng có thể nhận chính sách đó.

Theo tài liệu, bất kỳ GPO nào được liên kết với một OU sẽ áp dụng cho OU đó và tất cả các sub-OU bên dưới nó. 

Kế thừa GPO giúp quản trị viên áp dụng chính sách rộng hơn mà không cần link GPO nhiều lần. Tuy nhiên, nó cũng có thể gây rủi ro nếu không kiểm soát tốt.

Rủi ro khi không hiểu kế thừa GPO:

* chính sách áp dụng nhầm cho OU con;
* người dùng bị hạn chế ngoài dự kiến;
* máy chủ nhận chính sách của máy trạm;
* cấu hình bảo mật bị ghi đè;
* khó xác định chính sách nào đang tác động.

Khi thiết kế OU và GPO, cần kiểm tra kỹ:

* GPO link ở đâu;
* OU con nào bị ảnh hưởng;
* có cần Block Inheritance không;
* có GPO nào được Enforced không;
* Security Filtering có đúng không.

## 31.16. Cập nhật GPO với `gpupdate /force`

Thông thường, Windows tự động cập nhật Group Policy theo chu kỳ. Tuy nhiên, khi cần áp dụng chính sách ngay lập tức, có thể dùng lệnh:

```cmd
gpupdate /force
```

Lệnh này cưỡng chế cập nhật lại Group Policy trên máy tính hiện tại.

Cách chạy:

1. Mở Command Prompt hoặc PowerShell.
2. Chạy lệnh:

```cmd
gpupdate /force
```

3. Chờ quá trình cập nhật hoàn tất.
4. Khởi động lại hoặc đăng xuất nếu Windows yêu cầu.

Theo tài liệu, nếu đã tạo và liên kết GPO nhưng chính sách chưa hoạt động, có thể chạy `gpupdate /force` để cưỡng chế cập nhật GPO. 

Lệnh này hữu ích trong các trường hợp:

* vừa tạo GPO mới;
* vừa chỉnh sửa GPO;
* vừa di chuyển máy tính sang OU khác;
* vừa thay đổi Security Filtering;
* cần kiểm tra chính sách trong lab;
* chính sách chưa áp dụng ngay.

Ví dụ:

```cmd
gpupdate /force
```

Sau khi chạy, có thể kiểm tra GPO đã áp dụng hay chưa bằng các công cụ như:

```cmd
gpresult /r
```

Hoặc:

```cmd
rsop.msc
```

Từ góc độ quản trị và bảo mật, `gpupdate /force` là lệnh rất quan trọng khi triển khai hoặc kiểm tra chính sách trong Windows Domain.

Tóm lại, Group Policy là cơ chế cốt lõi giúp quản trị viên áp dụng cấu hình và chính sách bảo mật tập trung trong Active Directory. Hiểu rõ GPO, scope, security filtering, computer/user configuration và kế thừa chính sách là nền tảng quan trọng để quản lý Windows Domain an toàn.


# 32. Triển khai chính sách bảo mật bằng GPO

## 32.1. Hạn chế truy cập Control Panel

Một ví dụ phổ biến khi triển khai chính sách bảo mật bằng GPO là **hạn chế người dùng truy cập Control Panel**.

Control Panel và PC Settings cho phép người dùng thay đổi nhiều thiết lập quan trọng của hệ thống, ví dụ:

- cấu hình mạng;
- thiết lập tài khoản;
- thiết lập phần mềm;
- Windows Firewall;
- thiết bị phần cứng;
- cấu hình hệ thống;
- một số tùy chọn bảo mật.

Trong môi trường doanh nghiệp, người dùng thông thường không nên tự do thay đổi các thiết lập này. Nếu người dùng thay đổi sai cấu hình, máy tính có thể gặp lỗi hoặc không tuân thủ chính sách bảo mật của tổ chức.

Ví dụ, doanh nghiệp có thể muốn:

- bộ phận IT được phép truy cập Control Panel;
- người dùng phòng Sales, Marketing, Management không được truy cập;
- người dùng thông thường không được tự ý thay đổi cài đặt hệ thống.

Để thực hiện, có thể tạo một GPO riêng, ví dụ:

```text
Restrict Control Panel Access
```

Sau đó cấu hình chính sách chặn Control Panel và liên kết GPO này với các OU chứa người dùng cần bị hạn chế.

### 32.2. Chính sách Prohibit Access to Control Panel and PC Settings

Chính sách **Prohibit Access to Control Panel and PC Settings** dùng để chặn người dùng truy cập Control Panel và PC Settings.

Chính sách này thường nằm trong phần **User Configuration** vì nó áp dụng cho người dùng.

Đường dẫn cấu hình thường là:

```text
User Configuration
└── Policies
    └── Administrative Templates
        └── Control Panel
            └── Prohibit access to Control Panel and PC settings
```

Khi bật chính sách này ở trạng thái **Enabled**, người dùng bị áp dụng GPO sẽ không thể mở Control Panel hoặc PC Settings.

Các bước cấu hình cơ bản:

1. Mở **Group Policy Management**.
2. Tạo GPO mới, ví dụ:

```text
Restrict Control Panel Access
```

3. Nhấp chuột phải vào GPO và chọn **Edit**.
4. Đi đến đường dẫn:

```text
User Configuration → Policies → Administrative Templates → Control Panel
```

5. Mở chính sách:

```text
Prohibit access to Control Panel and PC settings
```

6. Chọn **Enabled**.
7. Nhấn **Apply** và **OK**.

Sau khi chính sách có hiệu lực, nếu người dùng thử mở Control Panel, Windows sẽ hiển thị thông báo rằng thao tác này bị quản trị viên hạn chế.

## 32.3. Liên kết GPO với OU người dùng

Sau khi tạo và cấu hình GPO, cần liên kết GPO với OU phù hợp để chính sách có hiệu lực.

Vì chính sách hạn chế Control Panel áp dụng cho **người dùng**, nên GPO cần được liên kết với OU chứa tài khoản người dùng.

Ví dụ, nếu muốn chặn người dùng trong các phòng ban sau:

* Marketing;
* Sales;
* Management.

Có thể liên kết GPO `Restrict Control Panel Access` với các OU tương ứng:

```text
company.local
├── Marketing
├── Sales
└── Management
```

Các bước liên kết GPO với OU:

1. Mở **Group Policy Management**.
2. Tìm OU cần áp dụng chính sách.
3. Nhấp chuột phải vào OU.
4. Chọn **Link an Existing GPO**.
5. Chọn GPO:

```text
Restrict Control Panel Access
```

6. Nhấn **OK**.

Nếu bộ phận IT vẫn cần truy cập Control Panel, không nên liên kết GPO này với OU `IT`.

Điều quan trọng là phải xác định đúng OU chứa người dùng cần áp dụng chính sách. Nếu liên kết nhầm, chính sách có thể ảnh hưởng đến người dùng không mong muốn.

## 32.4. Chính sách khóa màn hình tự động

Chính sách khóa màn hình tự động giúp bảo vệ phiên làm việc của người dùng khi họ rời khỏi máy tính nhưng quên khóa màn hình.

Trong môi trường doanh nghiệp, đây là chính sách bảo mật quan trọng vì máy tính đang đăng nhập có thể chứa:

* tài liệu nội bộ;
* email công việc;
* hệ thống quản trị;
* dữ liệu khách hàng;
* ứng dụng nội bộ;
* quyền truy cập tài nguyên mạng.

Nếu người dùng rời khỏi máy mà không khóa màn hình, người khác có thể lợi dụng phiên làm việc đang mở để truy cập dữ liệu hoặc thực hiện hành động trái phép.

Ví dụ chính sách có thể yêu cầu:

```text
Tự động khóa màn hình sau 5 phút không hoạt động
```

Có thể tạo GPO riêng, ví dụ:

```text
Auto Lock Screen
```

Chính sách này thường áp dụng cho máy tính hoặc người dùng tùy cách cấu hình. Trong bài lab, mục tiêu là cấu hình cho máy trạm và máy chủ tự động khóa màn hình sau 5 phút không hoạt động.

Lợi ích bảo mật:

* giảm nguy cơ người khác sử dụng phiên đăng nhập đang mở;
* bảo vệ dữ liệu khi người dùng rời khỏi máy;
* phù hợp với chính sách bảo mật doanh nghiệp;
* giảm rủi ro truy cập trái phép nội bộ.

## 32.5. Áp dụng GPO cho Workstations và Servers

GPO có thể được áp dụng trực tiếp cho các OU chứa máy tính, ví dụ:

```text
Workstations
Servers
Domain Controllers
```

Nếu chính sách khóa màn hình cần áp dụng cho máy trạm và máy chủ, có thể liên kết GPO `Auto Lock Screen` với các OU này.

Ví dụ:

```text
company.local
├── Workstations
│   ├── PC01
│   └── PC02
├── Servers
│   ├── FILE-SERVER01
│   └── WEB-SERVER01
└── Domain Controllers
    └── DC01
```

Các bước thực hiện:

1. Tạo GPO:

```text
Auto Lock Screen
```

2. Cấu hình chính sách khóa màn hình.
3. Link GPO với OU `Workstations`.
4. Link GPO với OU `Servers`.
5. Nếu cần, link với OU `Domain Controllers`.

Khi áp dụng chính sách cho máy chủ, cần cẩn thận hơn so với máy trạm. Một số chính sách có thể ảnh hưởng đến phiên quản trị hoặc dịch vụ đang chạy.

Khuyến nghị:

* kiểm tra chính sách trên nhóm nhỏ trước;
* không áp dụng chính sách quá rộng nếu chưa thử nghiệm;
* tách GPO cho Workstations và Servers nếu yêu cầu khác nhau;
* tránh áp dụng chính sách máy trạm trực tiếp lên Domain Controllers nếu không chắc chắn.

## 32.6. Áp dụng GPO ở cấp miền

Ngoài việc liên kết GPO với từng OU, quản trị viên có thể áp dụng GPO ở cấp **domain**.

Khi GPO được liên kết ở cấp miền, các OU bên dưới có thể kế thừa chính sách đó.

Ví dụ:

```text
company.local
├── Workstations
├── Servers
├── Domain Controllers
├── Sales
├── Marketing
└── IT
```

Nếu GPO `Auto Lock Screen` được liên kết với `company.local`, các OU con có thể nhận chính sách này.

Cách này phù hợp khi muốn áp dụng chính sách cho phạm vi rộng, ví dụ:

* chính sách mật khẩu;
* chính sách khóa tài khoản;
* cấu hình bảo mật chung;
* chính sách khóa màn hình toàn doanh nghiệp;
* một số cấu hình cơ bản bắt buộc.

Tuy nhiên, cần lưu ý rằng áp dụng GPO ở cấp miền có thể ảnh hưởng đến nhiều đối tượng. Nếu GPO chứa cấu hình không phù hợp, nó có thể gây lỗi trên diện rộng.

Ví dụ, nếu GPO chứa cấu hình dành cho máy tính nhưng được kế thừa bởi OU chỉ chứa người dùng, phần cấu hình máy tính sẽ không áp dụng cho người dùng. Tuy nhiên, việc thiết kế GPO vẫn cần rõ ràng để tránh nhầm lẫn.

Khuyến nghị:

* chỉ áp dụng GPO ở cấp miền khi chính sách thật sự cần áp dụng rộng;
* kiểm tra kỹ nội dung GPO;
* đặt tên GPO rõ ràng;
* không đưa quá nhiều cấu hình khác nhau vào một GPO;
* thử nghiệm trước khi triển khai toàn domain.

## 32.7. Kiểm tra hiệu lực của GPO

Sau khi triển khai GPO, cần kiểm tra xem chính sách đã có hiệu lực hay chưa.

Có thể kiểm tra bằng nhiều cách.

Cách 1: kiểm tra trực tiếp trên máy người dùng.

Ví dụ với chính sách chặn Control Panel:

1. Đăng nhập bằng tài khoản người dùng thuộc OU bị áp dụng GPO.
2. Thử mở **Control Panel**.
3. Nếu GPO hoạt động, Windows sẽ chặn truy cập.

Cách 2: kiểm tra chính sách khóa màn hình.

1. Đăng nhập vào máy thuộc OU được áp dụng GPO.
2. Không thao tác trên máy trong thời gian đã cấu hình.
3. Kiểm tra xem màn hình có tự động khóa hay không.

Cách 3: dùng lệnh kiểm tra GPO.

Trên máy client, có thể chạy:

```cmd
gpresult /r
```

Lệnh này hiển thị các GPO đã áp dụng cho người dùng và máy tính hiện tại.

Có thể dùng lệnh chi tiết hơn:

```cmd
gpresult /h report.html
```

Lệnh này tạo báo cáo HTML để xem GPO đã áp dụng.

Ngoài ra, có thể dùng:

```cmd
rsop.msc
```

Công cụ này hiển thị Resultant Set of Policy, tức là tập chính sách thực tế đang áp dụng trên máy.

Kiểm tra hiệu lực GPO là bước quan trọng để đảm bảo chính sách đã được triển khai đúng.

## 32.8. Xử lý lỗi GPO không áp dụng

Nếu GPO không áp dụng, cần kiểm tra theo từng bước.

Một số nguyên nhân thường gặp:

| Nguyên nhân            | Giải thích                                                           |
| ---------------------- | -------------------------------------------------------------------- |
| GPO chưa được link     | GPO đã tạo nhưng chưa liên kết với OU/domain                         |
| Link sai OU            | GPO được link vào OU không chứa đúng user hoặc computer              |
| Sai loại cấu hình      | Cấu hình user nhưng áp dụng vào OU chỉ chứa computer, hoặc ngược lại |
| Security Filtering sai | Đối tượng không có quyền Apply Group Policy                          |
| Máy chưa cập nhật GPO  | Client chưa đồng bộ chính sách mới                                   |
| GPO bị disable         | Phần User Configuration hoặc Computer Configuration bị tắt           |
| Kế thừa bị chặn        | OU có Block Inheritance                                              |
| GPO bị ghi đè          | GPO khác có độ ưu tiên cao hơn                                       |
| DNS/domain lỗi         | Máy client không liên lạc được Domain Controller                     |

Các bước xử lý cơ bản:

1. Kiểm tra GPO đã được link đúng OU chưa.
2. Kiểm tra OU có chứa đúng user hoặc computer không.
3. Kiểm tra GPO nằm trong User Configuration hay Computer Configuration.
4. Kiểm tra Security Filtering.
5. Chạy lệnh cập nhật GPO:

```cmd
gpupdate /force
```

6. Kiểm tra bằng:

```cmd
gpresult /r
```

7. Kiểm tra Event Viewer nếu vẫn lỗi.

Ví dụ, nếu chính sách chặn Control Panel không hoạt động, cần kiểm tra tài khoản người dùng có nằm trong OU được link GPO hay không.

Nếu chính sách khóa màn hình không hoạt động, cần kiểm tra máy tính có nằm trong OU được áp dụng GPO hay không.

## 32.9. SYSVOL là gì?

**SYSVOL** là thư mục chia sẻ trên Domain Controller dùng để lưu trữ và phân phối các tệp liên quan đến Group Policy trong domain.

SYSVOL là thành phần rất quan trọng trong Active Directory vì máy tính và người dùng trong domain cần truy cập SYSVOL để nhận chính sách.

Theo mặc định, SYSVOL thường nằm trên Domain Controller tại đường dẫn:

```text
C:\Windows\SYSVOL\sysvol\
```

Trong SYSVOL có thể chứa:

* Group Policy Templates;
* script đăng nhập;
* script đăng xuất;
* script khởi động;
* script tắt máy;
* một số tệp chính sách cần phân phối trong domain.

SYSVOL được chia sẻ qua mạng để các máy trong domain có thể truy cập khi đồng bộ Group Policy.

Ví dụ đường dẫn chia sẻ có thể có dạng:

```text
\\company.local\SYSVOL
```

Hoặc:

```text
\\DC01\SYSVOL
```

Nếu SYSVOL gặp lỗi, GPO có thể không được phân phối đúng, dẫn đến máy tính không nhận được chính sách mới.

## 32.10. Phân phối GPO qua SYSVOL

Khi quản trị viên tạo hoặc chỉnh sửa GPO, thông tin chính sách cần được phân phối đến các máy trong domain.

GPO thường gồm hai phần:

| Thành phần             | Ý nghĩa                         |
| ---------------------- | ------------------------------- |
| Group Policy Container | Phần lưu trong Active Directory |
| Group Policy Template  | Phần lưu trong SYSVOL           |

SYSVOL chứa các tệp chính sách mà máy client cần đọc khi cập nhật Group Policy.

Quá trình phân phối GPO cơ bản:

1. Quản trị viên tạo hoặc chỉnh sửa GPO.
2. Dữ liệu GPO được lưu trong Active Directory và SYSVOL.
3. Máy client trong domain định kỳ kiểm tra chính sách mới.
4. Client truy cập Domain Controller và SYSVOL.
5. Client tải thông tin GPO cần thiết.
6. Chính sách được áp dụng cho user hoặc computer.

Thông thường, việc cập nhật GPO có thể mất một khoảng thời gian. Nếu muốn cập nhật ngay trên một máy cụ thể, có thể chạy:

```cmd
gpupdate /force
```

Nếu domain có nhiều Domain Controller, SYSVOL cần được đồng bộ giữa các Domain Controller. Nếu quá trình đồng bộ lỗi, một số máy có thể nhận chính sách khác nhau tùy Domain Controller mà chúng kết nối.

Từ góc độ bảo mật, SYSVOL rất quan trọng vì nó có thể chứa script hoặc tệp cấu hình được phân phối trong domain. Cần kiểm soát quyền truy cập và theo dõi thay đổi bất thường trong SYSVOL.

Một số rủi ro cần chú ý:

* script độc hại bị đưa vào SYSVOL;
* GPO bị chỉnh sửa trái phép;
* SYSVOL không đồng bộ giữa các Domain Controller;
* quyền truy cập SYSVOL bị cấu hình sai;
* thông tin nhạy cảm bị lưu trong script hoặc file cấu hình.

Tóm lại, triển khai chính sách bảo mật bằng GPO giúp doanh nghiệp kiểm soát cấu hình Windows theo cách tập trung. Các chính sách như chặn Control Panel, khóa màn hình tự động và cấu hình bảo mật máy trạm/máy chủ cần được triển khai đúng OU, kiểm tra hiệu lực và giám sát thường xuyên.


# 33. Phương thức xác thực trong Windows Domain

## 33.1. Xác thực trong môi trường domain

Trong môi trường **Windows Domain**, xác thực là quá trình kiểm tra danh tính của người dùng hoặc máy tính trước khi cho phép truy cập vào hệ thống và tài nguyên mạng.

Khi người dùng đăng nhập bằng tài khoản domain, hệ thống cần xác minh rằng:

- username có tồn tại trong domain hay không;
- mật khẩu hoặc thông tin xác thực có đúng không;
- tài khoản có bị khóa hoặc bị vô hiệu hóa không;
- người dùng có được phép đăng nhập không;
- tài khoản có quyền truy cập tài nguyên hay không.

Ví dụ, khi người dùng đăng nhập bằng tài khoản:

```text
COMPANY\user01
```

máy tính sẽ không chỉ kiểm tra tài khoản cục bộ trên máy. Thay vào đó, nó sẽ liên hệ với **Domain Controller** để xác thực tài khoản trong Active Directory.

Trong Windows Domain, hai cơ chế xác thực quan trọng thường gặp là:

* Kerberos;
* NetNTLM.

Trong các hệ thống Windows hiện đại, **Kerberos** là giao thức xác thực mặc định khi máy tính tham gia domain. **NetNTLM** vẫn tồn tại chủ yếu để tương thích với hệ thống cũ hoặc trong các trường hợp Kerberos không thể sử dụng.

## 33.2. Vai trò của Domain Controller trong xác thực

**Domain Controller**, viết tắt là **DC**, là máy chủ chịu trách nhiệm xử lý xác thực trong Windows Domain.

Domain Controller lưu trữ dữ liệu Active Directory và xử lý các yêu cầu liên quan đến:

* đăng nhập domain;
* xác thực người dùng;
* xác thực máy tính;
* cấp ticket trong Kerberos;
* kiểm tra quyền truy cập;
* áp dụng chính sách domain.

Khi người dùng đăng nhập vào máy tính domain, quá trình cơ bản diễn ra như sau:

1. Người dùng nhập username và password.
2. Máy tính gửi yêu cầu xác thực đến Domain Controller.
3. Domain Controller kiểm tra thông tin tài khoản trong Active Directory.
4. Nếu thông tin hợp lệ, người dùng được xác thực.
5. Người dùng có thể truy cập tài nguyên theo quyền được cấp.

Trong Kerberos, Domain Controller còn đóng vai trò là **Key Distribution Center — KDC**. KDC chịu trách nhiệm cấp các loại vé xác thực cho người dùng và dịch vụ.

Nếu Domain Controller không hoạt động hoặc máy client không liên hệ được với DC, người dùng có thể gặp khó khăn khi đăng nhập hoặc truy cập tài nguyên domain.

## 33.3. Kerberos

**Kerberos** là giao thức xác thực mặc định trong môi trường Windows Domain hiện đại.

Kerberos hoạt động dựa trên cơ chế **ticket-based authentication**, tức là xác thực bằng vé. Thay vì gửi mật khẩu trực tiếp qua mạng, Kerberos sử dụng các ticket để chứng minh danh tính của người dùng hoặc máy tính.

Các thành phần quan trọng trong Kerberos gồm:

| Thành phần  | Ý nghĩa                                                     |
| ----------- | ----------------------------------------------------------- |
| KDC         | Key Distribution Center, thường chạy trên Domain Controller |
| AS          | Authentication Service, cấp TGT ban đầu                     |
| TGS         | Ticket Granting Service, cấp ticket truy cập dịch vụ        |
| TGT         | Ticket Granting Ticket, vé dùng để xin ticket dịch vụ       |
| TGS Ticket  | Vé dùng để truy cập một dịch vụ cụ thể                      |
| SPN         | Service Principal Name, định danh dịch vụ trong domain      |
| Session Key | Khóa phiên dùng trong quá trình giao tiếp an toàn           |

Quy trình Kerberos đơn giản có thể hiểu như sau:

1. Người dùng đăng nhập vào domain.
2. Máy client yêu cầu KDC cấp **TGT**.
3. Nếu thông tin hợp lệ, KDC cấp TGT cho người dùng.
4. Khi người dùng muốn truy cập dịch vụ, client dùng TGT để xin **TGS Ticket**.
5. Client gửi TGS Ticket đến dịch vụ cần truy cập.
6. Dịch vụ kiểm tra ticket và cho phép truy cập nếu hợp lệ.

Ưu điểm của Kerberos:

* không gửi mật khẩu trực tiếp qua mạng;
* sử dụng ticket thay cho xác thực lặp lại bằng mật khẩu;
* hỗ trợ xác thực mạnh hơn NetNTLM;
* phù hợp với môi trường domain hiện đại;
* có hiệu suất tốt hơn trong nhiều trường hợp;
* hỗ trợ xác thực giữa người dùng và dịch vụ.

Kerberos là nền tảng quan trọng trong xác thực Active Directory.

## 33.4. NetNTLM

**NetNTLM** là cơ chế xác thực cũ hơn trong Windows, dựa trên mô hình **challenge-response**.

Trong NetNTLM, máy chủ gửi một giá trị thử thách gọi là **challenge** cho client. Client dùng thông tin mật khẩu của người dùng để tính toán phản hồi gọi là **response**, sau đó gửi response về máy chủ để xác thực.

Điểm quan trọng là mật khẩu thực không được gửi trực tiếp qua mạng. Tuy nhiên, NetNTLM vẫn có nhiều hạn chế bảo mật so với Kerberos.

Quy trình NetNTLM đơn giản:

1. Người dùng cố gắng truy cập tài nguyên.
2. Máy chủ gửi challenge cho client.
3. Client tạo response dựa trên challenge và thông tin xác thực.
4. Máy chủ hoặc Domain Controller kiểm tra response.
5. Nếu response hợp lệ, người dùng được xác thực.

NetNTLM thường xuất hiện trong các tình huống:

* hệ thống cũ không hỗ trợ Kerberos;
* máy tính không thuộc domain;
* truy cập tài nguyên bằng địa chỉ IP thay vì hostname;
* cấu hình SPN không đúng;
* không liên hệ được Domain Controller;
* ứng dụng hoặc dịch vụ chỉ hỗ trợ NTLM.

NetNTLM vẫn còn tồn tại để hỗ trợ tương thích ngược, nhưng không nên được ưu tiên trong môi trường doanh nghiệp hiện đại.

## 33.5. So sánh Kerberos và NetNTLM

Kerberos và NetNTLM đều được dùng cho xác thực trong Windows, nhưng cơ chế hoạt động và mức độ bảo mật khác nhau.

| Tiêu chí                                 | Kerberos         | NetNTLM                      |
| ---------------------------------------- | ---------------- | ---------------------------- |
| Cơ chế xác thực                          | Ticket-based     | Challenge-response           |
| Giao thức mặc định trong domain hiện đại | Có               | Không                        |
| Cần Domain Controller                    | Có               | Có với tài khoản domain      |
| Vai trò của DC                           | KDC cấp ticket   | Kiểm tra response            |
| Gửi mật khẩu qua mạng                    | Không            | Không gửi mật khẩu trực tiếp |
| Mức độ bảo mật                           | Cao hơn          | Thấp hơn                     |
| Hỗ trợ môi trường hiện đại               | Tốt              | Chủ yếu để tương thích cũ    |
| Phụ thuộc SPN/DNS                        | Có               | Ít phụ thuộc hơn             |
| Rủi ro relay                             | Thấp hơn         | Cao hơn                      |
| Rủi ro Pass-the-Hash                     | Ít trực tiếp hơn | Đáng chú ý hơn               |

Nói ngắn gọn:

* **Kerberos** phù hợp với môi trường domain hiện đại, an toàn hơn và được dùng mặc định.
* **NetNTLM** là cơ chế cũ hơn, vẫn tồn tại để hỗ trợ các tình huống Kerberos không dùng được.

Trong thiết kế bảo mật doanh nghiệp, nên ưu tiên Kerberos và giảm phụ thuộc vào NetNTLM nếu có thể.

## 33.6. Vì sao Kerberos là giao thức mặc định?

Kerberos là giao thức mặc định trong Windows Domain hiện đại vì nó an toàn và phù hợp hơn cho môi trường doanh nghiệp.

Một số lý do chính:

* không cần gửi mật khẩu trực tiếp qua mạng;
* sử dụng ticket để xác thực;
* hỗ trợ xác thực với dịch vụ trong domain;
* có thể sử dụng cơ chế mã hóa mạnh;
* hiệu quả hơn khi người dùng truy cập nhiều tài nguyên;
* phù hợp với Active Directory;
* giảm một số rủi ro phổ biến của NTLM.

Kerberos cũng hỗ trợ mô hình xác thực tập trung. Người dùng sau khi đăng nhập có thể sử dụng ticket để truy cập nhiều dịch vụ khác nhau mà không cần nhập lại mật khẩu nhiều lần.

Ví dụ, một nhân viên sau khi đăng nhập domain có thể truy cập:

* file server;
* printer server;
* ứng dụng nội bộ;
* database;
* web application nội bộ.

Kerberos giúp quá trình này diễn ra an toàn và thuận tiện hơn.

Từ góc độ bảo mật, Kerberos được ưu tiên vì nó giảm sự phụ thuộc vào cơ chế challenge-response cũ của NTLM và hỗ trợ quản lý xác thực tốt hơn trong Active Directory.

## 33.7. Khi nào Windows sử dụng NetNTLM?

Windows có thể sử dụng NetNTLM khi Kerberos không thể hoạt động.

Một số tình huống thường gặp gồm:

#### Máy tính không thuộc domain

Nếu máy tính không tham gia Active Directory domain, nó không thể sử dụng Kerberos với KDC của domain theo cách thông thường.

Trong trường hợp đó, Windows có thể dùng NTLM cho xác thực.

#### Dịch vụ hoặc ứng dụng cũ không hỗ trợ Kerberos

Một số ứng dụng hoặc dịch vụ cũ chỉ hỗ trợ NTLM. Khi đó, Windows có thể phải dùng NetNTLM để duy trì khả năng tương thích.

#### Truy cập bằng địa chỉ IP thay vì hostname

Kerberos cần xác định dịch vụ thông qua **SPN — Service Principal Name**. Nếu người dùng truy cập máy chủ bằng địa chỉ IP, Kerberos có thể không xác định đúng SPN.

Ví dụ:

```text
\\192.168.1.10\Share
```

Trong trường hợp này, Windows có thể fallback sang NTLM.

Thay vào đó, nên truy cập bằng hostname hoặc FQDN:

```text
\\fileserver.company.local\Share
```

#### SPN bị thiếu hoặc cấu hình sai

Nếu dịch vụ không có SPN đúng, Kerberos có thể thất bại. Khi đó, hệ thống có thể chuyển sang NTLM.

#### Không liên hệ được Domain Controller

Kerberos cần liên hệ với Domain Controller để lấy ticket. Nếu client không liên hệ được DC, ví dụ do lỗi mạng hoặc không kết nối VPN, Kerberos có thể không hoạt động.

#### Môi trường legacy

Trong môi trường còn nhiều hệ thống cũ, NTLM có thể vẫn được sử dụng để đảm bảo ứng dụng hoặc máy chủ cũ tiếp tục hoạt động.

Tóm lại, NetNTLM thường được dùng như cơ chế dự phòng hoặc tương thích ngược, không phải lựa chọn ưu tiên trong domain hiện đại.

## 33.8. Rủi ro bảo mật của NetNTLM

NetNTLM có nhiều rủi ro bảo mật hơn Kerberos, vì vậy trong môi trường hiện đại cần hạn chế sử dụng nếu có thể.

Một số rủi ro quan trọng gồm:

#### Pass-the-Hash

**Pass-the-Hash** là kỹ thuật trong đó kẻ tấn công sử dụng NTLM hash để xác thực mà không cần biết mật khẩu thật.

Nếu kẻ tấn công đánh cắp được hash của tài khoản, họ có thể dùng hash đó để truy cập hệ thống trong một số điều kiện nhất định.

Rủi ro này đặc biệt nghiêm trọng nếu hash thuộc về tài khoản có quyền cao như:

* Domain Admin;
* local Administrator;
* service account có quyền rộng;
* tài khoản quản trị máy chủ.

#### NTLM Relay

**NTLM Relay** là kỹ thuật trong đó kẻ tấn công chặn hoặc chuyển tiếp quá trình xác thực NTLM đến một dịch vụ khác.

Nếu hệ thống không có biện pháp bảo vệ bổ sung như SMB Signing hoặc các cấu hình chống relay phù hợp, kẻ tấn công có thể lợi dụng xác thực NTLM để truy cập trái phép tài nguyên.

#### Không mạnh bằng Kerberos

NetNTLM là cơ chế cũ hơn, chủ yếu được giữ lại để tương thích. Nó không cung cấp mô hình ticket-based mạnh như Kerberos và khó kiểm soát hơn trong môi trường lớn.

#### Dễ bị lạm dụng trong nội bộ

Trong mạng nội bộ doanh nghiệp, nếu kẻ tấn công đã có vị trí trong mạng, họ có thể cố gắng ép máy nạn nhân thực hiện xác thực NTLM để thu thập hoặc relay thông tin xác thực.

#### Khó loại bỏ hoàn toàn

Một vấn đề thực tế là nhiều doanh nghiệp vẫn còn hệ thống cũ phụ thuộc vào NTLM. Nếu tắt NTLM ngay lập tức, một số ứng dụng hoặc dịch vụ có thể bị lỗi.

Vì vậy, cách tiếp cận an toàn hơn là:

* giám sát việc sử dụng NTLM;
* xác định hệ thống nào còn phụ thuộc NTLM;
* giảm dần NTLM theo kế hoạch;
* sửa cấu hình SPN để ưu tiên Kerberos;
* tránh truy cập dịch vụ bằng địa chỉ IP;
* bật SMB Signing nếu phù hợp;
* hạn chế tài khoản quyền cao đăng nhập vào máy trạm;
* giám sát sự kiện xác thực bất thường.

Từ góc độ SOC, cần chú ý các dấu hiệu như:

* nhiều sự kiện xác thực NTLM bất thường;
* tài khoản quyền cao dùng NTLM;
* xác thực NTLM đến máy chủ lạ;
* dấu hiệu NTLM Relay;
* truy cập SMB bất thường;
* nhiều thất bại xác thực trong thời gian ngắn.

Tóm lại, Kerberos là giao thức xác thực chính và an toàn hơn trong Windows Domain hiện đại. NetNTLM vẫn tồn tại để tương thích, nhưng cần được giám sát và hạn chế vì có nhiều rủi ro như Pass-the-Hash và NTLM Relay.

# 34. Kerberos Authentication

## 34.1. Kerberos là gì?

**Kerberos** là giao thức xác thực mặc định trong các môi trường Windows Domain hiện đại.

Kerberos sử dụng cơ chế **ticket-based authentication**, nghĩa là xác thực dựa trên vé. Thay vì gửi mật khẩu trực tiếp qua mạng mỗi khi người dùng truy cập dịch vụ, Kerberos cấp cho người dùng các vé xác thực để chứng minh rằng họ đã được xác thực trước đó.

Trong môi trường Active Directory, Kerberos giúp người dùng truy cập nhiều tài nguyên khác nhau như:

- file server;
- printer server;
- web server nội bộ;
- database;
- ứng dụng doanh nghiệp;
- tài nguyên chia sẻ trong domain.

Ví dụ, sau khi người dùng đăng nhập vào domain, họ có thể truy cập thư mục chia sẻ mà không cần nhập lại mật khẩu nhiều lần. Kerberos sử dụng ticket để chứng minh danh tính của người dùng với dịch vụ đó.

Kerberos quan trọng vì nó giúp xác thực an toàn hơn so với cơ chế cũ như NetNTLM.


## 34.2. Key Distribution Center — KDC

**KDC** là viết tắt của **Key Distribution Center**. Đây là thành phần trung tâm trong Kerberos, thường chạy trên **Domain Controller** trong môi trường Active Directory.

KDC chịu trách nhiệm cấp các loại vé Kerberos cho người dùng và dịch vụ.

KDC gồm hai thành phần chính:

| Thành phần | Vai trò |
|---|---|
| Authentication Service — AS | Xác thực ban đầu và cấp TGT |
| Ticket Granting Service — TGS | Cấp ticket để truy cập dịch vụ cụ thể |

Khi người dùng đăng nhập vào domain, máy client sẽ liên hệ với KDC để xin vé xác thực ban đầu. Nếu thông tin đăng nhập hợp lệ, KDC sẽ cấp **Ticket Granting Ticket — TGT**.

KDC rất quan trọng vì nếu không có KDC, Kerberos không thể cấp ticket và người dùng sẽ không thể xác thực bình thường trong domain.


## 34.3. Ticket Granting Ticket — TGT

**TGT** là viết tắt của **Ticket Granting Ticket**. Đây là vé ban đầu mà người dùng nhận được sau khi xác thực thành công với KDC.

TGT không dùng trực tiếp để truy cập dịch vụ cuối cùng. Thay vào đó, nó được dùng để xin các vé khác gọi là **TGS Ticket** khi người dùng muốn truy cập một dịch vụ cụ thể.

Có thể hiểu đơn giản:

- TGT chứng minh rằng người dùng đã đăng nhập hợp lệ vào domain;
- TGT được dùng để xin vé truy cập dịch vụ;
- người dùng không cần gửi lại mật khẩu mỗi lần muốn truy cập tài nguyên.

Ví dụ, sau khi người dùng đăng nhập thành công, họ nhận được TGT. Khi muốn truy cập file server, người dùng dùng TGT để xin ticket truy cập file server.

TGT được mã hóa và người dùng không thể tự ý đọc hoặc chỉnh sửa nội dung bên trong nó.


## 34.4. Ticket Granting Service — TGS

**TGS** là viết tắt của **Ticket Granting Service**. Đây là thành phần của KDC chịu trách nhiệm cấp ticket cho từng dịch vụ cụ thể.

Khi người dùng muốn truy cập một dịch vụ, ví dụ thư mục chia sẻ trên file server, client sẽ gửi TGT đến TGS để yêu cầu một ticket truy cập dịch vụ đó.

Ticket được cấp cho dịch vụ cụ thể thường gọi là:

```text
TGS Ticket
````

Ví dụ:

```text
Người dùng muốn truy cập \\FILE-SERVER\Share
→ Client dùng TGT để xin TGS Ticket
→ TGS cấp ticket cho dịch vụ file sharing trên FILE-SERVER
```

TGS Ticket chỉ hợp lệ cho dịch vụ mà nó được cấp. Điều này giúp giới hạn phạm vi sử dụng của ticket và tăng tính bảo mật.

Nếu người dùng muốn truy cập một dịch vụ khác, họ cần xin một TGS Ticket khác.

## 34.5. Session Key

**Session Key** là khóa phiên được sử dụng trong quá trình xác thực Kerberos.

Khi KDC cấp TGT cho người dùng, nó cũng cung cấp một Session Key. Khóa này được dùng để tạo và bảo vệ các yêu cầu tiếp theo khi người dùng muốn xin ticket truy cập dịch vụ.

Vai trò của Session Key:

* giúp client giao tiếp an toàn với KDC;
* dùng để mã hóa timestamp hoặc thông tin xác thực;
* chứng minh rằng client đang giữ thông tin hợp lệ;
* tránh việc phải gửi lại mật khẩu nhiều lần;
* hỗ trợ quá trình xin TGS Ticket.

Session Key chỉ có giá trị trong một phiên nhất định. Điều này giúp giảm rủi ro nếu thông tin xác thực cũ bị lộ.

Trong Kerberos, việc sử dụng Session Key giúp quá trình xác thực an toàn hơn và giảm việc truyền thông tin nhạy cảm qua mạng.

## 34.6. Service Principal Name — SPN

**SPN** là viết tắt của **Service Principal Name**. Đây là tên định danh duy nhất của một dịch vụ trong môi trường Active Directory.

SPN cho Kerberos biết người dùng muốn truy cập dịch vụ nào và trên máy chủ nào.

Một SPN thường có dạng:

```text
service/hostname
```

Ví dụ:

```text
HTTP/webserver.company.local
MSSQLSvc/sqlserver.company.local
CIFS/fileserver.company.local
```

Trong đó:

| Thành phần | Ý nghĩa                      |
| ---------- | ---------------------------- |
| `HTTP`     | Dịch vụ web                  |
| `MSSQLSvc` | Dịch vụ Microsoft SQL Server |
| `CIFS`     | Dịch vụ chia sẻ file SMB     |
| `hostname` | Tên máy chủ cung cấp dịch vụ |

SPN rất quan trọng vì Kerberos cần SPN để cấp đúng ticket cho đúng dịch vụ.

Nếu SPN bị thiếu hoặc cấu hình sai, Kerberos có thể không hoạt động và Windows có thể fallback sang NetNTLM. Đây là lý do trong môi trường doanh nghiệp, cấu hình SPN cần được quản lý cẩn thận.

## 34.7. Service Session Key

**Service Session Key** là khóa phiên được sử dụng giữa client và dịch vụ mà người dùng muốn truy cập.

Khi KDC cấp TGS Ticket cho một dịch vụ cụ thể, nó cũng tạo ra Service Session Key. Khóa này giúp client và service giao tiếp an toàn trong phiên làm việc đó.

Vai trò của Service Session Key:

* xác thực client với service;
* hỗ trợ bảo vệ phiên giao tiếp;
* giúp service xác minh ticket hợp lệ;
* giảm nhu cầu sử dụng mật khẩu trong quá trình truy cập dịch vụ;
* đảm bảo ticket chỉ dùng được trong phạm vi dịch vụ cụ thể.

Ví dụ, khi người dùng truy cập file server, Kerberos cấp ticket và Service Session Key cho phiên làm việc giữa client và file server.

Điều này giúp quá trình truy cập tài nguyên diễn ra an toàn hơn mà không cần gửi mật khẩu của người dùng đến file server.

## 34.8. Quy trình xác thực Kerberos

Quy trình Kerberos có thể chia thành ba giai đoạn chính:

1. Người dùng đăng nhập và xin TGT.
2. Người dùng dùng TGT để xin ticket truy cập dịch vụ.
3. Người dùng dùng ticket để truy cập dịch vụ.

Quy trình chi tiết:

#### Bước 1: Người dùng đăng nhập vào domain

Người dùng nhập username và password trên máy tính domain.

Client sẽ tạo yêu cầu xác thực gửi đến KDC. Yêu cầu này có thể bao gồm username và timestamp được mã hóa bằng khóa dẫn xuất từ mật khẩu người dùng.

```text
Client → KDC: Yêu cầu xác thực ban đầu
```

Nếu KDC xác minh thành công, nó cấp cho client:

* TGT;
* Session Key.

#### Bước 2: Client nhận TGT

TGT chứng minh rằng người dùng đã được xác thực với domain.

Client lưu TGT để sử dụng trong các yêu cầu tiếp theo. Người dùng không cần gửi lại mật khẩu mỗi khi truy cập dịch vụ khác.

```text
KDC → Client: TGT + Session Key
```

#### Bước 3: Người dùng yêu cầu truy cập dịch vụ

Khi người dùng muốn truy cập một dịch vụ, ví dụ file server, client sẽ gửi yêu cầu đến TGS.

Yêu cầu này gồm:

* TGT;
* username;
* timestamp được mã hóa bằng Session Key;
* SPN của dịch vụ cần truy cập.

```text
Client → TGS: TGT + SPN
```

#### Bước 4: TGS cấp ticket cho dịch vụ

Nếu yêu cầu hợp lệ, TGS cấp một TGS Ticket cho dịch vụ cụ thể.

Ticket này chỉ dùng để truy cập dịch vụ đã được yêu cầu.

```text
TGS → Client: TGS Ticket + Service Session Key
```

#### Bước 5: Client truy cập dịch vụ

Client gửi TGS Ticket đến dịch vụ, ví dụ file server.

```text
Client → Service: TGS Ticket
```

Dịch vụ kiểm tra ticket. Nếu ticket hợp lệ, người dùng được phép truy cập tài nguyên theo quyền được cấp.

Tóm tắt quy trình:

```text
User login
→ Client xin TGT từ KDC
→ Client dùng TGT để xin TGS Ticket
→ Client gửi TGS Ticket đến dịch vụ
→ Dịch vụ xác thực và cho phép truy cập
```

## 34.9. Ưu điểm bảo mật của Kerberos

Kerberos có nhiều ưu điểm bảo mật so với các cơ chế xác thực cũ.

Một số ưu điểm chính gồm:

| Ưu điểm                               | Ý nghĩa                                                     |
| ------------------------------------- | ----------------------------------------------------------- |
| Không gửi mật khẩu trực tiếp qua mạng | Giảm nguy cơ mật khẩu bị nghe lén                           |
| Dùng ticket để xác thực               | Người dùng không phải gửi lại thông tin đăng nhập nhiều lần |
| Có thời hạn ticket                    | Ticket chỉ hợp lệ trong khoảng thời gian nhất định          |
| Xác thực tập trung                    | Domain Controller/KDC quản lý quá trình cấp ticket          |
| Hỗ trợ dịch vụ trong domain           | Phù hợp với môi trường doanh nghiệp có nhiều tài nguyên     |
| An toàn hơn NetNTLM                   | Giảm một số rủi ro của cơ chế challenge-response cũ         |
| Hỗ trợ quản lý truy cập tốt hơn       | Kết hợp với AD, group và GPO để kiểm soát quyền             |

Kerberos giúp giảm rủi ro vì mật khẩu không được gửi trực tiếp đến từng dịch vụ. Thay vào đó, người dùng dùng ticket để chứng minh rằng họ đã được xác thực.

Trong môi trường doanh nghiệp, Kerberos giúp người dùng truy cập tài nguyên thuận tiện nhưng vẫn đảm bảo kiểm soát bảo mật.

Tuy nhiên, Kerberos vẫn cần được cấu hình và giám sát đúng cách. Một số vấn đề cần chú ý gồm:

* thời gian hệ thống giữa client và Domain Controller phải đồng bộ;
* SPN phải được cấu hình đúng;
* tài khoản dịch vụ cần được bảo vệ;
* Domain Controller cần được giám sát chặt chẽ;
* tài khoản có quyền cao không nên bị lộ thông tin xác thực.

Từ góc độ SOC, Kerberos là nguồn dữ liệu quan trọng để phân tích xác thực trong domain. Các log liên quan đến TGT, TGS, lỗi xác thực và truy cập dịch vụ có thể giúp phát hiện hành vi bất thường.

Tóm lại, Kerberos là giao thức xác thực chính trong Windows Domain hiện đại. Nó sử dụng ticket, KDC, TGT, TGS, Session Key và SPN để xác thực người dùng với dịch vụ một cách an toàn và hiệu quả.


# 35. NetNTLM Authentication

## 35.1. NetNTLM là gì?

**NetNTLM** là cơ chế xác thực cũ trong Windows, được sử dụng khi Kerberos không thể hoạt động hoặc khi hệ thống cần tương thích với các dịch vụ cũ.

NetNTLM thường được gọi chung là **NTLM authentication** trong môi trường Windows. Đây là cơ chế xác thực dựa trên mô hình **Challenge-Response**, nghĩa là máy chủ gửi một giá trị thử thách cho client, sau đó client tạo phản hồi để chứng minh danh tính.

NetNTLM có thể xuất hiện trong các trường hợp như:

- máy tính không thuộc domain;
- dịch vụ không hỗ trợ Kerberos;
- truy cập tài nguyên bằng địa chỉ IP thay vì hostname;
- SPN bị thiếu hoặc cấu hình sai;
- không liên hệ được Domain Controller;
- hệ thống legacy vẫn cần NTLM.

Trong các domain Windows hiện đại, Kerberos là giao thức mặc định. NetNTLM chủ yếu được giữ lại để đảm bảo khả năng tương thích ngược.


## 35.2. Cơ chế Challenge-Response

NetNTLM sử dụng cơ chế **Challenge-Response** để xác thực người dùng mà không gửi mật khẩu dạng rõ qua mạng.

Quy trình này có thể hiểu đơn giản như sau:

1. Client yêu cầu truy cập tài nguyên.
2. Server gửi một chuỗi ngẫu nhiên gọi là **challenge**.
3. Client dùng thông tin liên quan đến mật khẩu để tính toán **response**.
4. Response được gửi lại cho server.
5. Server hoặc Domain Controller kiểm tra response.
6. Nếu response đúng, người dùng được xác thực.

Điểm quan trọng là client không gửi mật khẩu thật qua mạng. Thay vào đó, nó gửi một giá trị phản hồi được tạo từ challenge và thông tin xác thực của người dùng.

Tuy nhiên, dù không gửi mật khẩu trực tiếp, NetNTLM vẫn có nhiều rủi ro bảo mật, đặc biệt là Pass-the-Hash và NTLM Relay.


## 35.3. Client gửi yêu cầu xác thực

Quá trình NetNTLM bắt đầu khi client muốn truy cập một tài nguyên trên mạng.

Ví dụ, người dùng truy cập thư mục chia sẻ:

```text
\\FILE-SERVER\Share
```

Client sẽ gửi yêu cầu xác thực đến server để chứng minh rằng người dùng có quyền truy cập.

Yêu cầu này có thể xuất hiện khi người dùng:

* truy cập file share;
* kết nối đến máy chủ nội bộ;
* truy cập ứng dụng cũ;
* kết nối SMB;
* dùng tài khoản domain để truy cập tài nguyên;
* truy cập tài nguyên bằng địa chỉ IP.

Ví dụ:

```text
Client → Server: Tôi muốn truy cập tài nguyên này
```

Server chưa tin tưởng client ngay lập tức. Nó sẽ yêu cầu client chứng minh danh tính bằng cách gửi challenge.

## 35.4. Server tạo Challenge

Sau khi nhận yêu cầu từ client, server tạo một giá trị ngẫu nhiên gọi là **challenge**.

Challenge là một chuỗi dữ liệu được server gửi về cho client. Client phải dùng challenge này để tạo response.

Ví dụ đơn giản:

```text
Server → Client: Đây là challenge, hãy chứng minh danh tính của bạn
```

Challenge có vai trò quan trọng vì nó giúp tránh việc client chỉ gửi lại một giá trị cố định. Mỗi lần xác thực, challenge có thể khác nhau, nên response cũng khác nhau.

Tuy nhiên, nếu quá trình này bị kẻ tấn công chặn và chuyển tiếp sang dịch vụ khác, nó có thể bị lợi dụng trong tấn công **NTLM Relay**.

## 35.5. Client tạo Response

Sau khi nhận challenge từ server, client sẽ tạo **response**.

Response được tính toán dựa trên:

* challenge từ server;
* thông tin liên quan đến mật khẩu của người dùng;
* NTLM hash;
* một số thông tin phiên xác thực.

Client không gửi mật khẩu thật. Nó chỉ gửi response được tạo ra từ quá trình tính toán.

Ví dụ:

```text
Client → Server: Đây là response của tôi
```

Response chứng minh rằng client có thông tin xác thực hợp lệ mà không cần truyền mật khẩu dưới dạng rõ.

Tuy nhiên, vì NTLM hash có thể được dùng để tạo response, nếu kẻ tấn công đánh cắp được hash, họ có thể lạm dụng nó trong một số kiểu tấn công.

## 35.6. Domain Controller xác minh Response

Nếu tài khoản được dùng là tài khoản domain, server thường cần Domain Controller để xác minh response.

Quy trình có thể hiểu như sau:

1. Server nhận response từ client.
2. Server gửi thông tin xác thực đến Domain Controller.
3. Domain Controller kiểm tra response dựa trên dữ liệu tài khoản trong Active Directory.
4. Nếu response hợp lệ, Domain Controller xác nhận người dùng.
5. Server cho phép hoặc từ chối truy cập tài nguyên.

Ví dụ:

```text
Server → Domain Controller: Response này có hợp lệ không?
Domain Controller → Server: Hợp lệ hoặc không hợp lệ
```

Nếu response hợp lệ, người dùng được xác thực. Tuy nhiên, việc được xác thực không có nghĩa là người dùng tự động có quyền truy cập mọi tài nguyên. Sau xác thực, hệ thống vẫn cần kiểm tra quyền truy cập.

## 35.7. Mật khẩu có được truyền qua mạng không?

Trong NetNTLM, **mật khẩu thật không được truyền qua mạng**.

Client không gửi mật khẩu dạng rõ cho server hoặc Domain Controller. Thay vào đó, client gửi response được tạo từ challenge và thông tin xác thực.

Điều này giúp tránh việc mật khẩu bị lộ trực tiếp trên đường truyền.

Tuy nhiên, cần hiểu rõ rằng:

* mật khẩu không được gửi trực tiếp;
* NTLM hash cũng không nhất thiết được gửi trực tiếp trong quá trình thông thường;
* response vẫn có thể bị chặn hoặc lạm dụng;
* nếu hash bị đánh cắp từ máy, kẻ tấn công có thể dùng cho Pass-the-Hash;
* nếu challenge-response bị chuyển tiếp, có thể xảy ra NTLM Relay.

Vì vậy, việc không truyền mật khẩu trực tiếp không có nghĩa là NetNTLM hoàn toàn an toàn.

## 35.8. Pass-the-Hash

**Pass-the-Hash** là kỹ thuật tấn công trong đó kẻ tấn công sử dụng NTLM hash để xác thực mà không cần biết mật khẩu thật.

Thông thường, khi người dùng đăng nhập, Windows có thể lưu thông tin xác thực dưới dạng hash trong bộ nhớ hoặc hệ thống. Nếu kẻ tấn công có quyền truy cập vào máy, họ có thể cố gắng trích xuất hash này.

Sau đó, thay vì bẻ khóa hash để tìm mật khẩu gốc, kẻ tấn công có thể dùng trực tiếp hash để xác thực đến hệ thống khác.

Ví dụ nguy hiểm:

* kẻ tấn công lấy được hash của local Administrator;
* nhiều máy dùng cùng mật khẩu local admin;
* kẻ tấn công dùng hash đó để truy cập các máy khác;
* phạm vi kiểm soát bị mở rộng trong mạng nội bộ.

Pass-the-Hash đặc biệt nguy hiểm khi hash thuộc về tài khoản có quyền cao như:

* Domain Admin;
* local Administrator;
* service account;
* tài khoản quản trị máy chủ.

Biện pháp giảm rủi ro:

* không dùng chung mật khẩu local Administrator trên nhiều máy;
* hạn chế đăng nhập tài khoản quyền cao vào máy trạm;
* sử dụng nguyên tắc least privilege;
* bật Credential Guard nếu phù hợp;
* giám sát đăng nhập bất thường;
* quản lý tài khoản quản trị cục bộ bằng giải pháp phù hợp;
* giảm phụ thuộc vào NTLM nếu có thể.

## 35.9. NTLM Relay

**NTLM Relay** là kỹ thuật tấn công trong đó kẻ tấn công chặn hoặc chuyển tiếp quá trình xác thực NTLM đến một dịch vụ khác.

Trong tấn công này, kẻ tấn công không cần biết mật khẩu thật. Họ lợi dụng quá trình challenge-response để chuyển tiếp thông tin xác thực từ nạn nhân sang một máy chủ khác.

Mô hình đơn giản:

```text
Victim → Attacker → Target Server
```

Quy trình có thể hiểu như sau:

1. Nạn nhân bị dụ xác thực đến máy của attacker.
2. Attacker chuyển tiếp yêu cầu xác thực đến target server.
3. Target server gửi challenge.
4. Attacker chuyển challenge về victim.
5. Victim tạo response hợp lệ.
6. Attacker chuyển response đến target server.
7. Target server xác thực attacker như thể đó là victim.

NTLM Relay nguy hiểm vì attacker có thể truy cập tài nguyên mà không cần biết mật khẩu của nạn nhân.

Rủi ro này tăng lên nếu hệ thống thiếu các cơ chế bảo vệ như:

* SMB Signing;
* LDAP Signing;
* Extended Protection for Authentication;
* cấu hình hạn chế NTLM;
* phân tách quyền phù hợp;
* giám sát xác thực bất thường.

Từ góc độ SOC, cần chú ý các dấu hiệu như:

* xác thực NTLM đến máy chủ lạ;
* nhiều kết nối SMB bất thường;
* tài khoản quyền cao xác thực bằng NTLM;
* sự kiện NTLM bất thường trong Event Viewer;
* truy cập tài nguyên từ máy không thường dùng.

## 35.10. Vì sao NetNTLM bị xem là lỗi thời?

NetNTLM bị xem là lỗi thời vì nó là cơ chế xác thực cũ và có nhiều hạn chế bảo mật so với Kerberos.

Một số lý do chính:

| Lý do                        | Giải thích                                          |
| ---------------------------- | --------------------------------------------------- |
| Cơ chế cũ                    | NetNTLM được thiết kế cho môi trường Windows cũ hơn |
| Bảo mật thấp hơn Kerberos    | Không dùng mô hình ticket-based mạnh như Kerberos   |
| Dễ bị relay                  | Có nguy cơ NTLM Relay nếu thiếu cấu hình bảo vệ     |
| Rủi ro Pass-the-Hash         | NTLM hash có thể bị lạm dụng nếu bị đánh cắp        |
| Khó kiểm soát trong mạng lớn | NTLM có thể xuất hiện ở nhiều dịch vụ legacy        |
| Chủ yếu để tương thích       | Vẫn tồn tại vì một số hệ thống cũ cần dùng          |

Trong môi trường hiện đại, nên ưu tiên Kerberos vì:

* an toàn hơn;
* phù hợp với Active Directory;
* sử dụng ticket;
* giảm nhu cầu xác thực lại bằng mật khẩu;
* hỗ trợ tốt hơn cho quản trị domain;
* ít phụ thuộc vào challenge-response kiểu cũ.

Tuy nhiên, việc tắt NetNTLM hoàn toàn cần được thực hiện cẩn thận. Một số ứng dụng cũ hoặc dịch vụ legacy có thể vẫn phụ thuộc vào NTLM. Nếu tắt đột ngột, hệ thống có thể bị lỗi xác thực.

Cách tiếp cận an toàn hơn là:

1. Giám sát việc sử dụng NTLM.
2. Xác định hệ thống nào còn dùng NTLM.
3. Sửa lỗi SPN hoặc DNS để Kerberos hoạt động.
4. Thay thế hoặc nâng cấp ứng dụng legacy.
5. Bật các cơ chế bảo vệ như SMB Signing nếu phù hợp.
6. Giảm dần NTLM theo kế hoạch.
7. Chỉ tắt NTLM khi đã kiểm tra đầy đủ.

Tóm lại, NetNTLM vẫn có thể xuất hiện trong Windows Domain, nhưng không nên được xem là cơ chế xác thực ưu tiên. Trong môi trường doanh nghiệp hiện đại, cần ưu tiên Kerberos, giám sát NTLM và giảm dần sự phụ thuộc vào NetNTLM để giảm rủi ro bảo mật.


# 36. Trees, Forests và Trusts

## 36.1. Tree trong Active Directory là gì?

**Tree** trong Active Directory là một nhóm các Windows Domain có chung một không gian tên liên tục.

Nói đơn giản, tree là một cấu trúc gồm nhiều miền có quan hệ cha — con với nhau và cùng thuộc một namespace.

Ví dụ:

```text
company.local
├── sales.company.local
├── it.company.local
└── hr.company.local
````

Trong ví dụ trên:

* `company.local` là domain gốc;
* `sales.company.local` là child domain;
* `it.company.local` là child domain;
* `hr.company.local` là child domain.

Tất cả các domain này cùng chia sẻ namespace `company.local`, vì vậy chúng thuộc cùng một tree.

Tree giúp doanh nghiệp tổ chức domain theo cấu trúc logic, ví dụ theo phòng ban, khu vực địa lý hoặc đơn vị quản lý.

### 36.2. Child Domain

**Child Domain** là miền con nằm dưới một domain cha trong Active Directory tree.

Ví dụ:

```text
company.local
└── sales.company.local
```

Trong đó:

* `company.local` là parent domain;
* `sales.company.local` là child domain.

Child Domain thường được dùng khi doanh nghiệp muốn tách biệt quản trị hoặc tài nguyên nhưng vẫn giữ cùng một namespace.

Ví dụ, một công ty có thể tạo child domain theo khu vực:

```text
company.local
├── eu.company.local
├── asia.company.local
└── us.company.local
```

Mỗi child domain có thể có:

* người dùng riêng;
* máy tính riêng;
* nhóm riêng;
* chính sách riêng;
* Domain Controllers riêng;
* đội ngũ IT quản lý riêng.

Tuy nhiên, các child domain vẫn thuộc cùng một tree và có quan hệ tin cậy với các domain khác trong tree.

## 36.3. Namespace trong Active Directory

**Namespace** là không gian tên dùng để tổ chức và định danh các domain trong Active Directory.

Trong một tree, các domain chia sẻ cùng một namespace liên tục.

Ví dụ:

```text
company.local
sales.company.local
it.company.local
hr.company.local
```

Các domain trên cùng thuộc namespace `company.local`.

Namespace giúp xác định vị trí logic của domain trong cấu trúc Active Directory. Nó cũng giúp người quản trị hiểu domain nào là domain cha, domain nào là domain con.

Ví dụ:

```text
asia.company.local
```

Tên này cho thấy domain `asia` nằm dưới domain `company.local`.

Nếu các domain không chia sẻ cùng namespace, chúng không nằm trong cùng một tree, nhưng vẫn có thể thuộc cùng một forest.

## 36.4. Forest trong Active Directory là gì?

**Forest** là cấu trúc cấp cao nhất trong Active Directory.

Một forest có thể chứa một hoặc nhiều tree. Các tree trong cùng một forest có thể có namespace khác nhau.

Ví dụ:

```text
company.local
```

và:

```text
mht.local
```

là hai namespace khác nhau. Nếu cả hai cùng nằm trong một môi trường quản lý Active Directory lớn hơn, chúng có thể thuộc cùng một forest.

Có thể hiểu đơn giản:

* **Tree** là nhóm các domain chia sẻ cùng namespace;
* **Forest** là tập hợp một hoặc nhiều tree;
* Forest là ranh giới quản trị và bảo mật lớn nhất trong Active Directory.

Forest giúp doanh nghiệp quản lý nhiều hệ thống domain khác nhau trong cùng một môi trường tổng thể.

Ví dụ, khi một công ty mua lại công ty khác, mỗi công ty có thể có tree riêng. Nếu cần tích hợp quản lý, các tree này có thể được đặt trong cùng một forest hoặc thiết lập trust giữa các forest.

## 36.5. Nhiều cây miền trong một forest

Một forest có thể chứa nhiều tree với các namespace khác nhau.

Ví dụ:

```text
Forest
├── company.local
│   ├── sales.company.local
│   └── it.company.local
└── mht.local
    ├── asia.mht.local
    └── eu.mht.local
```

Trong ví dụ này:

* `company.local` là một tree;
* `mht.local` là một tree khác;
* cả hai tree cùng nằm trong một forest.

Mô hình này phù hợp khi doanh nghiệp có nhiều đơn vị, công ty con hoặc hệ thống tên miền khác nhau.

Một forest nhiều tree có thể xuất hiện trong các tình huống:

* công ty sáp nhập với công ty khác;
* tập đoàn có nhiều thương hiệu riêng;
* các đơn vị có namespace khác nhau;
* mỗi khu vực địa lý có domain riêng;
* hệ thống cần phân tách quản trị nhưng vẫn duy trì liên kết.

Việc có nhiều tree trong một forest giúp tổ chức linh hoạt hơn, nhưng cũng làm tăng độ phức tạp trong quản trị và bảo mật.

## 36.6. Enterprise Admins

**Enterprise Admins** là nhóm quản trị cấp forest trong Active Directory.

Thành viên của nhóm này có quyền quản trị trên toàn bộ forest, không chỉ trong một domain riêng lẻ.

Enterprise Admins có thể thực hiện các tác vụ như:

* quản lý cấu trúc forest;
* thêm hoặc quản lý domain trong forest;
* quản trị nhiều domain;
* cấu hình trust ở cấp forest;
* thực hiện thay đổi ảnh hưởng đến toàn forest;
* quản lý các thiết lập cấp cao trong Active Directory.

Enterprise Admins là nhóm cực kỳ nhạy cảm. Nếu tài khoản thuộc nhóm này bị chiếm quyền, kẻ tấn công có thể ảnh hưởng đến toàn bộ forest.

Vì vậy, nhóm Enterprise Admins cần được kiểm soát rất chặt chẽ:

* chỉ thêm tài khoản thật sự cần thiết;
* không dùng cho công việc hằng ngày;
* giám sát mọi lần đăng nhập;
* giám sát thay đổi thành viên nhóm;
* dùng tài khoản quản trị riêng;
* áp dụng nguyên tắc least privilege;
* hạn chế đăng nhập vào máy trạm thông thường.

## 36.7. Domain Admins và Enterprise Admins

**Domain Admins** và **Enterprise Admins** đều là nhóm quyền cao trong Active Directory, nhưng phạm vi quyền khác nhau.

| Nhóm              | Phạm vi quyền           | Ý nghĩa                               |
| ----------------- | ----------------------- | ------------------------------------- |
| Domain Admins     | Trong một domain cụ thể | Quản trị toàn bộ domain đó            |
| Enterprise Admins | Toàn bộ forest          | Quản trị ở cấp forest và nhiều domain |

Ví dụ:

```text
Forest
├── company.local
└── mht.local
```

Nếu một tài khoản là **Domain Admin** trong `company.local`, tài khoản đó có quyền quản trị trong domain `company.local`, nhưng không nhất thiết có quyền quản trị trong `mht.local`.

Nếu một tài khoản là **Enterprise Admin**, tài khoản đó có quyền ở cấp forest và có thể ảnh hưởng đến nhiều domain trong forest.

So sánh đơn giản:

* **Domain Admins**: quyền cao trong một domain.
* **Enterprise Admins**: quyền cao hơn, phạm vi toàn forest.

Khuyến nghị bảo mật:

* hạn chế số lượng Domain Admins;
* hạn chế nghiêm ngặt Enterprise Admins;
* không dùng các tài khoản này cho công việc hằng ngày;
* không đăng nhập vào máy trạm thông thường;
* giám sát mọi thay đổi nhóm;
* sử dụng tài khoản quản trị tách biệt;
* kiểm tra định kỳ thành viên nhóm quyền cao.

## 36.8. Trust Relationship là gì?

**Trust Relationship** là mối quan hệ tin cậy giữa các domain hoặc forest trong Active Directory.

Trust cho phép một domain tin tưởng thông tin xác thực từ domain khác, từ đó có thể ủy quyền cho người dùng ở domain này truy cập tài nguyên ở domain kia.

Ví dụ:

```text
Domain A: company.local
Domain B: mht.local
```

Nếu có trust relationship giữa hai domain, người dùng từ `company.local` có thể được cấp quyền truy cập tài nguyên trong `mht.local`, nếu quản trị viên cấu hình quyền phù hợp.

Trust Relationship thường được dùng khi:

* có nhiều domain trong một tổ chức;
* công ty sáp nhập hoặc mua lại công ty khác;
* cần chia sẻ tài nguyên giữa các đơn vị;
* cần cho người dùng ở domain khác truy cập file server hoặc ứng dụng;
* có forest hoặc domain riêng nhưng cần liên kết xác thực.

Điều quan trọng là trust chỉ tạo điều kiện cho xác thực giữa domain. Nó không tự động cấp quyền truy cập vào mọi tài nguyên.

## 36.9. One-Way Trust

**One-Way Trust** là mối quan hệ tin cậy một chiều giữa hai domain.

Trong one-way trust, một domain tin cậy domain khác. Người dùng từ domain được tin cậy có thể được cấp quyền truy cập tài nguyên trong domain tin cậy.

Ví dụ:

```text
Domain AAA trusts Domain BBB
```

Điều này có nghĩa là:

```text
Người dùng từ Domain BBB có thể được cấp quyền truy cập tài nguyên trong Domain AAA
```

Hướng trust và hướng truy cập tài nguyên thường dễ gây nhầm lẫn. Nếu AAA tin cậy BBB, thì người dùng từ BBB có thể được ủy quyền truy cập tài nguyên trong AAA.

Mô hình đơn giản:

```text
Trust direction:
AAA  →  BBB

Resource access:
BBB user  →  AAA resource
```

One-Way Trust phù hợp khi chỉ cần cho phép truy cập theo một chiều.

Ví dụ, công ty A muốn cho người dùng công ty B truy cập một thư mục chia sẻ trong công ty A, nhưng không muốn người dùng công ty A truy cập tài nguyên của công ty B.

## 36.10. Two-Way Trust

**Two-Way Trust** là mối quan hệ tin cậy hai chiều giữa hai domain.

Trong two-way trust, cả hai domain tin cậy lẫn nhau. Điều này cho phép người dùng từ mỗi domain có thể được cấp quyền truy cập tài nguyên ở domain còn lại.

Ví dụ:

```text
Domain A trusts Domain B
Domain B trusts Domain A
```

Khi đó:

```text
User từ Domain A có thể được cấp quyền truy cập tài nguyên trong Domain B
User từ Domain B có thể được cấp quyền truy cập tài nguyên trong Domain A
```

Mô hình đơn giản:

```text
Domain A  ↔  Domain B
```

Two-Way Trust thường được dùng khi hai domain cần chia sẻ tài nguyên qua lại.

Theo mặc định, khi nhiều domain được tham gia vào cùng một tree hoặc forest, chúng thường có quan hệ tin cậy hai chiều. 

Ví dụ trong cùng một forest:

```text
company.local
├── sales.company.local
└── it.company.local
```

Người dùng ở `sales.company.local` có thể được cấp quyền truy cập tài nguyên ở `it.company.local`, và ngược lại, nếu quản trị viên cấu hình quyền phù hợp.

## 36.11. Trust không tự động cấp quyền truy cập

Một điểm rất quan trọng là **trust không tự động cấp quyền truy cập vào tất cả tài nguyên**.

Trust chỉ cho phép domain này tin tưởng xác thực từ domain khác. Sau đó, quản trị viên vẫn phải cấp quyền cụ thể trên tài nguyên.

Ví dụ, nếu Domain A và Domain B có trust relationship, điều đó không có nghĩa là mọi người dùng trong Domain A có thể tự động mở mọi thư mục trong Domain B.

Để người dùng truy cập được tài nguyên, cần có thêm bước phân quyền, ví dụ:

* thêm user từ Domain A vào group phù hợp trong Domain B;
* cấp quyền NTFS trên thư mục;
* cấp quyền share permission;
* cấp quyền truy cập ứng dụng;
* cấu hình quyền trong hệ thống liên quan.

Ví dụ:

```text
Domain A user: A\user01
Resource in Domain B: \\FileServerB\SharedFolder
```

Để `A\user01` truy cập được thư mục này, quản trị viên Domain B cần cấp quyền cụ thể cho user hoặc group tương ứng.

Tóm lại:

```text
Trust = cho phép xác thực giữa domain
Permission = cho phép truy cập tài nguyên cụ thể
```

Nếu chỉ có trust mà không có permission, người dùng vẫn không thể truy cập tài nguyên.

## 36.12. Ý nghĩa bảo mật của Trust Relationship

Trust Relationship có ý nghĩa bảo mật rất lớn trong Active Directory vì nó mở rộng phạm vi xác thực giữa các domain hoặc forest.

Nếu được cấu hình đúng, trust giúp doanh nghiệp chia sẻ tài nguyên linh hoạt giữa các đơn vị, công ty con hoặc hệ thống khác nhau.

Tuy nhiên, nếu cấu hình sai, trust có thể làm tăng rủi ro bảo mật.

Một số rủi ro cần chú ý:

* người dùng từ domain khác được cấp quyền quá rộng;
* trust không còn cần thiết nhưng vẫn tồn tại;
* tài khoản quyền cao từ domain khác có thể truy cập tài nguyên nhạy cảm;
* thiếu giám sát xác thực giữa các domain;
* nhầm lẫn giữa trust và quyền truy cập thực tế;
* cấu hình two-way trust khi chỉ cần one-way trust;
* domain được tin cậy bị tấn công và ảnh hưởng đến domain tin cậy.

Ví dụ, nếu Domain A tin cậy Domain B, nhưng Domain B bị compromise, kẻ tấn công có thể cố gắng lợi dụng mối quan hệ trust để truy cập tài nguyên trong Domain A nếu có quyền được cấu hình sai.

Khuyến nghị bảo mật:

* chỉ tạo trust khi thật sự cần;
* ưu tiên one-way trust nếu chỉ cần truy cập một chiều;
* không cấp quyền quá rộng cho người dùng từ domain khác;
* rà soát trust relationship định kỳ;
* giám sát xác thực giữa các domain;
* kiểm tra nhóm có chứa user từ domain khác;
* xóa trust không còn sử dụng;
* phân quyền tài nguyên theo nguyên tắc least privilege;
* ghi log và theo dõi truy cập tài nguyên qua trust.

Từ góc độ SOC, cần chú ý các dấu hiệu như:

* tài khoản từ domain khác truy cập tài nguyên nhạy cảm;
* xác thực bất thường qua trust;
* thay đổi cấu hình trust;
* thêm user từ domain khác vào nhóm quyền cao;
* truy cập tài nguyên ngoài phạm vi bình thường;
* nhiều lỗi xác thực giữa các domain.

Tóm lại, Trees, Forests và Trusts giúp Active Directory mở rộng và tổ chức nhiều domain trong môi trường doanh nghiệp. Tree dùng cho các domain chung namespace, Forest dùng cho nhiều tree, còn Trust Relationship cho phép xác thực giữa các domain hoặc forest. Tuy nhiên, trust chỉ tạo điều kiện xác thực, còn quyền truy cập tài nguyên vẫn phải được cấp riêng và cần được kiểm soát chặt chẽ.










