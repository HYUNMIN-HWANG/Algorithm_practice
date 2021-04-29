# 수 정렬하기2
'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
5
5
4
3
2
1

출력 
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
1
2
3
4
5
'''
# 파이썬 라이브러리 사용
# n = int(input())
# arr = []
# for i in range(n) : 
#     arr.append(int(input()))
# arr.sort()
# print(arr)
# >>>>>>>>>>>>>>> 시간초과

# 퀵 정렬 사용
# n = 5
# arr = [5,4,3,2,1]

# def quick_sort(arr) :
#     if len(arr) <= 1 :
#         return arr
    
#     pivot = arr[0]
#     tail = arr[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x >= pivot]

#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# for i in arr :
#     print(i)
# >>>>>>>>>>>>>>> 시간초과

# 파이썬에 내장된 sorted 기는 사용
# sys.stdin.readline(), sys.stdout.write()
import sys
n = int(input())
arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr) :
    sys.stdout.write(str(i)+'\n')