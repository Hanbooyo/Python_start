import numpy as np

ages = np.array([18,19,25,30,28])

#ages 에서 20세 이상만 고르는 조건식

y = ages > 20

print(y)

#논리적인 인덱싱

ages[ages > 20]*3

print(ages[ages > 20]*3)