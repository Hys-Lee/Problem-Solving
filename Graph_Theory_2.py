import sys
# n, m입력
n, m = map(int, sys.stdin.readline().split())
# parent초기화
parent = [i for i in range(n + 1)]
#연산 정의


def find_parent(parent, node_num):
  if parent[node_num] != node_num:
    parent[node_num] = find_parent(parent, parent[node_num])
  return parent[node_num]


def union_parent(parent, node1, node2):
  root1 = find_parent(parent, node1)
  root2 = find_parent(parent, node2)
  if (root1 < root2):
    parent[root2] = root1
  else:
    parent[root1] = root2


# 연산
for i in range(m):
  op, a, b = map(int, sys.stdin.readline().split())
  if op == 0:
    union_parent(parent, a, b)
  elif op == 1:
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a == root_b:
      print("YES")
    else:
      print("NO")
  else:
    print("ERR")
