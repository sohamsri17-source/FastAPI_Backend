from fastapi import FastAPI, Path
from typing import Optional
from typing import List
from pydantic import BaseModel

app = FastAPI()

students = {
    
    1: {
        "name": "soham",
        "age": 20,
        "year": 2

    },

    2: {
         "name": "jack",
         "age": 22,
         "year": 4

    }
}

class Student(BaseModel):
    age: int
    name: str
    year: int

@app.get("/") # Decorators
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view"), gt=0, lt=3):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] ==  name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id:  int, students: Student):
    if student_id in students:
        return ("Error: Student already exist.")