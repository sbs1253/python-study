# # 369 게임
# check_list = ["3","6","9"]
# a = int(input("최대 숫자를 입력 하시오 : "))
# b = []
# for i in range(1,a+1):
#     for l in check_list:
#         if l in str(i):
#             for j in range(str(i).count(l)):
#                  print("짝",end="")
#             print()
#             b.append(i)
#     if i not in b:
#         print(i)

# 369 게임
check_list = ["3","6","9"]
a = int(input("최대 숫자를 입력 하시오 : "))
b = []
for i in range(1,a+1):
    for l in check_list:
        if l in str(i):
            print("짝",end="")
            print()
            b.append(i)
    if i not in b:
        print(i)
