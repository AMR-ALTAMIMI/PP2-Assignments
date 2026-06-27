# Generator for numbers divisible by 3 and 4

def divisible_numbers(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test
n = 50

print("Numbers divisible by 3 and 4:")

for number in divisible_numbers(n):
    print(number) 
