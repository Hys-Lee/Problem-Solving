# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# 딱히 BST도 아니라, left to right로 탐색해야 할 듯.

# 그냥 tree탐색하는 그대로, 탐색하면서, 현재 높이만 체크
# 높이별로 array다르게 만들어서 집어 넣으면 될 듯.
# 그냥 recusion사용하면 될 듯.
# 리커젼함수(현재노드, 레벨)
# 왼족 자식 리커전
# 현재 노드 -> 현제 레벨에 맞는 리스트칸(없으면 만들고)에 현재 노드 val을 append하기.
# 오른쪽 자식 리커전

# 이렇게 나아가면 되지롱.

# ### 수도코드만들기
# ##
# 1. 결과 어레이 만들기 (초기화 []빈칸으로.)
# 1. 트리 탐색 함수 만들기
# 2. 트리 탐색 함수(현재 노드, 현재 레벨)
#     3. 현재 레벨에 대한 어레이가 없다면 만들기 (자식 내려가기 전에 미리 할 것들.)
#     4. if 어레이 길이<현재 레벨+1이면
#         어레이에 [] append
#     2. 왼쪽 탐색
#         왼쪽 없으면 건너뛰기
#     4. if 현재노드의 left가 None아니면
#          트리탐색 함수(현재.left, 현재레벨+1)
#     2. 현재 노드 처리

#     3. 현재 레벨에 대한 어레이에 현재 노드 val을 넣기
#     4.  어레이에 [현재 레벨] 인덱스에 현재 노드 val을 넣기
#     2. 오른족 탐색
#         오른쪽 없으면 건너뛰기
#     4. if 현재 노드 irhgt가 none이 아니면
#          트리 탐색 함수(현재.right, 현재레벨+1)
#     2. 종료
#         (return. 딱히 필요하진 않아보임.)
# 1. 트리 탐색 함수 루트에서 실행(루트, 0)
# 1. 결과 어레이 반환

# __ 알고리즘 대충 3분
# __ 수도코드 대충 18분

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        def travel(cNode, cLevel):
            ## test
            # print("clevel,ansewr: ",cLevel, answer,cNode)
            if len(answer)<cLevel+1:
                ## test
                # print("추가 전 answer: ",answer)

                answer.append([]) ## 될라나.
                
                ## test
                # print("추가 후 answer:" ,answer)
            if cNode.left!=None:
                travel(cNode.left, cLevel+1)
            answer[cLevel].append(cNode.val)
            ## test
            # print("answer[clevel],cnode, ", answer[cLevel],cNode.val)

            if cNode.right!=None:
                travel(cNode.right, cLevel+1)
            return
        ## test
        # print("root: ",root)
        if root==None:
            return []
        travel(root,0)
        ## test
        # print("answer: ",answer)
        return answer