# 일단 참고를 통해 풀어낼 수 있는 공식은 주어졌음.
# line개수는 최대 1000개임
# 대충 순서 안따지 2개를 집는다면, 대충 N^2쯤이긴 함.

# 조합 함수(라이브러리통해)를 사용하면 매우 편하게 끝날 것 같긴 함.
# 이거 없이 이 동작을 수행시키려면...
#     0번째는 1~끝까지, 1번째는 2~끝까지, ... 이런식으로 비교해야함.
    
# 교점이 정수인 것만 남기는 것까지는 ok

# 교점이 최대 N^2개이므로, y,x값대해 최대/최소값을 구하고, 최대와 최소의 차이를 구하면 됨.
# 이러면 가로 세로 크기는 나옴.

# 점찍는거 자체는 원점을 기준으로 찍는게 편하긴 한데, 이러면 정답으로 자르기 전 크기가 너무 커질 수 있음.
# 따라서, 정답의 가로세로 크기를 구하고, 정답 공간의 기준 점의 위치를 파악하고, 원점에서 그만큼 이동해서 그리면 될 듯.

# 원점에서 수학적 좌표로(-y,x) (5,5)라는 지점은, 정답박스 좌상단 기준점이(4,3)(-y,x)일 때
# array좌표로 (y,x) 지점은 (-1,2)가 되겠죠.


# 좌표 변환할 때, y값은 반대가 된다는점이랑, 정답박스에서의 위치는 상대위치 구하는 것처럼 하면 된다.
#     수학적 좌표는 원점에서 상대 좌표로 보듯 (값-원점), 정답박스에서의 위치 역시(값-기준) 이렇게.
#     다만 array좌표로 변환 위해 y값만 -붙여주면 끝.

    
# 헷갈리지 않는게 중요하겠다.    호흡이 좀ㅈ 김. 구현이라그런가

# ## 수도코드만들기

# 일단, 모든 직선들에 대해 만나는 점들을 체크
# (한점만남과 평행만 가능하니)

# interPs=[]: 교점 (y,x)들.

# for i (line크기-1) : 비교기준. 마지막 원소는 기준이 될필요가 없음. 그러면 비교 대상이 없으니.
#   for j [i+1,line크기) : 비교대상.
#     if i와 j에서 AD-BC가 0이라면 continue
#     y랑 x좌표 구하는 고자ㅓㅇ에서, 분모로 분자가 나눠떨어지면==정수되면 y,x좌표 구하기
#     정수인 y,x좌표를을 interPs에 넣기
         
# interPs에서 y의 최대최소, x의 최대최소를 각각 구하기.
# answer를 [y최대-최소+1][x최대-최소+1]칸으로 초기화, 내부 내용은 "."으로 초기화
# answer의 좌상단기준점 위치는 y최대, x최소 값으로 (이는 수학적 좌표. 위에까지도)

# for p interPs에서
#   p의 y,x좌표(수학적)를 answer에서의 좌표(array적)으로 변환
#   즉, (수학적)좌표-기준점좌표에, y값은 -1을 곱해준다.
#   해당 위치에 answer에서 내용을 "*"로 바꾼다.
         
#  결과에서, answer의 각 가로line을 str으로 변환해야 함. "".join(가로)쓰면 될 듯.
    
    
# __ 알고 대충 16분
# __ 수도코드 대충 25분
# __ 엣지 교점 1개일 때도 가능함. 대충 27분
#     또 생각남. 만약에 여러 직선이 하나의 교점에서 만나면, array에 교점 저장하는거 괜찮나?
#         딱히 상관 없긴 할 듯. 덮어쓰는 과정이 있지만 어차피 100만단위안에 끝날 듯.
# __ 46분 2개 실패(런타임에러)

def solution(line):
    interPs = []
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a,b,e = line[i]
            c,d,f = line[j]
            mother = a*d-b*c
            if mother==0:
                continue # 안만나는경우
            if (b*f-e*d)%mother ==0 and (e*c-a*f)%mother==0:
                y = (e*c-a*f)//mother
                x = (b*f-e*d)//mother
                interPs.append((y,x))
    # ## test
    # print("교점들: ", interPs)
    inf = 1e11 ## 10만*10만 단위도 가능할 수 있어서 고침.
    ## 무조건 업뎃되도록 각각을 초기화
    yM=-1*inf
    ym=inf
    xM=-1*inf
    xm=inf
    
    for py,px in interPs:
        if py>yM:
            yM = py
        if py<ym:
            ym = py
        if px>xM:
            xM = px
        if px<xm:
            xm = px
    # ## test
    # print("yM,ym, xM,xm: ", yM,ym, xM,xm)
    
    answer = [["." for _ in range(xM-xm+1)]for _ in range(yM-ym+1)]
    answerLTstandard = (yM,xm)
    
    for py,px in interPs:
        apy = (py-answerLTstandard[0]) * (-1)
        apx = (px-answerLTstandard[1])
        # ## test
        # print("변환전 y,x / 변환 후 y,x:", py,px,apy,apx)
        
        answer[apy][apx] = "*"
    
    # ## test
    # print("생answer: ", answer)
    
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    # ## test
    # print("변환 후 answer: ")
    # for i in answer:
    #     print(i)

    
    return answer