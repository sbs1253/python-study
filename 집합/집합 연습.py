s = "Love will find a way"
print("Love" in s)  # 소문자 대문자 구분분
print(s.split())  # 띄어쓰기 분리해줌


a = input("문자열을 입력하시오: ")  # 크기 비교해줌. 한글,알파벳순
b = input("문자열을 입력하시오: ")
if a < b:  # (a<b) 해도됨
    print(a, "가 앞에 있음")
else:
    print(b, "가 앞에있음")


# 머리 글자어 만들기 split 이용

phrase = input("문자열을 입력하시오: ")

acronym = ""
for word in phrase.upper().split():  # upper 대문자 변경
    acronym += word[0]
print(acronym)


# 문자, 공백, 숫자 개수 분석
sentence = input("문자열 입력: ")
table = {"alphas": 0, "digits": 0, "spaces": 0}

for i in sentence:
    if i.isalpha():
        table["alphas"] += 1
    if i.isdigit():
        table["digits"] += 1
    if i.isspace():
        table["spaces"] += 1
print(table)
