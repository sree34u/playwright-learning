from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# In-memory storage for demo
tasks = []
users = [{"username": "test", "password": "123"}]

# Models
class Task(BaseModel):
    id: int
    task: str
    status: str
    priority: str

class Profile(BaseModel):
    name: str
    email: str
    phone: str
    age: int

# Health check
@app.get("/status")
def read_status():
    return {"status": "ok"}

# Login endpoint
@app.post("/login")
def login(username: str, password: str):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return {"message": "Login successful"}
    return {"message": "Invalid credentials"}

# CRUD for tasks
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task added", "tasks": tasks}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i] = task.dict()
            return {"message": "Task updated", "tasks": tasks}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted", "tasks": tasks}
    raise HTTPException(status_code=404, detail="Task not found")

# Profile submission
@app.post("/profile")
def submit_profile(profile: Profile):
    if "@" not in profile.email:
        raise HTTPException(status_code=400, detail="Invalid email")
    if len(profile.phone) < 10:
        raise HTTPException(status_code=400, detail="Invalid phone")
    return {"message": "Profile submitted successfully"}
