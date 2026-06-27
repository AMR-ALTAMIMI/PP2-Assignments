# Generator to generate squares from 1 to N

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

# Test
N = 5

print("Squares:")
for square in square_generator(N):
    print(square)
