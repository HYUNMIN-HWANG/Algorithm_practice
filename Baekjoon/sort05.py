#  단어 정렬 https://www.acmicpc.net/problem/1181
'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력
조건에 따라 정렬하여 단어들을 출력한다. 
단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''

"""
import sys
n = 13
words = ['but','is','wont','hestiate','no','more','no','more','it','cannot','wait','im','yours']
# print(words)

n = int(input())
words = set()
for i in range(n) :
    words.add(str(sys.stdin.readline()))
# words = list(words)

# 내가 푼 것 : 퀵정렬 - 시간초과
for i in range(1, len(words)) :
    for j in range(i, 0, -1) :
        # print(words[j])
        if len(words[j]) < len(words[j-1]) :
            words[j], words[j-1] = words[j-1], words[j]
        elif len(words[j]) == len(words[j-1]) :
            if words[j] < words[j-1] :
                words[j], words[j-1] = words[j-1], words[j]
            else :
                break
        else :
            break
    # print("============")
for w in words :
    sys.stdout.write(str(w))
# print(words)
"""

n = int(input())
word_list = list()
sort_list = list()

for i in range(n) :
    word_list.append(input())
# print(word_list)

word_set = set(word_list)

for word in word_set :
    # print(word)
    sort_list.append((len(word), word))

sort_list.sort()
for i, w in sort_list :
    print(w)