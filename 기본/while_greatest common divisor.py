x = int(input("큰 수를 입력하시오: "))
y = int(input("작은 수를 입력하시오: "))


while y != 0:
    r = x % y
    x, y = y, r

print("최대 공약수는", str(x), "입니다.")
