# https://www.acmicpc.net/problem/1260
'''
DFS와 BFS

문제 : 
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력 : 
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4
========
5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5
=======
1000 1 1000
999 1000

1000 999
1000 999
'''
"""
# 내가 푼 것, 틀렸다고 나옴
n,m,v = map(int, input().split())
tmp_graph = []
for i in range(m) :
    input_list = list(map(int, input().split()))
    tmp_graph.append(input_list)
print(n,m,v)
print(tmp_graph)

graph = [[],]

for node in range(n) :
	same = []
	node = node + 1
	# print("node : ", node)

	for line in tmp_graph :
		if node == line[0] :
			same.append(line[1])
		if node == line[1] :
			same.append(line[0])
	same = list(set(same))
	# print(same)
	graph.append(same)
	# print("====")
print(graph)

visited = [False] * n
dfs_order = []

def dfs(graph, v, visited) :
	visited[v-1] = True
	print(v, end=' ')
	
	for i in graph[v] : 
		if not visited[i-1] :
			#print("스택에 넣기", i)
			dfs(graph, i, visited)
			#print("재귀")
			
dfs(graph, v, visited)

print()

from collections import deque

visited = [False] * n
bfs_order = []

def bfs(graph, v, visited) :
	queue = deque([v])
	#print(queue)
	visited[v-1] = True
	# bfs_order.append(v)
	
	while queue :
		n1 = queue.popleft()
		print(n1, end=' ')
		
		for i in graph[n1] :
			if not visited[i-1] : 
				queue.append(i)
				visited[i-1] = True
				
bfs(graph, v, visited)
# print(bfs_order)
"""

# 답안지
def dfs(v) :
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1) :
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

def bfs(v) :
    queue = [v]
    visit[v] = 0

    while queue :
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n+1) :
            if visit[i] == 1 and s[v][i] == 1 : 
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m) :
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1


dfs(v)
print()
bfs(v)