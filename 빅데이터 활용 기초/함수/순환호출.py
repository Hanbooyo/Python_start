#재귀 호출
def factorial(n):
    if n==1:
        return(1)
    else:
        return n * factorial(n-1)
    
print('n', "!=", factorial(10))