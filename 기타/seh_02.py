'''
문제 설명
당신은 송아지 한 마리를 키우고 있습니다. 
지금부터 n일 이내에 이 송아지를 반드시 먼저 팔고 새로운 송아지를 한 마리 사야만 합니다. 
송아지 가격은 하루 단위로 갱신되며, 같은 가격으로 유지될 수도 있습니다. 
다행히 n일 간의 송아지 가격은 정확히 예측됩니다. 당신은 판매 이익(판매가격 - 구매가격)이 최대가 되도록 판매일과 구매일을 잡아야 합니다.
단, 같은 날에 송아지를 팔고 살 수는 없습니다.

예1) n = 10 이고, 이 기간 동안 송아지 가격이 3, 1, 4, 1, 5, 9, 2, 6, 5, 3 원으로 예측되면, 
6 일째 되는 날 송아지를 팔고 7 일째 되는 날 송아지를 사는 것이 가장 유리합니다 (9 - 2 = 7 원 이익).

예2) n = 10 이고, 이 기간 동안 송아지 가격이 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 원으로 예측되면, 
10 일 이전에 아무 날이나 팔고 바로 그 다음 날 사는 것이 가장 유리합니다 (-1 원 이익, 즉 1 원 손실).

당신이 송아지를 팔고 사야하는 기간 n, 그리고 이 기간 중의 송아지 값을 담은 배열 v 가 매개변수로 주어질 때, 
최대 판매 이익을 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 1,000,000 이하인 자연수입니다.
v는 길이가 n인 정수형 배열입니다.
v의 원소는 송아지 값을 나타나며, 1 이상 1,000,000,000 이하인 자연수입니다.
입출력 예
n   v   result
10   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]   7
10   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   -1
6   [4, 1, 7, 6, 5, 2]   5
입출력 예 설명
입출력 예 #1
문제 예시와 같습니다.

입출력 예 #2
문제 예시와 같습니다.

입출력 예 #3
3 일째 되는 날 송아지를 팔고 6 일째 되는 날 송아지를 사는 것이 가장 유리합니다. (7 - 2 = 5 원 이익).
'''