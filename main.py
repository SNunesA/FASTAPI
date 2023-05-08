from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.post("/tasks")
async def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added successfully"}
