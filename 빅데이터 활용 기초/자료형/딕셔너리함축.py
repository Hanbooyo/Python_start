values = [1,2,3,4,5,6]

dic =   { x : x**2 for x in values if x % 2 ==0}
#딕셔너리  출력수식        입력리스트   조건식

print(dic)



#추가 예시

dic2 = {i:str(i) for i in [1,2,3,4,5]}
print(dic2)