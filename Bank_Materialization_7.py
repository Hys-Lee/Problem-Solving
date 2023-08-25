##
# 구현 문제인 듯.  완전 탐색(BFS,DFS)도 아님.
# 걍 가장 쉬운 난이도.
##

n = input()

split_size = len(n) // 2
left = n[:split_size]
right = n[split_size:]

left_nums = []
right_nums = []

for i in range(split_size):
  left_nums.append(int(left[i]))
  right_nums.append(int(right[i]))

if sum(left_nums) == sum(right_nums):
  print("LUCKY")
else:
  print("READY")
