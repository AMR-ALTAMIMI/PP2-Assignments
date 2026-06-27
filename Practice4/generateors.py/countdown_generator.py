# Countdown generator

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test
n = 10

print("Countdown:")

for number in countdown(n):
    print(number)
