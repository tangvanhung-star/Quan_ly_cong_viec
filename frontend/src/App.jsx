import { useState, useEffect } from 'react'

function App() {
  const [tasks, setTasks] = useState([])
  const [newTaskText, setNewTaskText] = useState('')

  const fetchTasks = () => {
    fetch('/tasks')
      .then(response => response.json())
      .then(data => setTasks(data))
      .catch(error => console.error("Lỗi kết nối:", error));
  }

  useEffect(() => { fetchTasks(); }, [])

  // Xử lý thêm mới
  const handleAddTask = (e) => {
    e.preventDefault();
    if (!newTaskText.trim()) return;
    fetch('/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: newTaskText, completed: false }),
    }).then(() => { setNewTaskText(''); fetchTasks(); });
  }

  // 1. Hàm cập nhật trạng thái (Toggle)
  const toggleTask = (task) => {
    fetch(`/tasks/${task.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...task, completed: !task.completed }),
    }).then(() => fetchTasks());
  }

  // 2. Hàm xóa công việc
  const deleteTask = (id) => {
    fetch(`/tasks/${id}`, { method: 'DELETE' })
      .then(() => fetchTasks());
  }

  return (
    <div style={{ padding: '40px', maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
      <h1>Task Manager V2</h1>
      
      <form onSubmit={handleAddTask} style={{ marginBottom: '30px' }}>
        <input value={newTaskText} onChange={(e) => setNewTaskText(e.target.value)} placeholder="Việc mới..." />
        <button type="submit">Thêm việc</button>
      </form>

      <ul style={{ textAlign: 'left', listStyle: 'none' }}>
        {tasks.map(task => (
          <li key={task.id} style={{ padding: '10px', borderBottom: '1px solid #eee', display: 'flex', justifyContent: 'space-between' }}>
            <div style={{ cursor: 'pointer' }} onClick={() => toggleTask(task)}>
              <input type="checkbox" checked={task.completed} readOnly />
              <span style={{ marginLeft: '10px', textDecoration: task.completed ? 'line-through' : 'none' }}>
                {task.title}
              </span>
            </div>
            <button onClick={() => deleteTask(task.id)} style={{ color: 'red' }}>Xóa</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
export default App