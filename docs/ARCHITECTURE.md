# KIẾN TRÚC HỆ THỐNG - ORDER MÌ CAY SEOULY

## 1. Mô hình kiến trúc: 3-Layer Architecture (Kiến trúc 3 lớp)
Hệ thống được tổ chức tách biệt thành 3 tầng độc lập để dễ bảo trì và phân chia công việc:

* **Presentation Layer (Tầng giao diện):** 
  * Hiển thị danh sách món ăn, trạng thái còn/hết, bộ chọn cấp độ cay (0–7) và giỏ hàng.
  * Tiếp nhận thao tác người dùng và gửi yêu cầu xuống tầng xử lý.
* **Business Logic Layer - Service (Tầng xử lý nghiệp vụ):**
  * Kiểm tra điều kiện đặt món (chặn nếu món đã hết hàng `IsAvailable == false` hoặc số lượng = 0).
  * Xử lý logic gắn cấp độ cay (`SpiceLevel`) vào món ăn (`Product`) và tính thành tiền hóa đơn.
* **Data Access Layer - Repository & Entity (Tầng truy xuất dữ liệu):**
  * Ánh xạ các lớp thực thể (`Product`, `SpiceLevel`, `Order`...) tương ứng với các bảng trong CSDL.
  * Thực hiện các truy vấn CRUD thông qua chuỗi kết nối (Connection String).

## 2. Công nghệ sử dụng (Tech Stack)
* **Frontend:** [Điền công nghệ nhóm chọn: HTML/CSS/JavaScript hoặc C# WPF / Java Swing]
* **Backend:** [Điền ngôn ngữ nhóm chọn: Python / C# .NET / Java]
* **Database:** SQL Server
* **Công cụ quản lý & Kiểm thử:** Jira, GitHub, [Tên Framework Unit Test nhóm chọn]

## 3. Luồng đi của dữ liệu (Data Flow)
`Người dùng chọn món & cấp độ cay` $\rightarrow$ `Presentation Layer gửi dữ liệu` $\rightarrow$ `Service Layer kiểm tra tồn kho & tính tiền` $\rightarrow$ `Repository Layer lưu đơn hàng xuống SQL Server` $\rightarrow$ `Trả kết quả về màn hình`.
