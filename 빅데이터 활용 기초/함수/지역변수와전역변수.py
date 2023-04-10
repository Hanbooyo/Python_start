#전역변수 호출하기


gx = 100
g = 200

def myfunc():
    global gx #전역변수 호출 예약어 global
    gx = g 
    print(gx)

myfunc()
print(gx)


#일반적으로 지역변수는 함수내에서 선언된 변수를 일컫음
#전역변수는 함수 바깥에 선언됨. 호출하여 사용할땐 global 사용