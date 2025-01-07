# 체크박스랑 dfs로 하면 끝이네.
# 최대 9만개라네.
# bfs로 해도 되긴 할 듯? 상하좌우로 1이 보이면 큐에 넣는거니까. 
# 큐 넣기 전에 체크박스 true 처리하고 넣으면 되겠네. 

# ### 수도코드만들기
# 체크박스 grid크기만큼 만들기
# dydx 를 상좌하우로 만들기 
# def bfs(큐)
#   while 큐가 끝날 때까지
#     큐에서 pop한 위치y,x

#     for 현재 위치에서 사방향으로 
#         if  범위 벗어나지 않은 곳에서 1이 발견된다면 그리고 체크박스false라면
#             체크박스에 y,x위치 true로 만들기
#             큐에 y,x위치를 넣기

# count=0초기화

# for i 그리드 크기
#   for j 그리드[0]크기
#     if i,j위치에 1이면서 체크박스 false라면 
#       true로 만들고 큐에 넣고 bfs실행시키기
#       count+=1


# __ 알고 대충 4분
# __ 수도코드 대충 13분
# __ 엣지 대충 13분(수도코드 짜며 수정함.), 코드짜며 수정함 bfs에서 체크박스

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        chklist=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dydx = [(-1,0),(0,1),(1,0),(0,-1)] # 상우하좌 (시계방향)
        def bfs(q):
            while(q):
                y,x = q.popleft()
                for dy,dx in dydx:
                    ny = y+dy
                    nx = x+dx
                    if 0<=ny<len(grid) and 0<=nx<len(grid[0]) and grid[ny][nx]=="1" and chklist[ny][nx]==False:
                        chklist[ny][nx] = True
                        q.append((ny,nx))

        count=0
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]=="1" and chklist[i][j]==False:
                    chklist[i][j] = True
                    q = deque([(i,j)])
                    bfs(q)
                    count+=1
        return count

