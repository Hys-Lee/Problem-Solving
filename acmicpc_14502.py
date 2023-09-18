# 1시간 18분 넘게 걸림...
# 사실 다 구현하고 보면, 어려운 부분은 딱히 없었다.
# 다만 time complexity를 계산해서 설계했어야 함.
# 시행착오 줄이게.
#############3

# 최대 64칸에
# 이 중 3개 벽을 고르는 경우 수는 64C3 = 4만가지 정도.
# 각 경우마다 64 cycle안에 끝난다 치면,
# 총 300만 times정도
# 전체 경우 다 따져도 될 듯.(걍 64cycle까지 기다리게.)

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

# map제작
the_map = []
vir_spr = []  # 바이러스 위치
for i in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  for j in range(len(tmp)):
    if tmp[j] == 2:
      vir_spr.append((i, j))
  the_map.append(tmp)

# 0 위치 파악 -> 이 중 3개 combinations로 정해야 함.

blank_pos = []
for i in range(n):
  for j in range(m):
    if the_map[i][j] == 0:
      blank_pos.append((i, j))

# def look_around(use_map, pos):
#   udlr_flag = [0, 0, 0, 0]  # 0=False, 1=True
#   y, x = pos
#   if y != 0 and use_map[y - 1][x] == 0:
#     udlr_flag[0] = 1
#   if y != len(use_map) - 1 and use_map[y + 1][x] == 0:
#     udlr_flag[1] = 1
#   if x != 0 and use_map[y][x - 1] == 0:
#     udlr_flag[2] = 1
#   if x != len(use_map[0]) - 1 and use_map[y][x + 1] == 0:
#     udlr_flag[3] = 1
#   if sum(udlr_flag) > 0:
#     return (True, udlr_flag)
#   else:
#     return (False, udlr_flag)


def play(use_map, vir_spr):
  # 최대 cycle 다 사용
  for c in range(16):  # 8*8에서 대각 양끝까지 cycle수.

    # 이 밑의 과정을하면 이미 아는 위치도 추가됨
    # for i in range(n):
    #   for j in range(m):
    #     if use_map[i][j] == 2:
    #       # dic, flags = look_around(use_map, (i, j))
    #       # if dic:
    #       #   vir_spr.append((i, j, flags))
    #       vir_spr.append((i, j))

    # 퍼뜨리기 바이러스끼리 겹쳐도 상관 없네. 그래도 일단 이대로 가자. 만약에 에러나면 걍 모든 바이러스에 대해 작동하게 하면 될 듯.
    # 새로운 바이러스 대해서만 해야되네.
    # 다만 굳이 look around할 필요가 없는 것.
    new_vir = []
    for v in vir_spr:
      # y, x, udlr = v
      # if udlr[0] == 1:
      #   use_map[y - 1][x] = 2
      # if udlr[1] == 1:
      #   use_map[y + 1][x] = 2
      # if udlr[2] == 1:
      #   use_map[y][x - 1] = 2
      # if udlr[3] == 1:
      #   use_map[y][x + 1] = 2

      y, x = v
      if y != 0 and use_map[y - 1][x] == 0:
        use_map[y - 1][x] = 2
        new_vir.append((y - 1, x))
      if y != len(use_map) - 1 and use_map[y + 1][x] == 0:
        use_map[y + 1][x] = 2
        new_vir.append((y + 1, x))
      if x != 0 and use_map[y][x - 1] == 0:
        use_map[y][x - 1] = 2
        new_vir.append((y, x - 1))
      if x != len(use_map[0]) - 1 and use_map[y][x + 1] == 0:
        use_map[y][x + 1] = 2
        new_vir.append((y, x + 1))
    vir_spr = new_vir


# print(the_map)
# play(the_map)
# print(the_map)

# combinations로 벽 3개 정하기
sel_tot = combinations(blank_pos, 3)
result = []

for sel in sel_tot:
  new_map = []
  for row in the_map:
    # 2차원이라. 원소도 array라서 arr은 전부 slice해야.
    new_map.append(row[:])
  # new_map = the_map[:]
  # map수정
  for i in range(3):
    new_map[sel[i][0]][sel[i][1]] = 1

# 퍼뜨리기
  play(new_map, vir_spr)
  # 결과들 카운팅하기
  sf_cnt = 0
  for i in range(len(new_map)):
    for j in range(len(new_map[0])):
      if new_map[i][j] == 0:
        sf_cnt += 1
  # 이 중 최대값 찾기
  result.append(sf_cnt)
print(max(result))


