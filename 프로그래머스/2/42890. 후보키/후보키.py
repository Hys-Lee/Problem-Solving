# 아니 문자열 비교게 O(N)이 걸리겠지 파이썬도?

# 만약 그렇다면, 8C1+8C2+...8C8은 대충 8!쯤이라고 하고, 
# 각각마다 20*8의 연산을 거친다고 치면...
# 87654321
# 56*30*12*2=1680*24=>얼마 안됨. 160곱해도 천만 단위도 안될 듯.

# 걍 하면 되는 듯? 구현문제인 듯.

# 그냥 콤비네이션을 써야 겠는데요?
#     그래서 컬럼들 조합을 알아내어서,
#     각 조합에 대해 row내려가면서 체크하면 될 듯.
#     이 때, 성공한 후보키들을 모아두고, 뭐 다음 구성개수에서 성공한 것들을 완전히 포함하는지 체크하면 됨.
#         이거 시간복잡도 오래 걸리지 않는 방식 없나?
        
#         성공한 후보키도, 조합도 Set으로 저장하고 있으면,
#             조합에 후보키 add시키고도, 조합에(개수 많은쪽이지) 개수 변화가 없다면, 완전히 포함하는거임.
#             이거면 뭐 가능할 듯?
#             이렇게 하면 O(N)느낌이 될 듯. (아니면 O(N^2)느낌이었음.)
            
# 직접 계산 해볼까?
# 8c1,8c2,8c3,8c4
# 8    28  56  56 ->합의 2배면 1000도 안됨. 
# 아니, 성공한 후보키가 최대 몇개까지 나올 수 있는지 계산이 잘 안되는데..
#     대충 8C4라고 할 수 있을 듯.. 56개.
#     그럼 말도 안되지만, 매 구성개수 증가마다 56개씩 체크한다고 치면...
    
#     1000*56 = 56000 에 row랑 문자열 길이 다 해도 56000*160 = 10,000,000 이면 천만임.
#     즉, 천만 이하이므로 쌉가능

    
# ### 수도코드만드릭

# 성공후보키들=[] # 내부에 set이 들어감.

# #relation[0]의 크기K에 대해 
# for i [1,k]
#   colI 조합들: [0~K-1]에서의 combination을 i 대해 진행
#   for colI조합 in 조합들
#       colI조합 내부 요소를 set에 투입. (set으로 만들기)
#       colISetLen = colISet의 기존 크기 측정
#       for 성공 후보키들
#           colISet에 성공 후보키를 추가
#           if colISet의 len이 colISetLen과 같다면 : 이 후보키구성은 이전을 포함하니, "최소성" 위배
#               continue -> 가 아니고, 이번 colISet을 버려야 하니, 바깥에 flag만들기
#       #"유일성 체크" : 뒤로 갈수록 후보키조합길이가 길어진건 위에서 걸러져서 부담 적을 것.
#       유일성박스 = set([]) : 후보키조합으로 relatoin에서 골라진 것들 키로 만들어 담는 통
#       for row in relation
#           rowResult = []: 일단 array에서 ("","",...) colILen길이만큼의 튜플로 만들거임.
#           for colI in colISet
#               rowResult에 row[colI]를 넣기
#           rowresult를 tuple로 만들기
#           유일성 박스에 튜플 넣기
#       if 유일성 박스 크기가 relation크기보다 작다면: 겹치는게 있다는 거임.
#           continue
#       ## 이거 넘으면 유일성 체크 통과이므로 
#       성공후보키.append(set(colI조합)) (tuple로 안되면 array로 바꾸고 set시키든가)

# return 성공후보키 크기
        
    
    
# __ 알고 대충 15분?
# __ 수도 대충 30분
# __ 엣지 (시간복잡도 초과하게 구현한게 있는가? )
#     - 뭐 딱히 없는 듯?, 구현하다가 조합들 중 조합하나를 고르는걸 까먹어서 추가., 최소성 체크할 때, for문 바깥을 멈춰야 해서 flag사용으로 변경, 성공 후보키는 set들을 저장할 필요는 없어 보임 오히려 불편함. tuple로 저장하자.

# __ 48분 틀림. 46.4점

from itertools import combinations

def solution(relation):
    sucCanKeys=[] # tuple들이 저장
    colLen = len(relation[0])
    colITemplates = [i for i in range(colLen)]
    for i in range(1,colLen+1):
        combis = combinations(colITemplates, i)
        for combi in combis:
            ## 최소성
            
            miniFlag = True
            for canKey in sucCanKeys: ## colIList는 쌓이는데, colIListLen은 그대로라 생기는 문제였네..
                colIList = list(combi) ## 처음부터 set으로 하지 말고, list로 했다가 하자.
                colIListLen = len(colIList)
                colIList.extend(list(canKey))
                colISet = set(colIList)
                ## test
                # # print("colIListLen, canKey,colISet: ", colIListLen, canKey,colISet)
                if len(colISet)==colIListLen: ## 길이가 같을 때 버려야지. 그래야 이미 존재한다는 거니까. -> 아니네. 일부만 겹칠 수도 있으니, 각 원본 길이 합이 더해진 합인지 체크해야하네. 동일하면 완전 다른거니까, 넘기는거고, 그렇지 않다면 일부라도 겹친는거니까 버러니느거.
                    ## 아하 일부 포함이 아니라 완전 겹치는 경우만 제외해야 하는데,
                    ## 일부 포함도 제외해버렸네. 즉, 개수 변화가 없을 때만 제외해야 하네.
                    miniFlag = False
                    break
            if(not miniFlag):
                continue
            
            
            ## 유일성
            uniqBox=set([])
            for row in relation:
                rowResult=[]
                for colI in list(combi):
                    rowResult.append(row[colI])
                uniqBox.add(tuple(rowResult))
            if(len(uniqBox)<len(relation)):
                continue
            
            sucCanKeys.append(combi) # colISet은 더렵혀짐
            ## test
            # print("sucCanKeys,combi, 잘 됨?: ", sucCanKeys, combi)
            
                
        
    answer = len(sucCanKeys)
    return answer