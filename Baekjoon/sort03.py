# 수 정렬하기3 https://www.acmicpc.net/problem/10989

'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# import sys
# n = int(input())
# arr = []
# for i in range(n) :
#     arr.append(int(sys.stdin.readline()))

# print(arr)

import sys
n = 10
arr = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
# arr = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7, 1, 1, 1, 1, 1, 2, 2, 2]

"""
arr.sort()
for i in arr :
    print(i)
# >>>>>> 메모리 초과
"""

"""
def count_sort(arr) : 
    count = [0] * max(arr)
    # print(count)

    for i in range(n) : 
        count[arr[i]-1] += 1
    # print(count)

    for number in range(len(count)) :
        for time in range(count[number]) :
            # print(number+1)
            sys.stdout.write(str(number+1)+'\n')

def quick_sort(arr) :

    if len(arr) <= 1 :
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


if len(arr) < 15 :  # 계수 정렬
    count_sort(arr)

else :  # 퀵 정렬
    arr_sort = quick_sort(arr)
    for nn in arr_sort :
        print(nn)
# >>>>>> 메모리 초과
"""

# 계수 정렬 count수를 미리 고정시켜준다.
count = [0] * 10000
print(len(count))


for i in range(n) :
    input_num = int(sys.stdin.readline())
    count[input_num-1] += 1  # 입력되는 숫자는 1부터 시작하기 때문에 -1 한다.

print("==========")

for j in range(10000) :
    if count[j] != 0 :
        for time in range(count[j]) :
            print(j+1)
