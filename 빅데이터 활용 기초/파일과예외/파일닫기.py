try: #예외가 발생할 가능성이 있는 작업들은 여기에 둔다
 f = open("빅데이터 활용 기초\파일과예외\est.txt","w", encoding='UTF-8')
 #여기서 작업 이것저것
finally: #예외가 발생하더라도 반드시 실행
 f.close()


with open("빅데이터 활용 기초\파일과예외\est.txt","w", encoding='UTF-8') as f:
 f.write("김자영\n")
 f.write("김영희\n")
