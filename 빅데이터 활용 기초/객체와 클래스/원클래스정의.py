import math

# Cirlce 클래스 정의

class Circle:
    def __init__(self,radius) -> None:
        self.radius = radius

    def getAtrea(self):
        return math.pi * self.radius * self.radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
# Circle객체생성
c = Circle(10)
print("원의 면적 ", c.getAtrea())
print("원의 둘레 ", c.getPerimeter())