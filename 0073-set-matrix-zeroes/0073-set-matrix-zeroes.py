# 그냥 0이 있는 row랑 col이 arr에서 어디 위치인지 알아내면 되자너.
# 문제는 좀 아래,오른쪽에 0이 나오는 경우인데, 이것도 뭐.
# space는 row길이만큼만 쓰면 되겠는데?
# row한줄씩 내려가면서는 row에 0으로 만드는 작업만 하고, 
# 마지막까지 도착했을 때 0이 어디 col에 위치해있는지만 보고, 한번 더 loop돌리면서 col해당하는 부분0으로 하면 됨.

# 그니까, row한줄씩 읽어내려가다가 0을 만나게 되면, row길이만큼의 arr에 0의 idx(col위치)를 true로 바꿔놓으면 됨.
# 아니 근데, 윗줄에서 0으로 바꾸면 밑에줄에서 바뀐0이 영향을 안미쳐야 하는데..
# 아니네 안미치겠네. ㄱㄱ

# 공간복잡도는 O(N)
# 시간복잡도는 O(N*M)

# ## 수도코드만들기
# zcols=[False maxtrix[0]길이]: 초기화
# for i matrix길이
#   hasZ=False #: 각 줄에 0 초기화
#   for j matrix[0]길이 ## 그냥 1줄 파악하고 있으면 for문 한번 더 써서 한줄 0으로 바꾸는 식으로 하자.
#     if [i][j]에 0이 있다면
#       hasZ를 True,
#       zcols[i]를 True로. 얘때문에 row전체 무조건 완주해야함.
#   if hasZ가 참이면
#     for j matrix[0]길이 : 이 row는 0으로 채우기
#         matrix[i][j]를 0으로 

# 이제 col대한0처리
# for i matrix 길이
#   for j matrix[0]길이
#     if zcols의j번째가 True면
#       [i][j]를 0으로


# __ 알고 대충 6분
# __ 수도코드 15분


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zcols=[False for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            hasZ=False
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    hasZ=True
                    zcols[j] = True
            if hasZ:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if zcols[j]:
                    matrix[i][j] = 0


        