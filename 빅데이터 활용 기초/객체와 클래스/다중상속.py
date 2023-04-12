class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

class Student:
    def __init__(self, id):
        self.id = id
    def getId(self):
        return self.id
    
class CollegeStudent(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self,name,age) # Super 대신에 각각 
        Student.__init__(self,id)       # 어디서 상속받는지 명시해줘야함

obj = CollegeStudent('Kim', 22, '100036')
obj.show()
print(obj.getId())