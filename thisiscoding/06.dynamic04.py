# 효율적인 화폐 구성
'''
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
M원을 만들기 위한 최소한의 화폐 개수를 구하여라

1<=N<=100, 1<=M<=10000
불가능할 떄는 -1을 출력

2 15
2
3
>> 5

3 4
3
5
7
>> -1
'''
# 못 풀었음
# 문제 풀이

n, m = map(int, input().split())
array = []
for i in range(n) :
    array.append(int(input()))

d = [10001] * (m+1) # 10001 : INF 값이 없음을 의미한다.
d[0] = 0

for i in range(n) :
    for j in range(array[i], m+1) :
        if d[j - array[i]] != 10001 :   # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])
