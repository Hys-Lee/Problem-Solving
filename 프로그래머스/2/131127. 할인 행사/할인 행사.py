# # 브루트포스는 1억이라 시간초과
# # 체크리스트나 dp같이, number랑 똑같이 만들자. matches
# # 그리고 matcehs에는 discount에서 number길이만큼의 윈도우에서 number의 각 인덱스 대응 품목이 몇개 있는지.
# # 윈도우를 움직일 때마다 한칸이 빠지고 새로 한칸이 들어오는데, 이에 맞춰서, 빠지는 품목에서 개수를-1,
# # 추가되는 품목에서 개수를 +1로 해주자.

# # 10만 * number크기 => 100만이면 끝날 듯 -> O(N)느낌임.

# #### 수도코드

# window:= number랑 똑같은 크기로 만들기 (일단 0채우자.)
# discount에서 0번째부터 number크기만큼 개수 세면서 window에 들어갈 수를 초기화. (각각에 해당하는 애들 개수 측정하기)

# answer=0

# window시작 지점을 wpointer로 잡고 0으로 초기화 하면 되네.
# for window시작 지점을 0번부터 (discount길이-개수) 인덱스까지
#     ## check
#     for문 window길이만큼
#         numbver원소랑 window원소 체크
#     if number랑 window랑 모든 원소가 같다면
#     answer+=1
    
#     (길이 11, number길이는 10이면, 1까지=>0,1으로 2칸 이동하니까 맞지.)
#     wpointer에서 dicount통해 품목 알아내, 몇번째 인덱스인지 알아내기 => mapping위해 dict가 필요. (인덱스를 값으로 값을 key로 하는.)=>(O(1))
#     해당 인덱스의 window에서의 값-=1
#     wpointer+=1
#     wpointer+window크기-1 위치 (10길이면 시작0이면 끝은 9니까) 품목이 몇번째 인덱스 알아내기
#     해당 인덱스의 window에서의 값+=1
    
    
# return answer


# __ 알고 대충 4분
# __ 수도 14분
# __ 엣지 대충 20분(없음)



def solution(want, number, discount):
    answer = 0
    curNum = [0 for i in range(len(number))]
    wantMap=dict([])
    for i in range(len(want)):
        wantMap[want[i]] = i
    
    ## test
    # print("wantMap", wantMap)
    
    windL = sum(number)
    
    ## 0번재부터.
    for i in range(windL):
        if discount[i] in want: ## 미친놈이 있어야 체크하지.. => 100연산 최대
            curNum[wantMap[discount[i]]]+=1 ## 이것도..
        
    chF=True
    for i in range(len(curNum)):
        if number[i] != curNum[i]:
            chF = False
    if chF:
        answer+=1
    
    
    for wsp in range(1,len(discount)-windL+1): # 마지막은 미포함이자너..
        
        
        
        ## 본문
        if discount[wsp-1] in want:
            curNum[wantMap[discount[wsp-1]]]-=1 ## 있다면.
        
#         # wsp+=1 ## 여기 중복되니까, 따로 계산 ㄱㄱ-> 마지막 
        lastP = wsp+windL-1
        if discount[lastP] in want:
            curNum[wantMap[discount[lastP]]]+=1 ## 있다면.
        
        ## test
        # print(curNum,number, wsp)
        
        chF=True
        for i in range(len(curNum)):
            if number[i] != curNum[i]:
                chF = False
        if chF:
            answer+=1
    
    return answer




