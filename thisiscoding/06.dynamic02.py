# 개미 전사
'''
문제
개미 전사는 식량 창고를 선택적으로 약탈하여 식량을 빼앗을 것이다.
창고를 고를 때 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야 한다.

개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하라

입력
첫째 줄 : 식량창고의 개수 N
두번째 줄 : 각 식량창고에 저장된 식량의 개수 K

출력
개미 전사가 얻을 수 있는 식량의 최댓값
'''
"""
# 내가 푼 알고리즘
n = 5
food = [1, 3, 1, 5, 2]

d = [0] * n
print("d=======", d)

def fx (food, x) :
    if x == 0 or x == 1 :
        d[x] = food[x]
        print("d[x]", d[x])
        return d[x]
    
    if d[x] != 0 :
        print("끝끝끝~")
        return d[x]
    
    d[x] = food[x] + fx(food,x-2)
    print("d[x]", d[x])

    return d[x]

print(len(food))
print(len(food)-1)

x1 = fx(food, len(food)-1)
x2 = fx(food, len(food)-2)
print("=====")
if x1 > x2 :
    print(x1)
else :
    print(x2)
"""

# 문제 풀이

n=int(input())
arr = list(map(int, input().split()))

d = [0] * 100

# 보텀업
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2] + arr[i])
# print(d)
print(d[n-1])


