### 전체 최대이려면..
### N-1까지 input에서 최대일 때
### N번째 input이 들어올 때도 최대이려면 Nth input이 최대한 커야함.
### 그러려면 input 정렬이...
### 내림차순이어야
### 그래야 작은거에 최대한 영향 안받지
## 근데, 이러면 N-1에서 최대일 때 N번째 받으면 줄어들어서 안받다가 N+1번째 오히려 늘어날 수도 있는데...
## 걍 전체 계산하고 max로 봐야하나?

### greedy로 볼 수 있지.
### 모든 element대해 optimal이 변경되는게 아니라
### 특정 조건 만족 element에서 optimal이 충족되는 경우인거지.
### element가 최소단위가 아닌 것.
### =>"""따라서 정렬한 다음, 이전 optimal과 이번 element로 인한 결과를 비교해가면서 전진하면 됨"""

n = int(input())
lopes = []
for i in range(n):
  lopes.append(int(input()))
lopes.sort()
lopes.reverse()
# print(lopes)

each_result = []
for i in range(n):
  each_result.append((i + 1) * lopes[i])
print(each_result)
print(max(each_result))