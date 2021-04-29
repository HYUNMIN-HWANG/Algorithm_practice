# 떡볶이 떡 만들기
'''
입력 
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다.
둘째 중에는 떡의 개별 높이가 주어집니다.
떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있습니다.
높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.

4 6
19 15 10 17

출력 :
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 최댓값을 출력합니다.
15

- 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정
- 현재 이 높이로 자르면 조건을 만족할 수 있는가? 확인한 뒤, 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
- 큰 탐색 범위를 보면 "이진 탐색"

- 시작점 0, 끝점 19, 중간점 9
- 이때 찾고자 하는 떡의 크기 : 6
- 잘려진 떡의 크기와 찾고자 하는 떡의 크기를 비교한다.

- 중간점은 시간이 지날수록 '최적화된 값'이 된다.
'''
def binary_sort(arr, target, start, end) :
    if start > end : 
        return None
    
    mid = (start + end) // 2

    len_sum = 0
    for i in arr :
        if i > mid :
            len_sum += (i - mid)
    # 떡의 양이 충분한 경우, 오른쪽 탐색
    if len_sum > target :
        return binary_sort(arr, target, mid+1, end)
    # 딱 맞는 떡의 양이 주어진 경우, 중간값 return 
    elif len_sum == target :
        return mid
    # 떡의 양이 부족한 경우, 왼쪽 부분 탐색
    else :
        return binary_sort(arr, target, start, mid-1)

n, m = map(int, input().split())
len = list(map(int, input().split()))
print(len)

start = 0       # 시작점
end = max(len)  # 끝 점
print(end)

point = binary_sort(len, m, start, end)
if point == None :
    print("원소가 존재하지 않습니다.")
else :
    print(point)