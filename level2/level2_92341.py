import math


def solution(fees, records):
    answer = []
    records_list = []
    cars = []
    hour_temp = []
    minute_temp = []
    car_num_temp = []
    parked_time = 0
    fee = 0
    exist = 0
    time_info = []
    temp = 0

    # fees 기본시간, 기본요금, 단위시간, 단위요금
    # records

    # records 리스트화
    for i in range(len(records)):
        records_list.append(list(records[i]))

    # 주차 시간 계산 후 time_info에 등록
    for i in range(len(records_list)):
        for j in range(6, 10):
            car_num_temp.append(records_list[i][j])
        for j in range(0, 2):
            hour_temp.append(records_list[i][j])
        for j in range(3, 5):
            minute_temp.append(records_list[i][j])

        car_num = ''.join(car_num_temp)
        hour = ''.join(hour_temp)
        minute = ''.join(minute_temp)

        if records_list[i][11] == 'I':
            cars.append([car_num, hour, minute])
        elif records_list[i][11] == 'O':
            for k in range(len(cars)):
                if cars[k][0] == car_num:
                    parked_time = (int(hour) - int(cars[k][1])) * 60 + int(minute) - int(cars[k][2])
                    temp = k

            del cars[temp]

            if len(time_info) == 0:
                time_info.append([car_num, parked_time])
            else:
                for l in range(len(time_info)):
                    # time_info에 이미 기록이 존재하나 확인
                    if time_info[l][0] == car_num:
                        exist = 1
                        temp = l

                # 이미 주차 기록 존재: 주차시간 누적
                if exist == 1:
                    time_info[temp][1] += parked_time
                # 첫 주차: 주차시간 등록
                else:
                    time_info.append([car_num, parked_time])

                exist = 0

        # 초기화
        car_num = []
        hour = []
        minute = []
        car_num_temp = []
        hour_temp = []
        minute_temp = []

    # 출차를 안한경우 출차시간 23:59로 등록
    for j in range(len(cars)):
        parked_time = (23 - int(cars[j][1])) * 60 + 59 - int(cars[j][2])

        for k in range(len(time_info)):
            if time_info[k][0] == cars[j][0]:
                exist = 1
                temp = k

        if exist == 1:
            time_info[temp][1] += parked_time
        else:
            time_info.append([cars[j][0], parked_time])

        exist = 0

    # 요금 계산
    for i in range(len(time_info)):
        if time_info[i][1] <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((time_info[i][1] - fees[0]) / fees[2]) * fees[3]

        answer.append([time_info[i][0], fee])

    # answer 리스트 차량 번호순으로 sort
    answer.sort()

    for i in range(len(answer)):
        answer[i] = answer[i][1]

    return answer