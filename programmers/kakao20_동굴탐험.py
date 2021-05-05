import sys
sys.setrecursionlimit(1000000)

def solution(n, path, order):
    
    graph = [[0] * n for _ in range(n)]
    for x, y in path :
        graph[x][y] = 1
        graph[y][x] = 1
    # print(graph)
    
    visited = [0]
    
    def dfs(v) :     
        for i in range(n) :
            # print(i)
            if graph[v][i] == 1 :
                visited.append(i)
                # print(visited)
                if len(set(visited)) < n :      
                    dfs(i)
                    answer = False
                else :
                    answer = True
                    return answer
        print(visited)
        
    dfs(0)
    answer = True
    print(answer)
    return answer

solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])