# 이거 완전 최단경로 문제...?  노드는 최대 4만개.
# edge cost는 0이상.
# 방향은 아래, 오른 방향만 가능.각 노드에서 엣지 최대 2개씩만 만들면 되네.
# 오른쪽에 붙어있다면 아래만, 아래쪽에 붙어있다면 오른쪽만. -> 두개 다 독립적으로
# 그래프 만드는데 노드 번호는 row길이*행 번호i+ 열 번호j. 다만, cost는 화살표 종착지에 있는 값을 사용해야 함.
# dist만들 때, 시작점에서의 값을 [0][0]의 값으로 초기화 하면 될 듯.
# 다잌스트라로 쌉가능일 듯.

# 시간복잡도가 뭐더라..  O(V+E)아님?

# ### 수도코드 만들기

# -그래프 만들기
# graph=[] : 초기화
# for i grid의 크기
#     for j grid[0]의 크기
#         vNum = grid[0]크기 * i + j : 노드 번호
#         if i가 마지막이면
#             오른쪽 방향만 엣지 추가
#         if j가 마지막이면
#             아래쪽 방향만 엣지 추가
        
#         오른쪽 방향, 아래쪽 방향 엣지 추가
#             (cost, 종점노드번호)

# -다잌스트라자 세팅
# inf=1e9
# dist=[inf가 grid크기*grid[0]크기 만큼] : 초기화
# dist[0] = grid[0][0] : 초기화
# q=[(dist[0], 0)]: 시작점 초기화<- heap을 사용할 것



# -다잌스트라자 돌리기
# while q가 비워질 때까지
#     repD, repV = q에서 heappop
#     if repD가 dist에서 repV 것의 거리보다 크다면 : 제시된(q에 들어있는) 것들 중 최단인 경로통한 V를 선택확정.
#         continue: 패스하기
    
#     for repV로부터 나아갈 수 있는 newV, newC (graph통해서)
#         newD = newC + repD 일 때 (현재 도착한 V통해 newV까지 가는 거리)
#         if newD가 dist[newV]보다 작다면 : 현재 V통해 newV까지 가는 거리가 원래 newV까지 가는 거리라 알고 있떤 것보다 작다면
#             dist[newV]를 newD로 업데이트
#             q에 (newD, newV)를 추가


# __ 알고리즘 (7분)
# __ 수도코드 17분
# __ 엣지케이스 21분
#     - 다잌스트라자로 푸렁도 되는가? (유형은 일치. 시간도 일치.)
#     - 다잌스트라자 구현 알고랑 문제 풀이랑 맞는가
#     - 여기선 너무 잘 규격화 되어있는 형식이라, 다른 특별한 케이스가 딱히 없음

import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        graph=[[] for _ in range(len(grid)*len(grid[0]))] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ## 마지막 종착지는 건너뛰기 -> 여기는 종착지라.
                if i==len(grid)-1 and j==len(grid[0])-1:
                    continue
                

                vNum = len(grid[0]) * i + j # 노드번호
                if i==len(grid)-1: #i가 마지막이면
                    #오른쪽 방향만 엣지 추가
                    graph[vNum].append((grid[i][j+1], vNum+1)) # 종착지는 위에서 처리
                    continue # 맨 밑의 과정피하기
                if j==len(grid[0])-1: #j가 마지막이면
                    #아래쪽 방향만 엣지 추가
                    graph[vNum].append((grid[i+1][j],vNum+len(grid[0]))) # 종착지는 위에서 처리
                    continue # 맨 밑의 과정피하기

                graph[vNum].append((grid[i][j+1], vNum+1)) # 종착지는 위에서 처리
                graph[vNum].append((grid[i+1][j],vNum+len(grid[0]))) # 종착지는 위에서 처리
        
        ## test
        # print("graph: ", graph)

        inf=1e9
        dist=[inf for _ in range(len(grid)*len(grid[0]))]
        dist[0] = grid[0][0] 
        q=[(dist[0], 0)]
        ## test
        # print("시작전 dist, q: ", dist, q)
        while(q):
            repD, repV =heappop(q)
            if repD>dist[repV]:
                continue
            ## test
            # print("포섭된 노드V, D: ", repV, repD)
            for newC, newV in graph[repV]:
                newD = newC + repD
                if newD< dist[newV]:
                    dist[newV]= newD
                    heappush(q, (newD, newV)) 
        
        ## test
        # print("final dist: ", dist)

        answer= dist[len(grid)*len(grid[0])-1]
        ## test
        # print("결과: ", answer)
        return answer