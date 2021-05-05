from collections import deque


def solution(board):
    n = len(board)
    visited = [[1000000 for _ in range(n)] for _ in range(n)]
    ds = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    q = deque()
    q.append((0, 0, 0, -1))
    visited[0][0] = 0
    while q:
        y, x, c, t = q.popleft()
        for i in range(4):
            ay, ax = y + ds[i][0], x + ds[i][1]
            if 0 <= ay < n and 0 <= ax < n and not board[ay][ax]:
                if t == i or t == -1:
                    if visited[ay][ax] >= c + 100:
                        visited[ay][ax] = c + 100
                        q.append((ay, ax, c + 100, i))
                elif t != i:
                    if visited[ay][ax] >= c + 600:
                        visited[ay][ax] = c + 600
                        q.append((ay, ax, c + 600, i))
    answer = visited[n - 1][n - 1]
    return answer


# 위에 꺼 참고한 나의 풀이
from collections import deque

def solution(board):
    queue = deque()
    queue.append((0,0,0,-1))    # x, y, cost, 방향
    
    n = len(board[0])
    
    visited = [[1000000] * n for _ in range(n)]
    visited[0][0] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue :
        x, y, c, t = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i] 
            
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] : 
                if t == i or t == -1  : # 방향이 같다. 직선거리 
                    if visited[nx][ny] >= c + 100 :     # 최소 가격으로 갱신하기 위함
                        visited[nx][ny] = c + 100
                        queue.append((nx, ny, c + 100, i))
                elif t != i :   # 방향이 달라짐. 곡선거리
                    if visited[nx][ny] >= c + 600 : 
                        visited[nx][ny] = c + 600
                        queue.append((nx, ny, c + 600, i))
                
    answer = visited[n-1][n-1]
    return answer
