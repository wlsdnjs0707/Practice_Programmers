def solution(s):
    answer = []
    temp = []
    temp_con = []
    tp = []

    index = 1

    s_list = list(s)

    # 문자열 -> 리스트화 하여 tp에 저장
    for i in range(len(s_list)):
        if ord(s_list[i]) >= 48 and ord(s_list[i]) <= 57:
            temp_con.append(s_list[i])
        elif s_list[i] == ',':
            if (len(temp_con) != 0):
                temp.append(''.join(temp_con))
                temp_con = []
        elif s_list[i] == '}':
            if len(temp_con) != 0:
                temp.append(''.join(temp_con))
                temp_con = []
            if len(temp) != 0:
                tp.append(temp)
                temp = []

    # tp를 이용해 튜플 추론
    while (index <= len(tp)):
        for i in range(len(tp)):
            if len(tp[i]) == index:
                for j in range(len(tp[i])):
                    if tp[i][j] not in answer:
                        answer.append(tp[i][j])
                        index += 1

    answer = [int(i) for i in answer]

    return answer