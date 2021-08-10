money = int(input("넣은 돈: "))
price = int(input("물건 값: "))

changes = money-price
coin_500 = changes//500
coin_100 = (changes % 500)//100
coin_50 = ((changes % 500) % 100)//50
coin_10 = (((changes % 500) % 100) % 50)//10

print("잔돈", changes)
print("500원 짜리 동전의 개수: ", coin_500)
print("100원 짜리 동전의 개수: ", coin_100)
print("50원 짜리 동전의 개수: ", coin_50)
print("10원 짜리 동전의 개수: ", coin_10)
