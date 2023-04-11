capitals = { "Korea": "Seoul", "USA": "Washington", "UK": "London"}

for key in capitals:
    print(key,":",capitals[key])

for k in capitals.items(): # items 요소를 통째로 k에 넣음
    print(k) # k에 key value 각각 들어가서 나옴


for k in sorted(capitals.keys()):
    print(k, end=" ")
print()

print("Korea" in capitals) # Key 값으로는 가능
print("Seoul" in capitals) # Value로는 불가능 (Key값 기준으로 조회하기때문)