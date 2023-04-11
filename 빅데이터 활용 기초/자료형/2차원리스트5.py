matrix = [['하나','둘','셋'],['넷','다섯','여섯'],['일곱','여덟','아홉']]
a = 1
for i in matrix: #matrix의 요소를 i에 
    for j in i: # i의 요소를 j에
        print(a,j)
        a+=1

