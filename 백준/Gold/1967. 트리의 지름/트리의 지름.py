import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
  parent, child, cost = map(int, sys.stdin.readline().split())
  graph[parent].append((child, cost))
  graph[child].append((parent, cost)) ## 양방향

## test
# print("graph: ", graph)


def bfs(distchk, startN):
  q = deque([])
  q.append((startN,startN, 0))
  # for v,c in distchk[startN]:
  #   q.append((startN, v, c))
  #   distchk[]
  while(q):
    pV,nV,nC = q.popleft()
    # if (distchk[nV]!=-1):
    #   continue
    # distchk[nV] = distchk[pV]+nC
    for nnV,nnC in graph[nV]:
      if distchk[nnV] ==-1:
        distchk[nnV] = distchk[nV]+nnC
        q.append((nV, nnV, nnC))

distForFirst=[-1 for _ in range(n+1)]
distForFirst[1] = 0
bfs(distForFirst, 1)

## test
# print("distForFirst결과: ", distForFirst)

startV = 0
maxDforF=0
for i in range(1, len(distForFirst)):
  if distForFirst[i]>maxDforF:
    maxDforF = distForFirst[i]
    startV = i

## test
# print("startV: ", startV)

distForEnd = [-1 for _ in range(n+1)]
distForEnd[startV] = 0
bfs(distForEnd, startV)

## test
# print("distForEnd결과: ", distForEnd)

print(max(distForEnd))