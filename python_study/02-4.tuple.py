#### 튜플의 항목 값은 변화가 불가능하다.
# t1 = (1,2,'a','b')
# del t1[1]
# TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c'
# TypeError: 'tuple' object does not support item assignment

#### 튜플 다루기
t1 = (1,2,'a','b')

#1. index
print(t1[0])    # 1
print(t1[3])    # b

#2. slicing
print(t1[1:])   # (2, 'a', 'b')

#3. plus
t2 = (3, 4)
print(t1+t2)    # (1, 2, 'a', 'b', 3, 4)

#4. mutiple
print(t2*3)     # (3, 4, 3, 4, 3, 4)

#5. length
print(len(t1))  # 4
