squares = []

for x in range(10):
    squares.append(x*x)

print(squares)

squares2 = [x*x for x in range(10) if x % 2 == 0]

print(squares2)

# 이와 같음
#  b = []
#  for x in range(10) : 
#      if x % 2 ==0:
#        b.append(x*x)  



a = [x*y for x in range(10) for y in range(10)]
print(a)