class Avante:   # 아반떼 설계도// 차 속성은 가격만 설정
    def __init__(self, price): #initialization 함수, 특수메소드
        print("객체 생성 완료")
        print(2500)

oshAvante = Avante(2500)

# 객체 - 사물
# 클래스 
# 인스턴스 - 클래스로부터 찍어낸 객체


class Sonata:
    def __init__(self, price, color) -> None:
        self.price = price
        self.color = color
    
    def driving(self):
        print("주행을 시작합니다.")

hbySonata = Sonata(3300, 'red')
kcsSonata = Sonata(2500, 'black')

print(hbySonata.price)
print(hbySonata.color)

hbySonata.driving() # 함수호출할때는 괄호
# Sonata.driving(hbySonata) 라는 뜻