#시험 범위 캡술화 변수까지
student1 = {"name":"민수", "score": 85}
student2 = {"name": "지영", "score": 92}

def get_grade(student):
    if student["score"] >= 90:
        return "A"
    elif student["score"] >= 80:
        return "B"
    else:
        return "C"

print(get_grade(student1))
print(get_grade(student2))

print("---")


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"

민수 = Student("민수", 85)
지영 = Student("지영", 92)
# 민수.name = name
# 민수.score = score

print(민수.get_grade())
print(지영.get_grade())

print("---")
#문자열화 메소드
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return'이름: {}, 점수: {}'.format(self.name, self.score)
              

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"

민수 = Student("민수", 85)
지영 = Student("지영", 92)

print(민수)
print(민수.name)

print('---')

#캡슐화
class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return'이름: {}, 점수: {}'.format(self.name, self.score)
              

    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >= 80:
            return "B"

민수 = Student("민수", 85)
지영 = Student("지영", 92)

print(민수)
print(민수.__name)




print('---')

class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def use(self, minutes):
        self.battery -= 0.5*minutes
        print(self.battery)

    def charge(self, minutes):
        self.battery += minutes
        print(self.battery)

my_phone = Phone('Galaxy', 80)

print(my_phone.use(30))
print(my_phone.charge(20))

print("---")
    
class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
    def my_phone(self):
        print('내 폰의 종류는 {}, 배터리는 {}'.format(self.brand, self.battery))

민수 = Phone("galaxy", 80)
지영 = Phone("iphone", 64)

print(민수.my_phone())
print(지영.my_phone())

