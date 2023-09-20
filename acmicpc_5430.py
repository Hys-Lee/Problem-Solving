# 50분 걸린 듯?
#   output 형식 제대로 확인하자.
#  예외처리나, 특별히 케어해야 하는 케이스 대해서도 output제대로 확인하자.
#######3

# 일단 구현이고,
# 계산을 해봤는데, 그냥 하라는 대로 하면 시간 초과 날 듯.
# 대충 1억번 안에 끝내야 할텐데,
# reverse가 O(n)이니까.
# 내 생각에는 R개수를 새고,
# 짝수 번째 R뒤에 나오는 D는 pop
# 홀수 번째 R뒤에 나오는 D는 front_pop을 해야 하는 듯.
# 즉 deque사용해서

from collections import deque
import sys

t = int(input())
# num_arr = list(sys.stdin.readline()[1:-2].split(','))
# tmp=[4,5,6,7]
# print(type(num_arr))
# print(type(tmp))
# d = deque(num_arr)
# d.pop()
# print(list(d))

for _ in range(t):
  p = input()
  n = int(input())
  num_arr = sys.stdin.readline()[1:-2]
  if len(num_arr) != 0:
    num_arr = list(map(int, num_arr.split(',')))
  num_arr = deque(num_arr)
  r_count = 0
  error = False
  for func in p:
    if func == "R":
      r_count += 1
    else:  # D이면
      if len(num_arr) == 0:
        error = True
        break
      if r_count % 2 == 0:
        deque.popleft(num_arr)
      else:
        deque.pop(num_arr)
  if r_count % 2 == 1:
    num_arr.reverse()

  if error:
    print("error")
  else:
    print("[", end="")
    for i in range(0, len(num_arr) - 1):
      print(num_arr[i], end=",")
    if len(num_arr) == 0:
      print("]")
    else:
      print(num_arr[-1], "]", sep="")
    # print(list(num_arr))
