#s = input("문자열 입력: ")
s = "여보안경안보여"
#s = "여보게저기저게보여"
s1 = s[::-1] # 역순정렬

if (s==s1):
    print("회문입니다")
else:
    print("회문이 아닙니다.")