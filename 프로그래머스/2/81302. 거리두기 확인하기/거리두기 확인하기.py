# 맨해튼 거리가 1과 2만 피하는 상황이면 되는거잖아?
# 1인 상황은 4가지 경우 -> 파티션이 의미가 없음.

# 2인 상황은 4(1+1)+4(2+0or0+2) 임. -> 파티션이 의미가 있음. 1+1상황은 2개가 필요, 2+0과0+2는 1개로 충분.

# 내가 상대에 비해 |1|+|-1| 이라면(y,x), 

# xp
# 나x => 나의 (-1,0)과 (0,+1)에 칸막이가 있어야 함. (dy,dx로 봤을 때)


# 내가 상대에 비해 |-2|+|0|이라면(y,x),

# 나
# x
# p   => 나의 (+1,0)에 칸막이기ㅏ 있어야 함.


# 즉, 각 p들은, 다른 모든 p와 맨해튼 거리를 계싼,
# 거리가 1이 존재하면 바로 0을 반환
# 거리가 2가 존재하면, 위의 두 경우로 칸막이의 위치를 확인.
#   칸막이 위치 확인할 때, 범위 밖 고려할 필요는 없어보임.
    
    
# ### 수도코드만들기

# def guri(pPos,place):
#  for pos in pPos
#     for otherP in pPos:
#         맨해튼 raw y, raw x (pos-otherP)
#         if 둘다 (abs씌우고 합하니)0이면 자기 자신이니 continue ->필요 없는 코드긴 하지만.
#         elif 둘다 abs 씌우고 합하니 1이라면 return 0
        
#         elif abs씌우고 합하니 2라면
#           if raw y의 abs랑 raw x의 abs가 1,1이라면,
#             posY+ raw y*-1,posX+0과 posY+0,posX+ raw x*-1에 모두 "X"존재하지 않다면 return 0
#           else: (2+0이거나 0+2)
#             if raw y의 abs가 2라면
#               posY+ raw y* -1/2,posX+0에 "X" 존재 안하면 return 0
#             else: (raw x으 ㅣabs가 2인거)
#               posY+0, posX+ raw x* -1/2 에 "X" 존재 안하면 return 0
#   return 1 (모두 넘겼으니)

# answer=[]
# for place in places
#   pPos=[] 여기에 (y,x)로 "P"위치를 다 저장하기
#   for i place
#     for j place
#       pPos채우기
#   answer에 guri(pPos,place)결과 append하기
  
    
# __ 알고 대충 14분
# __ 수도 대충 27분
# __ 엣지 알고상은 없고, 수도 상으로도 없어보이는데 28분
###   3개틀림 44분... 엣지케이스가 있나? 이해가 안가네. 그냥 구조적으로 없을 것 같은데
###     수도상 엣지였음. 질문하기보고 깨달음. (60분) 파티션이 하나라도 없으면 틀리는건데, 모두 없어야로 했음...

def solution(places):
    answer = []
    
    def guri(pPos,place):
        for pos in pPos:
            for other in pPos:
                # pos - other
                rawDy = pos[0]-other[0]
                rawDx = pos[1]-other[1]
                manhatnD = abs(rawDy)+abs(rawDx)
                if manhatnD ==0 or manhatnD>2:
                    continue
                if manhatnD==1:
                    return 0
                ## 맨해튼 거리 2인 것들
                
                #### test
                # print("int(0.5*rawDy), int(0.5*rawDx): ", 0.5*rawDy, int(0.5*rawDy), 0.5*rawDx, int(0.5*rawDx))
                
                
                if abs(rawDy)==1 and abs(rawDx)==1:
                    if place[pos[0]-rawDy][pos[1]]!="X" or place[pos[0]][pos[1]-rawDx]!="X":
                        return 0
                elif abs(rawDy)==2: # and abs(rawDx)==0이어야함
                    if place[pos[0]-int(0.5*rawDy)][pos[1]]!="X":
                        return 0
                else: ## abs(rawDx)==2이고, rawDy절대값은 0이어야함
                    if place[pos[0]][pos[1]-int(0.5*rawDx)]!="X":
                        return 0
        return 1
    
    for place in places:
        pPos=[]
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j]=="P":
                    pPos.append((i,j))
        
        res = guri(pPos,place)
        answer.append(res)
    
    
    
    return answer
