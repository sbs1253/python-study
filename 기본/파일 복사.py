# # 텍스트 파일 복사
# infilename = input("입력 파일 이름: ")
# outfilename = input("출력 파일 이름: ")

# infile = open(infilename,"r")
# outfile = open(outfilename,"w")

# s= infile.read()
# outfile.write(s)

# infile.close()
# outfile.close()

# 이진 파일 복사
infilename = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")

infile = open(infilename, "rb")
outfile = open(outfilename, "wb")

# 입력 파일에서 1024byte 씩 읽어서 출력 파일에 쓴다.
while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
