# Return multiple values

def student_statistics(grades):
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return average, highest, lowest

avg, high, low = student_statistics([80, 90, 75, 95, 88])

print("Average:", avg)
print("Highest:", high)
print("Lowest:", low)
