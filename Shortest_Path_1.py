import sys
n,m = map(int, sys.stdin.readline().split())
Inf=(1e9)
import heapq

min_nodes_heap=[]
edgesbynodes=[[]]*(n+1)

for i in range(m):
  a,b = map(int, sys.stdin.readline().split)
  edgesbynodes[a].append(b)
 x, k = map(int,sys.stdin.readline().split())

min_nodes_heap.heappush((0,1))
for i in range(2,n+1):
  min_nodes_heap.heappush((Inf, i))

attended=[0]*n+1
attended[1]=1
nodes=[Inf]*(n+1)
for e in range(m):
  for j in edgebynodes[min_nodes_heap.heappop()[1]]:
    nodes[j]=

