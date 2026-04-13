
#LAB 6-1
capital_dic = {'Korea': 'Seoul', 'China': 'Beijing', 'USA': 'Washigton DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

fruits_dic = {'apple': 5000, 'banana': 4000, 'grape':5300, 'melon':6500}
for key in fruits_dic:
    print("{}의 가격은 {}원입니다.".format(key, fruits_dic[key]))

#LAB 6-2
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
person['특기'] = '분신술'
print(person)

person['아버지'] = '홍판서'
print(person)

del person['나이']
print(person)

#LAB 6-3
capital_dic = {'Korea': 'Seoul', 'China': 'Beijing', 'USA': 'Washigton DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)

#LAB 6-4
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}
print(fruits_dic.keys())

print(fruits_dic.values())

fruits_dic.pop('apple')
print(fruits_dic)

fruits_dic.clear()
print(fruits_dic)

#LAB 6-5
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}
print(list(fruits_dic))

print(list(fruits_dic.values()))

print('fruits_dic 딕셔너리의 항목의 개수:', len(fruits_dic))

if 'apple' in fruits_dic:
    print('apple is in fruits_dic')
if 'mango' not in fruits_dic:
    print('mango is not in fruits_dic')

#LAB 6-6
the_day = (1919, 3, 1)
year, month, day = the_day
print('{}년 {}월 {}일은 삼일절입니다'. format(year, month, day))

lst = [10, 20, 30]
d, e, f = lst
print('a=', f)
print('b=', e)
print('c=', d)

#LAB 6-7
person = ('홍길동', 2019001, 179)

person_list = list(person)
person_list[1] = 202003
person = tuple(person_list)
print('학번 변동 후 person=', person)

#LAB 6-8
def square(x, y):
    return x**2, y**2
x = 10
y = 20
x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'. format(x, x_sq, y, y_sq))

num = (10, 20, 30) + (40, 50, 60)
print(num)

print('Hello'*3)
print(('Hello',)*3)

#LAB 6-9
lst = ['apple', 'mango', 'banana']
s1 = set(lst)
print(s1)

greet = 'Good afternoon'
s2 = set(greet)
print(s2)

#LAB 6-10
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))

#LAB 6-11
def product_set(A, B):
    result = set()
    for a in A:
        for b in B:
            result.add((a,b))
        return result
A = {1, 2}
B = {'A', 'B', 'C'}
print(product_set(A, B))
print(product_set(B, A))
print(product_set(A, A))
print(product_set(B, B))

#LAB 6-12
def tuple_sum(tup):
    if isinstance(tup, int):
        return tup
    else:
        accum = 0
        for element in tup:
            accum += tuple_sum(element)
        return accum

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}
    return res

def exp(input_set, exponent):
    res = input_set
    for _ in range(exponent -1):
        res = product_set(res, input_set)
    return res

dice = {1, 2, 3, 4, 5, 6}
cases = exp(dice, 3)
print("주사위를 세 번 던져 발생할 수 있는 사건은", len(cases), "가지 경우가 존재합니다")

count_10 = 0
for c in cases:
    if tuple_sum(c) >= 10:
        count_10 += 1
print('주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는', count_10, '가지입니다')

def prob_over(x):
    count = 0
    for c in cases:
        if tuple_sum(c) >= x:
            count += 1
    return (count / len(cases)) * 100
for x in range(3, 19):
    print(f'눈의 합으로 {x} 이상을 얻을 확률 {prob_over(x):.2f}%')

