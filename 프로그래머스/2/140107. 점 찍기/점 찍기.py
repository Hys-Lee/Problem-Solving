# (ak,bk)점들의 모음임. => 그냥 간격이 k배수인 점들이 찍혀있겠네. 선형을 띈다기 보다는.
# 1사문면만 생각하면 되고. (축이랑)

# 결국 원점을 중심으로하는 원 둘레가 있을 때, 얘가 주변 정사각형(작은쪽)의 꼭지점을 지나냐만 따지면 될 듯.

# 만약에 원 둘레가 안쪽 정사각형의 꼭지점보다 밖에 있다면 => 정사각형 이루는 점 개수(k=2고 d=4면 0,0/2,0 이렇게 한 변이 2개로 이루어지므로 2*2=4임. ) + 원으로 인해 d위치에 있는 점들(4,0과 0,4)

# 근데, 갈수록 꼭지점 이외의 다른 점도 못 담을 수 있음.
# 이는 정사각형의 꼭지점부터 변을 따라 한 길이 단위씩 내려오면서 체크해야 함.
# 4*4*2랑 5*5를 비교하고, 4*4+3*3이랑 5*5를 비교하는 식으로.

# 이러면, k=1일 때 기준으로 d가 100만이면, 한 변을 다 봐야하니 99만개는 봐야 함.
# 근데, 안에서 가장 바깥이외에 더 안쪽에 있는 정사각형도 다 못담을 수도 있네.

# 그, binary search같은 방식으로 원 안에 있는 정사각형의 꼭지점들 중 포함하는 것과 벗어나는 경계를 찾아야 겠음. =>O(log(D/k))
#     => 이거할 때, 정사각형은 한변이 D-k로 이뤄진 애까지 보는 것ㅇ로.
# 이후에 간신히 벗어나는 애의 변을 훑어야 할 듯. => O(D/k)


# ## 수도코드 만들릭

# #d^2랑 (d-k*n)^2*2들과 비교해야 함(n이 움직이며) : 꼭지점 비교=>굳이 binary안짜도 될 듯? O(D/k)일 듯.
# answer=0: 전체 점 개수
# crosslineI = 0 :초기화 정사각형 꼭지점이 원 둘레 안에 들어온 그 순간의 정사각형 한 변의 위치에 대한 점 인덱스
# for i [1,d//k]
#   if d**2>=((d-k*i)**2)*2인 경우: 정사각형 꼭지점이 원 둘레 안에 들어온 그 순간
#         crosslineI = i
#         break

# answer+=(crosslineI+1)**2 : 내부 정사각형은 온전하게 카운트 됨.

# for j [crosslineI+1, d//k]: (대칭이니까, x축에 붙어있는 애들부터 꼭지점까지 돌며 카운트하자) 가로
#     for i [0,j) : 꼭지점을 생각할 필요 없는게, crossline에서 이미 걸렀음.
#         if (k*j)**2:가로제곱 + (k*i)**2:세로제곱 > d**2:
#             break :세로 탐색은 종료
#         #else: 아니라면 즉, 원 두레 내부 안에 들어온거니
#         answer+=2 : 대칭 고려.  꼭지점을 생각할 필요 없는게, crossline에서 이미 걸렀음.
    



# __알고 33분
# __ 수도코드 46분
# __ 엣지 => 꼭지점이랑 둘레랑 겹치는 경우 체크함, 나머지는 직접 돌려보자걍. 52분
# __ 실패 및 시간초과 63분
#     아니 시간초과는 뭐야 => 제곱 때문이네. 제곱을 divide and conquer하는 메서드 만들어 해결 필요 없음 어차피 **2밖에 안함.
#     실패는 crossline체크할 때 for문으로 k만큼 움직이도록 수정해보자.
# __ 시간초과만  77분 : 딱 보니까, 이후에 삐져나온 부분 처리할 때도 bs써야하네...
#   ㄴ> 아니, 계산을 제대로 못했음... 이게 넓이다보니까, 높이가 낮아도 폭이 좀 있으면 2000만은 넘기는 듯. 대충 200높이에 100_000 너비면 2천만이니까...

import sys
def solution(k, d):
    sys.setrecursionlimit(10000) 


        
    answer = 0
    
    # for i in range(1,d//k+1):
    #     if d**2>=((d-k*i)**2)*2: ## 바깥부터 쪼여오며 체크했구만. => bs로 바꿔보자.
    #         crosslineI =d//k-i
    #         break
    def bs(s,e,k):
        if s>e:
            return 0
        m=(s+e)//2
        if ((m*k)**2)*2<=d**2 and (((m+1)*k)**2)*2>d**2:
            
            return m
        elif ((m*k)**2)*2<=d**2:
            s = m+1
        else:
            e = m-1
            
        return bs(s,e,k)
    crosslineI=bs(0,(d//k) * k,k)     
    # crosslineI = crossline//k
    ## 
    answer+=(crosslineI+1)**2
    ## test
    print("내부 정사각형으로 인한 점 개수: ", answer)
    # for j in range(crosslineI+1, d//k+1):
    #     for i in range(j):
    #         if (k*j)**2 + (k*i)**2>d**2:
    #             break
    #         answer+=2
    def bsH(s,e,k,w):
        if s>e:
            return 0
        m=(s+e)//2
        if ((m*k)**2+w**2)<=d**2 and (((m+1)*k)**2+w**2)>d**2:
            ## test
            # print("m*k, w, d", m*k, w, d)
            return m
        elif ((m*k)**2+w**2)<=d**2:
            s = m+1
        else:
            e = m-1
            
        return bsH(s,e,k,w)
    for j in range(crosslineI+1,d//k+1):
    # for j in range(crosslineI+k, (d//k) * k+1, k):
        heightI = bsH(0,j-1,k,j*k)
        ## test
        # print("height,j: ", heightI,j)
        answer+=(heightI+1)*2
    
    return answer