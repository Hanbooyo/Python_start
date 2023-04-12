class Car: #부모 클래스
    def __init__(self, make, model, color, price):
        self.make = make
        self.color = color
        self.model = model
        self.price = price
    
    def setMake(self, make): #설정자 메소드
        self.make = make
    
    def getMake(self):  #접근자 메소드
        return self.make
    
    #차량에 대한 정보를 문자열로 요약하여서 반환한다.

    def getDesc(self):
        return "차량 = ("+str(self.make)+","+\
                str(self.model)+","+\
                str(self.color)+","+\
                str(self.price)+")"
    
newCar = Car("KIA","K9","white","6500")
print(newCar.getDesc())

class ElectricCar(Car): #Car상속
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize =batterySize

    def getBatterySize(self): # 매개변수 X
        return self.batterySize
    
myCar = ElectricCar("Teslaa", "Model S", "Blue", 10000, 2)
myCar.setMake("Tesla")
myCar.setBatterySize(60)
print(myCar.getDesc())