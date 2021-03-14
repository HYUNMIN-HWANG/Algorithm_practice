# 모듈 : 함수, 변수, 클래스를 모아 놓는 파일
# 다른 파이썬 프로그램에서 불러와 사용할 수 있다.

def add(a, b) :
    return a + b
def sub(a, b) :
    return a - b

# 이 파일을 직접 실행할 때만 출력
# 해당 파일을 import 한 곳에서는 출력되지 않는다. 
if __name__ == "__main__" :
    print(add(1,4))
    print(sub(4,2))