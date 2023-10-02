# 2초
# 자기랑 크기 작(먹,통),같(통),큰
# 걍 시뮬
# 먹을 수 있는 쪽으로
# 크기랑 같은 수 물고기면 커짐

# 경로찾아야... 만약 이러면
# 6 0 0 0
# 6 0 6 0
# 2 0 6 0
# 0 0 6 9

# 20*20에 399개 물고기 최대
# 거리 측정이 O(f)이면 f:물고기 수.
#   400*400=160,000
# 거리 측정이 f*f면..
#   400*400*400=6,400만
# 즉, f*flnf까지 가능인데..
# 각 fish마다 flnf탐색.
# 시간 측정을 못하겠네
# 걍 recursive로 해보자.
#   실제 이동해야 하니 공간 정보 있어야..

import sys
from collections import deque

# bfs를 돌리면 전체를 다 전수조사한다고 봐야 함.
# 물론, deque안에 넣을 것들을 거르면 되긴 하는데,
# 계싼은 전수조사로 보면 될 듯.
# 400번., 물고기들까지 -> 400*400
# 이동마다-> 400*400*400
# 가능한 물고기 대해 -> 400*400*400*400 -> worst case(1로 도배 등)

# 답지 보니 가능한 물고기를 따로 추리지 않아서 봤더니
# 거기에 시간초과도 떠서 봤더니...
# +로, 제대로 설계또 안했고, bfs도 처음엔 생각 못했고,
#

# fs = open("input.txt", "r")
# while (True):
#   tmp = (fs.readline())
#   if not tmp:
#     break
#   print(tmp, end="")
# fs.close()
# pass

# 여러 예시볼 때, open을 이용하자 걍.


def path_search(current, f, space, size):
  # 여기서 막히네. 어케하지?
  # 모든 경우를 다 봤다는 걸 어케 알지?
  # 최소길 경우의 수 찾는 식 뭐지?
  # 이거랑 다른데...
  # ==>bfs로 해야하네. 먼저 만나면 바로 ret하면 거리 나오니까.
  # print("new start!\n", f)
  path = deque([])
  path.append((current, 0))
  d = 0
  while (1):
    if len(path) == 0:  # 길이 없으면.
      return 0
      d = 9999
      break
      # return 9999  # 0으로 하면 정렬할 때 맨 앞자리에 오니까

    # print(":", path, f, space)
    cur, d = deque.popleft(path)

    if space[cur[0]][cur[1]] != 9:
      if space[cur[0]][cur[1]]==-1 or\
      space[cur[0]][cur[1]]>size:

        continue
    space[cur[0]][cur[1]] = -1
    if cur == f[1]:
      return d
      break
      # return d
    if 0 < cur[0]:
      path.append(((cur[0] - 1, cur[1]), d + 1))
    if cur[0] < len(space) - 1:

      path.append(((cur[0] + 1, cur[1]), d + 1))
    if 0 < cur[1]:

      path.append(((cur[0], cur[1] - 1), d + 1))
    if cur[1] < len(space[0]) - 1:

      path.append(((cur[0], cur[1] + 1), d + 1))


# 이 부분이 필요 없었음...V


def distance(cur, fishes, space, size):
  result = []  #(거리, 위치)
  d = 0
  for f in fishes:
    # 지나갈 수 있는 길로 거리 측정해야..
    if size > f[0]:  # 먹을 수 있는 애들만.
      new_space = []
      for row in space:
        new_space.append(row[:])

      d = path_search(cur, f, new_space, size)
      # print("D", d, "f", f)
      # d==0이면 종료시켜야함.
      if d == 0:
        continue
      result.append((d, f[1]))
  result.sort()
  next = []
  # print("r",result)

  for r in result:

    if r[0] == result[0][0]:
      next.append(r)
  # print("n", next)
  next.sort(key=lambda x: x[1][0])
  for i in range(1, len(next)):
    if next[i][1][0] == next[0][1][0]:
      next.sort(key=lambda x: x[1][1])
      break
  # print("n", next)
  if len(next) == 0:
    return (0, cur)
  return next[0]
  # return 오름차순. 빈 []: 종료


n = int(input())

fishes = []  #크기,(y,x)
cur = (0, 0)
size = 2
space = []
for i in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  space.append(tmp)
  for j in range(len(tmp)):
    if tmp[j] == 9:
      cur = (i, j)
    elif tmp[j] != 0:
      fishes.append((tmp[j], (i, j)))

time = 0
meal_count = 0
while (1):
  # print("cycle!!", size, meal_count, cur, time)
  dists, pos = distance(cur, fishes, space, size)

  if dists == 0:
    print(time)
    break

  time += dists
  cur = pos
  space[cur[0]][cur[1]] = 0
  for f in fishes:
    if f[1] == pos:
      fishes.remove(f)
      break
  meal_count += 1
  if meal_count == size:
    size += 1
    meal_count = 0
