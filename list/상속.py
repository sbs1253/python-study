class Vehicle:  # 부모 클래스
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    def setMake(self, make):  # 설정자 메소드
        self.make = make

    def getMake(self):     # 접근자 메소드
        return self.make

# 차량에 대한 정보를 문자열로 요약하여서 반환한다.
    def getDesc(self):
        return "차량 = ("+str(self.make)+"," +\
            str(self.model)+"," +\
            str(self.color)+"," +\
            str(self.price)+")"


class Truck(Vehicle):  # 자식 클래스
    def __init__(self, make, model, color, price, payload):
        super().__init__(make, model, color, price)  # 부모 클래스를 먼저 실행
        self.payload = payload

    def setPayload(self, payload):  # 설정자 메소드
        self.payload = payload

    def getPayload(self):   # 접근자 메소드
        return self.payload

    def main():  # main 함수 정의의
        myTruck = Truck("Tesla", "Model S", "white", 10000, 2000)
        myTruck.setMake("Tesla")  # 설정자 메소드 호출
        myTruck.setPayload(2000)  # 설정자 메소드 호출
        print(myTruck.getDesc())  # 트럭 객체를 문자열로 출력


main = Truck.main()
main
