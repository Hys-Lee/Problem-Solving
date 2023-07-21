# Programmers에서 푸는 문제였어서 고민은 거기서 함.
# Greedy한 접근을 해보면,
# 가장 작은 시간이 걸리는 음식을 순서로 정렬
# 후 얘네부터 제거하는 방식을 이용.
# 그래서 답지에선 heapq를 사용했다.
# heapq는 n개 원소에 대해 다 push / pop하는 데 nlogn이 걸려서, 얘만 쓴다면 타당함.


import heapq

def solution(food_times, k):
  food_heap=[]
  for i in range(len(food_times)):
    heapq.heappush(food_heap,(food_times[i],i+1)

                   
  while(1):
    size = len(food_times)
    ele=heapq.heappop(food_times)
    if k<size*ele:
      break;
    elif k-size*ele<0:
      return -1
      
    else:
        k-=size*ele;
  
  r = sorted(food_heap, key=lambda x:x[1])
  r = r*ele[0]
  
  return r[k][1]

