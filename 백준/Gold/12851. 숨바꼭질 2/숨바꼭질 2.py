## method
def sol(n,k):
    from collections import deque, defaultdict

    Min, Max = 0, 1e5
    will_visit = deque([n])
    visited = [-1]*(int(Max+1))
    visited[n]= 0
    answer = 0 #가능한 가짓수

    while will_visit:
        vx =  will_visit.popleft()
        if vx == k:
            answer += 1

        for nx in [vx+1, vx-1, vx*2]:
            # 새로 방문하게 될 nx가 이미 업데이트 된 상태에도 queue에 nx를 넣어주어야 하기 때문에 해당 조건이 사용됩니다.
            # 업데이트 된 값과 같아도 업데이트 가능합니다.
            if Min <= nx <= Max and (visited[nx] >= visited[vx] + 1 or visited[nx] == -1):
                will_visit.append(nx)
                visited[nx] = visited[vx] + 1
    return visited[k],answer
            
## input
n, k = map(int, input().split())

## output
t,m = sol(n,k)
print(t)
print(m)