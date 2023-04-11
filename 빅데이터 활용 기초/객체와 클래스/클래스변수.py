class Counter:
    value = 0
    def __init__(self):
        Counter.value += 1
        self.count = Counter.value

a = Counter() # 선언과 동시에 0에서 +1

print(a.count) 

b = Counter()

print(b.count) #이미 a선언시점에 +1된 상태라 2가됨
