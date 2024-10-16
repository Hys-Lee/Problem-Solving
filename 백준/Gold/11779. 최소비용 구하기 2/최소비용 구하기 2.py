import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end, cost = map(int, sys.stdin.readline().split())
  graph[start].append((cost, end))

sV, eV = map(int, sys.stdin.readline().split())

## test
# print("graph: ", graph)
# print('sv,ev: ', sV, eV)

inf = 1e9
dist = [inf for _ in range(n + 1)]  # 0번은 안써요
dist[sV] = 0
allpath = []
q = [(0, sV, sV)]

while (q):
  repD, repV, preV = heapq.heappop(q)
  if repD > dist[repV]:
    continue
  ## 확정된 애는 allpath에
  allpath.append((repV, preV))

  ## test
  # print("repV,preV,dist: ", repV, preV, dist)

  for nextC, nextV in graph[repV]:
    nextD = nextC + repD
    if nextD < dist[nextV]:
      dist[nextV] = nextD  ## 업뎃 해줘야지..
      heapq.heappush(q, (nextD, nextV, repV))

## test
# print("다잌 이후 allpath: ", allpath)

mypath = []
targetV = eV
for i in range(len(allpath) - 1, -1, -1):
  curV, preV = allpath[i]
  if curV == targetV:
    mypath.append(curV)
    targetV = preV
    ## test
    # print("경로상 curV, 다음 targetV: ", curV, targetV)

mypath.reverse()

## test
# print("처리 이후 path: ", mypath)

print(dist[eV])
print(len(mypath))
#for i in range(len(mypath)):
#  print(mypath[i],end='')
pathstring=' '.join(map(str,mypath))
print(pathstring)

