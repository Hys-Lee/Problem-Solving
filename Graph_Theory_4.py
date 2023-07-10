# 커리큘럼 순서 -> 위상정렬

# import sys

# n = int(input())

# graph = [[] for _ in range(n + 1)]

# indegree = [0 for _ in range(n + 1)]
# time_needed = [0 for _ in range(n + 1)]
# time_needed[0] = -1  # 0번 index는 안쓰도록.

# for i in range(1, n + 1):
#   input_line = sys.stdin.readline().split()
#   time_needed[i] = (int(input_line[0]))
#   courses_needed = map(int, input_line[1:-1])
#   for c in courses_needed:
#     graph[c].append(i)
#     indegree[i] += 1
# time_result = [i for i in time_needed]
# q = []
# for i in range(1, n + 1):
#   if indegree[i] == 0:
#     q.append(i)
# while (len(q) > 0):
#   target_n = q.pop(0)

#   for i in range(len(graph[target_n])):
#     edge_from_this = graph[target_n][i]
#     # print("edge: ", edge_from_this)
#     time_result[edge_from_this] += time_needed[target_n]
#     indegree[edge_from_this] -= 1
#     if indegree[edge_from_this] == 0:
#       q.append(edge_from_this)

# for i in range(1, n + 1):
#   print(time_result[i])
#   # ## test
#   # for i in indegree:
#   #   print(i, end=' ')
#   # print()
#   # for i in time_needed:
#   #   print(i, end=' ')
#   # ##

##### 답지...

from collections import deque
import copy
import sys

n = int(input())

# 각 강의 고유 시간
time = [0 for _ in range(n + 1)]
# 각 노드가 가리키는 노드
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
result = []

# 입력받기
for i in range(1, n + 1):
  input_line = list(map(int, sys.stdin.readline().split()))
  time[i] = (input_line[0])
  for j in input_line[1:-1]:
    indegree[i] += 1
    graph[j].append(i)


def topology_sort():
  # time은 result니까 shallow copy피하기
  result = copy.deepcopy(time)
  q = deque()

  # 첫 시작 큐에 삽입
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지
  while len(q) > 0:
    # 큐에서 원소 꺼내기
    now = q.popleft()

    # 해당 원소랑 연결된 노드들 진입차수 -1해주기
    for next in graph[now]:
      result[next] = max(result[next], result[now] + time[next])
      indegree[next] -= 1

      if indegree[next] == 0:
        q.append(next)

  for i in range(1, n + 1):
    print(result[i])


topology_sort()

### 반성
# graph에 저장되는 것. 여기서는 pointed node였음
# deque사용 방법
# 왜 deepcopy를 사용해야 하는지 -> list라서 대입하면 shallow copy
# 동시에-> 비선형 operation생각
#   이 경우엔 max였음.
#     사실 ipad등에 그려보면 도움 됨.
