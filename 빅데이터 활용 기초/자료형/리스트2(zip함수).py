# zip함수
a = ['a','b','c']
b = [1, 2, 3]

#for i, j in (a,b):
#    print(i,j)
# error

for i, j in zip(a,b):
    print(i, j) #언패킹


Q = ['name','quest','color']
A = ['Kim', '파이썬', 'blue']

for q, a in zip(Q,A):
    print(f"What is your {q}? it is {a}")