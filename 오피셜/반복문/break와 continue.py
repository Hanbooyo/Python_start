
#break
i=0

while True:
    if i>10:
        break
    else:
        i+=1
        print(i)

#continue
for i in range(1, 11):
    if i%3 == 0:
        continue
    print(i,end=" ")

#continue는 해당부분을 만나면 바로 반복문으로 올라감. ( 그다음부터 )