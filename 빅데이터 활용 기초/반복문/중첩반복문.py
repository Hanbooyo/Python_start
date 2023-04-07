for i in range(5):
    for j in range(5):
        print("i",i,"j",j)


for i in range(5):
    for j in range(5):
        if i>=j:
            print("*", end="")
    print("")