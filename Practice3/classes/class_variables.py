class Student:

    university = "KazNU"

    def __init__(self, name):
        self.name = name

student1 = Student("Ahmed")
student2 = Student("Ali")

print(student1.university)
print(student2.university)

student1.name = "Mohammed"

print(student1.name)
print(student2.name)
