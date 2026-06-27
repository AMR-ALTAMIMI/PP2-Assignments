# Generator for squares between a and b

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Test
a = 3
b = 7

print("Squares from", a, "to", b)

for value in squares(a, b):
    print(value)
