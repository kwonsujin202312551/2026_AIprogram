tuple0=(1,0)
tuple1=(1,2,3)
print(tuple0)

def plusminus(a1, a2):
    return a1+a2, a1-a2
output = plusminus(10,2)
print(type(output))

def plusminus(a1, a2):
    return a1+a2, a1-a2
output = plusminus(10,2)
output_list = list(output)
print(type(output_list))

a =100
b =200
print('Before swap: ', a, b)
a, b = b, a
print('After swap:', a, b)

a =100
b =200
print('Before swap: ', a, b)
a = b
b = a
print('After swap:', a, b)
