# 크레인 인형뽑기 게임

def solution(board, moves):
    
    # 제거된 인형의 수
    answer = 0
    
    # 인형을 집을 위치
    line = 0

    # 뽑은 인형 리스트
    num = []

    for i in range(len(moves)):
        # 행 -> 가장 위에 있는 인형
        # 열 -> line (moves[i]-1)

        line = moves[i]-1

        # moves에 따라 그 line의 가장 위에 있는 인형 뽑기, 이후 뽑은 인형 제거
        for j in board:
            if j[line]!=0:
                num.append(j[line])
                j[line] = 0
                break

        # 같은 인형 연속 두개 쌓이면 제거
        if len(num)>=2:
            if num[-1]==num[-2]:
                num.pop()
                num.pop()
                answer += 2
            
    return answer