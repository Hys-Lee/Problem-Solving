# 동전이 배수 관계이므로
# 전형적인 greedy문제
# a1=1이라 못 만드는 값은 없음

import sys
# 입력 받기
n, k = map(int, sys.stdin.readline().split())

coins = [0 for _ in range(n)]

for i in range(n):
  coins[i] = int(input())

# coins는 오름차순 정렬 됨.
# 가장 높은 가격의 동전부터 최대한 채우기

# 루프 편하게 역순으로 정렬(큰거부터)
coins.reverse()

coin_count=0

#카운트 세면서, k값을 가격만큼 줄이면서 어떤 동전으로 할 지 체크
for i in range(n):
  if k==0:
    break
  elif k//coins[i]>0 :
    coin_count+=k//coins[i]
    k%=coins[i]


print(coin_count)


  