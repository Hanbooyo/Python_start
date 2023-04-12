# 오버 라이딩 => 메소드를 상속받아서 재 정의
class 부모:
    def test(self):
        return "부모"

class 자식(부모):
    def test(self):
        return "자식"

# 오버 로딩 => 메소드 이름이 같고, 매개변수의 개수나 타입이 다름
# 파이썬에서는 오버로딩 지원 안함
# class Test:
#     def __init__(self):
#     
#     def overloading(a):
#     
#     def overloading(a, b):