# from hangman.game import *
# from hangman.set_word import *
# from hangman.setting import *

# word = Set_word()
# turns = Setting()
# print(Check(turns, word))
# 위에껀 상위 폴더에서 불러오는 것

# game에서 *(모든것) 불러온다.
from game import *
from set_word import *
from setting import *

word = Set_word()
turns = Setting()
print(Check(turns, word))
