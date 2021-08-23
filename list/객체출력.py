# class 선언할 때 앞에 self 선언 해야함함
class Car:
    # 초기화 메서드: 객체생성시 반드시 실행됨
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    # print문 만나면 msg 처럼 출력되게 만듬
    def __str__(self):
        msg = "속도:"+str(self.speed)+" 색상:"+self.color+" 모델:"+self.model
        return msg

    def drive(self):
        self.speed = 60


# 0은 speed, blue는 color, E-class는 model\
# 여러개의 객체 생성 가능
myCar = Car(0, "blue", "E-Class")

youCar = Car(0, "silver", "A6")
meCar = Car(0, "red", "520d")

print(myCar)
print(youCar)
print(meCar)
