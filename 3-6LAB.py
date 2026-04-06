#3-6
for i in range(5):
    print('Hello, Python!')

for i in range(5):
    print(i)
#3-7
numbers = list(range(1,101))
print(numbers)

numbers = list(range(0,101, 2))
print(numbers)

numbers = list(range(1,101, 2))
print(numbers)

numbers = list(range(-1,-100, -1))
print(numbers)
#3-8
s = 0
for i in range(1, 101):
    s = s + i
print(s)

s = 0
for i in range(0, 101, 2):
    s = s + i
print(s)

s = 0
for i in range(1, 101, 2):
    s = s + i
print(s)
#3-9
n = 7
for i in range(n):
    print(" "*(n - i - 1),'#')

