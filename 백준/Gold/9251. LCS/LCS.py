import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

#첫줄은 채워야 알고 적용 가능할 듯

if str1[0] == str2[0]:
  dp[0][0] = 1
for j in range(1, len(str2)):
  if dp[0][j - 1] == 1:
    dp[0][j] = 1
  else:
    if str2[j] == str1[0]:
      dp[0][j] = 1

for i in range(1, len(str1)):
  if dp[i - 1][0] == 1:
    dp[i][0] = 1
  else:
    if str1[i] == str2[0]:
      dp[i][0] = 1

## ttest
# print("INIT DP: ", dp)

for i in range(1, len(str1)):
  for j in range(1, len(str2)):
    if str1[i] == str2[j]:
      if dp[i][j - 1] == dp[i - 1][j - 1]:
        dp[i][j] = dp[i][j - 1] + 1
              
      else:
        dp[i][j] = dp[i][j - 1]  # 그대로 가져와야지.
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 이전(에 매칭 됐을지 모르는)값을 가져와야지(큰놈으로)
    # print("i,j,dp: ", i, j, dp)

print(dp[len(str1)-1][len(str2)-1])
#   c a p c a k
# a 0 1 1 1 1 1
# c 1 1 1 2 2 2
# a 1 2 2 2 3 3
# y 1 1 1 1 1 1 ->이게 이상하네.
# k 1
# p 1
