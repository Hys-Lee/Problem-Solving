# 풀이 방향자체는 어렵지 않음.
# 그냥 k진수로 바꾸고
# 0을 기준으로 쪼개면 됨.(문자열로보고)

# 쪼개진 값들을 숫자로 바꾸고 소수인지만 판단하면 됨.
#     문제는 소수인지 판단하는거임.
    
#     만약에 가장 원초적인 방법을 쓴다고 가정해보자.
#         시간제한이 딱히 나와있지는 않은데,
        
#         원초적 방법은 2~자기자신-1까지 나눴을 때 안나눠 떨어지면 소수.
    
# 2^20승정도가 100만쯤 되니,
# k진수는 20자리 미만일 것임 최대가.



# ### 수도코드만들기

# n을 k로 나눈 나머지를 계쏙 array에 넣기.
# reverse시키고 문자열로 만들기

# 이후에 0으로 쪼개기

# 이후에 소수 구분하기. -> 함수로 제작 (2이상만 넣기.)
# 함수 소수찾기(값)
#   if 값<2: return false
#   divider=2
#   while divider<값 and 값%divider!=0
#     divider+=1
    
#   if divider가 값과 같다면 : 모두 통과
#     return true
#   return false
  

# 함수 통해 true인 애들만 카운트 해서 개수 세기.



# _ 알고 대충 10분쯤
# _ 수도 대충 16분쯤
# _ 엣지 -> 딱히 없음이 아니라, 소수 체크하는 거에 1은 들어가면 안됨. 2이상만 넣어야 함.->걍 함수안에서 처리하도록 함. 17분쯤
# _ 실패 31분(테스트1번에서 시간초과남.) -> 아마 소수 찾는거 때문에 그럴 듯.
# ㄴ> 그냥 소수 찾는 다른 알고리즘 인터넷에서 찾아보자.



import math
def solution(n, k):
#     ### n까지 소수들 모두 미리 알아내기
    
#     isPrime=[True for _ in range(n+1)]
#     isPrime[1] = False
#     isPrime[0] = False
#     for i in range(2,int(math.sqrt(n))+1):
#         j=2
#         while i*j<=n:
#             isPrime[i*j] = False
#             j+=1
    
    
    
    ###
    
    converted=[]
    moks = n
    while moks>0:
        converted.append(str(moks%k))
        moks = moks//k
    ## tset
    # print("converted: ", converted)
    converted.reverse()
    convertedString = "".join(converted)
    ## test
    # print("constring: ", convertedString)
    
    possiblity = convertedString.split('0')
    
    def check(targetNum):
        if targetNum<2: return False
        divider=2
        # while divider**2<targetNum and targetNum%divider!=0:
        for divider in range(2, int(targetNum**(1/2))+1):
            if targetNum%divider==0:
                return False
        return True
    ## test
    print("poss: ", possiblity)
    count=0
    for p in possiblity:
        if len(p)<1:continue ## ''같은 경우 배제
        ## test
        # print("p: ", p)
        p=int(p)
        if check(p):
        # if isPrime[p]:
            ## test
            print("소수: ", p)
            count+=1
    
    
    answer = count
    return answer