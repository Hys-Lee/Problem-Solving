# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 알았다.
# 그냥 자기-오른자식-왼자식 순서대로 탐방하면 됨.
# 다만, 높이를 기억해서, 자기 높이에 처음 왔따면(체크리스트상) answer에 해당 노드 value넣고 체크리스트 true하면 됨.
# 체크리스트는 높이에 대해서 존재하고.->전체 높이를 모르기 때문에, dynamic하게 추가해가야 겠는뎅

# ### 수도코드만들기

# answer=[]비우기
# chklist=[]비우기  맨 위를 깊이 0로 하자.

# def travel(curNode, depth)
#   if 현재 깊이를 chklist에서 찾을 수 없다면=chklist길이-1<depth라면,->와본적없다는 뜻 (false였던 적은 없을 거니 걍 이거로 퉁 가능.)
#     chklist에 True를 append
#     answer에 현재 node의 value를 append
#   # else chklist에서 현재 깊이 봤더니 True라면=>이미 왔던 깊이

#   right가 None이 아니라면 탐방
#   left가 None이 아니라면 탐방


# __ 알고 대충 10분
# __ 수도 대충 16분
# __ 엣지 -> root가 비었을 때는 빈 [] 반환 18분

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        answer=[]
        chklist=[]

        def travel(curNode, depth):
            if len(chklist)-1<depth:
                chklist.append(True)
                answer.append(curNode.val)
            
            
            if curNode.right is not None:
                travel(curNode.right, depth+1)
            if curNode.left is not None:
                travel(curNode.left, depth+1)



        travel(root, 0)
        return answer