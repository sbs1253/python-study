class FourCal:
    def __init__(self,a,b):
        self.first = a
        self.second = b
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def seq(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second != 0:
            result = self.first / self.second
            return result
        else:
            return "0으로 나누지마요"

a = int(input("숫자를 입력하시오: "))
b = int(input("숫자를 입력하시오: "))

s = MoreFourCal(a,b)

print("더하기:",s.add())
print("빼기:",s.sub())
print("곱하기:",s.mul())
print("나누기: "+ str(s.div()))

print("제곱:",s.seq())