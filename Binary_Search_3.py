# import time

# n, m = map(int, input().split())
# dduck_arr = list(map(int, input().split()))
# start_time = time.time()
# dduck_arr = sorted(dduck_arr, reverse=True)

# def findStandard(m):
#   # if 해당 떡길이 값>M(길이의 합 needed): 이보다 높은 길이들 중에서만 찾아보면 됨
#   cumul_sum = 0

#   for i in range(n):
#     if cumul_sum > m: break
#     cumul_sum += (dduck_arr[i] - dduck_arr[i + 1]) * (
#       i + 1)  ## 다음 떡 길이로 잘라 추가된 떡길이 * 지금까지 고려하고 있는 떡 개수

#   # for문 이후 i:고려한 떡 개수 and 현재 고려한 떡 길이의 바로 다음 떡 길이 인덱스
#   i = i - 1
#   cumul_sum -= (dduck_arr[i] - dduck_arr[i + 1]) * (i + 1)
#   height = dduck_arr[i]
#   while cumul_sum < m:
#     cumul_sum += i + 1
#     height += 1
#   return height

# print(findStandard(m))
# end_time = time.time()
# print("시간:", end_time - start_time)
# ##

### 책에서는 그냥 미리 sorting하지 않고 바로 binary search를 사용했다.
### 명확한 목표점을 갖고 사용하는게 아니라 마치 피벗처럼 중간점을 잡고 거기서 잘라서 만족하는지 판단하는 방식으로 했다.
### 이러면 binary로 logN에, 해당 지점에서 모든 떡들의 길이를 합하는 것이 N이 되므로, 총 NlogN만에 구할 수 있다.

## 반면, 내가 위에서 했던 방법은 binary search를 사용하지 않은 방법이다. 일단 sorting을 먼저 했다. 여기서 NlogN이상이 이미 들어간다.
## countingsort는 값 차이가 너무 나서 사용할 수 없었다.
## sorted가 NlogN이라고 함.

## 교재에서 사용한 방법은 다음과 같다.

# n,m = list(map(int, input().split()))
# array = list(map(int, input().split()))

# start=0
# end = max(array) ## max를 array에 사용하면 바로 최대값 알 수 있음...

# result=0
# while (start<=end):
#   total = 0
#   mid = (start+end)//2
#   for x in array:
#     if x>mid:
#       total += x-mid
#   if total <m: ## 떡이 부족하면 왼쪽 탐색
#     end = mid-1
#   else : ## 떡 충분하면 오른쪽 탐색
#     result = mid
#     start=mid+1
# print(result)

## 책에서는 현재의 떡볶이 양 따라 자를 위치를 정해야 해서 이를 재귀로 하면 귀찮기 때문에 그냥 반복문을 사용했다고 함.
