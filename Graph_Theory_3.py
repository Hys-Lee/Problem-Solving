# 일단 최소비용에 각 집합에서 모두 연결
# Minimum spanning tree인데..
# 두 개의 집합으로 나누는데,
# 나누고 길 정리했을 때 최소비용 되도록 이니까...
# 걍 전체에 MST걸고 이후에 그 중 가장 큰 cost인 edge를 잘라 두 그룹으로 나누면 될 듯.

# 크루스칼
# 길 cost순 정렬
# 가장 작은 것부터...
# cycle생성 여부 체크
#  ㄴ> 매 edge마다 union시키고
#      root체크
#      입력 받은 edge가 이미
#      root가 같다면 cycle임.
#      이 cycle되는 edge버리면 됨.

# 서로소 집합에서 하 듯
import sys
import heapq


def find_parent(parent, node_num):
  if (node_num != parent[node_num]):
    parent[node_num] = find_parent(parent, parent[node_num])
  return parent[node_num]


def union_parent(parent, node1, node2):
  root1 = find_parent(parent, node1)
  root2 = find_parent(parent, node2)
  if root1 < root2:
    parent[root2] = root1
  else:
    parent[root1] = root2


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
# min_heap_edges = [] #// heapq쓸 필요 없이
#// sort하면 됐었네... sort 많이 까먹었나봄.
edges = []
# result_cost = []
result_cost = 0
for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  # heapq.heappush(min_heap_edges, (c, a, b))
  edges.append((c, a, b))

# while (len(min_heap_edges) > 0):
#   target = heapq.heappop(min_heap_edges)
#   root1 = find_parent(parent, target[1])
#   root2 = find_parent(parent, target[2])
#   if root1 == root2:
#     continue
#   union_parent(parent, target[1], target[2])
#   result_cost.append(target[0])
edges.sort()
last = 0
for edge in edges:  # 가장 비싼건 자를거니.
  cost, node1, node2 = edge
  root1 = find_parent(parent, node1)
  root2 = find_parent(parent, node2)
  if (root1 == root2):
    continue
  union_parent(parent, node1, node2)
  result_cost += cost
  last = cost

# grouped_cost = sum(result_cost) - result_cost[-1]
# print(grouped_cost)

print(result_cost - last)

# 시간 복잡도 면에서 sort를 쓰든 heapq를 쓰든 차이는 없는 것 같음. 여기선 둘 다 ElogE 인 듯
#
