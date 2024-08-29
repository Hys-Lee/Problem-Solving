def solution(users, emoticons):
    scenario=[]
    def dfs(partOfS):
        discounts=[10,20,30,40]
        if len(partOfS)>=len(emoticons):
            ## test
            # print("종료, 기존시나리오들: ",scenario)
            scenario.append(partOfS)
            ## test
            # print("시나리오: ",scenario)
            return
        
        for d in discounts:
            newS=[d]
            newS.extend(partOfS)
            # newS.append(d)
            ## test
            # print("다음 단계로, newS", newS)
            dfs(newS)
    
    dfs([])
    ## test
    print("시나리오 크기: ",len(scenario)) ## 각 시나리오 라인 새로 만들어서 넣어줘야 하는 듯.
    # print("시나리오: ", scenario)
    
    
    ## test
    # scenario = [[0.4,0.4,0.2,0.4]] if len(emoticons)==4 else [scenario[0]]
    # print("시나리오: ", scenario)
            
    answer = []
    for i in range(len(scenario)):
        partialA=[0,0]
        indiPrices=[0 for _ in range(len(users))]
        for j in range(len(users)):
            
            for k in range(len(emoticons)):
                ## test
                # print("유저, 시나리오", users[j][0], scenario[i][k]*100)
                if users[j][0]<=scenario[i][k]:
                    indiPrices[j]+=emoticons[k]-emoticons[k]*scenario[i][k]//100
                    ## test
                    # print("만족하는 이모, 할인: ", users[j], scenario[i][k], indiPrices,j)
                    if indiPrices[j]>=users[j][1]:
                        indiPrices[j] = 0
                        partialA[0]+=1
                        ## test
                        # print("j번째", j, indiPrices)
                        break
                ## test
                # print("k번째 이모지 대한 j번째 사람의 비용: ", k,j,indiPrices[j])
        partialA[1] = sum(indiPrices)
        ## test
        # print("i번재 시나리오에 대한 결과: ", i, partialA)
        answer.append(partialA)
    
    answer.sort()
    ## test
    print("모든 시나리오 대한 결과들: ",answer)
    return answer[-1]
                
                    
                        
    
    # return answer