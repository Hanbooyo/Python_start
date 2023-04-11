#튜플은 괄호를 써도되고 안써도됨
#원소 하나 인 튜플은 컴마가 필요함 
single_tuple = ("apple",)

# ☆ 튜플은 값 변경안됨
# 튜플 <> 리스트 타입변환 가능

# enumerate()
fruits = ["apple","banana","grape"]
for idx, v in enumerate(fruits):
    print(idx,v)
# [(0,"apple"),(1,"banana"),(2,"grape")]