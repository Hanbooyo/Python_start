A  = {"apple","banana"}
B = { "apple","banana","kiwi" }

print(A<B) # 또는 A.issubset(B)
if A < B:
    print("A는 B의 부분집합입니다.")

C = A & B #교집합 또는 C = A.intersection(B)
D = A - B #차집합 또는 D = A.difference(B)
F = A | B #합집합 또는 F = A.union(B)


# 리스트 세트변환

list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print(set(list1)&set(list2))
