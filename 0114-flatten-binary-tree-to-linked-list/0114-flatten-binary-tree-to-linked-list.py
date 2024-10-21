# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 그냥 preorder traversal을 해서 순서대로 list에 node들을 모으고,
# 얘네 순차 loop한번 돌면서 left지우고 right를 다음 노드로 만들어 버리면 됨.

# ## 수도코드만들기

# preArr=[]
# preorder탐색 함수 만들기(array에 preorder탐색시킨 결과를 넣기)#
# 함수 preorder(현재 노드)#


#   현재 노드의 left를 preorder탐색 (있다면)#
#   현재 노드를 preArr에 append시키기#
#   현재 노드의 right를 preorder탐색(있다면)#

# preorder탐색시켜 array에 저장완료하기#

# array순차 돌면서 flatten시키기#
# for i 0번부터 마지막인덱스-1까지
#   i번째의 left는 null로,
#   i번째의 right는 i+1번째 노드를 가리키도록.
# 마지막 인덱스노드에 대해서는, left와 right모두 null로 만들기


# __ 알고리즘 1분
# __ 수도코드 8분

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return
        preArr=[]
        def preTraverse(curNode):
            ## test
            # print("curNode: ",curNode.val)

            preArr.append(curNode)
            if curNode.left!=None:
                preTraverse(curNode.left)
            if curNode.right!=None:
                preTraverse(curNode.right)
        ## test
        # print("root: ",root)
        preTraverse(root)
        ## test
        # print("어레이: ",preArr)

        for i in range(0, len(preArr)-1):
            preArr[i].left=None
            preArr[i].right=preArr[i+1]
        
        preArr[len(preArr)-1].left=None
        preArr[len(preArr)-1].right=None
        ## test
        for i in preArr:
            print(": ",i.val)

        