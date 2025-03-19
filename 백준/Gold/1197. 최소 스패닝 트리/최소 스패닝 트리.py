import sys

sys.setrecursionlimit(100_000)

v,e = map(int, sys.stdin.readline().split())

parents=[i for i in range(v+1)]
def find(node:int):
  if parents[node]==node:
    return node
  parents[node] = find(parents[node])
  return parents[node]

heights=[1 for _ in range(v+1)]

def union(node1, node2):
  p1 = find(node1)
  p2 = find(node2)
  if(p1==p2):
    return False
  if(heights[p1]>heights[p2]):
    parents[p2] = p1
    heights[p2]+=1
  else:
    parents[p1] = p2
    heights[p1]+=1
  return True
answer=0
edges = []
for _ in range(e):
  v1,v2,c = map(int, sys.stdin.readline().split())
  edges.append((v1,v2,c))

edges.sort(key = lambda x:x[2])
## test
# print("edges: ", edges)
for v1,v2,c in edges:
  res = union(v1,v2)
  if res:
    answer+=c

## test
# print("parents, heights: ", parents ,heights)

print(answer)