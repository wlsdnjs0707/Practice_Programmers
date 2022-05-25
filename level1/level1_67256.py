# 키패드 누르기

def solution(numbers, hand):
    # 왼손의 현재 위치, 누를 버튼까지와의 거리 저장
    position_left = 10
    ld = 0

    # 오른손의 현재 위치, 누를 버튼까지와의 거리 저장
    position_right = 12
    rd = 0

    # 정답 저장할 리스트
    ans = []

    for i in range(len(numbers)):

        # 2,5,8,0 누를 경우에만 거리 계산
        if numbers[i]==2 or numbers[i]==5 or numbers[i]==8 or numbers[i]==0:

            if position_left==1:
                if numbers[i]==2:
                    ld = 1
                if numbers[i]==5:
                    ld = 2
                if numbers[i]==8:
                    ld = 3
                if numbers[i]==0:
                    ld = 4
            elif position_left==4:
                if numbers[i]==2:
                    ld = 2
                if numbers[i]==5:
                    ld = 1
                if numbers[i]==8:
                    ld = 2
                if numbers[i]==0:
                    ld = 3
            elif position_left==7:
                if numbers[i]==2:
                    ld = 3
                if numbers[i]==5:
                    ld = 2
                if numbers[i]==8:
                    ld = 1
                if numbers[i]==0:
                    ld = 2
            elif position_left==10:
                if numbers[i]==2:
                    ld = 4
                if numbers[i]==5:
                    ld = 3
                if numbers[i]==8:
                    ld = 2
                if numbers[i]==0:
                    ld = 1
            if position_left==2:
                if numbers[i]==2:
                    ld = 0
                if numbers[i]==5:
                    ld = 1
                if numbers[i]==8:
                    ld = 2
                if numbers[i]==0:
                    ld = 3
            elif position_left==5:
                if numbers[i]==2:
                    ld = 1
                if numbers[i]==5:
                    ld = 0
                if numbers[i]==8:
                    ld = 1
                if numbers[i]==0:
                    ld = 2
            elif position_left==8:
                if numbers[i]==2:
                    ld = 2
                if numbers[i]==5:
                    ld = 1
                if numbers[i]==8:
                    ld = 0
                if numbers[i]==0:
                    ld = 1
            elif position_left==11:
                if numbers[i]==2:
                    ld = 3
                if numbers[i]==5:
                    ld = 2
                if numbers[i]==8:
                    ld = 1
                if numbers[i]==0:
                    ld = 0

            if position_right==3:
                if numbers[i]==2:
                    rd = 1
                if numbers[i]==5:
                    rd = 2
                if numbers[i]==8:
                    rd = 3
                if numbers[i]==0:
                    rd = 4
            elif position_right==6:
                if numbers[i]==2:
                    rd = 2
                if numbers[i]==5:
                    rd = 1
                if numbers[i]==8:
                    rd = 2
                if numbers[i]==0:
                    rd = 3
            elif position_right==9:
                if numbers[i]==2:
                    rd = 3
                if numbers[i]==5:
                    rd = 2
                if numbers[i]==8:
                    rd = 1
                if numbers[i]==0:
                    rd = 2
            elif position_right==12:
                if numbers[i]==2:
                    rd = 4
                if numbers[i]==5:
                    rd = 3
                if numbers[i]==8:
                    rd = 2
                if numbers[i]==0:
                    rd = 1
            elif position_right==2:
                if numbers[i]==2:
                    rd = 0
                if numbers[i]==5:
                    rd = 1
                if numbers[i]==8:
                    rd = 2
                if numbers[i]==0:
                    rd = 3
            elif position_right==5:
                if numbers[i]==2:
                    rd = 1
                if numbers[i]==5:
                    rd = 0
                if numbers[i]==8:
                    rd = 1
                if numbers[i]==0:
                    rd = 2
            elif position_right==8:
                if numbers[i]==2:
                    rd = 2
                if numbers[i]==5:
                    rd = 1
                if numbers[i]==8:
                    rd = 0
                if numbers[i]==0:
                    rd = 1
            elif position_right==11:
                if numbers[i]==2:
                    rd = 3
                if numbers[i]==5:
                    rd = 2
                if numbers[i]==8:
                    rd = 1
                if numbers[i]==0:
                    rd = 0

        if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
            ans.append('L')
            position_left = numbers[i] 
        elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
            ans.append('R')
            position_right = numbers[i] 
        else:
            if ld==rd:
                if hand=="left":
                    ans.append('L')
                    if numbers[i]==0:
                        position_left = 11
                    else:
                        position_left = numbers[i]
                else:
                    ans.append('R')
                    if numbers[i]==0:
                        position_right = 11
                    else:
                        position_right = numbers[i]
            elif ld<rd:
                ans.append('L')
                if numbers[i]==0:
                    position_left = 11
                else:
                    position_left = numbers[i]
            elif rd<ld:
                ans.append('R')
                if numbers[i]==0:
                    position_right = 11
                else:
                    position_right = numbers[i]            

    answer = ''.join(ans)

    return answer