#### bool 자료형
# True, False
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(1==1 )    # True
print(3>1)      # True
print(1>10)     # False

#### 자료형의 참, 거짓
# 비어있으면 거짓, 요소가 있으면 참
if []:          # 비어있기 때문에 >> 거짓
    print("참")
else :
    print("거짓")

if [1,2,3] :    # 안에 요소가 있기 때문에 >> 참
    print("참")
else :
    print("거짓")

#### bool 연산
print(bool('iloveyou')) # True
print(bool(''))         # False
print(bool([1,2,3]))    # True
print(bool([]))         # False
print(bool(0))          # False
print(bool(6))          # True
