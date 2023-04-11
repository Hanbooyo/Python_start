class Counter:
    def __init__(self, initValue): # initValue(매개변수값으로)
        self.count = initValue # count 를 initValue값으로 초기화
    
    def increment(self):
        self.count += 1