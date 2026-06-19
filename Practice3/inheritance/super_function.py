# Using super()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

student = Student("Ahmed", "Computer Science")

print(student.name)
print(student.major)
