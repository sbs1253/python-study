numbers = {2, 1, 3}
if 1 in numbers:  # 집합안에 1이 있는지 in
    print("집합안에 1이 있습니다.")

for x in numbers:
    print(x, end="")  # for문 집합사용 가능

numbers.add(4)  # set은 순서가 없다. typle와 list는 순서있음
