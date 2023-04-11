class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
#        print(self.x, other.x)
#        print(self.y, other.y)
#        print(self.x + other.x, self.y + other.y)
        return Vector2D(self.x + other.x, self.y + other.y)
#        print(test)
#        print(test.x)
#        print(test.y)

    def __str__(self):
        return f'({self.x},{self.y})'

u = Vector2D(0,1)
v = Vector2D(1,0)

result = u + v
print("result",u+v)