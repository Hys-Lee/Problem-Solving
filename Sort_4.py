# ### 그냥 각 array를 각각 솔팅해서(반대순서로)
# ### K-1번index까지 보면서 바꿀만하면 바꾸면 됨

# n, k = map(int, input().split())
# arrA = []
# arrB = []

# arrA = list(map(int, input().split()))
# arrB = list(map(int, input().split()))

# arrA.sort(reverse=False)
# arrB.sort(reverse=True)
# for i in range(k):
#   if arrA[i] < arrB[i]:
#     arrA[i], arrB[i] = arrB[i], arrA[i]

# print(sum(arrA))

# ### 책 해설을 보니, 원소 개수가 최대 10만개니까 O(NlogN)보장하는 정렬알고리즘 이용해야 한다고 함.
