# 1. Dynamic Programming
#   1부터 입력 최댓값 직전까지
#    하나씩 만들어 본다.
#      앞에거를 재사용 해서 계산하면서?
#         그러러면 앞에서 어떤 걸 몇개 썼는지 알아야 함.
#   ㄴ> 그러면 각 코인 몇개 인지 다 체크해봐야 함.
#    100만개 array쓸 듯.
# 2. Greedy
#    1부터 최댓값 직전까지
#     남은 것 중 가장 작은거를 더해서 만들수 있는지 체크

## 확실한 것은 sub problem으로 쪼개는 문제는 맞음.

## 그럼 max보다 작은 애들 다 만들 수 있으면, 그 보다 큰 애들도 만들 수 있나? -> 아님.   max가 3이면, 1,2,3만 있다면 7은 못만든다. 최대는 전체 합이겠지. 전체 합까지 greedy하자.

import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

total_max = sum(arr)
total = [0]*(total_max+1)
total[0] = 1 # index==0인건 패스

for i in range(1,len(total)):
  total[i]
