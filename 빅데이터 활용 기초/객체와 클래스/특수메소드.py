# 특수메소드는 __ __ 언더바가 양쪽에 들어감

# 특수메소드는 어떤 이벤트가 실행되었을때 수행하는 메소드

class Counter:
    def __init__(self,value):
        self.count = value
    
    def __eq__(self, other): # equal
        print("eq메소드 실행")
        return self.count == other.count
    
    def __str__(self): #일반적으로 객체의 데이터를 String으로 만들어 반환한다
        return "객체 출력!"

a = Counter(10)
b = Counter(10)

print("=============================")
print(a==b)

print(a) #__str__ 없이 찍으면 0xf4sdf32d 이렇게 나옴

