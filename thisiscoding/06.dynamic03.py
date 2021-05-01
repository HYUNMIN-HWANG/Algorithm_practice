# 1로 만들기
'''
정수 x가 주어졌을 때
1. x가 5로 나누어떨어지면, 5로 나눈다.
2. x가 3으로 나누어떨어지면, 3으로 나눈다.
3. x가 2로 나누어떨어지면 2로 나눈다.
4. x에서 1을 뺀다.

연산 4개를 사용해서 값을 1로 만든다.
연산을 사용하는 횟수의 최솟값을 출력하세요

26 -> 3
'''
"""
x = 26
d = [0] * 30000

d[2] = 1
d[3] = 1
d[5] = 1


def make(x) :
    if type(x) != int :
        # print("float")
        pass
    else :         
        if x == 1 :
            print("1이다!")
            d[x] += 1
            return d[x]

        d[x] = min(make(x/5), make(x/3), make(x/2), make(x-1))
        return d[x]

print(make(26))
    모르겠다 ㅠㅠ
"""

# # 문제 풀이
# x = int(input())

# d = [0] * 30001

# for i in range(2, x+1) :
#     # 현재의 수에서 1을 빼는 경우
#     d[i] = d[i-1] +1
#     # 현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0 :
#         d[i] = min(d[i], d[i//2]+1)
#     # 현재의 수가 3으로 나누어 떨어지는 경우
#     if i % 3 == 0 :
#         d[i] = min(d[i], d[i//3]+1)
#     # 현재의 수가 5로 나누어 떨어지는 경우 
#     if i % 5 == 0 :
#         d[i] = min(d[i], d[i//5]+1)
# print(d[:50])
# # print(d[x])
# print(d[4])

# 다시 풀기
n = int(input())

d = [0] * 30000

for i in range(2, n+1) :
    d[i] = d[i-1] + 1

    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5]+1)

print(d[n])
    

