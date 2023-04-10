#default argument

def greet(name, msg="별일 없죠?"):
    print("안녕", name+","+msg)


print(greet("영희"))
print(greet("철수","집에가")) #msg 오버라이팅