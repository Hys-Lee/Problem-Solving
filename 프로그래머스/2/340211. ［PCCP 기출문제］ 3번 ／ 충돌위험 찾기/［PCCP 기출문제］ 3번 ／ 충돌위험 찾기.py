# # 최단경로, (r,c)에서 r먼저 이동 (->최단경로 중 선택 기준)
# # 동 시간에 동일 위치인 경우들 개수 측정하기.

# # 최단경로가 1개로 고정되니까, 위험한 상황 개수도 확정되나본데
# #     ㄴ> 사실 최단경로 알고리즘이고 나발이고, 두가지 방향만으로 결정되는데,
# #         이 때, r이동 방향을 먼저 다 쓰도록 하는거니까.
        
# # 즉, 모든 최단 경로들이 다 예측이 되면, 시간당 어디 위치일지 다 알게 되네.

# # 즉, 시간과 로복 개수에 따라 시간복잡도가 결정되네
# #     로봇마다 경로 이루는 포인트 개수가 같은지 다른지는 모르겠네.
    
# #     경로 포인트가 3개 이상인 경우도 생각해야함.
# #         ㄴ> 인접하는 2개의 포인트로 경로를 다 짜놔야 할 듯.
        

# # 시간복잡도는 뭐, 100*1만 => 100만이라 쌉가능이고 걍 구현.

# # 포인트 2개로 경로 확정하기
# #     r차이, c차이를 알아내고,
# #     모든 로봇이 이를 갖고 있게 하면 되겠네. arr형태로. (경로 순서따라 갖게 하지.)
    
# # 로봇은 현재 위치랑 [[r차이,c차이],...]를 갖게 하면 될 듯.

# # ## 수도코드만들기
# # 포인트는 1부터 카운트. 좌표도 1부터 시작. 주의

# # convertedPoints=[[],...points]

# # robots=[] : [현재 위치, rcs, isValid]
# # for i routes
# #     현재 위치 = convertedPoitns[routes[i][0]]
# #     rcs=deque([]) -> queue로 만들어 사용. 
# #     for j [0,routes[i]길이-1]
# #         start=routes[i][j]
# #         end=routes[i][j+1]
        
# #         rdiff = end[0]-start[0]
# #         cdiff = end[1]-start[1]
# #         rcs.append([rdiff,cdiff])
    
# #     robots.append([현재위치,rcs,true]) 


# # def calcRcsZeros(로봇들)
# #     res=true
# #     for r 로봇들
# #         if r[1] 크기가 0이 아니면
# #             res = false
# #             break
# #     return res

# # rRcsZeros=false
# # answer=0
# # while(rRscZeros가 false라면 계속)
# #     curPs=[]
# #     for r robots
# #     ### 최종 목적지 도착하면 바로 robots에서 빼야 하나? -> 루프 크기 바뀌니까..
# #         ## ㄴ> 대신 validatoin flag가지도록 함.
        
# #         ## 여기서 validatoin으로 위험 체크 운송 종료 후에 한번만 실행되도록.
# #         if r[2]가 true면
# #             curPs.append(tuple(r[0]))
        
# #         if r[1][0]의 크기가 0이라면 
# #             r[2] = false : invalid로 처리 -> 위험 체크시 validation사용
# #             continue
        
# #         ## rcs가 있다는 가정
        
        
        
# #         if r[1][0]에서 [0]자리가 0이 아니라면 : r부터 조지기
# #             이동 = 0-r[1][0][0]
# #             r[0][0]+=이동 : 현재 위치에 반영
# #         else: c조지기
# #             이동 = 0-r[1][0][1]
# #             r[0][1]+=이동 : 현재 위치에 반영
        
# #         if r[1][0][0]이랑 r[1][0][1]모두 0이라면 (위 처리 후)
# #             r[1][0]은 popleft하기
    
    
    
# #     setCurPs = curPs를 set으로 만들기
# #     subCount=curPs크기 - setCurPs크기
# #     answer+=subCount
    
        
# #     rRcsZeros = calcRcsZeros(로봇들)

# # __ 알고 대충 18분
# # __ 수도 대충 42분

# 로봇 정보 초기화하기 로봇들:[현재위치, 이동정보 deque]

# #로봇마다 이동시키고, 한칸씩 이동 후 위험 체크하기 (초기 위치에서도 해야함)
# 루프: 모든 로봇의 이동정보 뎈이 빌 때까지 
    
#     #로봇들 현재 위치따라 위험 체크하기 -> 현재 위치가 중복 발생이 몇종류인지.
#     현재 위치 dict :초기화
#     루프: 로봇들 -> 정확히는 사라지지 않은 로봇들 : 이동정보 남아있는 로봇들
#         로봇들 현재 위치 dict에 있으면 +1 없으면 1로 생성
#     dict에서 1 초과인 장소들 개수를 answer+=하기
    
#     ## 아니, 체크하는 것은 도착한 당시까지임. 한턴 지나면 체크 제외됨.
#     ## 여기서 [최신 이동정보 사용 끝났다면 다음걸 최신으로 만들기]하자.
#     ## 왜냐면 이보다 위 작업에서는 이동정보에 대한 것은 건드리지 않고 읽기만 하므로.
#     루프: 모든 로봇들
#         if 최신이동정보 R,C모두 0이면
#             로봇의 이동정보.popLeft()    
    
    
#     #로봇마다 이동정보따라 1칸씩 이동
#     루프:로봇들
#         # 이동정보가 있다는 전재 하에서.. *** 이걸 떠올려야 함.
#         if 이동정보가 없다면 
#             넘기기
        
#         #이동정보 맨 왼쪽 참고해서 이동
#         #로봇 이동정보 중 R먼저 이동시키기. R이동 끝나면 C이동 시키기
#         if 로봇 이동정보에서 R이 0이 아니라면
#           R이 양수면 1, 음수면 -1만큼 현재 위치 이동.
#           이동정보에도 움직임 사용 반영
#         else
#             C에 대해 위와 같이 처리
            
#         #최신 이동정보 사용 끝났다면 다음걸 최신으로 만들기
#         ## 즉, 뎈에서 popLeft하는건데, 이는 while과 위험체크 모두 영향 미치니, 위에서 해도 될 듯. -> 즉, 여기 말고...
        
#### 실전
from collections import deque
def solution(points, routes):
    answer=0
    # 로봇 정보 초기화하기 로봇들:[현재위치, 이동정보 deque]
    robots=[]
    for route in routes:
        pointI = route[0]-1
        curP = points[pointI][:] ## -> 참조값 조심!
        mInfo = deque([])
        for i in range(len(route)-1):
            start=route[i]
            end = route[i+1]
            rDiff = points[end-1][0] - points[start-1][0]
            cDiff = points[end-1][1] - points[start-1][1]
            mInfo.append([rDiff,cDiff])
        robots.append([curP,mInfo])
    
    def allDeqEmpty(robots):
        res = True
        for r in robots:
            if len(r[1])>0:
                res = False
        return res

#     #로봇마다 이동시키고, 한칸씩 이동 후 위험 체크하기 (초기 위치에서도 해야함)
#     루프: 모든 로봇의 이동정보 뎈이 빌 때까지 
    loopStop = allDeqEmpty(robots)
    while(not loopStop):
    # loopCount=10
    # while(loopCount>0):
        curPs=dict([]) ## 키는 tuple로 해야함.
        for r in robots:
            if len(r[1])==0:
                continue
            curP = tuple(r[0])
            if curP in curPs:
                
                curPs[curP]+=1
            else:
                curPs[curP]=1

        for curPsKey in curPs:
            dupCount = curPs[curPsKey]

            if dupCount>1:
                answer+=1
        # ## test
        # print("ansdwer: ", answer)
#         #로봇들 현재 위치따라 위험 체크하기 -> 현재 위치가 중복 발생이 몇종류인지.
#         현재 위치 dict :초기화
#         루프: 로봇들 -> 정확히는 사라지지 않은 로봇들 : 이동정보 남아있는 로봇들
#             로봇들 현재 위치 dict에 있으면 +1 없으면 1로 생성
#         dict에서 1 초과인 장소들 개수를 answer+=하기
        
#         ## 아니, 체크하는 것은 도착한 당시까지임. 한턴 지나면 체크 제외됨.
#         ## 여기서 [최신 이동정보 사용 끝났다면 다음걸 최신으로 만들기]하자.
#         ## 왜냐면 이보다 위 작업에서는 이동정보에 대한 것은 건드리지 않고 읽기만 하므로.
#         루프: 모든 로봇들  - 수정
#             if 최신이동정보 R,C모두 0이면
#                 로봇의 이동정보.popLeft()    
        for r in robots: ## -> 이것도 레퍼런스 주소를 r에 담는거라 수정 들어가잖슴?
            ## 이도정보가 있다면....?
            if(len(r[1]))==0:
                continue
            if r[1][0][0]==0 and r[1][0][1]==0:
                r[1].popleft()
        # ## test
        # print("이동정보 최신화 후 robots: ",robots)
#         #로봇마다 이동정보따라 1칸씩 이동
#         루프:로봇들
        for r in robots:
#             # 이동정보가 있다는 전재 하에서.. *** 이걸 떠올려야 함.
#             if 이동정보가 없다면 
#                 넘기기
            if len(r[1])==0:
                continue

#             #이동정보 맨 왼쪽 참고해서 이동
#             #로봇 "최신"이동정보 중 R먼저 이동시키기. R이동 끝나면 C이동 시키기
#             if 로봇 이동정보에서 R이 0이 아니라면
            if r[1][0][0]!=0:
#               R이 양수면 1, 음수면 -1만큼 현재 위치 이동.
                move = 1 if r[1][0][0]>0 else -1
                r[0][0]+=move
#               이동정보에도 움직임 사용 반영
                r[1][0][0]-=move
#             else
            else:
#                 C에 대해 위와 같이 처리
                move = 1 if r[1][0][1]>0 else -1
                r[0][1]+=move
                r[1][0][1]-=move

#             #최신 이동정보 사용 끝났다면 다음걸 최신으로 만들기
#             ## 즉, 뎈에서 popLeft하는건데, 이는 while과 위험체크 모두 영향 미치니, 위에서 해도 될 듯. -> 즉, 여기 말고...
            
            # ## test
            # print("이동 후 robots: ", robots)
        # loopCount-=1
        loopStop = allDeqEmpty(robots)
    
    # answer=0
    return answer



##  ㄴ> 혼자 80분은 다 썼음...

# from collections import deque

# def solution(points, routes):
#     answer = 0
    
#     cpoints=[[]]
#     cpoints.extend(points)
    
#     robots=[] # [현재 위치, rcs, invalid]
#     # for i routes
#     #     현재 위치 = convertedPoitns[routes[i][0]]
#     #     rcs=deque([]) -> queue로 만들어 사용. 
#     #     for j [0,routes[i]길이-1]
#     #         start=routes[i][j]
#     #         end=routes[i][j+1]

#     #         rdiff = end[0]-start[0]
#     #         cdiff = end[1]-start[1]
#     #         rcs.append([rdiff,cdiff])

#     #     robots.append([현재위치,rcs,true]) 
    
#     for i in range(len(routes)):
#         curP = cpoints[routes[i][0]][:] ## cpoints에서 참조로 가져오는거라 공유되고 있었음...
#         rcs = deque([])
#         for j in range(len(routes[i])-1):
#             start=routes[i][j]
#             end=routes[i][j+1]
            
#             rdiff = cpoints[end][0]-cpoints[start][0]
#             cdiff = cpoints[end][1]-cpoints[start][1]
#             rcs.append([rdiff, cdiff])
            
#         robots.append([curP, rcs, True])
    
#     # def calcRcsZeros(로봇들)
#     #     res=true
#     #     for r 로봇들
#     #         if r[1] 크기가 0이 아니면
#     #             res = false
#     #             break
#     #     return res
#     def calcRcsZeros(robots):
#         res =True
#         for r in robots: 
#             if len(r[1])>0:
#                 res = False
#                 break
#         return res
        
    
#     rRcsZeros=False
#     answer=0
    
#     ## test
#     print("초기로봇: ",robots)
    
#     # tmpCount=4
    
#     # while(tmpCount>0):
#     while(not rRcsZeros):
#         curPs=[]
#         for i in range(len(robots)):
            
#             if robots[i][2]: ## valid하면 위험 지역 처리
#                 curPs.append(tuple(robots[i][0]))

                
#             if len(robots[i][1])==0:
#                 robots[i][2] = False ## invalid시키고 이동 동작은 안함
#                 ### Test
#                 print("이게 실행되는 때가 있나?")
#                 continue
#             else:    
#                 if robots[i][1][0][0] == 0 and robots[i][1][0][1]==0:
#                     robots[i][1].popleft()
            
#             ## 아래는 rcs가 있따는 가정
#             #### 이동할 때 1칸씩, 그리고 rcs도 같이 업뎃해야함..
#             if robots[i][1][0][0]!=0:
#                 move=1 if robots[i][1][0][0]>0 else -1 
#                 robots[i][0][0]+=move
                
#                 robots[i][1][0][0]-=move ## 업뎃
                
#             else:
#                 move=1 if robots[i][1][0][1]>0 else -1 
                
#                 robots[i][0][1]+=move
#                 robots[i][1][0][1]-=move
            
#             # ## test
#             # print("robots가 변하는 위치 찾기",robots)
            
         
        
#         ## test -> 수행 순서가 꼬였네.
#         print("robots: ",robots, curPs)
        
#         setCurPs = set(curPs)
#         subLen = len(curPs) - len(setCurPs)
#         subCount=0
#         ## ㅅㄷㄴㅅ
#         if(subLen>0):
#             for tup in setCurPs:
#                 count=0
#                 for cp in curPs:
#                     if cp==tup:
#                         count+=1
#                 if count>=2:
#                     subCount+=1
                
#             print("언제죠: ",curPs, setCurPs)
#         answer+=subCount ## 이것도 아니지. 겹친 튜플의 종류의 개수를 알아내야지.
#         ## test
#         print("answer: ",answer)
#         rRcsZeros = calcRcsZeros(robots)
#         # tmpCount-=1
    
    
#     return answer