import matplotlib.pyplot as plt  # matplotlib의 pyplot을 앞으로 plt라고 하겠다는 선언

X = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
Y1 = [15, 14, 16, 18, 17, 15, 19]
Y2 = [20, 23, 23.5 ,25, 23, 24, 26]


plt.plot(X,Y1, label="Seoul")
plt.plot(X,Y2, label="Busan")
plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(loc="upper left") # 왼쪽 위에 띄워줌
plt.title("Temperatures of Cities")
plt.show()
