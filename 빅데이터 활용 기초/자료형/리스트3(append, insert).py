#비어있거나 이미 값이있는 리스트에 값 추가 append

a = []

a.append("아이언맨")
a.append("헐크")

# 단점, 새 값이 뒤로 붙어서 생김
# 중간에 값을 삽입하고싶다면 insert 이용

a.insert(1,"캡틴아메리카")

print(a)

print(a.index("헐크"))