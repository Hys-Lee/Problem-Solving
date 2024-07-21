# # 그냥 봤을 때는 dijkstra인데?
# # 비용이 0일 수 도 있는것만 다른데..

# # 0이더라도, 사이클만 아니면 사실 뭐..
# # 사이클도 처리만 하면 되니까..

# # 시간이...
# # 걍 O(V+E) 아닌가?

# #### 수도
# n입력
# m입력
# graph m+1개 초기화 (0th버리기)
# for m번 동안
#   엣지 입력 받아서 graph에 추가  (비용,도착지)를 graph[출ㄹ발]에.
# 시작점, 종료점 입력 받기

# ##다이스트라자 만들자
# INF는 1e9 로.
# dist만들기 (m+1개) 시작점은 0, 나머지는 INF로
# q = [] : heapq할꺼임
# q에 시작점 넣기 (dist값,시작점)

# while q끝날 때까지
#   repD,repV를 q에서 heappop
#   if repD가 최신 dist[repV]보다 크면 continue:거르기
#   #이제야 S에 포함됨.
#   for newC,newV graph[repV]에서

#     newD=newC+repD :지금 V와 새로 만난 E로 만든 newV까지의 거리
#     if newD가 dist[newV]최신값보다 작으면:
#       dist를 newD로 업뎃
#       q에 heappush(newD, newV)

# ## 결과
# 결과는 dist[종료점]을 출력.

import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
  edgeStart, edgeEnd,edgeCost = map(int, sys.stdin.readline().split())
  graph[edgeStart].append((edgeCost, edgeEnd))

## test
# print(graph)

startV, endV = map(int, sys.stdin.readline().split())

### 다잌스트라자
INF = 1e9
dist = [INF if i != startV else 0 for i in range(N + 1)]
q = [(dist[startV], startV)]
while(q):
  repD, repV = heapq.heappop(q)
  if repD>dist[repV]: 
    continue

  for newC, newV in graph[repV]:
    newD = newC+dist[repV]
    if newD<dist[newV]:
      dist[newV] = newD
      heapq.heappush(q,(newD, newV))

## test
# print(dist)

print(dist[endV])
