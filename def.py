
def iplus(x1, x2):
    isum = x1 + x2
    return isum

hap = iplus(4, 5)
print(hap)

print('---')

def print_star():
    print('************')
print_star()

print('---')

def root(a, b, c):
    x1 = (-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    x2 = (-b-(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    return x1,x2
r1,r2 = root(1,2,3)
print(r1, r2)

print('---')

def root(a, b, c):
    if(b**2.0-4.0*a*c)<0:
        return None, None
    else:
        x1 = (-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a)
        x2 = (-b-(b**2.0-4.0*a*c)**0.5)/(2.0*a)
        return x1,x2
r1,r2 = root(1,2,3)
print(r1, r2)

print('---')

def root(a, b, c):
    x1 = (-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    x2 = (-b-(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    return x1,x2
r1,r2 = root(1,2,3)
if type(r1) == complex:
    print('허수입니다.')

print('---')

#위에 if문이랑 차이 
def root0(a, b, c):
    if -b(b**2.0-4.0*a*c)<0:
        return None, None
    else:
        x1 = (-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a)
        x2 = (-b-(b**2.0-4.0*a*c)**0.5)/(2.0*a)
        return x1,x2
r1,r2 = root(1,2,3)
print(r1, r2)

print('---')

def print_sum():
    result = a + b
    print('print_sum() 내부:', a, '과', b, '의 합은', result, '입니다.')

a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부:', a, '과', b, '의 합은', result, '입니다.')












