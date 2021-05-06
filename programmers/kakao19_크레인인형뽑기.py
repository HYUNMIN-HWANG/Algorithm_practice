"""
# 내 풀이
def solution(board, moves):
    
    graph = [[] for i in range( len(board) )]
    top = -1
    
    n = len(board)
    
    for i in range(n) :
        for j in range(n) :
            if board[i][j] != 0 :
                graph[j].append(board[i][j])
    # print(graph)    # [[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
    
    stack = []
    top = -1
    answer = 0
    for step in moves :
        try : 
            # print("뽑은 인형 : ", graph[step-1][0])
            stack.append(graph[step-1][0])
            top += 1
            del graph[step-1][0]
            
            if top >= 1 and stack[top-1] == stack[top] : 
                # print("same")
                answer += 2 
                del stack[top-1:top+1] 
                top -= 2
                # print(stack)
        except : 
            pass
    # print(stack)

    return answer
"""
"""
# 다른 사람 풀이

def solution(board, moves):
    stacklist = []
    answer = 0
    print(len(board))   # 5

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                print("인형 뽑기 ", board[j][i-1])
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0
                print(stacklist)

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        print(stacklist[-1], "중복제거 !!!! ")
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break
    print("answer ||| ", answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
"""
# 다시 풀이
def solution(board, moves):

    stack = []
    answer = 0
    n = len(board)

    for i in moves :
        for j in range(n) : 
            if board[j][i-1] != 0 :
                print("뽑은 인형 : ", board[j][i-1])
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                print(stack)
                if len(stack) > 1 : 
                    if stack[-1] == stack[-2] :
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break

    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
