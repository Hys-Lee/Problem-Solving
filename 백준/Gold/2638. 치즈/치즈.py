import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

world = []
for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  world.append(line)

## test
# print("world: ", world)

dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Cs = []
# time = 0


def bfs():
  Cs = []
  time = 0
  while (Cs or time == 0):
    nextCs = []
    nextOuter = deque([])
    if time == 0:
      ## 첫 위치는 일단 o랑 nextOuter로
      beforeOuter=deque([])
      beforeOuter.append((0,0))
      world[0][0] = 'o'
      nextOuter.append((0, 0))
      ## 이 부분을 bfs로 했어야 했는데 for문으로 전체를 돌려버렸네...
      while (beforeOuter):
        oy,ox = beforeOuter.popleft()
        for dy, dx in dydx:
          ny = oy + dy
          nx = ox + dx
          if not (0 <= ny < len(world) and 0 <= nx < len(world[0])):
            continue
          ## test
          # print("ny,nx: ",ny,nx)
          if world[ny][nx] == 0:

            world[ny][nx] = 'o'
            nextOuter.append((ny, nx))
            beforeOuter.append((ny,nx))

    ## test
    # print("time, Cs: ", time, Cs)

    for cy, cx in Cs:
      world[cy][cx] = 'o'
      nextOuter.append((cy, cx))

    ## test
    # print("nextOuter: ", nextOuter)

    while (nextOuter):
      oy, ox = nextOuter.popleft()
      for dy, dx in dydx:
        ny = oy + dy
        nx = ox + dx
        if not (0 <= ny < len(world) and 0 <= nx < len(world[0])):
          continue
        try:
          nVal = int(world[ny][nx])
          ## test
          # print("nVal값: ", nVal, ny,nx)
          if nVal == 0:
            world[ny][nx] = 'o'
            nextOuter.append((ny, nx))
          elif nVal > 0:  ## 치즈인 애들
            if nVal >= 2:  ## c로 바뀔 애들 이전에 한번 바깥공기 닿았고, 이번에도 닿은 애들이 여기 도착하니까.

              world[ny][nx] = 'c'
              nextCs.append((ny, nx))
            else:  # 아직 닿는 면 부족한 애들
              world[ny][nx] += 1
        except:
          ## test
          # print("world값: ", world[ny][nx])
          continue
          

    if len(nextCs) == 0:
      break
    Cs = nextCs
    time += 1
  ## test
  # print("time: ", time)
  return time


answer = bfs()
print(answer)
