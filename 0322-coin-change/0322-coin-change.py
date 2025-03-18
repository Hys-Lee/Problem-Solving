
# 일단 열어두고 생각해보자.
# 목표값은 0부터인데 코인 평가금은 1부터라 일단 이거 까먹지 마시구연

# 아니 걍 dp아님? 완전 일반적인?
# 코인 평가금이 될 수 있는 범위가 너무 넓어서 이 난이도인건가?
# 파이썬에선 상관 뭐 없지 않음?

# 그냥 일반 dp같이 처리하면 시간복잡도는 12*10^4라서 10만단위임.

# 코인들 일단 정렬해서 오름차순으로 만들고
# dp현재 위치에서 코인 만큼 이전 인덱스로부터 만들 수 있는지 체크
# 없으면 걍 -1을 반환

# ### 수도코드만들기

# coins를 오름차순 정렬
# dp=[] amount+1개의 크기로 정렬 -1채우기 (코인 개수가 들어감)
# dp[0] = 0으로 초기화
# for i [1,dp길이-1]
#   for c 코인들
#     if i-c번째가 dp범위 벗어나면 continue
#     if i-c번째 dp값이 -1=>초기값 이라면 return -1
#     ## else 만들수 있다면
#     dp[i] = min(dp[i-c]+1,dp[i]) ## 계속 진행.
#     ## 아니 사실 코인 값이랑 사용한 코인 수랑 크게 상관 없을 수도 있지.
#     ##  따라서, 그냥 min값이라면 바꾸도록 하는게 최고일 듯.

# return dp[amount]

# __ 알고 대충 10분
# __ 수도 대충 18분
# __ 엣지.. 전형적 dp에 min으로 처리하는 것정도면 끝일 듯. 따라서 없다.
        # ㄴ> 없기는 개뿔. 한번 쭉 읽어봐야 했는데 귀찮아서 안읽어본듯.
        # 코드 쓰면서 보니, -1로 초기화하면 min으로 업뎃을 못하므로 큰 값으로 초기화 했어야 함.
        # 2^32에대해 보자면, 2^10이 대충 1000쯤이니까, 1_000_000_000은 무조건 넘는다.
        # 넉넉하게 여기에 100은 곱해두자.
        # 그러면 10^11정도 될 듯.
        # 맥스 값을1e11로 해서 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        inf = 1e11
        dp = [inf for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, len(dp)):

            for c in coins:
                if i-c<0: continue
                if dp[i-c]==inf:
                    continue ## 생각해보니까 여기서 끝내면 안되지. 다른 코인 중에 되는게 있을수도 있잖슴.
                    # return -1
                dp[i] = min(dp[i-c]+1,dp[i])

        print(dp)
        if dp[amount]==inf:
            return -1
        return dp[amount]