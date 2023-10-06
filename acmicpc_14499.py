import sys


def roll(dydx_i, d):
  # dice 갱신
  next = [
    d,
    [d[3], d[1], d[0], d[5], d[4], d[2]],
    [d[2], d[1], d[5], d[0], d[4], d[3]],
    [d[4], d[0], d[2], d[3], d[5], d[1]],
    [d[1], d[5], d[2], d[3], d[0], d[4]],
  ]
  return next[dydx_i]


def change(dice, y, x, my_map):
  # dice랑 map관련 숫자 갱신
  if my_map[y][x] == 0:
    my_map[y][x] = dice[5]
    # dice[5] = 0
  else:
    dice[5] = my_map[y][x]
    my_map[y][x] = 0


def move(dydx, dice, y, x, n, m):
  print(":", y, x)
  # 밖으로 나가는지 체크
  if not (0 <= y + dydx[0] < n) or not (0 <= x + dydx[1] < m):
    return (False, (y, x))
  else:
    return (True, (y + dydx[0], x + dydx[1]))


def run():
  # ioio #
  n, m, y, x, k = map(int, sys.stdin.readline().split())
  my_map = []
  for _ in range(n):
    my_map.append(list(map(int, sys.stdin.readline().split())))
  cmds = list(map(int, sys.stdin.readline().split()))

  # 동서북남
  dydx = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

  #      위,앞,오,왼,뒤,아래
  dice = [0, 0, 0, 0, 0, 0]

  for c in cmds:
    able, next = move(dydx[c], dice, y, x, n, m)
    if not able:
      continue

    #굴리기
    dice = roll(c, dice)
    #칸이동
    y, x = next
    #눈 숫자 바뀌는거 체크
    change(dice, y, x, my_map)
    # top숫자
    print(dice[0], dice)


run()

# fi = open('input.txt', 'r')
# fo = open('output.txt', 'r')

# while (1):

#   rowi = fi.readline()
#   rowo = fo.readline()

#   pass
#   if not rowi or not rowo:
#     break

#   inputs = []
#   outputs = []

#   n, m, x, y, k = map(int, fi.readline().split())
#   my_map = []
#   for _ in range(n):
#     my_map.append(list(map(int, fi.readline().split())))
#   cmds = list(map(int, fi.readline().split()))

#   run(n, m, x, y, cmds)
#   print("---")
