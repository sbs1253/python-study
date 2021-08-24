import random

guesses = ""
turns = 30

infile = open("", "r")
lines = infile.readlines()
word = random.choice(lines)

while turns > 0:
    failed = 0
    for char in word.rstrip():
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
    if failed == 0:
        print("\n승리")
        break
    print("")
    guess = input("단어 입력: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("틀림")
        print(str(turns)+'번의 기회가남음')
        if turns == 0:
            print("졌다. 정답은"+word)
infile.close()


# 아직 뭔가 이상하므로 수정 필요
