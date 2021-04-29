# 좌표 정렬하기 https://www.acmicpc.net/problem/11650 
'''
문제
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
5
3 4
1 1
1 -1
2 2
3 3

출력 
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
1 -1
1 1
2 2
3 3
3 4
'''
import sys
n = 5
metrix = [[0,4],[1,2],[1,-1],[2,2],[3,3]]
# print(metrix)

# n = int(input())
# metrix = []
# for i in range(n) :
#     metrix.append(list(map(int, sys.stdin.readline().split())))


# 퀵 정렬
# print("===========")

# def sort(metrix) : 
#     if len(metrix) <= 1 :
#         return metrix

#     pivot = metrix[0][1]
#     pivot_xy = metrix[0]
#     tail = metrix[1:]

#     left_side = [x for x in tail if x[1] <= pivot]
#     right_side = [x for x in tail if x[1] > pivot]

#     return sort(left_side) + [pivot_xy] + sort(right_side)


# def sort2(metrix) : 
#     if len(metrix) <= 1 :
#         return metrix

#     pivot = metrix[0][0]
#     pivot_xy = metrix[0]
#     tail = metrix[1:]

#     left_side = [x for x in tail if x[1] <= pivot]
#     right_side = [x for x in tail if x[1] > pivot]

#     return sort(left_side) + [pivot_xy] + sort(right_side)

# result = sort2(sort(metrix))

# for x, y in result :
#     print(x, y)

# lambda
# metrix.sort(key=lambda x : (x[1], x[0]))
# print(metrix)

# x, y == y, x
n = int(input())
metrix = []
for i in range(n) :
    [x, y] = map(int, input().split())
    rev = [y, x]
    metrix.append(rev)

sort_met = sorted(metrix)
for a, b in sort_met :
    print(b, a)
# print(metrix)