# greedy
# sub problem으로 나누기 가능
# K-1번째 optimal 결과(가정)에
# K번째까지의 ele합을 더하면 결과인데,
# 이 결과가 optimal이려면
# K번째까지의 ele합이 최소이려면 됨.
# 즉, ele가 작은 순으로 정렬해서 오면 됨.

# n = int(input())
# cards_packs=[0 for _ in range(n)]
# for i in range(n):
#   cards_packs[i] = int(input())

# # 오름차순 정렬
# cards_packs.sort()
# # 시간초과 방지 위해 누적 합 미리 계산
# cumul_sum = [0 for _ in range(n)]
# if n>1:
#   cumul_sum[1] = cards_packs[0]+cards_packs[1]
#   for i in range(2,n):
#     cumul_sum[i] = cumul_sum[i-1]+cards_packs[i]
  

# if n==1:
#   print(0)
# else:
#   result = cumul_sum[1]
  
#   for i in range(2,n):
#     # result = result+sum(cards_packs[:i+1]) # 얘 때매 시간초과
#     result += cumul_sum[i]
  
#   print(result)


#----------------------------
# 2,2,3,3,
# ㄴ> (2+2) + (3+3) + (4+6) = 20...
# 무조건 accumulative하게 계산하는 건 아님..
# 결국, 중간 계산들의 합이 가장 작게 나오면 되는데,
# K-1까지 결과가 M개의 카드 팩이 되었다면,
# 이 중에서 2개 합한 결과가 가장 작은 것을 가지면 되는 것.
# 즉, 각 계산 후에 계속 오름차순 정렬을 해야 함.
# 즉, min heap이 필요 =>heapq사용

import heapq

n = int(input())

min_heap = []

# O(N) =  NlogN이니 50만?
for i in range(n):
  heapq.heappush(min_heap,int(input()))


result = 0
if n==1:
  print(0)
else:
  # O(N) = NlogN임. (각 push에 logN)
  for i in range(n-1):
    ele1 = heapq.heappop(min_heap)
    ele2 = heapq.heappop(min_heap)
    sub_sum = ele1+ele2
    result += sub_sum
    heapq.heappush(min_heap, sub_sum)
  print(result)
  
# 즉, 총 NlogN임.