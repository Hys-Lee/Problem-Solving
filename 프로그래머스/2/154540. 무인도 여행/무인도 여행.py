from collections import deque

def solution(maps):
    visited=[]
    for i in range(len(maps)):
        row=[]
        for j in range(len(maps[0])):
            row.append(False)
        visited.append(row)
    
    def bfs(startP):
        startY, startX = startP
        dydx = [(-1,0),(+1,0), (0,-1),(0,+1)] #상하좌우
        psum=0
        q=deque([])
        q.append((startY, startX))
        while(q):
            cy,cx = q.popleft()
            if visited[cy][cx]:continue
            ## test
            # print("숫자 가진 친구들 y,x: ", cy,cx)
            visited[cy][cx] = True
            ## test
            # print("숫자는 맞지?: ", maps[cy][cx])
            psum+=int(maps[cy][cx])
            
            for dy,dx in dydx:
                ny = dy+cy
                nx = dx+cx
                if ny<0 or ny>=len(maps) or nx<0 or nx>=len(maps[0]): continue
                
                if maps[ny][nx]=='X': continue
                
                q.append((ny,nx))

        return psum
            
    periods=[]
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if maps[i][j]=='X':
                ## test
                # print("X인 곳 y,x: ", i,j)
                visited[i][j] = True
                continue
            
            ##### 이미 돌았던 섬 다시 방문하면 0을 반환하는 구만. 처음일 때만 bfs쓰도록 하자.
            if not visited[i][j]:
                ## test
                # print("숫자인 곳 첫 방문 y,x: ",i,j)
                p = bfs((i,j))
                periods.append(p)
    ### periods가 비었을 때 [-1]리턴하도록 하는거.
    if len(periods)>0:
        periods.sort()
    
        return periods
    return [-1]
    
    # answer = []
    # return answer