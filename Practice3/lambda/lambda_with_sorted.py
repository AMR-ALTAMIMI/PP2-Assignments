# Sort students by GPA

students = [
    {"name": "Ahmed", "gpa": 3.2},
    {"name": "Ali", "gpa": 2.9},
    {"name": "Sara", "gpa": 3.8}
]

sorted_students = sorted(
    students,
    key=lambda student: student["gpa"],
    reverse=True
)

print(sorted_students)
