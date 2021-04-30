# 수 찾기 https://www.acmicpc.net/problem/1920
"""
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
5
4 1 5 2 3
5
1 3 7 9 5

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
1
1
0
0
1
"""
# from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# n = 5
# A = [4,1,5,2,3]
# m = 5
# B = [1,3,7,9,5]


A.sort()
# print(n,m)
# print(A, B)

def binary_search(arr, target, start, end) :
    
    if start > end : 
        # print("nothing")
        return None
    
    mid = (start + end) // 2
    # print("mid", mid)

    if arr[mid] == target :
        # print("find")
        return arr[mid]

    elif arr[mid] > target :
        # print("left >")
        return binary_search(arr, target, start, mid-1)

    else :
        # print("right >")
        return binary_search(arr, target, mid+1, end)

start = 0
end = n-1

for t in B :
    # print(t, "=============")
    result = binary_search(A, t, start, end)
    # print("result ::: ", result)
    if result == None :
        print(0)
    else :
        print(1) 
