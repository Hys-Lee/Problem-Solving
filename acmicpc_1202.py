## 가장 비싼 것들 뽑아야
## 가장 가방에 fit한 애들을 뽑아야

## 비싼 것들부터 뽑아서 얘네 무게 맞는 애들을 선택?
## 미리 보석이랑 가방이랑 무게로 순서를 매기자
##

# NlogN이 쓰일 것 같은데...
## 걍 뽑

## 걍 무게순 정렬둘다 하고,
## 가방에 넣을 수 있는 애들 중 비싼 애들로 가져가자.
## 이게 K*N아닌가? 몰라 걍 짠다

# import heapq
# import sys

# n, k = map(int, sys.stdin.readline().split())
# jews = []

# for i in range(n):
#   m, v = map(int, sys.stdin.readline().split())
#   heapq.heappush(jews, (-v, v, m))

# bag = [0 for _ in range(k)]
# for i in range(k):
#   bag[i] = int(sys.stdin.readline())

# bag.sort()  # 오름차순
# result_sum = 0
# for i in range(k):
#   next_jews = []
#   while (len(jews) > 0):
#     cur_jew = heapq.heappop(jews)
#     if bag[i] < cur_jew[2]:
#       heapq.heappush(next_jews, cur_jew)
#     else:
#       result_sum += cur_jew[1]
#       break

#   jews.extend(next_jews)
#   heapq.heapify(jews)

# print(result_sum)

## 힌트랑 지금까지 풀었던 greedy, heapq사용 같이 생각해보니 떠로는건데,
## 전체 가방, 보석 무게에 대해서 오름차순 정렬 후,
## 보석에 heapq걸어서 가방[i]에 들어가는 보석까지 selected_jews에 담기
## 이 selected_jews는 heapq로 가장 비싼 것을 뽑아낼 거임

## selected_jew에서 가장 비싼거 뽑아내고 result에 합산
## 남은전체 보석에서, 다음 가방[i+1]에 들어가는 보석까지 heapq로 또 selected_jews에 담기
## 이를 또 위와 같이 반복.
## 이러면 결국, max(N,K)*logN 임. 

import heapq
import sys

n, k = map(int, sys.stdin.readline().split())
jews = [(0, 0) for _ in range(n)]

for i in range(n):
  m, v = map(int, sys.stdin.readline().split())
  jews[i] = (m, v)

bag = [0 for _ in range(k)]
for i in range(k):
  bag[i] = int(sys.stdin.readline())

#정렬 무게순
jews.sort()  # 오름차순
bag.sort()  # 오름차순

# 가방에 들어갈 수 있는 애들 뽑기
# 그 중 가장 비싼거로
considering_jews = []
result = 0
for i in range(k):
  while (len(jews)>0): # jews가 비어있으면 pop못하게.
    this_jew = heapq.heappop(jews)
    if this_jew[0] > bag[i]:
      heapq.heappush(jews, this_jew)  # 다시 넣기
      break
    else:
      jew_for_max = (-1 * this_jew[1], this_jew[0])
      heapq.heappush(considering_jews, jew_for_max)
  ## else안거치고 bag에 맞는 보석이 하나도 없을 때 대비
  if len(considering_jews)>0:
    result += -1 * heapq.heappop(considering_jews)[0]

print(result)
## 테스트 해보기