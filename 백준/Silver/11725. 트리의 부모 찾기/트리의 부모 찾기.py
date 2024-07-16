#### 시작 ####
import sys
from collections import deque
n  = int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
  a,b = map(int ,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

parent = [i for i in range(n+1)]


q=deque([])
q.append((1,1))

# ## test
# print(graph)

while(q):
  # ## test
  # print("Q: ", q)
  prevNode, curNode = q.popleft()
  for nextNode in graph[curNode]:
    if nextNode!=prevNode:
      parent[nextNode] = curNode
      q.append((curNode,nextNode))

# ## test
# print(q)

for i in range(2,n+1):
  print(parent[i])