i = 0
while i<5:
    print('welcome to everyone!!')
    i += 1

print('---')

i = 0
for i in range(5):
    print('welcome to everyone!!')

print('---')

isum = 0
n_list = [0, 2, 5, 10]
for i in n_list:
    isum += i
print(isum)

print('---')

# 위 코드를 while문으로 바꾼것
n_list = [0, 2, 5, 10]
isum = 0
i = 0
while i<4:
    isum += n_list[i]
    i += 1
print(isum)

