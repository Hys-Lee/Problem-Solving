# 이거 그냥 O(N)으로 입력 훑으면서 2,3,4미터에서의 토크값을 키로 dict에 각각 저장하면 되는거 아님?

# 토크값에 저장된 애들 개수 k라면 KC2로 계산하면 됨.
#     ㄴ> 아니, 무게가 같은 애들은 거리에 상관없이 균형을 이루는데,
#         이러면 위 알고리즘대로면 3개가 나오지만,
#         결과는 1개가 나와야 함.

    ## -----
# 걍 무게 100~1000에 2배~4배까지 모두 체크하기 위해 200~4000리스트를 만들고,
# 해당 무게값인 인덱스에 weight의 요소들(인덱스로 체크) 이 몇개 들어갔냐로 체크할 수는 있는데,
# 결국 위에처럼 중복되어 체크될 수도 있단 말이지.
# 그러면, 2개 이상이 들어가있는 애들 중 짝꿍을 만들어야 하는데..
# 걍 숫자 계산만 시키면, 계산 한번에 들어가 있는 애들 개수 K면 K개가 필요함.
# 개수 계싼은 문제 없음.

# 문제는 위에 나온대로 숫자 값이 같은 것들끼리는 어떤 거리에서도 균형을 이룬다는 것.
# 다른 거리에서도 균형을 이루는 케이스는 없음. 
# 이들 사람은 각각 구분해야 하는데, 거리는 구분하면 안되는 거네.
# 튜플로 짝지은 애들(인덱스 값들어간)을 set에 보관하면 안되나?
# 튜플로 짝지으려면 combination과정이 필요한데, K^2만큼 걸림.
#     이러면 모든 값이 같은 값일경우, combination으로만 시간초과 남.

# 아니면, 동일 값 갖는 애들은 각각 몇개인지, 누구인지 체크해두고, 전부 set에 몰아넣어서 다 유니크 값들로 존재하기 만들기
#     얘네 끼리 짝을 짓고, 그 개수를 체크
#         짝을 짓는건 위랑 동일하게 무게에 대해서 할건데, 이러면 계산해보면 최악경우가 1000^1000이라 쌉가능이긴 함.
        
#     이들 중 동일 값 들어간 애들을 골라서,
#         1개 들어간 경우 (동일 값 a개)
#             1 * a
#         2개 들어간 경우에 따라 (동일값 a,b개)
#             1*a*b
#         각각 가능한 경우의 수를 계산해 곱하고,
#     나머지 애들은 경우의 수 1로 해서 모든 경우의 수 합을 때리면 될 듯?
#    여기에 동일 값들은 각 개수만큼 지들끼리 결합하는 경우를 추가로 더하면 됨.
#       이는 comb등을 쓸 필요 없이 O(N)만에 계산 가능. 케이스가 아니라 값만 계산하면 되니까.

### 수도코드만드릭
# wNum=[0으로 1001칸 초기화] ->100~1000 인덱스만 사용됨. 각 무게 몇개인지 체크
# sameW=[빈칸 초기ㅗ하]: wNum에서 동일 무게인 사람이 2명 이상인 무게만 뽑아놓기 
# for i weights에 대해
#     wNum에 해당 무게에 대해 +=1해두기
# for i wNum에 대해
#     값이 2이상인 경우는 sameW에 인덱스(무게) append해두기

# uniqueWs=set(weights) : 유니크 값들로만 만들기

# torq=[[]로 4001칸 초기화]: 200~4000인덱스까지만 사용함. 
# for i uniqueWs에 대해
#     i번째 값을 2배, 3배, 4배한 값들을 인덱스로 해서 torq에 원본 무게를 append

# allCombs=[] 콤비네이션 저장창고
# for i torq에 대해 
#     combination을 때린다. -> itertools를 사용해도되고, 이중 for써도 되고.
#     이렇게 나온 모든 comb경우의 수 튜플 혹은 2칸짜리 리스트들을 allComb에 append
# answer=0
# for allComb에 대해
#     l,r = allComb의 원소 중 하나 라면,
#     wNum[l]*wNum[r] 을 answer에 += 하기.  (어차피 1이상의 자연수라.)

# for sameW에 대해
#     sameW를 통해 알 수 있는 무게에 대해
#     wNum으로 해당 무게를 갖는 사람 수를 알아내고
#     #for문을 통해 이 안에서 O(N)으로 값 계산해 처리하기.
#     subresult=1, k가 사람수면,
#     for i [1~k]까지
#     subresult*= i하고
#     subresult/=2하고
#     for i [1~k-2]까지
#     subresult/=i하면 됨.
#     이subresult를 answer에 +=하면 됨.
    


# __ 알고리즘 36분
# __ 수도코드 55분
# __ 실패 85분
# __ 실패 95분 런타임에러
# __ 110 질문하기 체크
# __ 마지막 과정에서 형변환int떼고 //=로 바꿨더니 시간초과남.
from itertools import combinations
def solution(weights):
    wNum=[0 for _ in range(1001)]
    sameW=[]
    for w in weights:
        wNum[w]+=1
    for w in range(len(wNum)):
        if wNum[w]>=2:
            sameW.append(w)
    uniqueWs=set(weights)
    ## test
    # print("wNum, sameW, unique: ", wNum, sameW, uniqueWs)
    torq=[[] for _ in range(4001)]
    for uw in uniqueWs:
        torq[uw*2].append(uw)
        torq[uw*3].append(uw)
        torq[uw*4].append(uw)
    ## test
    # print("torq: ", torq)
    ## 조합 만들기
    allCombs=[]
    for people in torq:
        if len(people)>=2:
            startP=0
            res = list((combinations(people, 2)))
            allCombs.extend(res)
            # print("res: ",res)
          
            ## test
            # print("people, allCombs: ", people, allCombs)
                    
    answer = 0
    for comb in  allCombs:
        lc,rc = comb
        answer+=wNum[lc]*wNum[rc]
        ## test
        # print("comb, answer: ", comb, answer)
    
    for w in sameW:
        subresult=1
        subresult=subresult*wNum[w]*(wNum[w]-1)//2
        # for i in range(1,wNum[w]+1):
        #     subresult*=i
        # subresult//=2
        # for i in range(1,wNum[w]+1-2):
        #     subresult//=i
        answer+=subresult
        ## test
        # print("w, subresult, answer: ", w, subresult, answer)
            
        
    
    return answer

    