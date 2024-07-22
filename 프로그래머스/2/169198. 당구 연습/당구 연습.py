# 일단 (최대 가능한)4가지 방법 중에서 최소를 고르면 되는거임 
# 각 방법의 거리를 계산하는 방법은 어렵지 않아보임
#     1. 면에 부딪힐 때 == 상대 공과 내 공이 map과 평행(가로,세로)하지 않을 때:4, 평행할 때:2
#         - 평행
#             - 나와 상대가 x축에 평행
#                 y축 벽면과 부딪
#             - y축에 평행
#                 x축 벽면과 부딪
            
#         - 안 평행
#             모든 면과 부딪
#         => 내 좌표를 map밖으로 대칭이동시켜(부딪히는 면 대해)
#             해당 지점과 상대 위치의 거리제곱 구하기
            
#     2. 꼭지에 부딪힐 때 == 상대 공이 꼭지~내공 직선상에 있을 때 면+"추가로" 체크해봐야 함.
#         --> 직선상에 있는지 체크 => 꼭지점~나, 꼭지점~상대 기울기가 같을 때.
#         => 나를 꼭지대해 원점대칭 후 상대까지 거리제곱 구하기
    
#     대충 정리하면 8가지를 체크해야 함(면4 + 꼭4)
#     얘네 중 최소값을 array에 담기.
    
#     이러면 8*1000 이게 다일 듯?
    
#     걍 구현문제느낌.

# ## 수도코드

# #꼭지점 좌표 구하기
# (0,0),(m,0),(m,n),(0,n):좌하, 우하, 우상, 좌상  (x좌표, y좌표)
# 각 ball대한 최소거리 ballDist=[]초기화

# 가능한 거리 arr=[] 초기화
# #면 생각해서 계산하기
# 위의 알고리즘 그대로
# # 꼭지 생각해서 계산하기
# 위의 알고리즘 그대로

# # 최소 거리 찾기
# 최소거리 min으로 찾기

# # ballDist에 추가하기

# # 다 하고 ballDist리턴하기


def solution(m, n, startX, startY, balls): # 가로m,세로 n
    ## 꼭지점 구하기
    corner=[(0,0),(m,0),(m,n),(0,n)] #:좌하, 우하, 우상, 좌상  (x좌표, y좌표)
    
    ballDist=[]
    
    for ball in balls:
        bx=ball[0]
        by=ball[1]
        possibleD=[]
        
        # 면
        if (startX!=bx): ## 위아래 면은 사용 가능
            yUpFlip=n+(n-startY)
            possibleD.append(abs(startX-bx)**2+abs(yUpFlip-by)**2)
            
            yDownFlip = -1*startY
            possibleD.append(abs(startX-bx)**2+abs(yDownFlip-by)**2)
            
            ### 나랑 더 가까운 좌우 중 하나 벽에 바운스 (일직선)
            if(startY==by):
                if (startX<bx): # 좌측 벽에 바운스
                    xLeftFlip = -1*startX
                    possibleD.append(abs(xLeftFlip-bx)**2)
                else:
                    xRightFlip = m+(m-startX)
                    possibleD.append(abs(xRightFlip-bx)**2)
            
        if (startY!=by): ## 양옆 면은 사용 가능
            xLeftFlip = -1*startX
            possibleD.append(abs(xLeftFlip-bx)**2+abs(startY-by)**2)
            
            xRightFlip = m+(m-startX)
            possibleD.append(abs(xRightFlip-bx)**2+abs(startY-by)**2)
            
            ## 나랑 더 가까운 상하 중 하나
            if startX==bx:
                if(startY<by): # 아래벽에 bounce
                    yDownFlip = -1*startY
                    possibleD.append(abs(yDownFlip-by)**2)
                else:
                    yUpFlip=n+(n-startY)
                    possibleD.append(abs(yUpFlip-by)**2)
                
            
        ## test
        print("면추가후: ",possibleD)
        
        # 꼭   ---> 모든 꼭지가 아니라, 0쿠션 되는 상황은 피해야함.=>기울기같+나->꼭과 나->상대 방향 달라야. 즉, 꼭지가 아니라 나를 기점으로 벡터 비교하는게.. (-1곱한게 같아야하니.)
        for corn in corner:
            cx,cy = corn
            # if ((cy-startY)/(cx-startX) == (cy-by)/(cx-bx)) :
            # 슈바 x나 y중 하나만 좌표 같을수도 있는데, 이러면 기울기 볼 수 없자너.
            if (by==startY or bx==startX): continue
            if ((cy-startY)/(cx-startX) == -1*(by-startY)/(bx-startX)) :
                # 벡터로 계산
                cornerFlipX = cx+cx-startX
                cornerFlipY = cy+cy-startY
                
                possibleD.append(abs(cornerFlipX-bx)**2+abs(cornerFlipY-by)**2)           
        print("꼭추가후: ", possibleD)
        
        # 최소
        
        ballDist.append(min(possibleD))
        
        ##test
        # print("ballDist중간, ball", ballDist, ball)
    ## test
    print("ballDist결과: ", ballDist)
    
    return ballDist


## 테케를 봤는데, 면에 부딪힐 때도, 같은 y축이라면 3번의 경우가 가능함.
    ## 상대보다 가까운 면에 바운스 시켜도 되자너...