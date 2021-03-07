#### 변수
# python 변수 : 자료형을 따로 지정하지 않아도 된다.
a = [1,2,3]
print(id(a))    # 메모리 주소 : 1943988264512
b = a
print(id(b))    # 메모리 주소 : 1943988264512 (a와 동일함)

print(a is b)   # True : a와 b는 동일하다

a[1] = 4
print(a)        # [1, 4, 3]
print(b)        # [1, 4, 3] : a가 바뀔 때 b도 같이 바뀐다.

#### a 변수의 값을 가져오면서 a와 다른 주소를 가리키는 변수 b만들기
# 1) [:] 사용
a = [1,2,3]
b = a[:]
print(a is b)   # False >> a와 b는 다르다.
a[1] = 4
print(a)        # [1, 4, 3]
print(b)        # [1, 2, 3]

# 2) copy 모듈 사용
from copy import copy
a = [1,2,3]
b = copy(a)
print(a is b)   # False >> a와 b는 다르다.
a[1] = 4
print(a)        # [1, 4, 3]
print(b)        # [1, 2, 3]

#### 변수 만들기
a, b = ('python','life')
print(a)    # python
print(b)    # life

[a, b] = ['python', 'life']
print(a)    # python
print(b)    # life

a = b = 'python'
print(a)    # python
print(b)    # python

# 두 변수 바꾸기
a = 3
b = 5
a, b = b, a
print(a)    # 5
print(b)    # 3
