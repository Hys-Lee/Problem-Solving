# 근데, 무적권을 적이 가장 많을 때 쓰면 되는거아님?
# 어차피 E[0]~E[i]까지의 합이 n을 넘어섰을 때 종료니까, 
# 최대한 병사로 막은 E[~~]의 합이 적으면 되자너.
# 근데, 라운드가 엄청 많아서 적이 훨씬 많다면,
# 무조건 적이 가장 많을 때 쓰면 안됨. 애초에 거기까지 못갈수도 있으니.

# 최대 i까지 갔을 때, 0~i번째 중 그들 중 큰 애들에 무적쓴다 치면,
# 가능하면 i++아니면 중단 시킨다고 치면,
# =>이대로하면 O(백만^2)임.


# 전체 중 큰값부터 체크해서 무적권 쓴다고 체크 되어있다고 할 때, 
# 맨 뒤부터 하나씩 빼가면서, 가능한 지점이 생기면 그 때가 최대 길이일 것.
# 하나씩 빼면서 무적권 제외한 합이 n보다 작아지는지 체크 (전체에서 이미 가능하면 전체 길이. 아니면 작아진 순간을 길이로.)
# 뺄 대상이 무적권 대상일 경우, 얘 빼고, 다른 비무적권이었던 애들 중 가장 큰놈을 무적권으로 해서, 해당 값을 또 제외합에서 제외한 결과랑 n이랑 비교.

# 이를 위해서는, enemy의 (적 수, 무적권여부 ,원래 위치)로 하는 리스트를 만들고, 얘를 sort, reverse해야 함.
# 그다음에 나중애 O(1)로 참조할 수 있도록, enemy랑 위 리스트랑 연결하는 maplist만들기(enemy길이만한.)
# 여기서 최소 무적권 위치를 저장하는 minP라는 포인터로 위치 저장.
# 위 리스트를 돌면서 maplist[원래위치]에 인덱스 값을 저장시키기.

# enemy에 대해 maplist로 정보리스트에 접근해 적의 수랑 무적권 여부를 판단하기

# 이렇게 앞에서부터 k개를 무적권 사용(True)로.
# 나머지들의 합을 저장. (culSum으로.)
# 이후에 enemy에 대해 맨 뒤에서부터 시작해서 처음 방향으로 전진하면서,
# enemy[i]가 무적권이면 얘를 무적권 제외하고, minP를 한칸 아래로 맞춰서, 걔를 무적권으로 지정. (만약, 얘가 이미 i보다 큰애라면 이미 제외된 애니까 넘기고 한칸 더 아래로 내리면서 가능한 애를 무적권으로.)
#   이렇게 지정된 새로운 무적권의 값과 enemy[i]값을 culSum에서 빼서 업뎃.
#   culSUm이 n보다 작아졌다면 i를 반환. 아니라면 다음번을 기약
# enemy[i]가 무적권이 아니라면, 얘를 culSum에서 빼서 없뎃
#   culSUm이 n보다 작아졌다면 i를 반환. 아니라면 다음번을 기약

# O(enemy길이)=>100만단위로 본다.
    
# ## 수도코드

# dataList=[]
# for i enemy길이만큼
#   dataList에 (enemy[i], False, i)를 append

# dataList.sort()
# dataList.reserve() ## 적 수의 내림차순으로 정렬

# mapList=[-1로 enemy크기만큼 초기화]
# for i dataList에 대해
#   dataList[i]의 원본위치값([2])에 대해 mapList[원본위치값]=i로 매핑

# minP=0
# for i k만큼 반복([0,k-1])
#   dataList[i]의 무적권을 True로 
#   minP+=1 ## minP위치가 마지막 무적권(그중 최소인) 위치를 나타내는지 확인.
# culSum=0
# for i [k,dataList의 길이-1]
#   dataList[i]의 적수[0]을 culSUm에 +=


# for i [enemy길이-1,-1,-1] :뒤에서부터 반대방햫ㅇ으로 가면서,
#   ## 만약 i번째 대해서 아무것도 안해도 된다면
#   if culSUm이 n보다 작다면 
#     ret i+1 (길이니까)
#   # else: 아니면, 뭔가처리를 하기.


#   if mapList에 enemy[i]위치 찍어서 얻은 정보에서 무적권이 False면 (일단 i번째는 치우기)
#     culSum-= 해당 정보의 적수
#   else: mapList에 enemy[i]위치 찍어서 얻은 정보에서 무적권이 True면 (일단 i번째는 치우기)
#     해당 정보에서 무적권을 False로
#     minPsI=minP
#     for [minPsI,dataList길이-1]:
#         if minP에서 정보대해 원본위치값이 i보다 작다면
#           break
#         else: minP에서 원본 위치값이 i보다 크거나 같다면 (i번은 버리기로 정해진거니)
#           minP-=1 # 1칸 내리기
            
#     minP위치에 있는 정보의 무적권을 True로 새로 지정 : 새로 찾은 valid한 위치
    
#     culSum에 enemy의i번째에 대한 적의 수를 --, minP위치에 있는 적의 값을 --
    

    



# __ 알고리즘 31분
# __ 수도 대충 50분
# __ 엑지 53분(큰틀은 맞는 듯)
# __ 90분 실패. (런타임 에러도 있음.)
# __ 98분 런타임 에러만 남음.  14번 22번
# __ 106분 포기. => k가 enemy개수보다 클 경우....
# ㄴ> 엣지 케이스를 제대로 못 본 것.
#    가능한 경우를 다 따졌어야 함. -n이 enemy전체 합보다 클 경우,
#                                    - k값이 enemy개수보다 클 경우
#                                     - 작을 경우
#                              -n이 더작을 경우
#                                    - k값이 enemy개수보다 클 경우
#                                     - 작을 경우
#                               ㄴ> 최소 이거는 엣지 케이스에 포함되어있었어야 함. 


def solution(n, k, enemy):
    
    dataList=[]
    for i in range(len(enemy)):
        dataList.append([enemy[i], False, i])

    dataList.sort()
    dataList.reverse() ## 적 수의 내림차순으로 정렬
    ## test
    # print("dataList, enemy: ", dataList, enemy)

    mapList=[-1 for _ in range(len(enemy))]
    for i in range(len(dataList)):
        mapList[dataList[i][2]] = i
    
    ## etst
    # print("mapList: ", mapList)

    minP=0
    for i in range(k):
        if i>=len(dataList): ## k가 enemy개수보다 클경우
            break
        dataList[i][1] = True
        minP+=1
    ## test
    ## minP위치가 마지막 무적권(그중 최소인) 위치를 나타내는지 확인.
    # print("minP, 시작 dataList, ", minP, dataList)
    
    culSum=0
    for i in range(k, len(dataList)):
        culSum+=dataList[i][0]
    
    ## test
    # print("초기 culSum: ", culSum)
    
    ## test
    # print("이거 i번째 enemy의 무적권 정보맞나?: ", i,dataList[mapList[i]],dataList[mapList[i]][1] )
    
    for i in range(len(enemy)-1,-1,-1):
        if culSum<=n:
            ## test
            # print("끝날 때 culSum, n, i, dataList: ", culSum, n, i, dataList)
            return i+1
        
        if not dataList[mapList[i]][1] :
            culSum-=dataList[mapList[i]][0]
            ## test
            # print("무적권이 아닌 경우: ", i, culSum)
        else:
            dataList[mapList[i]][1] = False
            minPsI=minP
            for j in range(minPsI, len(dataList)): # 다음 minP부터시작이라.
                ## teest
                # print("i,minP, dataList[minP]: ", i, minP, dataList[minP])
                # if not dataList[minP][1] and dataList[minP][2]<i:
                minP=j
                if not dataList[j][1] and dataList[j][2]<i:
                    
                    break
                # else:
                #     minP+=1
                
            ## test
            # print("찾은 새로운 minP: ", minP) ## 이거 무조건 확인해봐야함.
            
            dataList[minP][1] = True
            ## test
            # print("minP에서 True한 dataList: ", minP, dataList)
            
            # culSum-=enemy[i]
            # ## test
            # print("현재 i위치의 값을 culSum에서 빼면(이번이 무적 아니었을 때): ", i, culSum)
            
            culSum-=dataList[minP][0]
            ## test
            # print("새로 무적권 쓴 위치의 값을 culSUm에서 빼면: ", dataList[minP][2], culSum)
            
            
    
    # answer = 0
    # return answer