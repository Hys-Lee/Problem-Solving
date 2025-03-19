# 일단 모든 노드 및 엣지를 체크해봐야 하네.

# 트리 하나당, 트리 구성하는 모든 노드 1개당 모든 엣지를 검사하므로,
# 노드개수*엣지 개수...

# 더 줄일 방법이 있나 위는 브루트포스긴함.

# 모든 노드에 대해 자기랑 연결된 애들에 대해 정보를 가질 수 있을 듯?
# 예시2에서 1번노드는 자기랑 연결된 8,4 에 대해

# 모든 노드는 자기 번호랑 연결된 엣지 개수를 알게 됨.
# 따라서, 자기번호가짝, 연결된 모든 엣지가 짝이라면,
#     자기가 루트일 때 짝수트리 (모든 엣지 개수)
#     자기가 중간일 때 역짝수트리가 되겠지. (모든 엣지 개수-1)
    
#     A랑 연결된 B는 A루트로보니 결이 맞는데, C때문에 결이 안맞음.
#     그러면 B는 루트로 볼 필요가 없음.
#         B를 루트로 보면 B는 반대결, A도 반대결이 되버림.
#         이거 그냥 흑백 뒤집기임.
#         따라서, 결이 안맞는 ...
        
#     1루트면 8,4가지니 역홀짝 노리겠지.
#         8가보니, 짝이라 틀림.
        
#         아하 루트를 8로 하면, 1과 8의 관계는 반대가 되지만,
#         루트를 8,1이외로 하면, 1만 관계가 뒤집혀서, 1과 8은 같은 결이 됨.
        
#         ㄴ> 즉, 탐색하다가 결 맞는 애들은 걍 건너뛰고, 결 안맞는애 만났다면,
#         "둘 중 하나와 연결되면서 아직 탐색하지 않은 쪽을 루트로 잡아보면 되겠네."
#             ㄴ> 이거 왜 보류했냐면, 
#                 이렇게하면 루트로 잡았다가 놓게 되는 경우가 여러번 발생 할 수 있어보여서.
#                 그러면 그냥 트리 모든 노드에 루트 넣어보는거랑 큰 차이가 없으니.
#                 그리고, 놓는 과정에서 다른 곳에미치는 여파를 저 노드 하나를 보는 시점에서는 알아내기 어려워서.
                
#         아니면 전지적으로 함 봐볼까? => 이게 맞다.
#             루트-일반 으로 볼때
#             1은 역홀-홀
#             8은 역짝-짝
#             4는 짝-역홀
#             6은 역짝-짝  을 노리게 되걸랑.
            
#             따라서 4만 루트로 잡으면 홀짝트리가 되겠네.
            
#             9는 역홀-홀
#             11은 홀-역홀
#             7은 홀-역홀
#             따라서 9만 루트면 역홀짝트리 완성
            
#             5는 역홀-홀
#             2는 짝-역짝
#             14는 역짝-짝
#             15는 홀-역홀
#             따라서 1개 루트로 잡는다고 아무것도 안생김.
            
            
            
#         예제1에서는..
#             루트-일반으로볼 때 
#             2는 역짝-짝
#             3은 홀-역홀
#             4는 역짝-짝
#             6은 역짝-짝
#             따라서, 3이 루트가 되면 홀짝트리.
            
#             9는 홀-역홀
#             11은 홀-역홀
#             따라서, 어떤걸 루트로 놔도 서로 반대 결이 됨.
            
            
#             이야 좋앗따.
#             그넫, 다음과같이 2개 연결되면 역홀짝, 홀짲ㄱ 둘다 나올 수 있을 듯.
            
#             2 - 3
            
#             루트-일반에서
#             2는 역짝-짝
#             3은 홀-역홀
            
#             따라서, 둘 중 아무거나 바꿔도 둘이 결이 맞게 됨.
#             2가 루트면 역홀짝, 3이 루트면 홀짝이 됨.

# 즉, 체크리스트를 일단 파는겨.
# 그리고, 트리 별로 루트-일반에서의 홀짝/역홀짝 결을 파악해야함.

# 일단, 결 파악하는거는 트리구조 다 해매지 않고, 그냥 graph를 통해 노드 번호 1개씩 올리면서도 체크 가능함.

# 이후에 완전탐색으로 tree이동하면서 트리를 이루는 노드 번호들을 파악해두면 되겠다.
# 그리고 한 트리안에서 루트 쪽에서 살펴보면서, 자기 자신만 뒤집히면 나머지와 결이 같아지는 경우에 count+=1하는거임.
#     ㄴ> 루트 쪽에 1바퀴 돌려서, 홀짝/역홀짝 개수를 구하면 됨.
#     if 홀짝개수==1
#     if 역홀짝 개수 ==1   => 이렇게 if로만 해서 둘다 가능하도록 하면 됨.

# ## 수도코드만들기



# 일단, 나중에 트리 구성하기 위해 graph를 만들어야함. 아니네 어차피 쓰네.

# graph=[[] 을 노드 최댓값+1개 만들기] :양방향 트리로 만들기 (어차피 체크리스트랑 같이 쓸거라)
# for edges
#     v1,v2 =  엣지1개
#     graph[v1].append(v2)
#     v2에 대해서도 v1으로.

# rightWrong=[[] 노드 최댓값+1개 만들기] : [루트,일반]
    
# for i  graph
#     if (연결 개수가 0이면 ) continue : 일단 불필요 부분 넘기자.
    
#     노드랑 연결된 애들 개수, 노드 번호랑 해서,
#     if (노드 번호가짝 and 연결개수가 짝) or (노드 번호가 홀 and 연결 개수 홀):
#         rightWrong[노드 번호] = [정,역]
#     else
#         rightWrong[노드 번호] = [역,정]
        
# 체크리스트=[False 노드 최댓값+1개]

# answer=[0,0] : [정,역]

# def 트리 탐색(시작지점)
#     트리 구성 노드번호=[시작지점]
#     체크리스트[시작지점] = True ## 엣지발견
#     q=[시작지점]
#     while(q바닥날때까지)
#         현재지점 =q에서 popleft
#         for 다음지점 graph[현재지머]
#             if 다음 지점이 checklist에 Trure면 
#                 continue : 이미 왔다 간거라
#             트리구성.append(다음지점)
#             q.append(다음지점)
#             체크리스트[다음지점] = true
    
#     루트 정 개수=0
#     루트 역 개수=0
    
#     for 구성노드 트리구성노드들
#         루트값 = rightWrong[구성노드][0]
#         if 루트값이 정이면
#             루트정개수+=1
#         else: 루트 값이 역이면
#             루트역개수+=1
    
#     if 루트 정 개수==1
#         answer[1]: 역 +=1
#     if 루트 역 개수==1
#         answer[0]: 정 +=1
        
        

# for n nodes
#     if n이 체크리스트상 False면 
#         트리탐색(n)
        
# return answer
    

        
    
# __ 알고 대충 39분 -> 힘들었는데, 정리할게 좀 있는 듯. 발상 과정    
# __ 수도 대충 58분 
# __엣지 대충.. 체크리스트 처리부분 1개 잡음.. 61분
            
    
from collections import deque
def solution(nodes, edges):
    graph=[[] for _ in range(max(nodes)+1)]
    for v1,v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    ## test
    # print("graph: ", graph)
    rightWrong = [[] for _ in range(max(nodes)+1)] #[루트,일반] - 정:True,역:False
    for i in (nodes):
        connCount = len(graph[i])
        if connCount==0: # 그래프에서 뒤지면 걍 없는 노드랑 홀로 존재하는 노드가 여기서 겹침. -> graph말고 nodes에서 노드번호 찾기: 연결 없으면 홀로 존재.
            if i%2==0:
                rightWrong[i] = [True,True] ## 이거 특수케이스
        if (i%2==0 and connCount%2==0) or (i%2==1 and connCount%2==1):
            rightWrong[i] = [True,False]
        else:
            rightWrong[i] = [False,True]

    chklist = [False for _ in range(max(nodes)+1)]
    answer = [0,0] # 정, 역
    
    # ## tset
    # print("정역: ", rightWrong)
    
    def explore(start):
        chklist[start] = True
        treeEles = [start]
        q = deque([start])
        while(q):
            curN = q.popleft()
            if len(graph[curN])==0:
                continue # 연결된 곳이 없는 홀로 노드
            for nextN in graph[curN]:
                if chklist[nextN]:
                    continue # 와본 곳이라.
                treeEles.append(nextN)
                q.append(nextN)
                chklist[nextN] = True
                
        rightCount=0
        wrongCount = 0
        
        ## test
        # print("start, treeEles: ", start, treeEles)
        
        if(len(treeEles)==1 and rightWrong[treeEles[0]][0] and rightWrong[treeEles[0]][1]):
            ## 1개는 루트가 정 및 역이 아니라 짝수여야 함.
            ## 짝수일 1개이면서 짝수일 때만 True,True발라놨으니 이게 플래그임.
            answer[0]+=1 # 그럼 정이 +=1되어야 함.
            return 
        
    
        for ele in treeEles:
            ## test
            # print("start,ele:",start, ele)
            rootVal = rightWrong[ele][0]
            if rootVal == True:
                rightCount+=1
            else:
                wrongCount+=1
        
        ## 홀로 존재하는 노드는 바꾸는 개념이 아니라 애매하지만, 결과는 맞게 되어서 일단 이대로 둠.->ㄴㄴ 생각해보니 결과가 반대네. 위에서 따로 처리 후 종료시키자 이 경우.
        
        if rightCount==1:
            # answer[1]+=1 # 역으로 바꾸면 역 완성 -> 바꾸는게 아니라 유지하면임.
            answer[0]+=1
        if wrongCount==1:
            # answer[0]+=1 # 정으로 바꾸면 정 완성 -> 바꾸는게 아니라 유지하면임.
            answer[1]+=1
            
        ## teset
        # print("rightCount, wrongCount, answer: ", rightCount, wrongCount, answer)
    
    for n in nodes:
        if not chklist[n]:
            explore(n)
            # continue
                
        
    return answer