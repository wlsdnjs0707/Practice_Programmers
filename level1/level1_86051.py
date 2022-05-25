# 없는 숫자 더하기

def solution(numbers):
    
    # 비교할 리스트 (0~9)
    all_numbers = [0,1,2,3,4,5,6,7,8,9]

    # numbers에 존재하면 all_numbers에서 삭제
    for i in numbers:
        all_numbers.remove(i)
    
    # all_numbers에 남은 숫자 모두 더하기
    answer = sum(all_numbers)
    
    return answer