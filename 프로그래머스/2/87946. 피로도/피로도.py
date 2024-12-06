# 처음에는 greedy로 정렬을 잘 하면 되지 않나 싶었는데,
#     생각해보면 무작정 최소필요도가 높은 순으로 본다고 최대로 돌 수 있지는 않을 것.
#         최소 필요도가 높은데, 소모피로도도 높다면 안 도는게 좋을 수도 있으니.
    
# 그리고 보니까 던전 최대 개수가 8개라서,
#     완전 탐색 시켜도 될 것 같은데 (애초세 사실 문제도 완전탐색 유형이라 하기도 하고)

# 8! = 56*30*12*2 = 1680*24= 얼마 안됨. 

# 첫 8개에 대해부터 dfs로 체크하면 될 듯? 
#     결과를 그냥 하나의 arr에 쑤셔 넣고 최대값만 뽑으면 될 듯.

    
# ## 수도코드만들기
# dcounts=[]
# def dfs(현재 경로, 현재 피로도)
#   cantmove=true
#   for 다음 던전 in 던전스
#     if 현재 경로 길이가 던전스 길이
#       ## 종료 상황
#       dcount에 8을 append
#       return : dfs종료
#     if 다음 던전이 in 현재 경로
#       continue
#     if 다음 던전의 최소 필요도>현재 피로도
#       continue
#     현재 피로도-=다음 던전의 소모 피로도
#     cantmove=false
#     dfs(현재경로에다음던전추가, 수정한 현재 피로도)
#     현재 피로도+= 다음 던전의 소모 피로도 (원상복구)
    
#   if cantmove
#     현재 경로 길이를 dcount에 append
    
# dfs에 빈거(set으로), k넣고 돌리기
# dcounts에 max값을 반환


# __ 알고 대충 10분정도
# __ 수도 대충 21분
# __ 엣지 없는 듯 25분 (k가1, 던전스가 1개 해봄.최소필요랑 소모피로는 같은 상황같은거 신경 안써도 될 듯.) , 엣지 생각남 -> 서로 다른 던전의 최소 필요랑 소모 피로가 같다면, set에서 구분 가능해야 함. -> 던전스를 재정의 하는것도 좋을 듯. 인덱스 값을 하나 더 넣어서 id로 사용하면 될 듯.



def solution(k, dungeons):
    ## 던전스 재정의
    for i in range(len(dungeons)):
        dungeons[i] = (dungeons[i][0],dungeons[i][1],i)
    ## test
    # print("던전스 재정의: ", dungeons)
    
    dcounts=[]
    def dfs(curP, curT):
        ## tset
        # print("curP, curT", curP,curT)
        
        cantmove= True
        for nextD in dungeons:
            if len(curP) == len(dungeons):
                dcounts.append(len(dungeons))
                return
            if nextD in curP:
                continue
            if nextD[0]>curT:
                continue
            curT-=nextD[1]
            cantmove=False
            curP.add(nextD)
            dfs(curP, curT)
            ## 원복
            curP.remove(nextD)
            curT+=nextD[1]
        if cantmove:
            dcounts.append(len(curP))
    
    mycurp = set([])
    dfs(mycurp, k)
    ## test
    # print("dcounts",dcounts)
    
    
    
        
    answer = max(dcounts)
    return answer