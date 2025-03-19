# 2가지 방법이 생각남.
# # 1. 그래프 사용. union-find를 개선해서 사용하면 nlogn보다 빠르지. size대해 처리하면 됨.->이건 폐기
# 2. 단순 반복문 사용 - dict안에 개수 카운트. 

# ㄴ> 생각해보니까, 그래프 사용 안하고 그냥 dict로 사용하는 것도 똑같음.
# 중요한거는 뭐든간에, 상우ㅏ k개를 저장하는거임.
# 아하 걍 frequency가능 개수만큼 arr만들고, 뒤에서부터 몇개씩 깎이는지 체크하면 되자너.

# ### 수도코드만들기
# count = dict([]) : 각 num대해 freq를 count
# for n nums대해
#   if(n이 count에 있다면 )
#     count[n]+=1
#   else
#     count[n]=1
# maxFreq = 0
# for  count에서
#   maxFreq  = max(maxFreq,값)

# freq=[maxFreq크기+1만큼 만들기 []으로 채우기]

# for  count에서
#     freq[값].append(키) ## 요 부분 가능 체크


# answer=[]
# for freq 거꾸로
#     for freq안의 arr
#         if answer크기가 k와 같아졌다면
#             break :이거 하나로 다 처리
#         ## else
#         answer.append(key인 num)
        
      
# __ 알고 대충 16분
# __ 수도 대충 23분
# __ 엣지 대충... dict에서 key랑 value뽑는거 해봐야 함, kCount지우고 answer크기로 바꿈.
#   ㄴ> for문으로는 key값 뽑을 수 있어서 value는 이걸로 구하면 끝. 27분





class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict([])
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        
        maxFreq=0
        for key in count:
            val = count[key]
            maxFreq = max(maxFreq, val)
        
        freq = [[] for _ in range(maxFreq+1)]
        for key in count:
            val = count[key]
            freq[val].append(key)
        ## test
        print("FREQ: ",freq)
        answer=[]
        for i in range(len(freq)-1,-1,-1):
            for eachNum in freq[i]:
                if len(answer)==k:
                    break
                answer.append(eachNum)
        return answer
        