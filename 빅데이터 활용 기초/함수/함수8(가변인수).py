#딕셔너리

def myfunc(**kwargs):
    print(kwargs)
    result=""
    for arg in kwargs.values():
        result += arg
    return result

print(myfunc(ace = "Hi!", bee="Mr.", name="Kim"))

#values를 이용한 value값을 출력 