import numpy as np

def solution(places):
    answer = []
    for time in range(5):
        answers = []
        test = places[time]
        temp_list = []

        for x in range(5):
            for y in range(5):
                if test[x][y] == "P":
                    temp_list.append(np.array([x,y]))
                else:
                    continue

        for i in range(len(temp_list)): 
            for j in range(len(temp_list)):
                if np.abs(temp_list[i]-temp_list[j])[0]+np.abs(temp_list[i]-temp_list[j])[1] == 1:
                    answers.append("0")
                elif np.abs(temp_list[i]-temp_list[j])[0]+np.abs(temp_list[i]-temp_list[j])[1] == 2:
                    x_dif = np.abs(temp_list[i]-temp_list[j])[0]
                    y_dif = np.abs(temp_list[i]-temp_list[j])[1]
                    if x_dif == 2:
                        mid_x = int((temp_list[i][0]+temp_list[j][0])/2)
                        mid_y = temp_list[i][1]
                        if test[mid_x][mid_y]=="X":
                            answers.append("1")
                        else:
                            answers.append("0")
                    elif y_dif == 2:
                        mid_x = temp_list[i][0]
                        mid_y = int((temp_list[i][1]+temp_list[j][1])/2)
                        if test[mid_x][mid_y]=="X":
                            answers.append("1")
                        else:
                            answers.append("0")
                    else:
                        mid_1_x = temp_list[i][0]
                        mid_1_y = temp_list[j][1]
                        mid_2_x = temp_list[j][0]
                        mid_2_y = temp_list[i][1]
                        if test[mid_1_x][mid_1_y]=="X" and test[mid_2_x][mid_2_y]=="X":
                            answers.append('1')
                        else:
                            answers.append('0')

                else:
                    answers.append("1")
        if answers.count("0") != 0 :
            answer.append(0)
        else:
            answer.append(1)
        
    return answer