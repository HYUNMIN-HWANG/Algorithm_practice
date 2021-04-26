문제 : 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
입력 : 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
출력 : N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

num = int(input())

for i  in range(2, num+1) :
    if num == 1 :   # 1은 소수 아님
        break
    elif num == i : # 자기 자신만 나눌 수 있을 때 소수
        print(i)
        break
    elif num % i == 0 : # 자기 자신이 아닌 수로 나누어지면 소수 아님
        while (num % i == 0) :
            print(int(i))
            num = num/i
    else :
        continue

# 참고 답안
num = 20
# num = int(input())
i = 2
while num != 1 :
    if num % i == 0 :
        print(i)
        num = num /i
    else :
        i += 1
        
