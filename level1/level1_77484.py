def solution(lottos, win_nums):
    check = 0
    zeros = 0
    max_rank = 0
    min_rank = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeros += 1

    for i in range(len(win_nums)):
        for j in range(len(lottos)):
            if win_nums[i] == lottos[j]:
                check += 1

    max_rank = check + zeros
    min_rank = check

    if zeros == 0:
        if check == 0:
            max_rank = 6
            min_rank = 6
        else:
            max_rank = 7 - max_rank
            min_rank = 7 - min_rank
    else:
        if check == 0:
            max_rank = 7 - zeros
            min_rank = 6
        else:
            max_rank = 7 - max_rank
            min_rank = 7 - min_rank

    answer = [max_rank, min_rank]
    return answer