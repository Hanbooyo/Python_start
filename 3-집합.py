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

# add, 여러개는 update를 이용해 추가 (중복되는것은 자동으로 걸러짐)
# remove 로 원소삭제