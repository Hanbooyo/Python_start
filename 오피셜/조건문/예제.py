Richter = float(input("리히터 규모를 입력해주세요: "))
#Richter = 4.0

if Richter < 2.0:
    print("지진계에 의해서만 탐지 가능합니다")
elif Richter < 3.9 and Richter >= 2.0:
    print("물건이 흔들리거나 떨어집니다")
elif Richter < 6.9 and Richter >= 4.0:
    print("빈약한 건물은 큰 피해가 있습니다")
elif Richter < 7.9 and Richter >= 7.0:
    print("지표면에 균열이 발생합니다")
else:
    print("대부분의 구조물이 파괴됩니다.")