#LAB 7-1
from datetime import datetime
now = datetime.now()

year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second

if hour < 12:
    period = '오전'
    display_hour = hour
else:
    period = '오후'
    display_hour = hour

print('{}년 {}월 {}일 {} {}시 {}분 {}초'.format(year, month, day, period, display_hour, minute, second))

#LAB 7-2
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas - dt.datetime.now()
print('다음 크리스마스까지는 {}일 {}시간 남았습니다'.format(\
    time_gap.days, time_gap.seconds // 3600))

import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
new_year = dt.datetime(2027, 1, 1)
time_gap = new_year - dt.datetime.now()
print('다음 새해까지는 {}일 {}시간 남았습니다'.format(\
    time_gap.days, time_gap.seconds // 3600))

import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
birthday = dt.datetime(2026, 11, 25)
time_gap = birthday - dt.datetime.now()
print('다음 생일까지는 {}일 {}시간 남았습니다'.format(\
    time_gap.days, time_gap.seconds // 3600))

#LAB 7-3
import datetime as dt
print('오늘=', dt.datetime.now())
thousand = dt.timedelta(days = 1000)
plus1000day = dt.datetime.now() + thousand
print('1000일 후 =', plus1000day)

from datetime import datetime, timedelta
y, m, d = map(int,input('처음사귄 연도와 월, 일을 입력하시오').split())
start = datetime(y, m, d)
day_100 = start + timedelta(days=100)
print(f"100일 기념일: {day_100.year}년 {day_100.month}월 {day_100.day}일")

#LAB 7-4
import math
for i in range(2, 11):
    print(f'4 ** {i}= {math.pow(4, i)}')

import math as m
for i in range(0, 181, 10):
    radians = m.radians(i)
    print('{}degree = {} radian'.format(i, radians))

import math as m
for i in range(0, 181, 10):
    sins = m.sin(i*m.pi/180)
    print('sin{} = {}'.format(i, sins))

#LAB 7-5
import random as rd
result =[rd.randrange(0, 101, 5) for _ in range(3)]
print(result)

import random as rd
a = list(range(1, 11))
print(rd.sample(a, 3))

#LAB 7-7
import turtle as t
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.done()

import turtle as t
for _ in range(3):
    t.forward(100)
    t.left(120)
for _ in range(3):
    t.forward(200)
    t.left(120)
t.done()

import turtle as t
for i in range(4):
    for _ in range(3):
         t.forward(100*(i))
         t.left(120)
t.done()

import turtle as t
for _ in range(4):
    t.forward(100)
    t.left(90)
t.done()


#LAB 8-1
try:
    a = [10, 20, 30]
    a[3]
except Exception as e:
    print('error:', e)

try:
    n = int('20%')
except Exception as e:
    print('error:', e)

try:
    a = 100 + '200'
except Exception as e:
    print('error:', e)

#LAB 8-2
try:
    print(10 * (30 / 0))

    x = int(input('정수 x를 입력하세요: '))

    import sys
    f = open('myfile.txt')
    s = f.readline()

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

except ValueError:
    print("정수를 올바르게 입력하세요.")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

finally:
    print("프로그램을 종료합니다.")

#LAB 8-3
a = [1, 2, 3, 4, 5]

try:
    x = int(input("a의 요소를 하나 선택하시오 : "))
    index = a.index(x)
    print(f"{x} 은(는) {index + 1} 번째 요소입니다.")
except ValueError:
    print("오류: 입력값이 정수나 실수가 아님.")
