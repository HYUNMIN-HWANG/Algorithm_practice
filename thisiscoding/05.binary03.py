# 정렬된 배열에서 특정 수의 개수 구하기
'''
- N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있을 때
x가 등장하는 횟수를 계산하세요.

입력
첫재 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
둘째줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
7 2

출력
수열의 원소 중에서 값이 x인 원소의 개수를 출력
단, 값이 x인 원소가 하나도 없다면 -1을 출력
1 1 2 2 2 2 3

시간복잡도 O(logN) 으로 동작하는 알고리즘을 요구하고 있음
선형 탐색으로 하면 시간 초과 판정받는다.
'''

n, x = map(int, input().split())    
arr = list(map(int, input().split()))


from bisect import bisect_left, bisect_right

def count_range(arr, right, left) :
    right_idx = bisect_right(arr, right)
    left_idx = bisect_left(arr, left)
    return right_idx - left_idx

num = count_range(arr, x, x)
if num == 0 :
    print(-1)
else :
    print(num)