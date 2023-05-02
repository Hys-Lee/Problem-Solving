# 하나 고르면 1칸 혹은 2칸 넘기면서 골라야 함.
#어차피 NlogN시간일 듯. 모든 케이스 따지는데. 다이나믹 쓰더라도

import sys

n = int(input())
arr = map(int, sys.readline().split())

# 다이나믹 프로그래밍 -> 작은 문제들 푸는 방법=큰 문지 푸는 방법
# 전체 식량창고 개수가 1개일 때붵 시작해서 n개일 때까지 늘려가면서 이전 기록 재사용.
# 이 때 참고하는 기록은 직전과 직전의직전기럭 2가지임.

dynamic_arr = [0]  #0번째 어레이는 날리고 시작
dynamic_arr.append(arr[0])
dynamic_arr.append(arr[1])  #참고자료 2개 생성
for i in range(3, n + 1):
  if dynamic_arr[i - 2] > dynamic_arr[i - 3]:
    dynamic_arr.append(arr[i - 1] + dynamic_arr[i - 2])
  else:
    dynamic_arr.append(arr[i - 1] + dynamic_arr[i - 3])

print(dynamic_arr[n])
