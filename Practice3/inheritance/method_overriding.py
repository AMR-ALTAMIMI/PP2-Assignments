# Method overriding example

class Employee:
    def work(self):
        print("Employee is working")

class Programmer(Employee):
    def work(self):
        print("Programmer is writing code")

employee = Employee()
programmer = Programmer()

employee.work()
programmer.work()
