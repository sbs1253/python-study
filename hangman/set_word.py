import random


def Set_word():
    file_location = open("", "r")
    lines = file_location.readlines()
    word = random.choice(lines)
    file_location.close
    return word.rstrip()
