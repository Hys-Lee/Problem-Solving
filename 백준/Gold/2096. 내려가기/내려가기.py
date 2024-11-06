import sys

n = int(sys.stdin.readline())
dp = [[0, 10] for _ in range(3)]  #(최대,최소)
mymap = []


def doDP():
  inf = 1e9
  nextdp = [[-1, inf] for _ in range(3)] # 최대를 어케해야 하지 dp초기화인데, 내가 처음에도 잘못잡긴했네.inf로 잡았어야 하네 dp는 누적합이니까.
  for j in range(3):
    for k in range(-1, 2):
      if j + k < 0 or j + k > 2:
        continue
      submax = max(nextdp[j][0], mymap[j] + dp[j + k][0])
      submin = min(nextdp[j][1], mymap[j] + dp[j + k][1])

      nextdp[j] = [submax, submin]
      ## test
      # print("mymap,dp,nextdp: ", mymap, dp, nextdp)
  dp.clear()
  dp.extend(nextdp)


for h in range(n):
  mymap = list(map(int, sys.stdin.readline().split()))
  if h == 0:  ## dp초기화

    for g in range(3):
      dp[g][0] = mymap[g]
      dp[g][1] = mymap[g]
    continue
  doDP()
  ## tset
  # print("mymap,dp: ", mymap, dp)
# for i in range(3):
#   dp[0][i] = [mymap[0][i], mymap[0][i]]

# for i in range(1, len(dp)):

## test
# print("i, j, k, submax,submin: ", i,j,k,submax,submin)

# totmax = dp[len(dp)-1][0][0]
# totmin = dp[len(dp)-1][0][1]
# for i in range(3):
#   totmax = max(totmax, dp[len(dp)-1][i][0])
#   totmin = min(totmin, dp[len(dp)-1][i][1])
totmax = dp[0][0]
totmin = dp[0][1]
for i in range(3):
  totmax = max(totmax, dp[i][0])
  totmin = min(totmin, dp[i][1])
print(totmax, totmin)
