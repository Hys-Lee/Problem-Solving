import collections
import sys


## 움직임 구현
# 우+오->하, 우+왼->상, 좌+오->상, 좌_왼->하
# 상+오->우, 상+왼->좌, 하+오->좌, 하+왼->우
# 현재 방향 + turn left/right
# 0,1,2,3 => 좌,상,우,하
# 오: +1)%4, 왼: -1)%4
def move(cur_dir, y, x):
  if cur_dir == 0:  #좌
    return [y, x - 1]
  elif cur_dir == 1:  #상
    return [y - 1, x]
  elif cur_dir == 2:  #우
    return [y, x + 1]
  elif cur_dir == 3:  #하
    return [y + 1, x]


def move_change(cur_dir, turn):
  if turn == "L":
    return (cur_dir - 1) % 4
  elif turn == "D":
    return (cur_dir + 1) % 4


n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
# apples = []
for _ in range(k):
  new_apple = list(map(int, sys.stdin.readline().split()))
  board[new_apple[0] - 1][new_apple[1] - 1] = 1
  # apples.append(new_apple)

l = int(input())
movements = collections.deque([])
for _ in range(l):
  x, c = sys.stdin.readline().split()
  movements.append((int(x), c))

print(movements)

### cycling
# 빈칸:0, 사과:1, 뱀: -1
cur_dir = 2  # 0,1,2,3 => 좌,상,우,하
snake_pos = [0, 0]
board[0][0] = -1
seconds = 0
snake_body_pos = collections.deque([[0, 0]])
while (True):
  seconds += 1
  # move

  # 방향대로 다음 머리 위치 결정
  snake_pos = move(cur_dir, snake_pos[0], snake_pos[1])
  # print("head: ", snake_pos)
  # 다음 위치에 보드 밖 확인
  if not (0 <= snake_pos[0] < n) or not (0 <= snake_pos[1] < n):
    # print("out of")
    break
  # 자기랑 부딪 check
  else:
    isCrash = False
    for body in snake_body_pos:
      if snake_pos[0] == body[0] and snake_pos[1] == body[1]:
        isCrash = True
        # print("Crash")
        break
    if isCrash:
      break
  # 다음 위치에 사과 여부 -> 꼬리
  ate_apple = False
  if board[snake_pos[0]][snake_pos[1]] == 1:
    ate_apple = True
    #사과 없애기
    board[snake_pos[0]][snake_pos[1]] = 0
  # 머리 움직이기
  snake_body_pos.appendleft([snake_pos[0], snake_pos[1]])
  # # 나머지 움직이기
  # for i in range(1, len(snake_body_pos)):
  #   snake_body_pos[i][0] = snake_body_pos[i - 1][0]
  #   snake_body_pos[i][1] = snake_body_pos[i - 1][1]
  # 꼬리 제거 확인
  if not ate_apple:
    snake_body_pos.pop()

  # print("all: ", snake_body_pos)
  # 회전 시간 체크 => 다음 방향 체크
  if len(movements) != 0 and movements[0][0] == seconds:
    cur_dir = move_change(cur_dir, movements.popleft()[1])

print(seconds)
