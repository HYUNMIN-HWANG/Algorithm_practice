문제 :  0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
입력 :  첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
출력 :  첫째 줄에 N!을 출력한다.

n = int(input())
# ans = 1

def factorical (n) :
    if n == 0 : 
        ans = 1
    else :
        ans = n * factorical(n-1)
    return ans

result = factorical(n)
print(result)
