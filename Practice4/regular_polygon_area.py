import math

# Input values
number_of_sides = 4
side_length = 25

# Calculate area
area = (number_of_sides * side_length ** 2) / (4 * math.tan(math.pi / number_of_sides))

print("Number of sides:", number_of_sides)
print("Length of each side:", side_length)
print("Area of the polygon:", round(area))
