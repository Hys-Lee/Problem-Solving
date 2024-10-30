# # 상자 번호랑 카드 번호랑 다르기 때문에 일어나는 일인ㄹ데,
# 이미 체크한 상자번호가 카드에서 나와야 종료되는거자너.

# 그리고 최고 점수를 구하는거니까,
# 일단 그룹지을 수 있는것들은 다 지어놓고

# 상자수 값 크기별로 정렬해서 큰거 2개 고르면 되네.

# 근데, 체크리스트만들고 그냥 루프 달리면 되는거 아닌가?
# 그럼 for안에 while있는 느낌이겠네.
# 카드 최대 100개이고, 체크리스트 쓰니까 걍 O(N)인 것 같은데..

# 왜 30%인거지

# 일단 저정도로.

# ## 수도코드만드릭


# 체크리스트=[false를 카드 수만큼 초기화]
# 그룹크기들=[]: 그룹에 속하는 카드 개수들을 저장.

# def 그룹만들기(현재 상자인덱스)
#   현재그룹크기=1
#   체크리스트[현재상자인덱스] = true
#   다음 상자인덱스 = cards[현재상자리스트]-1
#   while(체크리스트[다음상자인덱스]가 true만나면 종료)
#      체크리스트[다음상자인덱스] = true
#      현재그룹크기+=1
#      다음 상자 인덱스= cards[다음상자인덱스]-1  : 업뎃
     
    
#   ret 현재그룹의크기

# baseI=0
# while 카드 전체 다 돌 때까지(개수로 체크)
#   if 체크리스트로 baseI가 True면 continue
#   그룹크기들.append(그룹만들기(현재 baseI))
  
#   baseI+=1

# 그룹크기들 정렬
# 그룹크기들 reverse
# return 그룹크기[0] * [1]을 => [1]이 없으면 0을 곱하게 됨.
    
    
# __ 알고 대충 6분
# __ 수도대충 15분
# __ 엣지 : 상자 더 열게 없을 때, 카드값-1을 인덱스로 해야함. (문제 읽으며 조건 및 제한 체크하며 찾음)
#   더 없어 보임. 20분

def solution(cards):
    checklist=[False for _ in range(len(cards))]
    groupSizes=[]
    
    def makeGroup(curBi):
        curGsize=1
        checklist[curBi] = True
        nextBi = cards[curBi]-1
        while(not checklist[nextBi]):
            checklist[nextBi]= True
            curGsize+=1
            nextBi = cards[nextBi]-1
        
        return curGsize
    
    ## test
    # print("makegroup에 0번째 넣고 돌려보면: ", makeGroup(7),checklist)
    # return 0

    baseI=0
    while baseI<len(cards):
        if checklist[baseI] == True: 
            baseI+=1 ## 얘를 빼먹었었음.
            continue
        newGsize = makeGroup(baseI)
        ## test
        # print("newGsize, baseI에서, checklist: ", newGsize, baseI, checklist)
        groupSizes.append(newGsize)
        baseI+=1
        
    groupSizes.sort()
    groupSizes.reverse()
    ## test
    # print("groupSizes:"  ,groupSizes)
    
    if len(groupSizes)==1:
        return 0
    return groupSizes[0] * groupSizes[1]
        
    
    
    
    answer = 0
    return answer