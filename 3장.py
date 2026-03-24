game_score = int(input('game score ='))
if game_score >= 1000:
    print('당신은 고수입니다.')


num_a = int(input('num_a ='))
num_b = int(input('num_b ='))
if num_a == num_b:
    print('두 값이 일치합니다.')


n = int(input('정수를 입력하세요:'))
if n%2 == 0:
    print(n, '은(는) 짝수입니다.')


n = int(input('정수를 입력하세요:'))
if n >=0:
    print('X=', n)
    print(n, '은(는) 자연수입니다.')
else:
    print('X=', n)


game_score=int(input('게임점수를 입력하시오:'))
if game_score >=1000:
    print('고수입니다')
else:
    print('입문자입니다')


num_a = int(input('한 정수를 입력하시오'))
num_b = int(input('다른 정수를 입력하시오'))
if num_a == num_b:
    print('두 값이 일치합니다.')
else:
    print('두 값이 일치하지 않습니다.')


age = int(input("당신은 성인인가요? (성인이면 1, 미성년이면 0): "))
if age == 0:
    print("당신은 미성년자입니다.")
    exit()
else:
    print("당신은 성인입니다.")


age = int(input("당신은 성인인가요? (성인이면 1, 미성년이면 0): "))
if age == 0:
    print("당신은 미성년자입니다.")
    exit()
else:
    marry = int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0): '))
    if marry == 0:
        print('당신은 결혼하지 않은 성인입니다.')
    else:
        print('당신은 결혼한 성인입니다.')


num = int(input("num= "))
print(1 <= num and num <= 10)


age = int(input('age='))
if 10 <= age and age <=19:
    print('청소년입니다.')


speed = int(input('자동차의 속도를 입력하세요(단위: km/h): '))
if speed >= 100:
    print('고속')
elif 60 <= speed and speed < 100:
    print('중속')
else:
    print('저속')
