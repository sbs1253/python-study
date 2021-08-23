# tuple는 ()로 묶여있고 변경될 수 없는 리스트
from operator import eq
import math

number = (1, 2, 3, 4, 5)
colors = (1, 2, 3)

t = number+colors
print(t)

print(max(t))

(x, y, z) = colors

for i in range(len(colors)):  # 배열은 range(숫자)해야하므로 len 사용
    print(i)

print(x, y, z)


def calCircle(r):  # pi=3.14
    area = math.pi*r**2
    circum = 2*math.pi*r
    return(area, circum)


radius = float(input('원의 반지름을 입력하시오: '))
(a, c) = calCircle(radius)
print("원의 넓이는 "+str(a)+'이고 원의 둘레는 '+str(c)+"이다.")
