# object = thing
class Car:
    def drive(self):
        self.speed = 60


myCar = Car()
myCar.color = "blue"
myCar.model = "E-Class"
myCar.speed = 0
myCar.year = "2017"

print("자동차 객체를 생성 하였다.")
print("속도:", myCar.speed)
print("색상:", myCar.color)
print("모델:", myCar.model)
print("자동차를 주행합니다")

myCar.drive()
print("속도:", myCar.speed)
