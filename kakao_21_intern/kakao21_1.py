
def solution(s):
    answer = 0
    test = s
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(10):
        b = test.replace(alpha[i], num[i])
        test = b
        answer = test        
    answer = int(answer)
    
    return answer