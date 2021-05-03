import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    print(op)   # ['*', '+', '-']
    op = [list(y) for y in permutations(op)]    # 모든 경우의 수만큼 만들어준다.
    print(op)   # [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '*', '+'], ['-', '+', '*']]
    ex = re.split(r'(\D)',expression)   # '(\D)' : 숫자가 아닌것 을 기준으로 자른다.
    print(ex)   # ['100', '-', '200', '*', '300', '-', '500', '+', '20']

    #2
    a = []
    for x in op:
        print("==========", x)
        _ex = ex[:]
        for y in x:
            while y in _ex:
                print("-")
                tmp = _ex.index(y)
                print(tmp)
                print("계산 : ", eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        print("//_ex : ", _ex)
        a.append(_ex[-1])
        print("=============", a)

    #3
    return max(abs(int(x)) for x in a)

aaa = solution("100-200*300-500+20")

print("결론 :", aaa)