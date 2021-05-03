def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

expression = str(100-200*300-500+20)
print(type(expression)) # <class 'int'>
operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
answer = []
for op in operations:
    print(op)   # ('+', '-', '*')
    a = op[0]   #
    b = op[1]   # 
    print(a, b) # + -
    temp_list = []
    print(expression.split(a))  # ['-60380']
    for e in expression.split(a):
        print(e.split(b))   # ['', '60380']
        temp = [f"({i})" for i in e.split(b)]
        print(temp) # ['()', '(60380)']
        temp_list.append(f'({b.join(temp)})')
        print(temp_list)    # ['(()-(60380))']
    answer.append(abs(eval(a.join(temp_list))))
print(answer)
