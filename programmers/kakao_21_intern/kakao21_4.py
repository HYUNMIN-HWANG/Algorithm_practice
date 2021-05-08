def solution(n, start, end, roads, traps):
    
    # n 방 개수
    # start 출발 방 
    # end 도착 방
    # roads 통로와 시간 [통로 출발, 통로 도착, 걸리는 시간]
    # traps 함정방
    
    location = start
    time = 0
    trapc = 0
    
    for num1 in range(10):
    
        for num in roads:
            
            if trapc == 0:
                if location == num[0]:
                    location = num[1]
                    time += num[2]
            else:
                num.reverse()
                if location == num[1]:
                    location = num[2]
                    time += num[0]

            try:
                if traps.index(location) >= 0:
                    trapc = 1
            except:
                trapc = 0

        if location == end:
            break

    
    return time