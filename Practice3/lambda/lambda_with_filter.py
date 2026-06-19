# Select students who passed

grades = [45, 70, 82, 39, 91, 58]

passed = list(
    filter(lambda grade: grade >= 60, grades)
)

print(passed)
