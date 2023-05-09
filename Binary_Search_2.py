# binary search는 정렬한 후에 진행해야하는데, 그냥 해버림. 이러면 o(logN)이 아니게 되어서 의미가 없음,
#또한, 책에서보니 다양한 방법으로 풀 수 있었음. ㅇ예를 들어서, counting sort?계수정렬?의 방식을 차용해서, 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤, 리스트의 인덱스에 직접 접근하는 방식으로 만들 수도 있음. 또한, 단순히 특정한 수가 한번이라도 등장했는지를 검사하면 되기 때문에 집합 자료형을 사용할 수도 았다고 한다, set()함수는 집합 자료형 초기화에 사용한다곻 함.
#다양한 방법으로 풀 수 있다는 것을 알고 여 러 방ㅂ버을 모두 이용해 효과적을풀 수도 있어야 한다고 함.

# import sys

# n = int(input())
# narr = list(map(int, sys.stdin.readline().rstrip().split()))
# narr.sort()
# m = int(input())
# marr = list(map(int, sys.stdin.readline().rstrip().split()))

# def binarysearch(num, start, end):
#   middle = (start + end) // 2
#   if start >= end: return "no"
#   if narr[start] == num:
#     return "yes"
#   elif narr[end] == num:
#     return "yes"
#   elif narr[middle] == num:
#     return "yes"
#   if binarysearch(num, start, middle) == "yes" or binarysearch(
#       num, middle + 1, end) == "yes":
#     return "yes"
#   else:
#     return "no"

# for ele in marr:
#   print(binarysearch(ele, 0, n - 1), end=" ")
