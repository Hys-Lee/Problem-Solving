import sys
from collections import deque

n = int(sys.stdin.readline())

world = []
for _ in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  world.append(line)

curPos = (0, 0)
fishNum = 0
for i in range(n):
  for j in range(n):
    if world[i][j] == 9:
      world[i][j] = 0
      curPos = (i, j)
    elif world[i][j] != 0:
      fishNum += 1


def bfsdist(curPos, curSize):
  curY, curX = curPos
  q = deque([])  # y,x,curPos부터 거리
  q.append((curY, curX, 0))
  dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  chklist = [[False for _ in range(len(world[0]))] for _ in range(len(world))]
  chklist[curY][curX] = True ## 첫 위치는 체크리스트 체크
  minDistCandidates = []
  mindist = 1e9  ## INF
  while (q):
    curY, curX, dist = q.popleft()
    ## test
    # print("curY,curX,dist: ",curY,curX,dist)
    
    for dy, dx in dydx:
      ny = dy + curY
      nx = dx + curX
      if not (0<=ny<n and 0<=nx<n): ## world밖으로 나가는건 제외
        continue
      if world[ny][nx] > curSize or chklist[ny][nx]:
        continue
      elif world[ny][nx] == curSize or world[ny][nx] == 0:
        chklist[ny][nx] = True
        q.append((ny, nx, dist + 1))
      else:  ## 이 때는world[ny][nx] < curSize  밖에 없나?
        ## 즉, 먹을 물고기 만났다면
        if dist+1 > mindist:
          continue
        elif dist+1 < mindist:
          mindist = dist+1
          minDistCandidates.append((ny, nx))
          chklist[ny][nx] = True ## 체크하긴 해야지
        else:
          minDistCandidates.append((ny, nx))
          chklist[ny][nx] = True ## 체크하긴 해야지

  return (minDistCandidates, mindist)


def move(candidates):
  minY = 1e9

  for cy, cx in candidates:
    if cy <= minY:
      minY = cy
  upperCandi = []
  for cy, cx in candidates:
    if cy == minY:
      upperCandi.append((cy, cx))

  ## test
  # print("minY,upperCandi: ", minY, upperCandi)
  result = (-1, -1)
  if len(upperCandi) > 1:
    minX = 1e9
    leftmostCandi = (-1, -1)
    for cy, cx in upperCandi:
      if cx <= minX:
        minX = cx
    for cy, cx in upperCandi:
      if minX == cx:
        leftmostCandi = (cy, cx)

    result = leftmostCandi
  else:
    result = upperCandi[0]
  return result


time = 0
curSize = 2
eatCountOnSize = 0

for _ in range(fishNum):
  candi, minDist = bfsdist(curPos, curSize)
  ## test
  # print("후보, curSize: ",candi,curSize)
  if len(candi) == 0:
    continue
  endY, endX = move(candi)
  world[endY][endX] = 0
  ## 현재 위치도 업뎃했어야 했는데..
  curPos = (endY,endX)

  if eatCountOnSize < curSize:
    eatCountOnSize += 1
  if eatCountOnSize == curSize:
    curSize += 1
    eatCountOnSize  = 0 # 초기화도 놓쳤음..
  ## ㅅㄷㄴㅅ
  # print("endY,endX,minDist,curSize,eatCount: ", endY,endX,minDist,curSize,eatCountOnSize)
  time += minDist

print(time)
