# 폰으로 모의로 짠 것, (거의 수도코드) 옮기는 느낌으로 해봄.
# 괜찮을 것 같긴 함.
# 그런데, 귀찮아서 날림으로 if문 썼던게,
#  구현하려고 하니 나머지 부분도 살짝씩 바꾸게 된 계기가 됨.
# 또한, 수도코드로 짰었는데, 미처 생각 못한 부분과, 틀린 부분이 있었다.
# 진짜 실제 코드 수준의 직전까지 자세하게 수도코드를 작성한다면 그나마 낫겠지만,
# 그렇다고 안 틀릴 수는 없을 것 같다.
# 왜냐면 수도코드 작성 따로하고 이걸 실제 코드로 옮긴다면, 디버깅 과정은 딱히 없으니까...
# 어차피 실제 코드로 옮길 때 단계 밟아가면서, 체크하면서 나아가야 한다.
# 그렇다면 수도코드를 어느정도 자세하게 작성할지 고민해 봐야 할 듯.
#
# 점점 자세히 발전시키는 방향도 좋을 듯.
# 어떤 방법과 단계로 할지 쫘라락 comment하고,
# 각 방법과 모듈 전체 흐름봤을 때 필요한 자료구조 형태를 체크
# 그거에 맞춰서 각 부분을 완성,체크 하며 진행.

# 폰으로 하게 된다면 위 방식으로 최대한 자세하게 짜는게 더 연습에 효과적일 듯.
# 막히는 부분이 있으면 다양한 케이스 가정해서 만들고,
# 진짜 거의 코드 직직전까지 만드는게 효과적일 듯 이 때는.

import sys

n, m = map(int, sys.stdin.readline().split())

# d=  0:위,1:동,2:남,3:서 (시계)
r, c, d = tuple(map(int, sys.stdin.readline().split()))

cur = (r, c)

# room  받기
room = []
for i in range(n):
  room.append(list(map(int, sys.stdin.readline().split())))


# 여기도 반환으로 바꿨음. 아니면 안 바뀌니까. 포인터가 아니라서 원시값이라서.
def rotate(d):
  if d == 0:
    return 3
  else:
    return d - 1


## move가 실제로 짜려다보니 기존에 수도로 했던거랑 좀 달라짐. 수도로 했을 때, 단순히 "if 벽 or 끝"이라고 했던 부분을 실제 구현하려니 이런식이 되네. 그 때 귀찮아서 이렇게 했는데 역시 코드로 하려고보니 조금 달라지긴 함. 실제 코드 짜려는 마인드로 하는게 맞는 듯?
def move(room, cur, d, is_back):
  # 가능: (turn, next),불능: (false,next)
  # 코드 줄이기 위해 미리 세팅해볼까

  lmts_back = [  # 양수일 때 안전
    len(room) - 1 - cur[0],
    cur[1] - 0,
    cur[0] - 0,
    len(room[0]) - 1 - cur[1],
  ]
  nexts_back = [
    (cur[0] + 1, cur[1]),
    (cur[0], cur[1] - 1),
    (cur[0] - 1, cur[1]),
    (cur[0], cur[1] + 1),
  ]
  lmts_front = [  # 양수일 때 안전
    cur[0] - 0,
    len(room[0]) - 1 - cur[1],
    len(room) - 1 - cur[0],
    cur[1] - 0,
  ]
  nexts_front = [
    (cur[0] - 1, cur[1]),
    (cur[0], cur[1] + 1),
    (cur[0] + 1, cur[1]),
    (cur[0], cur[1] - 1),
  ]

  # for d_i in range(4):
  safe = 0
  y, x = (0, 0)
  if is_back:
    safe = lmts_back[d]
    y, x = nexts_back[d]
  else:
    safe = lmts_front[d]
    y, x = nexts_front[d]
  # print(safe, y, x, is_back, room[y][x])
  if safe > 0 and not is_back and room[y][x] == 0:
    return (True, (y, x))
  # 이 분기는 수도코드 짤 때는 미처 생각 못함.
  elif safe > 0 and is_back and room[y][x] == 2:
    return (True, (y, x))
  else:
    return (False, cur)


stop = False

# 청소된 칸은 2로 한다
while (not stop):
  # test

  if room[cur[0]][cur[1]] == 0:
    room[cur[0]][cur[1]] = 2

  dirty = False
  if cur[0] > 0 and room[cur[0] - 1][cur[1]] == 0:  # 상
    dirty = True
  if cur[1] < len(room[0]) - 1 and room[cur[0]][cur[1] + 1] == 0:  # 우
    dirty = True
  if cur[0] < len(room) - 1 and room[cur[0] + 1][cur[1]] == 0:  # 하
    dirty = True
  if cur[1] > 0 and room[cur[0]][cur[1] - 1] == 0:  # 좌
    dirty = True

  if not dirty:
    # 여기도 is_ok로 반환값 바뀜.
    is_ok, next = move(room, cur, d, True)
    if is_ok:
      cur = next
    else:
      stop = True

  # dirty
  else:

    for _ in range(4):
      d = rotate(d)

      is_ok, next = move(room, cur, d, False)

      if is_ok:
        cur = next
        break  # 이걸 까먹네
      # 설계 때 여기의 else부분이 break였는데, 오류임.

clean = 0
for i in range(len(room)):
  for j in range(len(room[0])):
    if room[i][j] == 2:
      clean += 1

print(clean)
