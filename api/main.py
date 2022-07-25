from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

fakedb=[]

class Task(BaseModel):
    id:int
    name:str
    desc:str
    is_completed:Optional[bool]=None

@app.get("/")
def read_root():
    return {"message":"Welcome "}

@app.get("/tasks")
def get_tasks():
    return fakedb

@app.get("/task/{task_id}")
def get_a_task(task_id:int):
    task=task_id-1
    return fakedb[task]

@app.post("/task")
def add_task(task:Task):
    fakedb.append(task.dict())
    return fakedb[-1]

@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    fakedb.pop(task_id-1)
    return {"task":"deletion sucessful"}