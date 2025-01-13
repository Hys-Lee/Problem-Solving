# 이거 그래프 중에, 자기한테 꽂히는 애들 개수 카운트해서
# 0개부터 없애면서 꽂히는 개수 줄이면서 하는거

# numCourses개수만큼 back=[0 for 넘코스개수]로 초기화 (0번부터 시작하니까)

# prerequisities는 엣지 만드는데 사용하는거니까,
# 이거로 graph만들면서 전형적으로. 동시에, 하나하나에 대해 back에 자기한테 꽂히는 애들 개수 카운팅하기

# 최대 4백만번이면 끝날 듯?
# (노드 하나 없애면서 back들 처리 한번하는데 2천번. 이를 노드마다 처리하니..)

# 즉, for루프 2개로, 노드와 연결된 다른 ㅗㄴ드들은 그래프를 통해. 한번 back이 0이 있어 얘 대해 조질 때마다 back길이만큼 반복시키는거고.
# 만약에 back에 0이 존재하지 않으면 false를 반환.
# 결국 모든 back의 값들이 전부 0이라면 true를 반환.(따로 떨어진게 있어도 얘들은 back이 0일거니까 혼자 존재하면.)

# #### 수도코드만들기

# back = [0 for 넘코스 크기만큼]
# graph=[[]for 넘코스 크기만큼] # 얘도 0부터 시작하니까
# for last,first 프리리퀴짓
#    graph[first]=last  (first->last로)
#    back[last]+=1

# # back에서 0찾기
# # back전체 돌면서 얘로부터 연결된 놈들 graph에 찾아서 전부 -=1 하기
# # ㄴ> 이 2과정은 대충 7000따리임. 엣지 개수가 5000개라.

# # 위 과정을 back크기만큼 반복

# # 따라서..


# for back크기만큼

#   for j in range(len(Back))
#     if back[j]가 0이라면,
#       for 타겟노드 in graph[back]:
#         back[타겟노드]-=1

# zerocount=0 # 따로 떼어내서 체크 위에서 안해도, zero없으면 아무것도 안하는거니
# for i back크기만큼
#   if back[i]에 0이면 zerocount+=1
# if zerocount가 back크기만큼이라면
#     return true
# else # 다른 모든 경우는 false임. 0이 하나도 없든, 0이 일부만 있든.
#     return false







# __ 알고 대충 7분
# __ 수도 대충 21분
# __ 엣지 없는듯 23분



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        back=[0 for _ in range(numCourses)]
        graph=[[]for _ in range(numCourses)]
        chklist=[False for _ in range(numCourses)]
        for last, first in prerequisites:
            graph[first].append(last)
            back[last]+=1
        
        ## test
        # print("back, graph: ", back,graph)

        ## 그러네.. 엣지 체크를 제대로좀하지 귀찮더라도.. 보니까, 0인부분은 계속 처리가 되네.
        ## 체크포인트처럼, 이미 처리한 곳은 따로 처리해야겠다.
        for i in range(len(back)):
            for j in range(len(back)):
                if back[j]==0 and chklist[j]==False:
                    chklist[j]=True
                    for t in range(len(graph[j])):
                        ## test
                        target = graph[j][t]
                        # print("i, target", i,target, graph[j], len(graph[j]))
                        back[target]-=1
        ## test
        # print("back: ", back)
        zCount=0
        for i in range(len(back)):
            if back[i]==0:
                zCount+=1
        if zCount==len(back):
            return True
        return False
        