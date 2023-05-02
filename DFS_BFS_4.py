# bfs는 전진하미녀서 자기 주변을 다 훑어보는 느낌이니 여기선 bfs가 더 적절하지 않을까.
### 내가 짠 것의 문제점
# 일단 제대로 count를 못센다. BFS로 했을 때 길 잘못 들어간 경우를 제거하고 최단거리 경로만 셀 수 있나?
# 부등호 등을 잘못 사용해서 시간 쳐먹음
# while문 안쪽을 제대로 작성하지 못해서 시간 쳐먹음
#  ㄴ> 언제 다음을 상태를 바꿔야 하는지 등
# 설계를 잘 해놓고 옮기는게 맞는 것 같은데..
# 그리고 도착점에 도착하자마자 끝내는 것을 구현 안함
# ㄱ
#  V
# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(n)]

# #start and end with 1 always

# deq = deque()
# count = 0
# next_fucking_box = 0
# x = 0
# y = 0
# deq.append(0)
# graph[y][x] = 0
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# while next_fucking_box < n * m:
#   next_fucking_box = deq.popleft()
#   count += 1
#   print("next: ", next_fucking_box)
#   y = next_fucking_box // m
#   x = next_fucking_box % m
#   graph[y][x] = 0
#   for i in range(4):
#     if not (0 <= (x + dx[i]) < m) or not (0 <= (y + dy[i]) < n):
#       continue
#     elif graph[y + dy[i]][x + dx[i]] == 1:
#       deq.append((y + dy[i]) * m + x + dx[i])
#   ### 여기 이상함
# print(count)

## 답지에서는 우리가 손으로 최단경로 찾을 때 하는 것처럼 그대로 함.
## 이거때문에 BFS를 생각해낸 것이나 다름 없는 듯
## 또한, while문 돌릴 때 deque가 빌 때까지 돌림.
##   ㄴ> 이를 확인하는 방법은 그냥 if문에 deque객체넣어서
##        false면 비어있는것.
##     또다른 방법은 그냥 len((deque객체)) 넣으면 됨.
## 또한, 그냥 bfs라고 함수를 만들어서 돌림....`

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def bfs(x,y):
#   queue = deque()
#   queue.append((x,y))
#   while len(queue):
#     x,y = queue.popleft()
#     for i in range(4):
#       nx = x+dx[i]
#       ny = y+dy[i]
#       if nx<0 or ny<0 or nx>=n or ny>=m:
#         continue
#       if graph[nx][ny] == 0:
#         continue
#       if graph[nx][ny] == 1:
#         graph[nx][ny] = graph[x][y]+1
#         queue.append((nx,ny))
#   return graph[n-1][m-1]
# print(bfs(0,0));
