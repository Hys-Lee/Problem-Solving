### 전체가 가장 작은 값이 되려면
### 각 번째 수도 가장 작은 값이 되어야 가능한한
### B가장 큰 값과 A가장 작은 값을 곱하는 식으로 해야
### B랑 A의 정렬을 반대로 해서 매칭시키자
### element단위가 각 input숫자 각각이다(최소단위)
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
# print(A)
B = list(map(int, sys.stdin.readline().split()))

B.sort()
B.reverse()
# print(B)
result = 0
for i in range(len(A)):
  result += A[i] * B[i]

print(result)
