# Task 1: Break at Number 5

i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1


# Task 2: Stop at Number 3

x = 1

while x <= 5:
    if x == 3:
        break
    print(x)
    x += 1


# Task 3: Break Using Condition

count = 0

while True:
    print(count)
    count += 1

    if count == 4:
        break


# Task 4: Student Attempts

attempt = 1

while attempt <= 5:
    print("Attempt", attempt)

    if attempt == 3:
        break

    attempt += 1


# Task 5: Break After Success

success = True

while success:
    print("Login Successful")
    break
