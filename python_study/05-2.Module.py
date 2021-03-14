# import 모듈이름
import mod1
print(mod1.add(4,2))    # 6
print(mod1.sub(6,3))    # 3

# from 모듈이름 import 모듈함수
from mod1 import add, sub
print(add(5,5))     # 10
print(sub(10,5))    # 5

# 변수, 클래스 가져오기
import mod2
print(mod2.PI)  # PI 변수 >>  3.141592

a = mod2.Math() # Math 클래스 
print(a.solv(2))    # Math 클래스 내 함수 slov >> 2.566368

print(mod2.add(mod2.PI, 4.4))   # add 함수 >> 7.5415920000000005
