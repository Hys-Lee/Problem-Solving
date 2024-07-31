import sys

N = int(sys.stdin.readline())
house = []
for _ in range(N):
  house.append(list(map(int, sys.stdin.readline().split())))

dp = [[[0, 0, 0] for _ in range(len(house[0]))] for _ in range(len(house))]
# 초기화
dp[0][1][0] = 1

## test
# print("처음 디피: ", dp)

for i in range(len(dp)):
  for j in range(2, len(dp[i])):  ## 0~1th col은 필요없으니
    if house[i][j] == 1: continue

    if j - 1 >= 0:
      dp[i][j][0] += dp[i][j - 1][0]
      dp[i][j][0] += dp[i][j - 1][2]
    if i - 1 >= 0:
      dp[i][j][1] += dp[i - 1][j][1]
      dp[i][j][1] += dp[i - 1][j][2]
    
    if i - 1 >= 0 and j - 1 >= 0:
      if house[i - 1][j] == 0 and house[i][j - 1] == 0:
        dp[i][j][2] += dp[i - 1][j - 1][2]
        dp[i][j][2] += dp[i - 1][j - 1][1]
        dp[i][j][2] += dp[i - 1][j - 1][0]

    ## test
    # print("이번 위치,dp: ",i,j,dp)

## test
# print("DP: ", dp)
print(sum(dp[N - 1][N - 1]))
