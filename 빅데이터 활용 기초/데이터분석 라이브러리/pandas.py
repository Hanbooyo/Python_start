# pandas 

# 시리즈

# 데이터프레임 (인덱스와 열 이름)
# 인덱스, colums, values

import pandas as pd
# pip install pandas
titanic = pd.read_csv("빅데이터 활용 기초\데이터분석 라이브러리\titanic.csv") # 절대경로

print(titanic)

titanic["Age"] 
print(type(titanic["Age"])) # 시리즈 타입

titanic[["Age"]] #이중 괄호를 하면 데이터 프레임 형태로 됨