## 단순 구현, dict로 차량 번호마다 정보를 저장하면 됨.
# 해당 차량 입차 출차를 한 stack안에 다 넣자.
# ㄴ> 잘 못 된 경우는 없으니
#     혹수->마지막 케이스는 23:59 자동 출차
#     짝수-> 입차출차 짝 다 있음.
#     ㄴ> 홀수 경우는 맨 마지막빼고, 짝수경우는 그런거 없이 2개씩 뽑으면서 시간 측정하면 됨.
#     (시간도 오름차순 정렬되어 입력되어서.)

# 이후 dict의 keys를 정렬시켜서, 해당 번호의 stack에 대해 계산 후 결과를 answer에 담는걸 반복.

#####수도코드

# 정보dict
# records에서 ' '로 split해서 차량 번호 대해 list에 시간 저장 HH:mm append

# 함수 시->분 변환(시각 문자열)
#   문자열 ':'으로 분리
#   시를 number로 변환, 분도 number로 변환
#   분+=시*60
#   return 분

# 함수 resultForCar(차량번호)
#   시간스택:=dict[차량 번호] : 로 정보 찾아서 홀짝 체크
    
#   totalTime=0초기화

#   if 시간스택 데이터 개수 홀이면
#     23:59를 변환한 것 - pop결과 시각 을 totalTime에 추가
#   ## 공통
#   while 스택 빌 때까지
#     종료시각 = 시간스택.pop
#     시작시각 = 시간스택.pop
    
#     totalTime+= 종료시각 변환 - 시작시각 변환

#   if totalTime>기본시간
#     return 기본요금 + 올림((totalTime-기본시간)/단위시간) * 단위요금
#                         ㄴ> 그냥 %로 나눠지나 체크해서 안나눠지면 올림하자 안전하게.
  
#   # else  
#   return 기본요금

# 차량번호들 := 정보 dict .keys
# 차량번호들 오름차순 sort
# answer=[]
# for 차량번호 in 차량번호들
#   answer에 resultForCar를 append
# return answer

# __ 알고 대충 10분?
# __ 수도 대충 20분
# __ 엣지 나누기 수정 23분 대충 끝.
import math
def solution(fees, records):
    info = dict([])
    for r in records:
        timeString, carNumber, inOut= r.split(' ')

        if carNumber in info.keys(): ## 존재하면
            info[carNumber].append(timeString)
        else:
            info[carNumber] = [timeString]
    
    def hTm(timeString):
        h,m = map(int,timeString.split(':'))
        m+=h*60
        return m
    def resultForCar(carNumber):
        timeStack=info[carNumber]
        ## test
        # print("timeSTack: ", timeStack)
        totalMinute=0
        
        if len(timeStack)%2==1:
            totalMinute+= hTm('23:59') - hTm(timeStack.pop())
        
        while (timeStack):
            endT = timeStack.pop()
            startT = timeStack.pop()
            totalMinute+= hTm(endT) - hTm(startT)
            
        if totalMinute>fees[0]:
            extraTime = (totalMinute-fees[0])//fees[2] if (totalMinute-fees[0])%fees[2] == 0 else math.ceil((totalMinute-fees[0])/fees[2])
            
            ## test
            # print("엑스트라 시간: ", extraTime)
            
            extraFee=extraTime * fees[3]
            
            
            return fees[1] + extraFee
        
        return fees[1]
    
    
    answer = []
    
    cNums = list(info.keys())
    cNums.sort()
    ## test
    # print("info: ", info)
    for cN in cNums:
        
        # test
        # print("math", math.ceil(1.4))
        result = resultForCar(cN)
        ## test
#         print(result)
        
        answer.append(result)
        
    
    
    return answer