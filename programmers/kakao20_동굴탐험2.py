from collections import deque
import sys

sys.setrecursionlimit(1000000)

def find_cycle(start, parents, visited, recStack):
    # print("start ", start, ">>>>>>>>>>>>>>>>>>>>>>>>>")
    visited[start] = True
    # print("visted : ", visited)
    recStack[start] = True
    # print("recStack : ", recStack)

    for next_node in parents[start]:
        if not visited[next_node]:
            # print("find_cycle", next_node)
            if find_cycle(next_node, parents, visited, recStack):
                return True
        elif recStack[next_node] :
            return True

    print(start, end=' ')
    recStack[start] = False
    # print("final visited", visited)
    # print("final recStack", recStack)
    # print('-')
    return False

def solution(n, path, order):
    answer = True

    graph = [[] for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)    # [[1, 3, 7], [0, 8, 2], [1], [0, 6], [7], [7], [3], [0, 4, 5], [1]]

    q = deque()
    q.append(0)
    visited = [False] * n
    visited[0] = True
    parents = [[] for _ in range(n)]    # [[], [], [], [], [], [], [], [], []]
    # print(parents)

    while q:
        node = q.popleft()
        print("pop ::: ", node)

        for next_node in graph[node]:   # node에 연결된 노드들
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                parents[next_node].append(node)
        print("parent node > ", parents)
    print("============[while]============")

    for parent, child in order:
        parents[child].append(parent)
        print(parents)

    visited = [False] * n
    recStack = [False] * n

    print("============[find cycle]===========")
    for i in range(n):
        if not visited[i] :
            if find_cycle(i, parents, visited, recStack):
                return False

    return answer

solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]])