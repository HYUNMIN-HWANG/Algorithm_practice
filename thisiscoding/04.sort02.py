# 두 배열의 원소 교체
'''
동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
동빈이는 최대 K번의 바뿨치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.
동빈이의 최종 목표는 A의 모든 원소의 합이 최대가 되도록 하는 것
N, K, 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오

N=5, K=3
A = [1,2,5,4,3]
B = [5,5,6,6,5]
답 26
'''
'''
# 선택정렬 : 하지만 시간 초과에 걸릴 수 있다.
n=5
k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
# n , k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

def sort1(arr) :    # 오름차순 정렬
    for i in range(len(arr)) :
        arr_min = arr[i]
        print(arr_min)
        for j in range(i+1, len(arr)) :
            if arr_min > arr[j] :
                arr_min = arr[j]
                print("chane >", arr_min)
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def sort2(arr) :    # 내름차순 정렬
    for i in range(len(arr)) :
        arr_max = arr[i]
        print(arr_max)
        for j in range(i+1, len(arr)) :
            if arr_max < arr[j] :
                arr_max = arr[j]
                print("chane >", arr_max)
                arr[i], arr[j] = arr[j], arr[i]
    return arr

A_up = sort1(a)
B_down = sort2(b)

print(A_up)
print(B_down)

for kk in range(k) :
    # print(kk)
    A_up[kk], B_down[kk] = B_down[kk], A_up[kk]

print(A_up)
print(B_down)
print(sum(A_up))
'''

# 파이썬 라이브러리 sort 사용
n=5
k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
# n , k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

a.sort()    # 오름차순으로 정렬
b.sort(reverse=True)    # 내림차순으로 정렬

print(a)
print(b)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k) :
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break

print(a)
print(b)
print(sum(a))
