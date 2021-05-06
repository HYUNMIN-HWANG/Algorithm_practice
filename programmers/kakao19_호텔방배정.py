# 내가 푼 형식

def room(i, full, answer) :

    if full[i-1] == False :
        # print("성공 :: ", i)
        full[i-1] = True
        answer.append(i)
    else :
        # print("이미 선택된 좌석", i)
        room(i+1, full, answer)

def solution(k, room_number):
    answer = []
    full = [False] * k  # 손님이 들어가면 True로 바꿔주기
    
    for i in room_number :
        room(i, full, answer)
    
    return answer