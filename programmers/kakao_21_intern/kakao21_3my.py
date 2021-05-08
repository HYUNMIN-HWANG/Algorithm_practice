import re

def solution(n, k, cmd):
    # print(n, k)
    # print(cmd)
    m = len(cmd)
    cmd_list = [[] for _ in range(m)]
    # print(cmd_list)
    for i in range(m) :
        tmp = re.split(r'(\s)', cmd[i])
        for j in tmp :
            if j == ' ' :
                pass
            else :
                cmd_list[i].append(j)
        # print(cmd_list) 
        # [['D', '2'], ['C'], ['U', '3'], ['C'], ['D', '4'], ['C'], ['U', '2'], ['Z'], ['Z']]
    # print(cmd_list)
    
    table = ['O'] * n
    now = k
    stack = []
    
    for ord in cmd_list :
        # print(ord)
        if ord[0] == 'D' :
            check = int(ord[1])
            while check > 0 :
                now += 1
                if table[now] == 'X' :
                    pass
                else :
                    check -= 1
            # print(now)
        elif ord[0] == 'U' :
            check = int(ord[1])
            while check > 0 :
                now -= 1
                if table[now] == 'X' :
                    pass
                else :
                    check -= 1
            # print(now)
        elif ord[0] == 'C' :
            if now == n-1 : # 마지막 행이면 삭제하고 위 칸으로 이동
                table[now] = 'X'
                stack.append(now)
                check = 1
                while check > 0 :
                    now -= 1
                    if table[now] == 'X' :
                        pass
                    else :
                        check -= 1
            else :
                table[now] = 'X'
                stack.append(now)
                check = 1
                while check > 0 :
                    now += 1
                    if table[now] == 'X' :
                        pass
                    else :
                        check -= 1
        else : # 'Z' 
            pop_node = stack.pop()
            # print(pop_node)
            table[pop_node] = 'O'
                
    # print(table)
    
    answer = ''
    for ans in table :
        answer = answer + ans
    
    return answer