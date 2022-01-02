# 신규 아이디 추천

def solution(new_id):
    
    id = list(new_id)

    # 문자 제거시 사용 0,1
    check = 0

    # 마침표 치환시 사용
    dot = 0

    # 1단계: 대문자를 소문자로 변경
    for i in range(len(id)):
        if ord(id[i]) >= 65 and ord(id[i]) <= 90: # 아스키 코드가 65~90 이면
            id[i] = chr(ord(id[i])+32) # 32를 더해 소문자로 변경

    # 2단계: 영어 소문자, 숫자, -, _, . 를 제외한 모든 문자를 제거
    for i in range(len(id)):

        # 영어 소문자 체크
        if ord(id[i]) >= 97 and ord(id[i]) <= 122:
            check = 1

        # 숫자 체크
        if ord(id[i]) >= 48 and ord(id[i]) <= 57:
            check = 1

        # 특수문자 체크
        if id[i] == '-' or id[i] == '_' or id[i] == '.':
            check = 1

        # 체크가 되었으면 통과, 안되었으면 제거할 리스트에 삽입
        if check==1:
            pass
        else:
            id[i]='#' # 제거할 문자 '#'으로 통일
        check = 0 # 초기화
    # '#' 문자 모두 제거
    try:
        while(True):
            id.remove('#')
    except:
        pass

    # 3단계: 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    for i in range(len(id)):
        if id[i] == '.':
            dot += 1
            if dot >= 2:
                id[i]='#'
        elif dot>=1:
            dot = 0
    # '#' 문자 모두 제거
    try:
        while(True):
            id.remove('#')
    except:
        pass

    # 4단계: 처음과 끝의 마침표 제거
    if id[0]=='.':
        id[0]='#'
    if id[-1]=='.':
        id[-1]='#'
    # '#' 문자 모두 제거
    try:
        while(True):
            id.remove('#')
    except:
        pass

    # 5단계: 빈 문자열이라면 'a'를 대입
    if len(id)==0:
        id.append('a')

    # 6-1단계: 16자 이상이면 첫 15개 제외 나머지 제거
    if len(id)>=16:
        for i in range(len(id)):
            if i>=15:
                id[i]='#'
    # '#' 문자 모두 제거
    try:
        while(True):
            id.remove('#')
    except:
        pass

    # 6-2단계: 마침표가 끝에 위치하면 마침표 제거
    if id[-1]=='.':
        id[-1]='#' 
    # '#' 문자 모두 제거
    try:
        while(True):
            id.remove('#')
    except:
        pass

    # 7단계: 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 끝에 붙임
    if len(id)<=2:
        temp = id[-1]
        if len(id)==1:
            id.append(temp)
            id.append(temp)
        elif len(id)==2:
            id.append(temp)

    answer = ''.join(id)
    
    return answer