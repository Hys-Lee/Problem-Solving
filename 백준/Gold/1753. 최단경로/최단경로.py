import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]  ## [(weight,to),...]

for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())

  graph[u].append((w, v))

inf = 1e9
dist = [inf if i != start else 0 for i in range(V + 1)]

dist[0] = -1  # 혹시 몰라서. 0th는 안 쓴다.

q = []
heapq.heappush(q, (0, start))
while (q):
  repW, repV = heapq.heappop(q)

  ## 이미 제보된 거면 패스
  if (repW > dist[repV]): continue
  ## 신입이 됨.

  for tarW, tarV in graph[repV]:
    newW = tarW + repW
    if newW < dist[tarV]:
      ## 최신화 필요하면
      dist[tarV] = newW
      heapq.heappush(q, (newW, tarV))

for validD in (dist[1:]):
  if validD == inf:
    print('INF')
  else:
    print(validD)
