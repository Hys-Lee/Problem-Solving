# 이거 따로 알고리즘도 있는데..
# 끝나는 시간 기준 정렬
# 다음 회의 시작시간과 이전회의 끝 시간 체크

import sys

n = int(input())

times=[(0,0) for _ in range(n)]
for i in range(n):
  start,end = map(int, sys.stdin.readline().split())
  times[i]=(end,start)

# 끝 시간 기준 정렬
times.sort()

# 맨 처음 끝나는 것은 무조건 갖고 가니
count=1

# 각 끝시간 대해 다음 회의 시작시간 체크
# now_start를 계속 찾고, 찾으면 prev_end가 now_start가 되게

prev_end = times[0][0]
for i in range(1,n):
  
  now_start = times[i][1]
  if prev_end<=now_start:
    count+=1
    prev_end = times[i][0]


print(count)
  

