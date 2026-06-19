class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

student1 = Student(
    "Ahmed",
    "Computer Science",
    3.5
)

print(student1.name)
print(student1.major)
print(student1.gpa)
