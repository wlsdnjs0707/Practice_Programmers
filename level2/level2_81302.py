def solution(places):
    answer = []

    sit = []

    temp = []

    checklist = []

    for k in range(5):

        for i in range(5):
            temp = list(places[k][i])

            sit.append(temp)

            temp = []

        for i in range(5):

            for j in range(5):

                if sit[i][j] == 'P':
                    checklist.append(check(sit, i, j))

        if sum(checklist) == len(checklist):

            answer.append(1)

        else:

            answer.append(0)

        checklist = []

        sit = []

    return answer


# check = 1이면 통과

def check(sit, row, col):
    # 1칸 내에 P존재

    if row > 0:

        if sit[row - 1][col] == 'P':
            return 0

    if row < 4:

        if sit[row + 1][col] == 'P':
            return 0

    if col > 0:

        if sit[row][col - 1] == 'P':
            return 0

    if col < 4:

        if sit[row][col + 1] == 'P':
            return 0

    # 2칸 내에 P존재하고 파티션 없음

    if row > 2:

        if sit[row - 2][col] == 'P' and sit[row - 1][col] != 'X':
            return 0

    if row < 3:

        if sit[row + 2][col] == 'P' and sit[row + 1][col] != 'X':
            return 0

    if col > 2:

        if sit[row][col - 2] == 'P' and sit[row][col - 1] != 'X':
            return 0

    if col < 3:

        if sit[row][col + 2] == 'P' and sit[row][col + 1] != 'X':
            return 0

    # 대각선에 P존재하고 파티션 없음

    if row == 0:

        if col == 0:

            if (sit[row + 1][col + 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

        if col >= 1 and col <= 3:

            if (sit[row + 1][col + 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

            if (sit[row + 1][col - 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

        if col == 4:

            if (sit[row + 1][col - 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

    if row == 4:

        if col == 0:

            if (sit[row - 1][col + 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

        if col >= 1 and col <= 3:

            if (sit[row - 1][col + 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

            if (sit[row - 1][col - 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

        if col == 4:

            if (sit[row - 1][col - 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

    if row >= 1 and row <= 3:

        if col == 0:

            if (sit[row + 1][col + 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

            if (sit[row - 1][col + 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

        if col >= 1 and col <= 3:

            if (sit[row + 1][col + 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

            if (sit[row + 1][col - 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

            if (sit[row - 1][col + 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col + 1] == 'P' and sit[row][col + 1] == 'O'):
                return 0

            if (sit[row - 1][col - 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

        if col == 4:

            if (sit[row + 1][col - 1] == 'P' and sit[row + 1][col] == 'O') or (
                    sit[row + 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

            if (sit[row - 1][col - 1] == 'P' and sit[row - 1][col] == 'O') or (
                    sit[row - 1][col - 1] == 'P' and sit[row][col - 1] == 'O'):
                return 0

    return 1