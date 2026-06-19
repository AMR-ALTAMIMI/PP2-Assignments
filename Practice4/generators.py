# generators.py

my_list = ["apple", "banana", "cherry"]

it = iter(my_list)

print(next(it))
print(next(it))
print(next(it))


def count_up():
    yield 1
    yield 2
    yield 3

for x in count_up():
    print(x)


squares = (x * x for x in range(5))

for num in squares:
    print(num)
