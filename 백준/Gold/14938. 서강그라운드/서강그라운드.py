
import sys

n,m,r = map(int, sys.stdin.readline().split())

items=[0]
items.extend(list(map(int, sys.stdin.readline().split())))

## test
# print("Items: ", items)

inf=1e9
dists=[[inf for _ in range(n+1)]for _  in range(n+1)]
for i in range(1,n+1):
  dists[i][i] = 0 ## 자기 위치는 0

for _ in range(r):
  v1,v2,c = map(int,sys.stdin.readline().split())
  dists[v1][v2] = c
  dists[v2][v1] = c

## test
# print("초기 세팅 dists: ", dists)

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if dists[i][j]>dists[i][k]+dists[k][j]:
        dists[i][j] = dists[i][k]+dists[k][j]

## test
# print("마지막 dists: ", dists)

givens=[0 for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1, n+1):
    if dists[i][j]<=m:
      givens[i]+=items[j]

## test
# print("givnes: ", givens)

print(max(givens))
### 1~n+1로 범위 수정한거랑 [i][i]거리=0으로 수정한거 있었음.