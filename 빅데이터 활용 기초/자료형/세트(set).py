#세트의 초기화는 
values = set()
# vlaues = {} 이렇게 하면안된다.


# all() 
# any() 
# enumerate()
# len() # 길이
# max() # 최대값
# values.add() #추가
# values.remove() #삭제
# in  으로 특정값이 있는지 확인가능


# 세트도 컴프리핸션 가능
aList = [1,2,3,4,5,1,2]
result = { x for x in aList if x%2 == 0}
print(result)

# 세트(집합)은 중복을 허용하지않는다, 따라서 2,4 만 출력 (2가 두번 나오지 않음)