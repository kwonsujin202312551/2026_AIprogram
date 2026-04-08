person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
print(person['이름'])
print(person['나이'])
print(person['몸무게'])

students = { 2019001:'이순신', 2019002:'김유신', 2019003:'강감찬'}
print(students[2019001])
print(students[2019002])
print(students[2019003])

#키 추가
person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
person['국적'] = '대한민국'
print(person)

#키 삭제
person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
del person['나이']
print(person)

person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
person['국적'] = '대한민국'
print(person.keys())
print(person.values())

person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
person['국적'] = '대한민국'
for key in person:
    print('{}:{}'.format(key, person[key]))

