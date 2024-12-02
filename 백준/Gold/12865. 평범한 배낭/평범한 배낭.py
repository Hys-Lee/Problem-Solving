import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[(0, 0) for _ in range(n + 1)] for _ in range(k + 1)]

inputs = [(0, 0)]  # 0th 비우기
for _ in range(n):
  w, v = map(int, sys.stdin.readline().split())
  inputs.append((w,v))

## test
# print("INPUTS: ", inputs)

for i in range(1,len(dp)):
  for j in range(1,len(dp[0])):
    if inputs[j][0] + dp[i][j-1][0]<=i:
      wsum = inputs[j][0] + dp[i][j-1][0]
      vsum = inputs[j][1]+dp[i][j-1][1]
      dp[i][j] = (wsum,vsum)
    else :
      prev = dp[i][j-1]
      ablek = i-inputs[j][0]
      
      maybe = (0,0)
      if ablek>=0:
        maybe = (dp[ablek][j-1][0]+inputs[j][0],dp[ablek][j-1][1]+inputs[j][1])

      dp[i][j] = maybe if maybe[1]>prev[1] else prev


# print("과연dp")
# for i in range(len(dp)):
#   print(": ", dp[i])
print(dp[-1][-1][1])
        
      
        
      
