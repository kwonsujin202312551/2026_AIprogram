
# 사각형을 클래스로 정의
class Rectangle:
    def __init__(self, side=0):
        self.side = side

    def getArea(self):
        return self.side*self.side
r1 = Rectangle(10.0)

# 사각형 객체와 반복횟수를 받아서 변을 증가시키면서 면적을 출력
def printAreas(r, n):
    while n >= 1:
        print(r.side, "\t", r.getArea())
        r.side = r.side + 1
        n = n - 1
print('---------')

class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber
    def __str__(self):
        return '{}'.format(self.number)
t1 = Television()
t2 = Television()
myTv = Television()
print(t1, t2, myTv)
print('---------')

class Car:

    def __init__(self, name="", speed=0):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def __str__(self):
        return '{}의 속도는 {}입니다'.format(self.name, self.speed)

    def speedUp(self, value):
        self.speed += value

    def speedDown(self, value):
        self.speed -= value
    
car1 = Car()
car2 = Car('벤츠', 30)
car1.speedUp(40)
car2.speedUp(10)
car1.speedDown(10)
print(car1)
print(car2)

# 상속
class Sedan(Car):
    def speedUP(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
myCar = Sedan("K5", 50)
print(myCar)
print('---------')

class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다')

    def __del__(self):
        print(self.length, '길이의 선이 삭제되었습니다')

    def __repr__(self):
        return '선의 길이:' +str(self.length)

    def __add__(self, other):
        return Line(self.length + other.length)

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.length == other.length
myLine1 = Line(100)
myLine2 = Line(200)
myLine3 = myLine1 + myLine2
print(myLine1)
print(myLine3)

print('두 선의 길이 합: ', myLine1 + myLine2)

if myLine1 < myLine2:
    print('선분 2가 더 기네요')
elif myLine1 == myLine2:
    print('두 선이 같네요')
else:
    print('모르겠네요')
del(myLine1)
print('---------')
        
import time
class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~~ 달립니다. \n'
            print(carStr, end = '')
            time.sleep(3)
car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')

car1.runCar()
car2.runCar()
car3.runCar()

# 스레드
import threading
import time
class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~~ 달립니다. \n'
            print(carStr, end = '')
            time.sleep(3)
car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')

th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()



import multiprocessing
import time
class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0, 3):
            carStr = self.carName + '~~~ 달립니다. \n'
            print(carStr, end = '')
            time.sleep(3)
if __name__ == "__main__":
    car1 = RacingCar('@자동차1')
    car2 = RacingCar('#자동차2')
    car3 = RacingCar('$자동차3')

    mp1 = multiprocessing.Process(target = car1.runCar)
    mp2 = multiprocessing.Process(target = car2.runCar)
    mp3 = multiprocessing.Process(target = car3.runCar)

    mp1.start()
    mp2.start()
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()
    
