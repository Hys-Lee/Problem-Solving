# 미래도시
#
#1번->K번->X번으로 이동
# cost 동등, 양방향
# 회사 수, 경로 수 100이 최대
# 100^3 = 10^6이니
# 더 편한 Floyd-warshall 이 가능.

import sys

n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)

floyd_list = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
  floyd_list[i][i] = 0

for i in range(m):
  n1, n2 = map(int, sys.stdin.readline().split())
  floyd_list[n1 - 1][n2 - 1] = 1
  floyd_list[n2 - 1][n1 - 1] = 1

x, k = map(int, sys.stdin.readline().split())

# print(k - 1, x - 1)
# ### 초기화 테스트 ###
# for i in range(n):
#   for j in range(n):
#     print(floyd_list[i][j], end=" ")
#   print('')
# print("----")
# ### 굳

for t in range(n):
  for s in range(n):
    for e in range(n):
      floyd_list[s][e] = min(floyd_list[s][e],
                             floyd_list[s][t] + floyd_list[t][e])

### 출력 ###
### index조심

if floyd_list[k - 1][x - 1] == INF:
  print(-1)
else:
  print(floyd_list[1 - 1][k - 1] + floyd_list[k - 1][x - 1])
