# infile= open("","w")

# infile.write("good\n")
# infile.write("god\n")
# infile.write("good\n")

# infile.close()

# infile= open("","a")

# infile.write("good\n")

# infile.close()


# {공백을 제거 한 단어들 출력

infile = open("", "r")

print(infile.read())

infile.close()

# infile= open("","r")

# for line in infile:
#     line= line.rstrip()  # 공백을 제거 해준다. r은 오른쪽 공백, l은 왼쪽 공백
#     word_list= line.split()
#     for word in word_list:
#         print(word)
# infile.close()  }
