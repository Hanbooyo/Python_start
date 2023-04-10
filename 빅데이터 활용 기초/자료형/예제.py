before = [10.0,9.0,8.3,7.1,3.0,9.0]

def solver(lst):
    print("제거 전 :",lst)
    lst.remove(max(lst))
    lst.remove(min(lst))
    print("제거 후 : ",lst)

solver(before)