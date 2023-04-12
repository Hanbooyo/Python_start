# 파일객체 = open(파일이름, 파일모드)
#파일모드 r  읽기        w 쓰기(append와 다른점은 쓰면 이전내용이 지워짐)          a 추가모드    r+ 읽기와 쓰기모드


# infile = open("빅데이터 활용 기초\파일과예외\input.txt","r", encoding='UTF-8')
infile = open("빅데이터 활용 기초\파일과예외\input.txt","r", encoding='UTF-8')
print(infile)
print(infile.read()) #전부 다 읽음, 통째로
infile.close()

print("================================")

infile = open("빅데이터 활용 기초\파일과예외\input.txt","r", encoding='UTF-8')
print(infile.readline()) # 한줄씩 읽음
infile.close()

print("================================")
infile = open("빅데이터 활용 기초\파일과예외\input.txt","r", encoding='UTF-8')
print(infile.readlines()) # 줄 수만큼의 요소를 리스트로 반환
infile.close()