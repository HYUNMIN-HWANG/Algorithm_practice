def solution(gems):
    unique = set(gems)
    
    d = [100000] * len(gems)
    # print(d)
    min =  100000
    answer = [-1, -1]
    
    for i in range(len(gems)-1) :
        # print(i,"번 부터 시작할 때,>>>>>>>>>")
        box = [gems[i]]
        # print(len(set(box)))
        
        j = i+1
        # print("j",j)
        
        while len(unique) > len(set(box)) :
            box.append(gems[j])
            j += 1
            if j >= len(gems) :
                break
        if len(unique) == len(set(box)) :
            d[i] = j-1
            
            if min > d[i] - i : 
                min = d[i] - i
                answer = [i+1, d[i]+1]
                print("answer", answer) 
    print(d)

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])

# 정답은 맞는데 효율성이 많이 떨어짐, 효율성 0점 나옴
