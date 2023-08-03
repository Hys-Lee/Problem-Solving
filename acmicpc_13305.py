# greedy임. 약간 전형적인걸 꼰 느낌?
# subproblem으로 나눠 생각할 수 있고,
# optimal, suboptimal생각해야 함.
# 이전 작업이 그대로 수행되는건 아니니 dynamic은 아닌 듯 하고.


import sys

n = int(input())

roads_length = list(map(int, sys.stdin.readline().split()))

oil_cost_for_cities = list(map(int, sys.stdin.readline().split()))

# 현재 위치에서(이전은 optimal이면)
# 자기보다 싼 주유소에서 최대한 많이 사면 됨.
# 거기까지 가는데 최소한 비용으로 가면 됨.(없으면 끝까지)
# =>즉, 각 순간에 자기보다 싼 곳까지 거리를 체크


cur_city_idx = 0
cost=0

for i in range(1,n):
  cost+=oil_cost_for_cities[cur_city_idx] * roads_length[i-1]
  if oil_cost_for_cities[cur_city_idx]>oil_cost_for_cities[i]:
    cur_city_idx = i

  
print(cost)


