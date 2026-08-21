# Hướng dẫn Xây dựng Hệ thống Task Manager (V2)

Chào mừng bạn đến với tài liệu hướng dẫn xây dựng hệ thống Quản lý Công việc (Task Manager) phiên bản 2.0. Tài liệu này ghi lại hành trình chúng ta cùng nhau xây dựng một hệ thống Full-stack từ con số 0.

## 1. Mục tiêu Dự án
Xây dựng một hệ thống quản lý công việc với kiến trúc tách biệt giữa Frontend và Backend:
*   **Backend**: FastAPI (Python) quản lý logic và kết nối database.
*   **Frontend**: React (Vite) cung cấp giao diện người dùng hiện đại.
*   **Database**: PostgreSQL lưu trữ dữ liệu bền vững.

## 2. Kiến trúc Hệ thống
Hệ thống vận hành theo cơ chế "Nhà hàng":
*   **Nhà bếp (Backend)**: Nấu nướng dữ liệu từ PostgreSQL và phục vụ qua các "cửa sổ" API (GET, POST, PUT, DELETE).
*   **Phòng khách (Frontend)**: Giao diện React hiển thị thực đơn và tương tác với khách hàng, gửi yêu cầu sang "Nhà bếp" qua API.
*   **Cầu nối**: Các yêu cầu HTTP (fetch) giúp Frontend và Backend trò chuyện với nhau.

## 3. Các bước Thực hiện chính
### Bước 1: Khởi tạo và Thiết lập
*   **Backend**: Thiết lập kết nối PostgreSQL, cấu hình CORS để cho phép Frontend truy cập.
*   **Frontend**: Khởi tạo bằng Vite, dọn dẹp các thành phần không cần thiết để có không gian làm việc sạch sẽ.

### Bước 2: Xây dựng Tính năng (CRUD)
*   **GET (Xem)**: Sử dụng `useEffect` và `fetch` để lấy danh sách từ Backend khi vừa tải trang.
*   **POST (Thêm)**: Tạo Form nhập liệu và gửi yêu cầu tạo mới vào database.
*   **PUT (Cập nhật)**: Cập nhật trạng thái hoàn thành (Checkbox).
*   **DELETE (Xóa)**: Loại bỏ các công việc không còn nhu cầu.

## 4. Bài học từ các Lỗi kỹ thuật
Trong quá trình phát triển, chúng ta đã gặp và giải quyết các vấn đề cốt lõi:
*   **Lỗi 404 (Not Found)**: Bài học về việc thiếu các "cửa sổ tiếp nhận" (Endpoint) trên Backend. Chúng ta đã bổ sung `PUT` và `DELETE` vào `main.py` để Backend hiểu được lệnh từ Frontend.
*   **Tư duy lập trình**: Hiểu rõ lý do tại sao cần tách biệt logic (Backend) và hiển thị (Frontend).

## 5. Hướng phát triển tiếp theo
Hệ thống hiện đã hoàn thiện về logic CRUD cơ bản. Các bước tiếp theo để đưa hệ thống vào thực tế:
1.  **Cấu hình Server (VPS)**: Sử dụng IIS Server làm "cửa ngõ" chính.
2.  **Triển khai (Deployment)**: Chạy Backend bằng tiến trình bền vững (như PM2 hoặc dịch vụ Windows) và build Frontend để chạy tĩnh trên IIS.
3.  **Bảo mật**: Sử dụng Certify The Web để cài đặt chứng chỉ SSL/HTTPS.
## 🐍 Bước 2: Xây dựng kết nối với Python (Backend)
- **Môi trường ảo (Virtual Environment):**
  - Tạo lệnh: `python -m venv venv`
  - Kích hoạt lệnh (trên Windows PowerShell): `.\venv\Scripts\activate`
- **Thư viện kết nối PostgreSQL:** Cài đặt bằng lệnh `pip install psycopg2-binary`.
---
*Tài liệu được biên soạn dựa trên quá trình xây dựng thực tế. Chúc bạn tiếp tục làm chủ hệ thống của mình!*
🌟 1. Tổng quan kiến trúc hệ thống
Hệ thống của chúng ta được vận hành theo mô hình phân tách rõ ràng (Decoupled Architecture) trên một máy chủ Windows Server (103.228.74.205):

Database (Kho lưu trữ): PostgreSQL chạy ngầm như một Windows Service ổn định 24/7.

Backend (Nhà bếp xử lý logic): FastAPI (Python) chạy ngầm thông qua công cụ quản lý dịch vụ NSSM (TaskManagerBackend).

Frontend (Sảnh đón khách giao diện): React (đã được build tĩnh thành các file HTML/JS/CSS) và được quản lý trực tiếp bởi IIS Web Server dưới tên miền phụ taskmanager.thpstyle.vn.

🛠️ 2. Công cụ và thành phần đã sử dụng
Hệ điều hành: Windows Server (VPS).

Web Server: IIS (Internet Information Services) - Đóng vai trò lễ tân điều hướng cổng 80/443.

Process Manager (Quản lý dịch vụ nền): NSSM (Non-Sucking Service Manager) để biến FastAPI thành Windows Service.

Database: PostgreSQL.

Tên miền & Mạng: Custom Subdomain taskmanager.thpstyle.vn trỏ về IP VPS.

🚀 3. Sơ đồ vận hành & Quy trình cấu hình đã thực hiện
A. Cơ sở dữ liệu (PostgreSQL)
Được cài đặt trực tiếp trên VPS và cấu hình chạy tự động ở chế độ Automatic trong services.msc.

Tạo schema/database riêng trên VPS để phục vụ môi trường thực tế (production).

B. Backend (FastAPI + NSSM)
Thư mục làm việc: C:\Quan_ly_cong_viec\backend

Cài đặt dịch vụ chạy ngầm với NSSM:

Bash
C:\tools\nssm.exe install TaskManagerBackend
Cấu hình chi tiết trong NSSM:

Path: C:\Quan_ly_cong_viec\backend\venv\Scripts\python.exe

Startup directory: C:\Quan_ly_cong_viec\backend

Arguments: -m uvicorn main:app --host 127.0.0.1 --port 8000

Ý nghĩa: Giúp FastAPI luôn chạy ngầm, nhận yêu cầu nội bộ từ IIS và tự khởi động lại khi VPS bật máy.

C. Frontend (React + IIS + Subdomain)
Thư mục chứa bản build: C:\Quan_ly_cong_viec\frontend\dist

Cấu hình trên IIS:

Tạo Website mới mang tên TaskManagerFrontend, trỏ đường dẫn vật lý (Physical Path) về thư mục dist của React.

Cấu hình Bindings: Thêm cổng 80 với Host name là taskmanager.thpstyle.vn để tách biệt hoàn toàn với các trang web khác trên cùng VPS.

Đảm bảo tắt hoặc cấu hình đúng Default Web Site để tránh xung đột cổng.

🔐 4. Kế hoạch tiếp theo (Tiếp tục vào lần tới)
Cài đặt chứng chỉ bảo mật SSL (HTTPS) cho taskmanager.thpstyle.vn thông qua công cụ Certify The Web để khóa ổ khóa xanh an toàn cho trang web.