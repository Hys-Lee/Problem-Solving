# 사실 아예 1차원 배열로 되어있으면 바로 binary search쓰면 끝나는데,
# 2차원 배열이라 좀 애매함.
# 2차원을 1차원으로 바꾸면 이미 시간 넘어갈 듯.

# 걍 2차원 배열 자체로 binary search쓰면 될 듯.
# 맨 앞 숫자로 binary search써서, 있을 만한 row를 고르고, 여기에 그 row에 대해 binary search하면
# log(m)+log(n) = log(m*n)임.

# rows중 고르는거는
#     mat[0][0]를 s, mat[마지막][0] e라 하고 m을 그 둘의 절반으로 잡아서,
#     m하고 target비교로..

# 여기서 targetRow 고르면, 그 안에서도 비슷하게 ㄱㄱ
# 못찾으면 false반환

# ## 수도코드 짜기
# targetRow=[] ### 초기화
# def bsMat(s,e): ## 얘는 row를 찾는거니까... j와 j+1을 비교해야지.
#     이 때, s,e는 인덱스 값(matrix전체의)
#     m = (s+e)//2 : m 잡기
#     if s>e:
#         target이 아예 메트릭스 바깥에 존재할 수 있으니, 이 때는 row수준에서 걸러주는거.
#         return : 기본

#     if m이 마지막 row 이거나, m번째(포함)랑 m+1번째(미포함) 사이 범위에 target이 존재한다면 :
#         targetRow를 할당하기.
#         함수 종료

#     elif target이 m의 값보다 작다면, e를 m-1으로.
#     elif target이 m+1의 값보다 크-같다면, s를 m+1으로.  (위에서 m이 마지막 row가능성 가로채니까.)

# if targetRow가 비워져 있다면
#   ret False

# def bsRow(s,e):
#     m = (s+e)//2
#     if s>e:
#         return False
    
#     if targetrow의 m번쨔ㅐ==target:
#         return True
    
#     elif target이 m번째 값보다 작다면, e를 m-1로
#     else: target이 m번쨔 값보다 크다면, s를 m+1로.

# bsMat(0, 매트릭스 마지막 인덱스)

# bsRow(0,row마지막 인덱스)



# ___ 알고리즘 10분
# __ 수도코드 25분
# __ 엣지 28분(s움직이는 경우 수정)
# __ 틀림 45분 


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow=[]
        def bsMat(s,e):
            m = (s+e)//2
            ## test
            # print("s, m, e, mat[m][0], mat[m+1][0]", s, m, e, matrix[m][0],matrix)
            if s>e:
                return
            
            if m==len(matrix)-1 or matrix[m][0]<=target<matrix[m+1][0]:
                ## test
                # print("와우, targetRow: ", targetRow)
                targetRow.extend(matrix[m])
                return
            
            elif target<matrix[m][0]:
                e = m-1
            elif target>=matrix[m+1][0]:
                s=m+1
            bsMat(s,e)
                
        bsMat(0,len(matrix)-1)
        ## test
        # print("targetRow: ", targetRow)
        if len(targetRow)==0:
            ## test
            # print("target이 matrix최소보다 작다: ", target, matrix[0][0])
            return False
        
        def bsRow(s,e):
            m = (s+e)//2
            ## test
            print("s,m,e,targetRow", s,m,e,targetRow)
            if s>e:
                ## test
                # print("이건 틀린경우")
                return False
            
            if targetRow[m]==target:
                ## test
                # print("정답 찾음")
                return True
            elif targetRow[m]>target:
                e = m-1
            else: ## m이 크다면
                s = m+1
            return bsRow(s,e)
        answer = bsRow(0,len(targetRow)-1)
        return answer
