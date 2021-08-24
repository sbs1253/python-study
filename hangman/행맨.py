
def Set_word():
    import random
    file_location = open("", "r")
    lines = file_location.readlines()
    word = random.choice(lines)
    file_location.close
    return word.rstrip()


def Setting():
    turns = int(input("횟수 입력: "))
    return turns


def Check(turns, word):
    def Input():
        guess = input(str(i+1)+"번째 단어 입력: ")
        while len(guess) > 1:
            print('한글자만 써 ')
            guess = input("단어 입력: ")
        return guess
    guesses = ''
    for i in range(turns):
        guesses += Input()
        score = 0
        result = ''
        # print("")

        for char in word:
            if char in guesses:
                print(char, end="")
                score += 1
                if score == len(word):
                    result = '\n승리'
                    return result
            else:
                print("_", end="")
            # print("틀림\n",str(turns)+"번의 기회 남음")

    #     if guess not in word:
    #         turns -= 1
    #         print("틀림")
    #         print(str(turns)+'번의 기회가남음'
        print()
    result = '패배'
    return result
# ----------------------------------------------------------


word = Set_word()
# word = 'about'
turns = Setting()
print(Check(turns, word))
