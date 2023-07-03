# 방향있고, cost, 한 곳-> 다른 모든 곳 : digkstra's
# inf가 아닌 노드 개수, 최고 cost

INF = int(1e9)

import sys
import heapq

n, m, c = map(int, sys.stdin.readline().split())

distance = [INF for _ in range(n + 1)]
distance[c] = 0
graph = [[] for _ in range(n + 1)]  # 출발지가 index

for i in range(m):
  x, y, z = map(int, sys.stdin.readline().split())
  graph[x].append((z, y))  # 코스트가 맨 앞에 오게.

## test : graph
for i in range(n + 1):
  print(graph[i])
##

min_heap = []
heapq.heappush(min_heap, (0, c))
while min_heap:
  current_distance, current_node = heapq.heappop(min_heap)
  if distance[current_node] < current_distance:
    continue
  ## update pointing nodes
  for i in range(len(graph[current_node])):
    pointing_distance, pointing_node = graph[current_node][i]
    new_distance = pointing_distance + current_distance
    if new_distance < distance[pointing_node]:
      distance[pointing_node] = new_distance
      heapq.heappush(min_heap, (new_distance, pointing_node))

# target = c

# for j in range(m):
#   for i in range(len(graph[target])):
#     cost, dest = graph[target][i]
#     if distance[dest] > cost:
#       distance[dest] = cost
#   if len(min_heap) > 0:
#     target = heapq.heappop(min_heap)

## test : distance
print("test: distance")
for i in range(n + 1):
  print(distance[i])
##

num = 0
max_cost = 0
for i in range(n + 1):
  if distance[i] < INF and distance[i] > 0:
    num += 1
    if max_cost < distance[i]:
      max_cost = distance[i]

print(num, max_cost)
