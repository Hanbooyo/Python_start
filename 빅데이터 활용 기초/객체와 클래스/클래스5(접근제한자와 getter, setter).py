class Student:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age
    #파이썬에서 인스턴스 변수를 private로 정의하려면
    # 변수 이름 앞에 __ (언더바 두개)를 붙이면 된다
    # __ 은닉화 된 정보는 Getter Setter로 접근

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age    

newStd = Student("김학생",29)

print("학생의 이름은",newStd.getName())
print("학생의 나이는",newStd.getAge()) #접근 제한자떄문에 getter로 접근