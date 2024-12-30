
import sys
def solution(grid):
    sys.setrecursionlimit(2600000)
    
    
    nodemap =[[row[i] for i in range(len(row))]  for row in grid]
    chklist = [[[False for _ in range(4)]for _ in range(len(nodemap[0]))]for _ in range(len(nodemap))]
    
    
    
    dydx = [(-1,0), (0,-1),(1,0),(0,1)] 
    def moving(curPos,overDirI):
        overDir = dydx[overDirI]
        
        if curPos[0]+overDir[0]>=len(nodemap) :
            return (0,curPos[1]+overDir[1])
        elif curPos[0]+overDir[0]<0:
            return (len(nodemap)-1, curPos[1]+overDir[1])
        elif curPos[1]+overDir[1]>=len(nodemap[0]) :
            return (curPos[0]+overDir[0], 0)
        elif curPos[1]+overDir[1]<0:
            return (curPos[0]+overDir[0], len(nodemap[0])-1)
        else: # 정상
            return (curPos[0]+overDir[0], curPos[1]+overDir[1])
    
    def dfs(curPos, curDirI):
        # curY,curX = curPos
        
        if chklist[curPos[0]][curPos[1]][curDirI]:
            return 0
        
        chklist[curPos[0]][curPos[1]][curDirI] = True
        
        curPos = moving(curPos, curDirI)
        if nodemap[curPos[0]][curPos[1]]=="L":
            curDirI = (curDirI+1)%4
        elif nodemap[curPos[0]][curPos[1]]=="R":
            curDirI = (curDirI-1) if curDirI-1>=0 else 3
        ## else면 "S"인데, 이 때는 curDirI는 그대로
        
        return dfs(curPos,curDirI)+1
        
        
        
#         nextPos=(-1,-1) # 초기화
#         nextDirI=-1 # 초기화
#         if nodemap[curY][curX]=="S":
#             nextPos = moving(curPos, curDirI)
#             nextDirI = curDirI
#         elif nodemap[curY][curX]=="L":
#             nextDirI = (curDirI+1)%4
#             nextPos = moving(curPos,nextDirI)
#         else : # nodemap[curY][curX]=="R"
#             # nextDirI = (curDirI-1)%4
#             nextDirI = (curDirI-1) if curDirI-1>=0 else 3
#             nextPos = moving(curPos, nextDirI)
        
#         if chklist[curPos[0]][curPos[1]][nextDirI]:
#             return 0 
        
#         chklist[curPos[0]][curPos[1]][nextDirI] = True
        
        
#         count = dfs(nextPos,nextDirI)
#         return count+1
  
    answer = []
    
    for i in range(len(chklist)):
        for j in range(len(chklist[0])):
            for k in range(len(chklist[0][0])):
                if not chklist[i][j][k]:
                    count = dfs((i,j),k)
                    if count>0:
                        answer.append(count)
        
            
    answer.sort()
    
    
    
    return answer