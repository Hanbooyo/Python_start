#%%
import matplotlib.pyplot as plt  
# matplotlib의 pyplot을 앞으로 plt라고 하겠다는 선언
X = [1,2,3,4,5,6,7]
Y = [15, 14, 16, 18, 17, 15, 19]
Z = ['M', 'T', 'W', 'T', 'F', 'S', 'S']

plt.plot(X,Y)
plt.xlabel("day")
plt.ylabel("temperature")
plt.show()
