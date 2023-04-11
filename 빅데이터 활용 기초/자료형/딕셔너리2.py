capitals = { "Korea": "Seoul", "USA": "Washington", "UK": "London"}

print(capitals.items()) # 키 값 다 나옴
print(capitals.keys()) # 키만 나옴
print(capitals.values()) # 밸류만 나옴

print(list(capitals.items())[0]) # 리스트로 변환후 인덱싱 가능
# => 반복문 응용 가능