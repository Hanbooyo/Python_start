target = 2000
money = 1000
year = 0
rate = 0.07

#현재금액이 목표보다 작으면 반복
while money < target:
    money = money + money*rate
    year += 1

print(year, "년")