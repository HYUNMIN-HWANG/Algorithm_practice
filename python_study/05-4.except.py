########## 예외처리

# [1] try ~ except
# 오류가 발생하면 except 문을 실행시킨다.
# except 발생오류 as 오류 메세지 변수 : 오류가 발생했을 때 오류 메세지 변수로 오류 내용을 알려준다.

# [2] try ~ finally
# try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.


try : 
    a = [1, 2]
    print(a[3])    
    4 / 0 
except ( IndexError , ZeroDivisionError) as e  :
    # print("인덱싱할 수 없습니다.")
    # print("0으로 나눌 수 없습니다.")
    print(e)
# finally :
    # f.close()

print("=============")
########## 오류 회피하기
try :
    f = open('No file.txt', 'r')
except FileNotFoundError :  # 파일이 없더라도 오류를 발생시키지 않고 통과한다.
    pass


########## 오류 발생시키기
class Bird :
    def fly (self) :
        raise NotImplementedError   # 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 발생시킴

# class Eagle (Bird) :
    # pass

# eagle = Eagle()
# eagle.fly() # NotImplementedError >> Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird에 있는 fly 함수가 실행되고 오류가 발생함

class Eagle (Bird) :
    def fly(self) :
        print("very fast")

eagle = Eagle()
eagle.fly() # very fast

print("=============")

# 예외 만들기
class MyError(Exception) : # Exception 클래스 상속
    def __str__ (self) :    # 오류 메세지 출력 : print(e) 처럼 오류 메세지를 print문으로 출력할 경우에 호출되는 메서드
        return "허용되지 않은 별명입니다."
    pass

def say_nick(nick) :
    if nick == 'babo' :
        raise MyError()
    print(nick)

try : 
    say_nick('angle')   # angle
    say_nick('babo')    # __main__.MyError >> 허용되지 않은 별명입니다.
# except MyError : 
    # print("허용되지 않은 별명입니다.")
except MyError as e :
    print(e)    # 허용되지 않은 별명입니다.

