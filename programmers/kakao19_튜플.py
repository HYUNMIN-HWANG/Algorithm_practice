# 내 풀이

"""
import re
from itertools import permutations

def solution(s):
    answer = []
    # print(s)
    # print(len(s))


    ex = re.split(r'\D', s)
    # print(ex)   # ['', '', '2', '', '', '2', '1', '', '', '2', '1', '3', '', '', '2', '1', '3', '4', '', '']
    ex = ex[1:-1]
    # print(ex)   # ['', '2', '', '', '2', '1', '', '', '2', '1', '3', '', '', '2', '1', '3', '4', '']

    t = [[] for i in range(500)]
    idx = -1

    for i in range(1, len(ex)-1) :
        if ex[i] != '' and ex[i-1] == '' :
            # print("새로운 리스트 시작하는 부분", ex[i])
            idx += 1
            t[idx].append(int(ex[i]))
        if ex[i] != '' and ex[i-1] != '' :
            # print("연속 숫자", ex[i])
            t[idx].append(int(ex[i]))

    t = sorted(t, key=len)

    for check_list in t :
        if check_list :
            # print(check_list)
            for num in check_list :
                if num not in answer :
                    answer.append(num)

    print(answer)

    return answer
"""
# 다른 사람 풀이

def solution(s):

    find_all = re.findall('\d+', s)
    print(find_all) # ['2', '2', '1', '2', '1', '3', '2', '1', '3', '4']
    s = Counter(re.findall('\d+', s))
    print(s)    # Counter({'2': 4, '1': 3, '3': 2, '4': 1})

    print(sorted(s.items()))    # [('1', 3), ('2', 4), ('3', 2), ('4', 1)]
    print(sorted(s.items(), reverse=True))    # [('4', 1), ('3', 2), ('2', 4), ('1', 3)]
    print(sorted(s.items(), key=lambda x: x[1], reverse=True))    # [('2', 4), ('1', 3), ('3', 2), ('4', 1)]

    for k , v in sorted(s.items(), key=lambda x: x[1], reverse=True) :
        print(k)
        # 2
        # 1
        # 3
        # 4

    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

print("결과", solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))