def solution(str1, str2):
    str1_cut = []
    str2_cut = []
    str1_cut_copy = []
    str2_cut_copy = []
    temp = []
    intersection = []
    union = 0
    answer = 0

    # ord 65~122 -> 영어

    # 두 글자씩 끊어 세팅 (.lower() 함수로 소문자로 통일)
    for i in range(len(str1) - 1):
        if (ord(str1[i]) >= 65 and ord(str1[i]) <= 122) and (ord(str1[i + 1]) >= 65 and ord(str1[i + 1]) <= 122):
            if (ord(str1[i]) < 91 or ord(str1[i]) > 96) and (ord(str1[i + 1]) < 91 or ord(str1[i + 1]) > 96):
                temp.append(str1[i].lower())
                temp.append(str1[i + 1].lower())
                str1_cut.append(''.join(temp))
                temp = []

    for i in range(len(str2) - 1):
        if (ord(str2[i]) >= 65 and ord(str2[i]) <= 122) and (ord(str2[i + 1]) >= 65 and ord(str2[i + 1]) <= 122):
            if (ord(str2[i]) < 91 or ord(str2[i]) > 96) and (ord(str2[i + 1]) < 91 or ord(str2[i + 1]) > 96):
                temp.append(str2[i].lower())
                temp.append(str2[i + 1].lower())
                str2_cut.append(''.join(temp))
                temp = []

    if (len(str1_cut) == 0 and len(str2_cut) == 0):
        return 65536

    str1_cut_copy = str1_cut.copy()
    str2_cut_copy = str2_cut.copy()

    # 교집합 구하기 (리스트)
    for i in str1_cut_copy:
        if i in str2_cut_copy:
            intersection.append(i)
            str2_cut_copy.remove(i)

    # 합집합 구하기 (개수)
    union = len(str1_cut) - len(intersection) + len(str2_cut)

    answer = int(len(intersection) / union * 65536)

    return answer