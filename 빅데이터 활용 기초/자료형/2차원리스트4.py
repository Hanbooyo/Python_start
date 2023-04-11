matrix = [[0,0,0], [1,1,1], [2,2,2]]

result = []

for row in matrix: # matrix 요소를 row 에
    for num in row: # row는 0,0,0  1,1,1  2,2,2 가 차례로들어가고  
                    # num에 0 0 0 1 1 1 2 2 가 각각 차례로
        result.append(num) # result에 각각
print(result)