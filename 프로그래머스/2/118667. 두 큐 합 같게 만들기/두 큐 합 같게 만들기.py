# 두개 길이가 최대 30만이니까, 총 60만?

# 일단, 큐 동작 경우의 수는 2^30만 승이거덩요

# 생각해보면, 한쪽만 절반 합을 맞추면 나머지는 자동이자너?

# 그래서 브루트포스로 하면 걍 N^2임.

# 근데, 결과적으로 두 큐를 이어붙인 하나의 큐에서 특정 연속된 구간의 합이 목표값이 되면 되는걸임.

# 최소 횟수는 큐를 붙이는 2가지 경우 중에서 각각의 계산 중 최소를 찾아내면 되니까 일단 ok.


# greedy하게 대충 목표 값에 근점할 때까지 구간 길이를 늘리고, 다음 걸 포섭하면 목표값 넘어선다? 그러면 구간 시작점을 한칸 땡겨보고, 또 부족하면 한칸 땡겨보는 식
# -> 이건 O(N)일거아니야.

# -1이 나오는 경우는 두 방식으로 큐를 붙여서 greedy하게 구간 작업했는데, 마지막까지 가도 안나오는 경우겠네. 둘다
# 산술 오버플로우 생각해보면, 10^9*300000의 가능성이 있긴 함. 대충. 그래도 뭐 파이썬은 가능하겠지.


# 예시1
# 3,[2,7,2,4],6,5,1 ->3밀어내고 4땡겨오니 2
# 4,6,5,[1,3,2,7,2] ->4,6,5밀어내고 3,2,7,2땡겨오니 7
# 예시2
# 1,2,1,2,/1,[10],1,2 -> 1,10 땡겨오니 1,2,1,2,1 밀어내면 7
# 1,[10],1,2,/1,2,1,2 -> 1밀어내고 10밀어내고 1,2,1,2땡겨오고 1 한번 더 땡겨오면 만들어지는데 7

# ㄴ> 괄호 마지막번째까지 땡겨오고 괄호 시작 이전까지 밀어내면 완성이네.
#     ㄴ> 큐 분리지점은 중간임. 둘의 길이는 항상 같나봄.
# 예시3
# 1,1,1,5  -> 괄호가 길이가 0이 될 때까지 쪼그라들게 됨. 못찾아서
# 1,5,1,1 -> 얘도 같음.

# 에시4 만약에 큰거때문이 아니라 적당한걸 못찾으면? -> 전체 원소 합이 홀수면.. 무조건 -1이네.
# 3, 1, 2, [4]   => 마지막 괄호가 끝까지 갔을 때도 못찾은 경우.

# ㄴ> 따라서 종료되는 경우는 합이 -1, 괄호 크기가 0이 되어서, 괄호 끝이 전체 끝에 닿았는데도 못찾아서 부족할 때.

# ## 수도코드
# 케이스1:= 큐1뒤에 큐2붙이기
# 케이스2:= 큐2뒤에 큐1붙이기

# totSum = 케이스1(2도 상관x)의 합
# if totSum 이 홀수 -> -1 반환.

# target = totSum//2


# def findTarget(합친 큐)으로 밑의 내용 함수 만들기
#     answerSp는 0, answerEp는 1이 되게 하자.
#     subSum=초기 구간 합(맨앞에 하나 값)으로 초기화 #해당 구간 합을 매번 계산할 순 없으니, 기억해야 함.
#     findF = False로 플래그 초기화
#     while answerEp가 합친큐의 길이값에 닿을 때까지 ok (answerEp는 다음거를 미리짚고 있음.)
#       if answerSp>=answerEp가 되면(쪼그라들면)
#         break


#       if subSum+answerEp자리값이 target보다 크면
#         subSum에서 answerSp위치의 값을 빼고 업뎃 후
#         answerSp위츠를 +=1
#       elif subSum+answerEp자리값이이 target보다 작으면
#         subSum을 answerEP자리값 더한걸로 업뎃.
#         answerEp+=1
#       else subSum+answerEp자리값이 target과 같으면
#         findC1플래그 True로 바꾸고 break
    
#     if findF가 False면 
#       return -1 반환
    
#     #findF가 True면..
#     answer=0 : 초기화
#     if answerEp-1위치가 절반 위치보다 앞에 있다면: 
#         # 만약에 0,0,[0,0],0,/0,0,0,0,0라면?
#         answer+= answerEp : 괄호 마지막 위치까지 다은 큐에 넣기.
#         answer+= 전체큐크기//2+answerSp앞의 개수들(0번부터니, "answerSp값" 그 자체임.) (다른쪽 큐에 대해서 빼기.)
#     else  -> 정확하게는 절반 위치 뒤에 있다면.
#         # 0,0,0,[0,0,/0,0,0],0,0  => 8-5
#         answer+= answerEp - 절반 위치 : 한쪽 큐에 정답에 들어가는 애들까지 넣기
#         answer+= answerSp : 해당 큐에서 정답 범위 시작 전애들을 다 빼기
     # if *** answerEp가 절반 위치에 있다면
         # 0,0,0,[0,0],/0,0,0,0,0 => 3번이면 됨.
        # answer+=answerSp 면 끝.
        # if answerEp-1위치가 tot의 맨 끝이리ㅏ면 -> 
         # 0,0,0,0,0,/0,0,0,[0,0] => 3번이면 됨.
        # answer+=answerSp-len(tot)//2
          
    
    
# 케이스1과 케잉스2에서 findTarget거쳐서 작은 값을 반환. (-1도 포함되어 처리되겠지.)

# __ 알고 대충 29분
# __ 수도 대충 54분
# __ 엣지 대충 (알고는 해봤고, 수도도 좀 해봄.) 55 분
# __ 틀림 80분 2번,29번  -> 알고리즘에 문제가 있는 듯 findF가 true일 때의 방법.. -> flag true이후 방법.
# __ 틀림 91분 2번 

from collections import deque
def solution(queue1, queue2):
    
    case1 = queue1[:]
    case1.extend(queue2)
    case2 = queue2[:]
    case2.extend(queue1)
    
    
    totSum = sum(case1)
    if totSum%2==1: return -1
    target = totSum//2
    
    def findTarget(totque, target):
        answerSp=0
        answerEp=1
        subSum = totque[0]
        findF=False
        while(answerEp<=len(totque)-1): ## 이게 맞지. answerEp위치를 담으니까 마지막 인덱스여야지..
            ## test
            # print("Sp, Ep, subSum, totque,target: ", answerSp, answerEp, subSum, totque, target)
            # if answerSp>=answerEp:
            if answerSp>answerEp:
                break
            
            if subSum+totque[answerEp]>target:
                subSum-=totque[answerSp]
                answerSp+=1
            elif subSum+totque[answerEp]<target:
                subSum+=totque[answerEp]
                answerEp+=1
            else: # subSum+totque[answerEp]==target:
                answerEp+=1 ## answerEp칸도 포섭했으니까.
                findF = True
                break
        
        if not findF:
            return -1
        
        answer=0
        if answerEp==len(totque)//2:
            answer+=answerSp
        elif answerEp==len(totque):
            answer+=answerSp-len(totque)//2
        elif answerEp-1<len(totque)//2:
            answer+=answerEp
            answer+=len(totque)//2+answerSp
            ## test
            # print("이런 answer: ", answer)
        else :
            answer+=answerEp-len(totque)//2
            answer+=answerSp
            ## test
            # print("저런 answer: ", answer)
        return answer
        
                
    res1 = findTarget(case1, target)
    res2 = findTarget(case2, target)
    return min(res1, res2)
    
    # return answer