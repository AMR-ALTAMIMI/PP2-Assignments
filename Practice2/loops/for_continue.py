# Task 1: Skip Banana

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue

    print(fruit)


# Task 2: Skip Number 3

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# Task 3: Skip Letter h

for letter in "Python":
    if letter == "h":
        continue

    print(letter)


# Task 4: Skip Student

students = ["Amr", "Ali", "Ahmed"]

for student in students:
    if student == "Ali":
        continue

    print(student)


# Task 5: Skip Even Numbers

for x in range(1, 11):
    if x % 2 == 0:
        continue

    print(x)
