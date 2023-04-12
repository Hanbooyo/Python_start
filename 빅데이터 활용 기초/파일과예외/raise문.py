try:
    print("예외 시작")  

    raise Exception("일부러 발생")

    print("예외 끝")

except Exception as e :
    print(e)