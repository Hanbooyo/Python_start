a = {1: 'a'}
a['name'] = "익명"

b = {1 : "김연아", 2:"박지성", 3:"박찬호"}

print(a)
print(b.keys())
print(b.values())
print(b.items())
#리스트와의 차이는 역시 Key, Value 형태의 구성이다
#java Map처럼 get() 함수 가능
for k in b.keys():
    print(k)