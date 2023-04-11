# 0부터 99까지 정수중에서 2의 배수이면서 동시에 3의배수들을 리스트로

numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]

print(numbers)

nums = [x*y for x in range(5) for y in range (5)]

print(nums)

alist = ['짝수' if i%2 == 0 else '홀수' for i in range(10)]

print(alist)