#04-1. 함수

#함수를 사용하는 이유 : 똑같은 내용을 반복해서 작성하기 위함
#매개변수(함수에 입력으로 전달된 값을 받는 변수)
#인수(함수를 호출할 때 전달하는 입력값)



#기본적인 함수 구조
def add(a, b) : # a, b : 매개변수
    return a+b
print(add(3,4)) # 3, 4 : 인수



#함수의 형태
#1. 일반적인 함수 : 입력값이 있고 결괏값이 있는 함수
def add2(a, b) :
    result = a+b
    return result

#2. 입력값이 없는 함수
def say() :
    return 'Hi'

#3. 결괏값이 없는 함수 (return 명령어가 없음)
def add3(a, b) :
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

#4. 입력값도 결괏값도 없는 함수
def say2() :
    print("Hi")



#여러 개의 입력값을 받는 함수 -> *매개변수 (*를 붙이면 입력값을 전부 모아서 튜플로 만들어 줌)
def add_many(*args) :
    result = 0 
    for i in args :
        result = result + i
    return result



#함수의 결괏값은 하나
#1.튜플 값에 두 결과값이 저장됨 
def add_and_mul(a,b) :
    return a+b, a*b 
result1, result2 = add_and_mul(7,12) #result = 7, result=12가 저장된다.

#2.두 개의 return 명령어 사용하면 처음있는 return만 시행됨
def add_and_mul2(a,b) :
    return a+b
    return a*b
result = add_and_mul2(2,3) #result = 5 (곱셈 결과는 안 나온다.)



#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True) : 
    # man이라는 변수에 입력값이 주어지지 않는다면 초깃값은 True , 초기화시키고 싶은 매개변수를 항상 뒤쪽에 위치해야 함
    print("나의 이름은 %s입니다." % name)
    print("나의 나이는 %d살 입니다." % old)
    if man :
        print("남자입니다.")
    else : 
        print("여자입니다.")


#함수 안에서 선언한 변수의 효력 범위
#함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과 전혀 상관이 없다.
# global 명령어 : 함수 안에서 함수 밖의 변수를 직접 사용하겠다. (그다지 잘 사용되지는 않는다.)


#lamda
#함수를 생성할 때 사용하는 예약어, def와 동일한 역할을 한다, return 명령어가 없어도 결괏값을 덜려준다.
add4 = lambda a, b : a+b
result = add(3,4)
