#인덱싱과 슬라이싱
# "파이썬은 0부터 숫자를 센다."


#인덱싱
a = "Life is too short, You need Python"
#a[번호]
a[0] #출력결과 : 'L'
a[3] #출력결과 : 'e'
a[-1] #출력괄과 : 'n'
a[-5] #출력결과 : 'y'

#슬라이싱
#a[시작 번호 : 끝 번호] : 끝 번호에 해당하는 것은 포함하지 않는다.
a[0:4] #출력결과 : 'Life'
a[12:17] #출력결과 : 'short'
a[19:] #출력결과 : 'You need Python'
a[:17] #출력결과 : 'Life is too short'
a[:] #출력결과 : 'Life is too short, You need Python'
