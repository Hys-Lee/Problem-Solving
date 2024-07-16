##### 시작 #####
## 입력 받기
import sys

n = int(sys.stdin.readline())
oriArr = list(map(int, sys.stdin.readline().split()))

## dp만들기
dp = [1 for _ in range(n)]
# dp[0] = 1

for cur in range(1, n):
  for prev in range(cur):
    if oriArr[cur] > oriArr[prev]:
      dp[cur] = max(dp[prev] + 1, dp[cur])

## 결과 -> max
print(max(dp))