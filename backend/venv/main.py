from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from pydantic import BaseModel

app = FastAPI(title="Personal Task Manager API V2")

# --- BẢO VỆ CỬA (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hàm mở cửa kho dữ liệu PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123456",  # Nhớ thay bằng mật khẩu của bạn nhé!
        host="127.0.0.1",
        port="5432"
    ) 
    return conn

# 1. Đường dẫn kiểm tra cơ bản
@app.get("/")
def read_root():
    return {"message": "Chào mừng bạn đến với hệ thống Quản lý công việc V2!"}

# --- BỔ SUNG MỚI: Món ăn lấy danh sách công việc từ kho ---
@app.get("/tasks")
def get_tasks():
    # 1. Mở cửa kho
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Đọc tất cả dữ liệu từ kệ 'tasks'
    cursor.execute("SELECT id, title, completed FROM tasks ORDER BY id DESC;")
    rows = cursor.fetchall()
    
    # 3. Đóng cửa kho, trả lại kết nối
    cursor.close()
    conn.close()
    
    # 4. Đóng gói dữ liệu thành dạng danh sách JSON để phục vụ bên ngoài
    task_list = []
    for row in rows:
        task_list.append({
            "id": row[0],
            "title": row[1],
            "completed": row[2]
        })
        
    return task_list
# --- KHUÔN MẪU ĐƠN HÀNG (Pydantic Model) ---
# Định nghĩa hình dáng của một đơn hàng mới gửi lên cần những gì
class TaskCreate(BaseModel):
    title: str
# --- MÓN ĂN THỨ HAI: Thêm công việc mới vào kho ---
@app.post("/tasks")
def create_task(task: TaskCreate):
    # 1. Mở cửa kho
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Chèn công việc mới vào bảng 'tasks'
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (%s, FALSE) RETURNING id, title, completed;",
        (task.title,)
    )
    new_task = cursor.fetchone()
    
    # 3. Lưu chính thức thay đổi vào cơ sở dữ liệu (Commit)
    conn.commit()
    
    # 4. Đóng cửa kho, trả lại kết nối
    cursor.close()
    conn.close()
    
    # --- THÊM LỚP BẢO VỆ NÀY ĐỂ CHIỀU LÒNG ANH BẢO VỆ PYLANCE ---
    if new_task is None:
        return {"error": "Không thể tạo công việc mới"}
    
    # 5. Đóng gói kết quả vừa tạo thành JSON trả về cho người gọi
    return {
        "id": new_task[0],
        "title": new_task[1],
        "completed": new_task[2]
    }
    # --- MỞ RỘNG: Khuôn mẫu cho đơn hàng Sửa thông tin ---
class TaskUpdate(BaseModel):
    title: str
    completed: bool

# --- MÓN ĂN THỨ BA: Cập nhật (Sửa) trạng thái công việc ---
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    # 1. Mở cửa kho
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Tìm và cập nhật công việc theo ID
    cursor.execute(
        "UPDATE tasks SET title = %s, completed = %s WHERE id = %s RETURNING id, title, completed;",
        (task.title, task.completed, task_id)
    )
    updated_task = cursor.fetchone()
    conn.commit()
    
    # 3. Đóng cửa kho
    cursor.close()
    conn.close()
    
    if updated_task is None:
        return {"error": "Không tìm thấy công việc để cập nhật"}
        
    return {"id": updated_task[0], "title": updated_task[1], "completed": updated_task[2]}

# --- MÓN ĂN THỨ TƯ: Xóa công việc khỏi kho ---
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # 1. Mở cửa kho
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 2. Xóa công việc theo ID
    cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()
    
    # 3. Đóng cửa kho
    cursor.close()
    conn.close()
    
    return {"message": "Đã xóa thành công"}