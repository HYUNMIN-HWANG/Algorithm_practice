

def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        print(i, "=============================")
        n = i
        visit = [n]
        print("[[[[while]]]]")
        while n in room_dic:
            print(n)
            n = room_dic[n]
            visit.append(n)
            print("visit", visit)
        ret.append(n)
        print("ret : ", ret)
        print("[[[[while end]]]]]")
        for j in visit :
            room_dic[j] = n+1
            print("room_dict ::: ", room_dic)
    return ret

solution(10, [1,3,4,1,3,1])


"""
1 =============================
[[[[while]]]]
ret :  [1]
[[[[while end]]]]]
room_dict :::  {1: 2}
3 =============================
[[[[while]]]]
ret :  [1, 3]
[[[[while end]]]]]
room_dict :::  {1: 2, 3: 4}
4 =============================
[[[[while]]]]
ret :  [1, 3, 4]
[[[[while end]]]]]
room_dict :::  {1: 2, 3: 4, 4: 5}
1 =============================
[[[[while]]]]
1
visit [1, 2]
ret :  [1, 3, 4, 2]
[[[[while end]]]]]
room_dict :::  {1: 3, 3: 4, 4: 5}
room_dict :::  {1: 3, 3: 4, 4: 5, 2: 3}
3 =============================
[[[[while]]]]
3
visit [3, 4]
4
visit [3, 4, 5]
ret :  [1, 3, 4, 2, 5]
[[[[while end]]]]]
room_dict :::  {1: 3, 3: 6, 4: 5, 2: 3}
room_dict :::  {1: 3, 3: 6, 4: 6, 2: 3}
room_dict :::  {1: 3, 3: 6, 4: 6, 2: 3, 5: 6}
1 =============================
[[[[while]]]]
1
visit [1, 3]
3
visit [1, 3, 6]
ret :  [1, 3, 4, 2, 5, 6]
[[[[while end]]]]]
room_dict :::  {1: 7, 3: 6, 4: 6, 2: 3, 5: 6}
room_dict :::  {1: 7, 3: 7, 4: 6, 2: 3, 5: 6}
room_dict :::  {1: 7, 3: 7, 4: 6, 2: 3, 5: 6, 6: 7}
"""