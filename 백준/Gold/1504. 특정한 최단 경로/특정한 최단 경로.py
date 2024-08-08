import sys
import heapq

N,E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
  a,b,c = map(int, sys.stdin.readline().split())
  graph[a].append((c,b)) 
  graph[b].append((c,a))

v1,v2 = map(int,sys.stdin.readline().split())

def dijk(start,end):
  dist =[1e9 for _ in range(N+1)]
  dist[start] = 0

  q=[(0,start,start)]
  while(q):
    repD, repV,prevV = heapq.heappop(q)
    if repD>dist[repV]: continue

    for newC,  newV in graph[repV]:
      if newV == prevV:continue

      newD = newC+repD
      if newD<dist[newV]:
        dist[newV] = newD
        heapq.heappush(q, (newD, newV, repV))
  return dist[end]

path1 = dijk(1,v1)+dijk(v1,v2)+dijk(v2,N)
path2 = dijk(1,v2)+dijk(v2,v1)+dijk(v1,N)
## test
# print("P1,p2: ", path1, path2)
answer = min(path1, path2)
if answer<1e9:
  print(answer)
else:
  print(-1)
