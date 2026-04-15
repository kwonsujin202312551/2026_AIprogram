#예외 처리 가볍게 넘어가
try:
    a = 1/0
except:
    print("0으로 나누지 마세요")

while(True):
    try:
        a, b = input('두 수를 입력하시오: ').split()
        result = int(a) / int(b)
        print('{}/{} = {}'.format(a, b, result))
        break
    except:
        print('수가 정확한지 확인하세요')

while(True):
    try:
#        a, b = input('두 수를 입력하시오: ').split()
#        result = int(a) / int(b)
        a, b = map(int, input('두 수를 입력하시오: ').split(','))
        result = a/b
        print('{}/{} = {}'.format(a, b, result))
        break
    except:
        print('수가 정확한지 확인하세요')

str3 = input('세개의 숫자를 입력하세요').split()
print(str3)

str3 = input('세개의 숫자를 입력하세요').split()
istr3 = list(map(int, str3))
print(istr3)

a, b, c = map(int, input('세개의 숫자를 입력하시오').split())
print(a, b, c)

try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('오류: 0으로 나눔을 시도했습니다')
except ValueError:
    print('오류: 입력 값이 정수나 실수가 아닙니다')
except:
    print('오류: 10 2와 같이 두 정수를 입력하세요')
else:
    print('{}/{} = {}'.format(a, b, result))










