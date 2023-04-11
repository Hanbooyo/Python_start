class Car:
    def __init__(self, model, color, year, price) -> None:
        self._model = model
        self._color = color
        self._year = year
        self.__price = price
    #파이썬에서 인스턴스 변수를 private로 정의하려면
    # 변수 이름 앞에 __ (언더바 두개)를 붙이면 된다
    # __ 은닉화 된 정보는 Getter Setter로 접근

    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price

newCar = Car("Genesis","Green","2023","6800")

print("자동차의 모델은",newCar._model)
print("자동차의 색상은",newCar._color)
print("자동차의 연식은",newCar._year)
print("자동차의 가격은",newCar.getPrice()) #접근 제한자떄문에 getter로 접근