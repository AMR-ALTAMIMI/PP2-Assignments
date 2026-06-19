# Multiple inheritance example

class Father:
    def drive(self):
        print("Can drive a car")

class Mother:
    def cook(self):
        print("Can cook food")

class Child(Father, Mother):
    pass

child = Child()

child.drive()
child.cook()
