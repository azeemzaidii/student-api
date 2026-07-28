from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str

students = {}

@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    students[student_id] = student
    return {"message": "Student added!", "student": student}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, {"error": "Student not found"})

@app.get("/students")
def get_all_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id] = student
    return {"message": "Student updated!", "student": student}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted!"}