def transpose_graph(n, graph, idx) : # 행 <-> 열 바꾸기
    new_graph = list(map(list, zip(*graph)))
    y_axis = graph[idx]
    graph[idx] = new_graph[idx]
    for i in range(n+1) :
        graph[i][idx] = y_axis[i]
    return graph


def dfs(v, arr, traps) :
    global n
    for i in range(len(arr[v])) :
        if arr[i] != 0 :
            if i in traps :
                arr = transpose_graph(n, graph, i)

        

        else :
            




def solution(n, start, end, roads, traps):
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    # print(graph)
    for i, j, cost in roads :
        graph[i][j] = cost        
    # print(graph)
    # print(graph[2][:])




    new_list = transpose_graph(n, graph, 2) # 행 <-> 열 바꾸기
    print(new_list)


    
    
    answer = 0
    return answer

# solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])