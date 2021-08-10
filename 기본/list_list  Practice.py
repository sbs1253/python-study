heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치", ]
heroes[1] = "닥터 스트레인지"  # 배열 자리를 변경
print(heroes)

heroes.append("캡틴 아메리카")  # 뒷부분에 추가
print(heroes)

heroes.insert(1, "베트맨")  # 배열 번호 안에 추가
print(heroes)

heroes.remove("헐크")  # 배열안에 항목 삭제
print(heroes)

if '슈퍼맨' in heroes:  # 슈퍼맨이 있다면 삭제 > 없다면 오류나기 때문에 이용
    heroes.remove("슈퍼맨")

del heroes[1]  # 배열 번호 항목 삭제
print(heroes)

last_hero = heroes.pop()  # 마지막 항목 삭제, 리턴값도 줌
print(last_hero)
print(heroes)

print(heroes.index("스칼렛 위치"))  # 항목의 위치를 확인 시켜줌

for hero in heroes:  # 리스트 순서대로 출력(방문)
    print(hero)

heroes.sort()  # 알파벳, 한글, 숫자 순으로 정렬. reverse()는 값을 역순으로 정렬
print(heroes)

print(heroes.pop(0))  # 배열 인덱스 항목 삭제
print(heroes)

# 리스트.extend([]) 는 여러값 추가 할수 있음. 리스트 += 값 과 같은것임
