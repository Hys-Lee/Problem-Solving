# 최대한 많이 쪼개야 하니까
# 많이 필요한 애들을 기준으로 보고,
# 얘네한테 최대한 적게 주면 되는 듯
# 많이 필요한 애들끼리 모아두고.

# 모든 모험가를 그룹에 넣을 필요는 없대.

import sys

n = int(input())

fear = list(map(int, sys.stdin.readline().split()))

fear.sort()  # 작은 순으로 하는게 최적. 공포도 높은애는 버리는게 최고.
# fear.reverse()
# print(fear)

count = 0
index_pointer = 0
# index_pointer += fear[index_pointer]
while (index_pointer < n):
  index_pointer += fear[index_pointer]
  if index_pointer <= n:
    count += 1

## 만약 하나의 그룹으로 만들기 위한 사람이 부족하면 걍 마을에 두면 되니, 이 가능성 커버.
##
print(count)
