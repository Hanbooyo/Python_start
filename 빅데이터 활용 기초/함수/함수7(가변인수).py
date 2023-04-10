#가변인수

def verfunc(*args):
    print(args)

def aa(*b):
    print(b)

verfunc("a", 120, "ff")
aa("b","c",1,2,3)

def test(*b):
    for i in b:
        print(i)

test(10,20,30)

# 튜플 타입으로 반환되기 때문에 응용가능

print("하나의 값")
verfunc(10)

print("여러개의 값")
verfunc(10,2,4,5,6)