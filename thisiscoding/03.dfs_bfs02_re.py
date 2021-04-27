# 음료수 얼려 먹기
'''
N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫여 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요
다음의 4X5 얼음 틀 예시에서는 아이스크림이 3개 생성됩니다.
00110
00011
11111
00000

key : 연결 요소 찾기(인접한 노드의 개수)

입력 : 세로 길이 N, 가로 길이 M, 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다.
츌력 : 아이스크림 개수

1. 0이면서 아직 방문하지 않은 지점이 있다면 방문한다.
2. 방문한 지점에서 다시 상, 하, 좌, 우 살펴보면서 1번을 반복하면 연결된 모든 지점을 방문할 수 있다.
'''

# n, m 입력 받기
n, m = map(int, input().split())
# print(n, m)

# 2차원 리스트의 맵 정보 입력 받기
graph = []

for i in range(n) : 
    graph.append(list(map(int, input())))
print(graph)

# dfs 정의하기
def dfs (x, y) :
    if x <=-1 or x >= n or y <= -1 or y >= m :
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1

print(result)