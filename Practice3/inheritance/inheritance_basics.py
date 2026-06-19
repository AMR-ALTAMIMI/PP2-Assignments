# Basic inheritance example

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def study(self):
        print("Studying Python")

student = Student("Ahmed")

student.introduce()
student.study()
