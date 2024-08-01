# 근데, 왔던길로 되돌아갈 수도 있는거 아님?
# 보면, 출구 있는칸 지나갈 순 있지만, 출구 도착(최종)할 때는 레버를 당겼어야 종료되는 듯.
# 글고 다 상관없이 여러번 지날 수 있다니..

# 근데,뭐 최단거리 2번 구한다고 생각하면 되긴 함.

# 그래프를 양방향 그래프로 만들어 두면 될 듯?

# 길 없을수도 있음. ->-1반환


# #수도코드#
# graph=맵 크기에 대해 2차원 빈 배열로 미리 세팅해야 함.
# maps를 읽으면서 graph생성. -> 양방향 그래프로.
#     자기 상하좌우로 갈 수 있다면 (맵 제한 체크) 해당 노드로 연결
#     읽으면서 시작점, 레버, 출구의 노드번호 기억.
#     노드번호는 maps[i][j] = i*len(maps[0])+j임. => 0~제곱수-1

# q를 위한 heapq생성.
# 생각해보니까, q에 repD값도 필요할 듯. (cost가 아니라 dist니까.)
# 그래서 q에 들어가는 원소는 (repDist, repV, prevV) 이 tuple임.
# 여기서부터 dijstra인데
# repV에서 연결된 다른 노드 찾을 때, prevV는 건너뛰고 찾는거임.

# 다잌스트라를 2번써야함.
# start->레버
# 레버->exit으로.

# 만약, start->레버 최단거리나 레버->exit나 둘 중 하나라도 INF면 -1반환
# 아니면 둘의 합을 반환.

## 45분-제출 시 런타임 에러로 실패가 생김.
## 1시간 - 슈바 모르겠음. 왜 에러나는지.
#### 쉬바 maps이 정사각형이라고 생각했음.... 직사각형임..

import heapq
def solution(maps):
    graph=[[]for _ in range(len(maps)*len(maps[0]))]
    start=-1 # 초기화
    exit=-1 # 초기화
    lever = -1 # 초기화 예네가 없을리는 없긴한데...
    ##test
    print(graph)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            nodeNum = i*len(maps[0])+j
            if maps[i][j]=='S': start = nodeNum
            elif maps[i][j]=='L':lever = nodeNum
            elif maps[i][j]=='E':exit = nodeNum
            
            if maps[i][j] != 'X':
                ##test
                # print("NN: ",nodeNum)
                if i-1>=0 and maps[i-1][j]!='X': #상
                    ##test
                    # print("상")
                    graph[nodeNum].append((1,(i-1)*len(maps[0])+j))
                if i+1<len(maps) and maps[i+1][j]!='X': #하
                    ##test
                    # print("하")
                    graph[nodeNum].append((1,(i+1)*len(maps[0])+j))
                if j-1>=0 and maps[i][j-1]!='X': #좌
                    ##test
                    # print("좌")
                    graph[nodeNum].append((1,(i)*len(maps[0])+j-1))
                if j+1<len(maps[0]) and maps[i][j+1]!='X': #우
                    ##test
                    # print("우")
                    graph[nodeNum].append((1,(i)*len(maps[0])+j+1))
            else:## X경우
                continue
    ##test
    # print("G: ",graph)
    ### 다잌스트라자 - 시작->레버까지
    INF = 1e9
    dist=[INF for _ in range(len(maps)*len(maps[0]))]
    dist[start] = 0
    ## test
    # print("DIST INIT: ", dist)
    
    q=[(0,start,start)] ## 시작점이니까 prev는 의미없도록 자기자신으로.
    while(q):
        repD, repV, prevV = heapq.heappop(q)
        ##test
        # print("repD,repV,prevV in start->laver: ",repD,repV,prevV)
        if (repD>dist[repV]) : continue
        
        for newC, newV in graph[repV]:
            ## 되돌아가는 경우는 제외하기
            if prevV == newV:
                continue
            
            newD = newC + repD
            if(newD<dist[newV]):
                dist[newV] = newD
                heapq.heappush(q,(newD, newV,repV))
    
    ## test
    # print("final dist: ",dist)
    
    if(dist[lever]==INF):
        return -1
    finalDistLever = dist[lever]
    
    ### 다잌스트라자 - 레버->출구까지
    INF = 1e9
    dist=[INF for _ in range(len(maps)*len(maps[0]))]
    dist[lever] = 0
    ## test
    # print("DIST INIT: ", dist)
    
    q=[(0,lever,lever)] ## 시작점이니까 prev는 의미없도록 자기자신으로.
    while(q):
        repD, repV, prevV = heapq.heappop(q)
        if (repD>dist[repV]) : continue
        
        for newC, newV in graph[repV]:
            ## 되돌아가는 경우는 제외하기
            if prevV == newV:
                continue
            
            newD = newC + repD
            if(newD<dist[newV]):
                dist[newV] = newD
                heapq.heappush(q,(newD, newV,repV))
    
    ## test
    # print("final dist: ",dist)
    
    if(dist[exit]==INF):
        return -1
    finalDistExit = dist[exit]
    
    ## test
    print("finalDistLever, Exit: ",finalDistLever, finalDistExit)
    return finalDistLever+finalDistExit
    # answer = 0
    # return answer