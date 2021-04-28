# 수 정렬하기 https://www.acmicpc.net/problem/2750
'''
문제 :
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력 :
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
5
5
2
3
4
1

출력 :
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
1
2
3
4
5
'''
# [1] append 혹은 add 사용하기
# n = int(input())
# arr =set()
# for i in range(n) :
#     # arr.append(int(input()))
#     arr.add(int(input()))

# arr = list(arr)
# arr.sort()
# for n in arr :
#     print(n)

# [2] 삽입정렬
# n = 5
# arr = [5, 2, 3, 4, 1]

# for i in range(len(arr)) :
#     min = arr[i]
#     for j in range(i+1, len(arr)) :
#         if min > arr[j] :
#             min = arr[j]
#             arr[i], arr[j] = arr[j], arr[i]

# print(arr)

# [3] 버블정렬
n = 5
arr = [5, 2, 3, 4, 1]

for i in range (1, len(arr)) :
    while (i>0) & (arr[i] < arr[i-1]) :
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i -= 1

print(arr)