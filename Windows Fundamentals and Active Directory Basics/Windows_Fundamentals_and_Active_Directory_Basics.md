# Windows Fundamentals and Active Directory Basics

## Mục lục

1. [Tổng quan về hệ điều hành Windows](#1-tổng-quan-về-hệ-điều-hành-windows)

2. [Giao diện Desktop của Windows](#2-giao-diện-desktop-của-windows)


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

