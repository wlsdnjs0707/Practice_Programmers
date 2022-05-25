# 숫자 문자열과 영단어

def solution(s):
    
    # 리스트로 변환
    num = list(s)

    # 숫자만 담을 리스트
    ans = []

    # 문자 길이만큼 건너 뛸 횟수 저장
    count = 0

    for i in range(len(num)):

        if ord(num[i])>=48 and ord(num[i])<=57: # 숫자이면
            ans.append(num[i])
        else: # 문자이면
            # zero one two three four five six seven eight nine
            # two - three, four - five, six - seven 은 다음 문자까지 확인하여 구분 이외 숫자는 한 문자만 보고 유추
            if count>=1: # 건너 뛸 횟수가 남아있으면
                count-=1 # 건너 뜀
            elif num[i]=='z':
                count = 3
                ans.append('0')
            elif num[i]=='o':
                count = 2
                ans.append('1')
            elif num[i]=='t':
                if num[i+1]=='w':
                    count = 2
                    ans.append('2')
                elif num[i+1]=='h':
                    count = 4
                    ans.append('3')
            elif num[i]=='f':
                if num[i+1]=='o':
                    count = 3
                    ans.append('4')
                elif num[i+1]=='i':
                    count = 3
                    ans.append('5')
            elif num[i]=='s':
                if num[i+1]=='i':
                    count = 2
                    ans.append('6')
                elif num[i+1]=='e':
                    count = 4
                    ans.append('7')
            elif num[i]=='e':
                count = 4
                ans.append('8')
            elif num[i]=='n':
                count = 3
                ans.append('9')
                
    answer = ''.join(ans)
    answer = int(answer)
    
    return answer