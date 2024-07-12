## 그래프로 표현 가능한가?
#### 엣지 개수가 그럼 99*2*99*2 => 1만 단위라 괜찮은 듯.
####   최단거리 다익스트라자 -> log(E+V)라 이걸로 하면 될 듯.
#### 예시1에서 (0,0)은 (0,2)랑 (2,0)만. (0,1)은 (0,2)랑 (0,0)만, 0,2)는 0,0)과 3,2)만.

from collections import deque

def makeNodeNum(yVal,xVal, rowLen):
    #### 번호는 i*가로길이+j
    return yVal*rowLen+xVal
def solution(board):
    ## 그래프 만들기
    startV=(0,0) # (y,x)
    goalV = (0,0)
    graph=[[] for _ in range(len(board)*len(board[0]))] ## [0번~board내부 모든 원소 개수)
    
    #### 번호는 i*len(board)+j
    for i in range(len(board)):
        for j in range(len(board[0])):
            ## 각 지점에서의 가로, 세로 만 조사 -> i*j*(i+j):100^3=100만
            if board[i][j]!='D':
                if board[i][j]=='R':
                    startV = (i,j)
                elif board[i][j]=='G':
                    goalV = (i,j)
                
                ## 현재 지점에서 양쪽으로 뒤져야 함 y,x모두
                for y in range(len(board)):
                    
                    ## y축(자기 빼고)아래방향 뒤지기 -> D나오면 멈추기
                    if y<=i:
                        continue
                    if board[y][j]=='D' :
                        ## test
                        if (makeNodeNum(i,j,len(board[0]))==1):
                            print("y아래",i,j,y,y-1)
                        if y-1==i: break         
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(y-1,j,len(board[0])))
                        break
                    elif (y==len(board)-1 and board[y][j]!='D'):
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(y,j,len(board[0])))
                        break
                    
                        # graph[i][j].append((y,j))
                for y in range(len(board)-1,-1,-1):
                    ## 윗방향 뒤지기
                    if y>=i:continue
                    if board[y][j]=='D' :
                        ## test
                        if (makeNodeNum(i,j,len(board[0]))==1):
                            print("y위",i,j,y,y+1)
                        if y+1==i: break         
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(y+1,j,len(board[0])))
                        break
                    elif (y==0 and board[y][j]!='D'):
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(y,j,len(board[0])))
                        break
                        # graph[i][j].append((y,j))
                        
                for x in range(len(board[0])):
                    ## x축(자기 빼고)오른쪽 뒤지기 -> D나오면 멈추기
                    if x<=j:continue
                    if board[i][x]=='D':
                        ## test
                        if (makeNodeNum(i,j,len(board[0]))==1):
                            print('x오른',i,j,x,x-1)
                        if x-1==j: break
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(i,x-1,len(board[0])))
                        break
                    elif (x==len(board[0])-1 and board[i][x]!='D'):
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(i,x,len(board[0])))
                        break
                for x in range(len(board[0])-1,-1,-1):
                    ## x축(자기 빼고)왼쪽 뒤지기 -> D나오면 멈추기
                    if x>=j:continue
                    if board[i][x]=='D' : ## 맵의 끝...
                        ## test
                        if (makeNodeNum(i,j,len(board[0]))==1):
                            print('x왼',i,j,x,x+1)
                        if x+1==j: break
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(i,x+1,len(board[0])))
                        break
                    elif (x==0 and board[i][x]!='D'):
                        graph[makeNodeNum(i,j,len(board[0]))].append(makeNodeNum(i,x,len(board[0])))
                        break
#                         # graph[i][j].append((i,x))
    

                    
    ## test
    print("GRAPH", graph)
        
                
                
    ## 다익스트라자
    INF = 1e9
    startNodeNum = makeNodeNum(startV[0],startV[1], len(board[0]))
    goalNodeNum = makeNodeNum(goalV[0],goalV[1], len(board[0]))
    dist=[INF if i!=startNodeNum else 0 for i in range(len(graph))]
    q = deque([(0,startNodeNum)])
    ## test
    # q.popleft()
    # print(list(q))
    while (q):
        repD,repV = q.popleft()
        if repD>dist[repV]:continue
        
        for tarV in graph[repV]:
            newD = 1+repD
            if newD<dist[tarV]:
                dist[tarV] = newD
                q.append((newD, tarV))
    
    # print(dist[goalNodeNum])
        
    
        
    ## start지점의 dist구하기
    answer = dist[goalNodeNum] if dist[goalNodeNum] != INF else -1
    return answer