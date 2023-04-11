class Car:
    def __init__(self, model, color, year, price) -> None:
        self.model = model
        self.color = color
        self.year = year
        self.price = price

newCar = Car("Genesis","Green","2023","6800")

print("자동차의 모델은",newCar.model)
print("자동차의 색상은",newCar.color)
print("자동차의 연식은",newCar.year)
print("자동차의 가격은",newCar.price)