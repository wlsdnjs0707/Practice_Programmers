def solution(m, n, board):
    answer = 0
    count = 0
    del_list = []
    new_del_list = []
    flag = 0
    temp = 0

    # 입력 = m * n board

    # 지워진 블록 = 0 삽입, 붙어있는 블록 체크 시 0은 제외

    # setting: board 붙어있는 문자열 리스트화
    for i in range(len(board)):
        board[i] = list(board[i])

    while (flag == 0):

        # 붙어있는 블록 체크 (4개 블록의 왼쪽 상단 블록부터 체크, 0 제외) 후 삭제 예정 리스트에 저장
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i < m - 1 and j < n - 1) and board[i][j] != 0:
                    if board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == \
                            board[i + 1][j + 1]:
                        del_list.append([i, j])
                        del_list.append([i + 1, j])
                        del_list.append([i, j + 1])
                        del_list.append([i + 1, j + 1])

        # del_list 중복 제거
        for i in del_list:
            if i not in new_del_list:
                new_del_list.append(i)

        del_list = []

        # 더이상 삭제할 블록이 없으면 반복문 탈출
        if (len(new_del_list)) == 0:
            flag = 1

        # 블럭 삭제, 삭제한 개수 + 1, del_list 초기화
        for i in range(len(new_del_list)):
            board[new_del_list[i][0]][new_del_list[i][1]] = 0
            count += 1

        new_del_list = []

        # 블럭 내려옴 (역순으로 확인, 빈 곳부터 위로 체크해서 블럭 내림)
        for i in range(m - 1, 1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 0:
                    for k in range(i, -1, -1):
                        if board[k][j] != 0:
                            temp = i - k
                            break
                    for k in range(i, -1, -1):
                        if k >= temp:
                            board[k][j] = board[k - temp][j]
                        else:
                            board[k][j] = 0

    return count