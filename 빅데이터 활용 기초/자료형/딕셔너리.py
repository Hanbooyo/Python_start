#딕셔너리 (Java 의 HashMap과 비슷함)

# 딕셔너리 규칙
# 딕셔너리의 키는 수정이 불가능한 타입만 가능.
# 숫자, 문자열, 튜플 등

#딕셔너리 이름 = { 키1:값1, 키2:값2 ....}
capitals = { "Korea": "Seoul", "USA": "Washington", "UK": "London"}

#딕셔너리는 인덱싱을 번호가 아닌, key로 함

print(capitals["Korea"]) # Seoul

#딕셔너리 항목 추가

capitals2 = {} #초기화
capitals2["Korea"]="Seoul" # key를 인덱스처럼
capitals2["USA"]="Washington" # = 값
capitals2["UK"]="London"
capitals2["France"]="Paris"
capitals2["Japan"]="Tokyo"

print(capitals2)

#항목 삭제는 pop

c = capitals2.pop("Japan") #값을빼서 c에 넣음 (딕셔너리에서는 해당 값 제외됨)
print(c) # pop에 의해 빠진값의 value를 c에 저장함
print(capitals2)