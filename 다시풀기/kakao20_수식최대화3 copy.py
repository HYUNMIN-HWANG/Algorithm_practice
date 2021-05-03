import re
from itertools import permutations

def solution(expression):
    
    op = [ x for x in ["*", "+", "-"] if x in expression]
    # print(op)
    op = [list(y) for y in permutations(op)]
    # print(op)
    
    ex = re.split(r'(\D)', expression)
    print(ex)   # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    
    a = []
    for i in op :
        _ex = ex[:]
        
        for y in  i :
            while y in _ex :
                print("-")
                temp = _ex.index(y)
                
                _ex[temp-1] = str(eval(_ex[temp-1] + _ex[temp] + _ex[temp+1]))
                _ex = _ex[:temp] + _ex[temp+2:]
    
        a.append(_ex[-1])
             
    
    answer = max(abs(int(x)) for x in a)
    return answer

print(solution("100-200*300-500+20"))