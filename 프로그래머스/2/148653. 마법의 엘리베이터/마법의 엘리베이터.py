# 뭔가 화폐로 돈 만드는 느낌과 유사하지? 
# 근데, -도 가능한게 거시기함.
# 그리고 층 최대 개수가 1억개니까, 무작정 dp하긴 좀 그럼

# 생각해보니까, 사실 +,-버튼들 누르는 순서는 상관 없잖아.
# -를 먼저 생각해도, 실제로는 +를 먼저 눌러서 이동했다고 보면 되니까.

# 그러니까 무조건 0근처로 가는 것만 먼저 생각해도 될 듯.

# 한번에 이동 가능한 초대 범위도 있음. 절댓값으로 10^8 임.
# 60층은 -100 x 1 에 +10 x 4 이 빠름ㅗ  -10 x 6 보다.
# 50층은 -10 x 5 가 가장 빠름.

# 중간을 넘으면 -쪽으로 넘겨주는게 가장 빠른가?
# 55층은 -100 x 1 +10 x 4 +1 x 5 =>10
#         -10 x 5 -1 x 5 => 10
# 56층은 -100 x 1 + 10x 4 + 1 x 4 => 9   
#         -10 x 5 -1 x 6 => 11
# 51층은 -100 x 1 + 10 x 4 + +1 x 9 => 14
#        - 10 x 5 -1 x 1 => 6

# ㄴ> 밑의 자리 수에 영향을 받는다. 어떤게 최선인지는.
# ㄴ> dp로 봐도 될 듯?
#  각 자리수에 대해서 -를 2번할지 3번할지, 각각에서 그 다음 자리수에 대해서는 어케 움직일지...
    
# 위처럼 타겟 지점에 대해 양옆 근처에서 어떤 선택을 할지를 계속 하는건, 가능한 경우가 최대..
# 층 최대가 10의 8승이니까  2^8아님? 모든 가능한 경우의수가.
# 이 중 최소를 뽑으면 되잖아.

# 그럼 약간 dp라기보다는 dfs로 접근해야 할 듯.
# 각 단위에서 분기가 갈라져도, 끝까지 몇 번 눌렀는지 누적으로 끌고가긴 해야하니까, 현재 케이스에서는.
# 어떻게 보면 시나리오들을 만드는거임. 이 최대 2^8개의 시나리오들 중 최솟값을 가져오면 됨.

# dfs네.
# 값이 있을 때, 예를 들어 2345면, -2000할지 -3000할지로 나누고, -2000에서는 -400할지-300할지 나누고...

# 만약에 1001이면.. -1000하고 시작하겠지.
# 그럼 999면.. -900이랑 -1000 둘을 봐야하는데, -1000은 다른 단위잖아.
# 근데, 이게 nested로 계속 다른단위인지 체크할 필요는 없는게, 이미 이전 단위에서 반영되어 내려온 것.
# 예를 들어 999에서 -900을 골랐다면, -100할지 -90할지 선택해야 할텐데,
#     그 이전엥 -1000을 생각해놨다면 -100은 의미없는 선택지가 됨.
#     즉, 현재 단위에서 체크를 못한다면(단위가 넘어간다면) 그 선택지는 포기.(이미 반영되었으니)

# 따라서, 맨 처음에만 단위 잘 체크하면 됨.2000이라면 -10000 x 1이랑 -10000 x 0 에서 시작하도록 하는거.


# ## 수도코드 만들기
# maxIdx = storey가 몇자리수인지 알아내기
# results=[] : dfs끝까지 갔을 때 최종 누를 횟수들 저장
# def dfs(curV, numIdx, clickNum) : 타겟에 대해 양옆 2개씩의 케이스에 대해 타겟으로 다가가는 방법. 어떤 단위에 대해서인지도 필요할 듯. -> numIdx는 0일 때는 1의자리에 대한거로 보도록.
#   curv가-1234라면 +1000할지+2000할지 고민
#   curv가 1234라면 -1000할지 -2000할지 고민. 결국 현재 인덱스자리만큼 혹은 하나더(절댓값으로.)
#     그 중 자리수가 넘어가면 그냥 포기.
    
#   if numIdx<0:
#     result.append(clickNum)
    
#   accessor=절댓값(curV) // (10**numIdx)
#     ***** 위의 방식으로 해도 되는지체크(부호)    
    
#   if accessor + (10**numidx) 를 10**numidx로 나눴을 때 몫이 10이상이면 
#     continue (이 방향에서는 패스)

#   nextV1=0
#   nextV2 = 0
  
#   if curv가 양수면 
#     nextV1 = curv-accessor*(10**numIdx)
#     nextV2 = curv-(accessor+1)*(10**numIdx)
#   else : curv가 음수면
#     nextV1 = curv+accessor*(10**numIdx)
#     nextV2 = curv+(accessor+1)*(10**numIdx)
#   dfs(nextV1, numidx-1, clickNum+accessor)
#   dfs(nextV2, numidx-1, clickNum+accessor)

# #맨청므에는 n자리수(maxidx+1)라고 한다면 n+1자리수(maxidx+2) 처리 하고 dfs를 돌려야 함.
# dfs(storey, maxIdx)
# dfs(storey-10^(maxIdx+1), maxIdx) : 1자리수는 10^0이니까, -10^1를 해야 하니.

# 이후에 min(result)를 반환

# __ 알고 생각함 29:45
# __ 수도코드 (좀 너무 자세하수도) 57:30
# __ 틀림 89분 엣지 한번 생각한거긴 한데..


## 엣지케이스 생각해보면, 10=>1, 99999999 =>2 , 1=>1로 해보자 => 통
## 위의 다른 엣지 케이스도 맞는데..





def solution(storey):
    maxIdx = 0
    for i in range(8,-1,-1):
        if storey // (10**i) != 0:
            maxIdx = i
            break
    
    ## test
    # print("storey는 10의 i승 단위 값: ", i)
    
    results=[]
    
    def dfs(curV, numIdx, clickNum):
        # if numIdx<0:
        if curV==0:
            ## test
            # print("curV는 0이어야 하는뎅, clickNum: ", curV, clickNum)
            results.append(clickNum)
            return
        accessor  = abs(curV) // (10**numIdx)
        ## test
        # print("accessor,numIdx: ", accessor,numIdx)
        if (accessor + (10**numIdx)) // (10**numIdx) >= 10: ###
            
            ## test
            # print("이미 상정한 경우: ",accessor , (10**numIdx))
            return # 이번 시나리오는 이미 한거라 필요 없음
        # if accessor == 0:## 1024에서 0에서 100에서 10자리?
        #     ## 여기서 그냥 넘기는게 아니라, 현재 자릿수 처리해야함. 마치 맨 처음처럼.
        #     ## 1024면 0에서 
        #     dfs(curV, numIdx-1, clickNum)
        #     return 
        
        nextV1=0
        nextV2 = 0
        #### 애매한게, -10이면 +10이랑 +20을 고려할거란 말이지. +20의 경우는 +10이 다음 값이고. 이러면 영원히 -10, +10으로 진동하게 됨.
        if curV>0:
            nextV1 = curV-accessor*(10**numIdx)
            nextV2 = curV-(accessor+1)*(10**numIdx)
        elif curV<0 :# curv가 음수면
            nextV1 = curV+accessor*(10**numIdx)
            nextV2 = curV+(accessor+1)*(10**numIdx)
        else : ## curv==0이면. 즉, idx가 0자리 가기 전에 찾았다면.
            ## test
            # print("0th가기 전에 끝냈다면 curV,numIdx, accessor, clickNum: ", curV,numIdx, accessor, clickNum)
            # print("근데 이거하면 idx가 -1은 영원히 없을텐데")
            results.append(clickNum+accessor)
            return
        ## test
        # print("nextV1, nextV2: ", nextV1,nextV2)
        dfs(nextV1, numIdx-1, clickNum+accessor)
        if nextV1 != 0:
            dfs(nextV2, numIdx-1, clickNum+accessor+1) # 한번 더 간거 고려한거니.
    
    
    ## test
    # print("storey, storey-10**(maxIdx+1): ", storey, storey-10**(maxIdx+1))
    dfs(storey, maxIdx,0)
    dfs(storey-10**(maxIdx+1), maxIdx,1)# : 1자리수는 10^0이니까, -10^1를 해야 하니.
    
    ## tset
    # print("results: ", results)
    
    answer = min(results)
    return answer