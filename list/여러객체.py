# class 선언할 때 앞에 self 선언 해야함함
class Car:
    def __init__(self, speed, color, model):  # 초기화 메서드: 객체생성시 반드시 실행됨됨
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60


myCar = Car(0, "blue", "E-Class")
# 0은 speed, blue는 color, E-class는 model\
# 여러개의 객체 생성 가능
youCar = Car(0, "silver", "A6")
meCar = Car(0, "red", "520d")

print("자동차 객체를 생성 하였다.")
print("너의 차의 모델:", youCar.model)
print("내 차의 모델:", myCar.model)
print("나의 차:", meCar.model)

print("속도:", myCar.speed)
print("색상:", myCar.color)
print("자동차를 주행합니다")

myCar.drive()
print("속도:", myCar.speed)
