## greedy로 되는 것 같은뎅.
## 걍 가장 작은 순서대로 줄을 서면 됨.
##
## 같은 길이 누적 합 array만들자.


import sys
## 입력
n = int(input())

Pis = list(map(int, sys.stdin.readline().split()))
# 정렬
Pis.sort()

## 누적 합 
acc_sum = [0 for _ in range(n)]

## 누적 합 계산
for i in range(n):
  # 0th index는 이전index가 없으니..
  if i==0:
    acc_sum[i] = Pis[i]
  else:
    acc_sum[i] = Pis[i]+acc_sum[i-1]


print(sum(acc_sum))
