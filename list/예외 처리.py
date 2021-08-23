while True:
    try:
        n = input("숫자를 입력하시오: ")
        n = float(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오.")


# try:
#     name = input("파일이름을 입력하세요: ")
#     file = open(name,"r")
# except IOError:
#     print("파일을 발견할수 없다.")
# except ValueError:
#     print("문법오류")
# else:
#     print("성공")
# finally:
#     file.close()
