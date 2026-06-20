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
# 5
myStr = 'banana'
myit = iter(myStr)
for i in myStr:
    print(i)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 2
class myNum:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x

myc = myNum()
myit = iter(myNum)

print(next(myit))
print(next(myit))
print(next(myit))

# 3
class myn:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myx = myn()
y = iter(myn)
for x in y:
    print(x)
    
