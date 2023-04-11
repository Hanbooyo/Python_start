#상속

class Car: #부모 클래스
    def __init__(self, Car_price, color, km):
        self.Car_price = Car_price
        self.color = color
        self.km = km

class Avante(Car): #자식클래스   (상속받음)
    def __init__(self, Car_price, color, km, year): #기존에 + year 추가
        super().__init__(Car_price, color, km)
        #super() => 부모  즉, Car()
        self.year = year

hbyAvante = Avante(3000, "white", "9,000km", "2023")

print(hbyAvante.Car_price)