def solution(progresses, speeds):
    answer = []
    current = []
    count = 0

    for i in range(len(progresses)):
        current.append([progresses[i], speeds[i]])

    while (True):
        if len(current) == 0:
            break

        for i in range(len(current)):
            current[i][0] += current[i][1]

        while (True):
            if len(current) >= 1 and current[0][0] >= 100:
                count += 1
                current.pop(0)
            else:
                break

        if count > 0:
            answer.append(count)
            count = 0

    return answer