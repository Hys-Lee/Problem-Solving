# 5의 20승까지 r이 가능하니, n에 대해서 문자열을 만들긴 어려울 듯.
# 10의10승만 해도 10,000,000,000 100억단위니까.

# 주어진 구간 부근만 처리하면 될 듯?
# 근데, 구간 길이도 최대 1000만개까지긴 함. -> 이건 ok긴함.

# 만약 n번째의 [4,17]을 보고싶다면, n-1번째의 [1,4]를 봐야함. (각 위치에서 5개가 생기는 거니까.)
# 구간 길이도 길이지만, 인덱스 값이 중요하네.
# 5의 s배 <=l < 5의 s+1배라면(5의 s배 구간), 그리고 5의 e배<=r<5의 e+1배 라면(5의 e배 구간), 
#     [s,e]를 봐야함.

# 구간이 1000만 단위라면  이전 번째 칸토어 구간 200만 단위를 봐야 함.

# n이 1일 때는 구간보다 비트열이 작으므로, 비트열 전체를 다 보며 변경 가능(1->11011)
# n이 2로 갈 때는 길이가 구간은 14, 비트열은 25이니, 이전 비트열에서 필용한 부분만 보면 됨.
#     l이 4이니, 5의 1배수 구간에 속하므로(1~5) 1번째 인덱스,
#     r이 17이니, 5의 4배수 구간에 속하므로(16~20) 4번째 인덱스를 보면 됨, 이전 비트열에서.

    
# 간단히 하기 위해 0base로 보고 나중에 1base로 바꾼다고 하면,
# [4,17]->[3,16] (n=2)이 되기 전에는 [3//5,16//5]=[0,3](n=1) 구간을 봐야하고,
# 그 이전에는 [0//5,3//5]구간(n=0)을 봐야함.
# 이렇게 보니까, n일 때는 l-1,r-1구간에 가려면 n-1일 때는 l-1)//2, r-1)//2 구가능ㄹ 봐야하는 것.

# 따라서,n값부터 n=0일 때까지 l과 r을 5씩 계속 나눠 어떤 단계에서 어떤 구간을 봐야할지 알아내면 됨.

# 이러면, 1000만+200만+40만+...가 되니까, 2000만은 안될 듯.

# 만약에 이게 안되면 걍 규칙찾아서 1개수를 계산해야함.

# ### 수도코드
# canList=[1] : 초기 칸토어 집합(0단계)  0base 인덱스로. 
# lrByLevel=[(l-1,r-1)] : 0base 인덱스로. 일단은.
# for i [n-1,0] 레벨 내려가며
#     pl,pr = lrByLevel의 맨 끝에 있는것
#     lrByLevel에  (pl//5,pr//5) append
    
# lrByLevel을 reverse : level증가 순서대로 lr맞추기 (0번째는 0번째칸토어 1칸이니 (0,0)일 것)


# for i [0,n-1]:
#     nextCan = [] : 0베이스 인덱스로
#     thisl,thisr = lrByLevel의 i번째
#     for j [thisl, thisr]
#         if canList의 j번째 값이 1이면
#             nextCan에 [1,1,0,1,1]을 extend
#         else : 0이면
#             nextCan에 [0,0,0,0,0]을 extend
#     canList = nextCan으로 바꿔치기
        
# ret canList에서 [l,r]범위를 끊어서 1의 개수 새기 (canList는 내가 원하는 영역을 포함한 가장 짧은 5배수 인덱스 묶음으로 이뤄진 친구라. l,r이 같은 5배수 인덱스 묶음 안에 있을 수 있어서, 잘라야함.)



# __ 알고리즘 (26분)
# __ 수도코드 37분
# __ 엣지케이스   (0,1)을 알고 싶다면, 그 직전은(0,0). 얘를 다음단계로하면 11011이 되고, 여기서[0,1] 끊고 1개수를 알아내야 함.  (이거로 수도코드 수정 40분)
# __ 테스트 케이스 생각하는 중, l,r이 19,20에 대해 해봤더니 틀림
#     생각해보면 canList크기가 l,r사이 크기보다 작을수도 있음.
#         ㄴ> 그리고 lrByLevel에서의 모든 l,r쌍은 전체 비트열에 대해서의 위치임.
#         근데, canList는 필요한 부분만 갖고 있음. => lrByLevel에서 보정해줄 필요가 있음.
#         내가 했던건 0~r+@까지는 갖고있따는 생각 안에서였음.
        
#         - 0베이스로 l-1이 3일 때는 pl은 0, r-1이 16일 때는 pr은 3 
#         - 만약 pl이 1이라면, 이거로 canList만들면 0base에서 5번부터임.
#         - 만약 pl이 3이라면, 이거ㅣ로 canList만들면, 0base에서 15번부터임.
#         - 따라서 pl값에 따라서 다음 l과r(0base)값은 5배수로(빼서) 보정해줘야함
#         =>보정 lr을 따로 만들어야 겠다.
#             원본pl이 3이고, 다음 원본l이 17이면 17-3*5를 해줘야 보정 l임. (여까지 대충 67분)
#               원본의 pl에 대해서만 원본 r,l에 계산하는거임.
        # 뭔가 좀 틀린데, 18,19 =>3,3 => 0,0
        #                 0,0=>3,3(5칸 15~19)=>3,4  => *5해야 했는데 *3을 했네;;



def solution(n, l, r):
    canList=[1]
    lrByLevel=[(l-1,r-1)]
    for i in range(n-1,-1,-1):
        pl,pr = lrByLevel[-1]
        lrByLevel.append((pl//5,pr//5))
    lrByLevel.reverse()
    
    handledLr=[(0,0)]
    for i in range(1,n+1):
        oriL,oriR = lrByLevel[i]
        oriPl = lrByLevel[i-1][0]
        handledLr.append((oriL-5*oriPl,oriR-5*oriPl))
    ## test
    print("handledLr", handledLr)
        
        
    
    ## test
    # print("lrByLevel: ", lrByLevel)
    
    for i in range(n):
        nextCan=[]
        # thisl,thisr = lrByLevel[i]
        thisl,thisr = handledLr[i]
        ## test
        # print("현재 n(i), thisl,thisr, canList", i, thisl, thisr, canList)
        for j in range(thisl, thisr+1): # 인덱스 안넘음.
            if canList[j] == 1:
                nextCan.extend([1,1,0,1,1])
            else:
                nextCan.extend([0,0,0,0,0])
        ## test
        # print("다음 canList: ", nextCan)
        canList = nextCan
            
    
    answer = 0
    hFinalLR = handledLr[-1]
    result = canList[hFinalLR[0]: hFinalLR[1]+1] # [핸들드l-1 "," 핸들드r-1]
    ## test
    # print("result: ",result)
    answer = sum(result) # 1개수가 1의 합이고, 0은 합에 의미없으니.
        
    return answer