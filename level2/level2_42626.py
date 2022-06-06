def solution(scoville, K):
    answer = 0
    a = 0
    b = 0
    count = 0
    flag = 1

    while (flag >= 1):

        if len(scoville) == 1:
            count = -1
            break

        flag = 0

        scoville.sort()
        a = scoville.pop(0)
        b = scoville.pop(0)

        scoville.append(a + (b * 2))
        count += 1

        for i in scoville:
            if i < K:
                flag = 1

    return count