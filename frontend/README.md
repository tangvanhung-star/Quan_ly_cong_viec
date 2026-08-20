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
