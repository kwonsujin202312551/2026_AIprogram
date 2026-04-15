#tutle 뒤에 안 들어감 시험
import math as m
print(m.sin(m.pi/2.0))


import random as rd
a = rd.random()
print(a)


import random as rd
a = list(range(1, 11))
rd.shuffle(a)
print(a)


import turtle as t
t.setup(width = 400, height = 400)
for i in range(200):
    t.forward(i)
    t.left(93)
t.done
