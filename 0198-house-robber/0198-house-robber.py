# dp? 냅색? 완전탐색? 이 셋 중 하나일 듯.
# n이 100이라 냅색이나 완전탐색 의심해봐야..

# 어차피 냅색은 dp나 완전탐색으로 구현되므로...

# 그냥 dp해도..?

# An = Max(An-1, An-2 + an)
# An+1 = 

# an-2 an-1 an an+1
#  2           400

# 걍 dp해도 되는뎅

# 근데 불안하네 100개밖에 없어서..
# 그렇다고 완전탐색은 쫌...

# 브루트포스는... 어렵겠고.

# 일단 dp로 갑시다

# ### 수도코드만들기

# dp를 nums길이만큼 만ㄷ르고, 첫 칸은 nums[0]그대로 채우기, 두번째도.

# 이후부터 dp[i] = dp[i-1], dp[i-2]+nums[i] 중 최대로 채우면 끝.

# dp마지막 번을 답으로...




# __ 알고 대충 14분
# __ 수도 대충 16분
# __ 엣지 체크.. 뭐 없는데? 19분 -> nums개수가 1일 때는 따로 빼줘야함 (2까지 수동으로 채우니까)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        dp=[0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0]) ### 2번째 채울 때 놓쳤음.
        # dp[1] = nums[1]

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[len(nums)-1]
        