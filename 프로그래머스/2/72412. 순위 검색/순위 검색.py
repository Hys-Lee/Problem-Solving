# 문제 상황 자체는 심플하지만,
# 중요한건 시간복잡도 관리겠다.

# 아예 저장할 때, 구분해서 저장해야겠는데?

# 개발언어*직군*경력*소울푸드 -> 3*2*2*2로 저장하는거 자체는 간단하겠는데,

# 문제는, 쿼리에서 - 를 입력했을 때가 아닐까?

# ㄴㄴ
# 근본적인 문제는, 어떻게 저장을 하든, 점수에서 정렬이 되어있어야 시간복잡도를 줄일 수 있다느 ㄴ것.
# BS를 쓰면 logN만에 되니까.

# 모든 분기 따져봐도 3*2*2*2*log50000쯤에 * 10만일거임. 쌉가능일 듯 이러면?

# 그럼 분기 따져서 저장하고 맨 마지막에 각각 정렬시킨다면, 위 식의 절반일테니 가능하고.

# #### 수도코드만들기
# ## lang - 0:cpp, 1:java, 2:python
# ## area - 0:backend, 1:frontend
# ## career - 0:junior, 1:senior
# ## food - 0:chicken, 1:pizza    ## 주석으로 기억하자 -> 그냥 dict로 매핑하자. 저장할 때 이게 최고임.

# mapping = [dict() for _ in range(4)]
# ㄴ> 각 인덱스마다 lang,area,career,food로 매핑

# db = [[[[[]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(3)]로 초기화

# for i in info길이
#   info[i]를 " "로 끊어서 매핑으로 찾은 인덱스로 찾아서 db에 append하기
  
# for 를 4개로 깊게 파서 db에 있는 애들 sort시키기

# def bs(arr,target,left,right)
#   if left>right면 return -1
#   mid = left+right)//2
#   if arr[mid]가 target이면 return mid
#   if mid에서의 값이 target보다 크면 
#     return bs(arr,target,left,mid)하기
#   else # target보다 mid가 작다면
#     return bs(arr,target,mid,right)하기
    
  

# for eachQ in query
#   eachQ를 " "로 끊고 얘네들 중 0,2,4,6,7번째만 사용하면 됨
  
#   조건으로 arr찾고 점수와 함께 bs보내 인덱스 알아내기
#   if 반환값이 -1이면 못찾은거니 answer에 0을 append하기
#   else 해당 arr의 길이 - 인덱스를 answer에 append하기
  
# return answer

# __ 알고 대충 11분
# __ 수도 대충 29분
# __ 엣지는.. 딱히 없어요. 의도대로 코드도 짠 것 같고. 다 전형적으로 짜진 코드라 엣지도 딱히 없는 듯.
# __ 정확성 한 5~6개 틀림 76분 -> 느낌이 bs쪽에서 인 듯.
## 아이거 그냥 각 마지막 dict의 leaves마다 10만1개씩 리스트 만들면 될 듯? 리스트 잘라서 합 때리면 되잖아.
##  (시간초과 2개가 생겨서 이 생각 함.) 그리고 sort하지말고, 맨 뒤부터 누적하면 n점 이상힌 인원은 n번째 값으로 O(1)만 걸리고, sort하는데 nlogn이 들지 않고 누적에 n드니 이게 더 좋을 듯.
import sys
def solution(info, query):
    sys.setrecursionlimit(6000000)
    
    
    answer = []
    ## 0:lang, 1:area, 2:career, 3:food
    mapping=[dict([]) for _ in range(4)]
    
    ## mapping 0 
    mapping[0]['cpp'] = 0
    mapping[0]['java'] = 1
    mapping[0]['python'] = 2
    ## mapping 1
    mapping[1]['backend'] = 0
    mapping[1]['frontend'] = 1
    ## mapping 2
    mapping[2]['junior'] = 0
    mapping[2]['senior'] = 1
    ## mapping 3
    mapping[3]['chicken'] = 0
    mapping[3]['pizza'] = 1
    
    db = [[[[[0 for _ in range(100_001)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(3)]
    
    for eachInfo in info:
        ele = eachInfo.split(' ')
        ## test
        # print("ele: ", ele)
        langI = mapping[0][ele[0]]
        areaI = mapping[1][ele[1]]
        careI = mapping[2][ele[2]]
        foodI = mapping[3][ele[3]]
        ## test
        # print("val: ",int(ele[4]))?
        # db[langI][areaI][careI][foodI].append(int(ele[-1]))
        db[langI][areaI][careI][foodI][int(ele[4])] +=1
    
    
    for i in range(len(db)):
        for j in range(len(db[0])):
            for k in range(len(db[0][0])):
                for l in range(len(db[0][0][0])):
                    for m in range(len(db[0][0][0][0])-2,-1,-1):
                        db[i][j][k][l][m] += db[i][j][k][l][m+1]
    
    

    
    # for i in range(len(db)):
    #     for j in range(len(db[0])):
    #         for k in range(len(db[0][0])):
    #             for l in range(len(db[0][0][0])):
    #                 db[i][j][k][l].sort()
    

    
    
#     def bs(arr,target,left,right): ## 정확한 값을 찾는게 아님!!!
#         if left>right or len(arr)==0:
#             return -1
#         mid = (left+right)//2
#         ## 현재 mid가 target이 아니라면, 자기 포함 오른쪽이 정답일 때 멈추도록 해야함.
#         ## 이 때는 자기 왼쪽이 존재한다면 이는 target보다 작으면서 mid가 target보다 크고,
#         ## 자기 왼쪽이 존재하지 않아야 함. mid가 타겟보다 크고
#         if arr[mid]==target or (mid==0 and arr[mid]>target) or (mid>0 and arr[mid-1]<target and arr[mid]>=target):
#             return mid
        
#         elif arr[mid]<target:
#             return bs(arr,target,mid+1,right)
#         elif arr[mid]>target :
#             if mid!=0 and arr[mid-1]>target:
#                 return bs(arr,target,left,mid-1)
#             return -1
    
    ## test
    # arr=[1,3]
    # target=2
    # print("TEST: ",bs(arr,target,0,len(arr)-1))
    
    
    
    for eachQ in query:
        ele = eachQ.split(' ')
        ## test 0,2,4,6,7
        # print("ele: ", ele)
        #### 여기 생각 미처 못했는데, 그냥 for문으로 만들고, index가 나오면 거기만 조사고, 아니면 전체 조사하도록 하면 될 듯.
        count=0
        lang = ele[0]
        for i in range(0 if lang=='-' else mapping[0][lang], 3 if lang=="-" else mapping[0][lang]+1):
            area = ele[2]
            for j in range(0 if area=='-' else mapping[1][area], 2 if area=='-' else mapping[1][area]+1):
                career = ele[4]
                for k in range(0 if career=='-' else mapping[2][career], 2 if career=='-' else mapping[2][career]+1):
                    food = ele[6]
                    for l in range(0 if food=='-' else mapping[3][food], 2 if food=='-' else mapping[3][food]+1):
                        target  = int(ele[-1])
                        count += db[i][j][k][l][target]
#                         arr = db[i][j][k][l]
#                         target = int(ele[-1])
                        
                        
                        
#                         idx = bs(arr,target,0,len(arr)-1)
                        
#                         ## test
#                         # print("i,j,k,l,arr,target,idx:", i,j,k,l,arr,target,idx)
                        
#                         if idx==-1:
#                             continue
#                         count += len(arr)-idx
        answer.append(count)
                        
                
        
        
        
    
    return answer 