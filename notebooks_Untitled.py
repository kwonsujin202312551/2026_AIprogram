'''
radius = float(input('원의 반지름을 입력하시오: '))
print(type(radius))
area = 3.14*radius**2
circle = 2.0*3.14*radius
print('면적:', area, '둘레: ', circle)

a = [1, 2, 3]
print(a)
print(type(a))
print(a[0])

a='1, 2, 3'
print(a)
print(type(a))
print(a[0])

a='cat'
print(a)
print(type(a))
print(a[0])

txt4 = 'Hello'+'Python'
txt4

txt5 = 'banana\napple\norange'
print(txt5)

txt5 = 'banana\tapple\torange'
print(txt5)

c1 = 2+3j
c1.real  #c1의 실수부 출력

c1 = 2+3j
c1.imag  #c1의 허수부 출력

c1 = 2+3j
c1.real  #c1의 실수부 출력
c1.imag  #c1의 허수부 출력
c2 = 1 + 1j
c3= c1*c2

c1 = 2 + 3j
c2 = c1.conjugate()
c2
abs(c1)

x=100
y=100
com= x==y
print(com)
print(type(com))

x=100
y=100
z=200
(x==y) and (x>z)

x=100
y=100
z=200
(x==y) or (x>z)

x=100
y=100
z=200
not (x>z)

x= 4
y= 6
z= x & y
print(z)
'''

age = int(input("나이를 입력하세요:"))

if age < 20:
    print("청소년 할인")
elif age > 65:
    print("경로 우대")



