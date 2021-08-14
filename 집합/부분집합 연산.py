A = {1, 2, 3}
B = {1, 2, 3}
print(A == B)

C = {1, 2, 3, 4, 5}
D = {1, 2, 3}
print(D < C)

print(B.issubset(A))  # 부분 집합인가가

print(C | D)  # 합집합
print(C & D)  # 교집합 == intersection 과 같음음
print(C-D)  # 차집합
