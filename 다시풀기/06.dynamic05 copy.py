# 금광 
'''
N X M 크기의 금광이 있다. 1 X 1 크기의 칸으로 나뉘어져있다.

채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
맨 처음에는 첫 번쨰 열의 어느 행에서든 출발할 수 있습니다.
이후에는 m-1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

입력
첫째 줄에 테스트 케이스 T 가 입력됩니다.

매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <=n, m <= 20)
둘째 줄에 n X m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력 1<= 각 위치에 매장된 금의 개수 <= 20
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

출력
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력
19
16
'''
'''
# 내가 푼 것 > 못 풀었음
n, m = 4, 4
array = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]

d = [0] * (n*m)

for j in range(m) :
    for i in range(n) : 
        d[i*n] = array[i*n]
        print(d[i*n],"==================")
        
        if i*n >= m-1 :
            d[i-(m-1)] = max(d[i-(m-1)], d[i]+array[i-(m-1)])
            print("오른쪽 위 : ", d[i-(m-1)])

        if i*n + m+1 <= n*m :
            d[i+(m+1)] = max(d[i+(m+1)], d[i]+array[i+(m+1)])
            print("오른쪽 아래 :", d[i+(m+1)])

        d[i+1] = max(d[i+1], d[i]+array[i+1])
        print("오른쪽 : ", d[i+1])

print(d)
'''

# 세 가지 중 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해준다.
# 인덱스가 벗어나지 않는지 확인한다.

for tc in range(int(input())) :
    # 금광 정보 입력
    # n, m = map(int, input().split())
    # array = list(map(int, input().split()))
    n, m = 4, 4
    array = [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]
    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n) :
        dp.append(array[index:index+m])
        index += m
    print(dp)
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m) :  # 열
        for i in range(n) : # 행
            # 왼쪽 위에서 오는 경우
            if i == 0 : # 첫번째 행에서는 윗줄이 없기 때문에 해당 경우가 없다.
                left_up = 0
            else :
                left_up = dp[i-1][j-1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n-1 :   # 마지막 행에서는 아랫줄이 없기 때문에 해당 경우가 없다.
                left_down = 0
            else :
                left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]

            # 3가지를 비교해서 가장 큰 값과 해당 자리에 있는 금광의 수를 더한다.
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)

result = 0
for i in range(n) :
    result = max(result, dp[i][m-1])
print(result)

