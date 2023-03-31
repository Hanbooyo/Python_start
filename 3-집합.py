s1 = set([1,2,3]) # set을 이용한 정의
s2 = {1,2,3} # 중괄호를 이용한 정의
print(s1)

#집합은 중복된 요소를 불허한다.
#순서가 없다 (Unordered)

l = [1,2,3,3,4,5]
newList = list(set(l)) # 중복이 없어진 list가 됨
s = "Hello"
sList = list(set(s))
print(newList)
print(sList)