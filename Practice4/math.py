# math.py

import math
import random

print(min(5, 2, 8))
print(max(5, 2, 8))

print(abs(-10))

print(round(3.7))

print(pow(2, 3))

print(math.sqrt(25))

print(math.ceil(4.2))

print(math.floor(4.9))

print(random.randint(1, 10))

names = ["Ali", "Ahmed", "Sara"]

print(random.choice(names))

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)


# math.py
# Built-in math, the math module, and the random module

import math
import random

numbers = [4, 9, 2, 7, 1]
print("min:", min(numbers))       # smallest
print("max:", max(numbers))       # largest
print("abs:", abs(-15))           # absolute value -> 15
print("round:", round(3.14159, 2))# round to 2 decimals -> 3.14
print("pow:", pow(2, 8))          # 2 to the power 8 -> 256
print("sum:", sum(numbers))


# MATH MODULE FUNCTIONS 
print("sqrt:", math.sqrt(64))     # square root -> 8.0
print("ceil:", math.ceil(4.1))    # round UP -> 5
print("floor:", math.floor(4.9))  # round DOWN -> 4
print("factorial:", math.factorial(5))  # 5! -> 120

# Constants
print("pi:", math.pi)
print("e:", math.e)

# Trigonometry (input is in radians)
print("sin(pi/2):", math.sin(math.pi / 2))  # ~1.0
print("cos(0):", math.cos(0))                # 1.0

# Convert degrees to radians first
angle_deg = 90
angle_rad = math.radians(angle_deg)
print("sin(90 degrees):", math.sin(angle_rad))


#  RANDOM MODULE 
print("random float 0-1:", random.random())        # float between 0 and 1
print("random int 1-100:", random.randint(1, 100))  # integer in range, inclusive

colors = ["red", "green", "blue", "yellow"]
print("random choice:", random.choice(colors))      # pick one item

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)                                 # shuffle in place
print("shuffled:", deck)

# random.sample picks several unique items
print("sample of 3:", random.sample(range(1, 50), 3))
