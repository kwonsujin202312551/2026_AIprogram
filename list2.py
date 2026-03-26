score = [87, 84, 95, 67, 88, 94, 63]
print(score)
print(type(score))

print('---')

score = [87, 84, 95, 67, 88, 94, 63]
for i in score:
    print(i)

print('---')

score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희"]
for i in names:
    print(i)

print('---')

score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희", score]
for i in names:
    print(i)

print('---')


score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희", score]
addressbook = ["영호", 25, "010-1234-5678"], ["순자", 30, "010-1234-9678"]
for i in addressbook:
    print(i)

print('---')

ri = list(range(5))
print(ri)

print('---')

myString = "apple"

for ch in myString:
    print(ch)

myString = "apple"

for ch in myString:
    print(ch)

listString = list(myString)
print(listString)

print('---')

n_list =[10, 20, 30, 40]
n_list.append(50)
print(n_list)

print('---')

n_list = [11, 22, 33, 44, 55, 66]
print(n_list)

n_list.remove(44)
print(n_list)

print('---')

n_list = [11, 22, 33, 44, 55, 66]
a = n_list.pop()
print(a)
print(n_list)

print('---')

a_list = [10, 20, 30, 40]
print(10 in a_list)
print(10 not in a_list)

print('---')

list1 = [20, 10, 40, 50, 30]
list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)

print('---')

list1 = [20, 10, 40, 50, 30]
list2 = sorted(list1)
print(list1)
print(list2)

print('---')

list1 = [1, 2, 3, 4]
list2 = [2, 3, 3, 4]
print(list1 > list2)
print(list1 < list2)
