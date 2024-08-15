# ## 약간 dp처럼, 1큐에 체크하는 느낌으로 보면,

# dp를 dict로 만들어서, 
# numbers하나씩 훑어가면서 처음 보는 숫자면 dict의 키 만들고 -1로 초기화 시키기.

# 이렇게 해도 각 자리마다 큰거 못찾은 애들 다 뒤져가면서 지금 위치의 값과 비교해야 하잖아?
# 이런 반복작업을 없애는 방법이뭐가 있을까 생각해봤는데..


# 걍 1차적으론 크기로 sort, 2차적으론 index로 sort하면 될 듯.
# 이러면 누구 뒤에(같은 값을 제외하고) 다음 큰 값을 알아낼 수 있는데,
# 문제는 이러면 2번째 예시에서 1,2...이 순서대로 정렬해서 틀린 결과가 나올 듯.

# 그럼...

# 비교값을 들고다니는 전략
#     인덱스 전진마다, 처음엔 비교값=처음값, 다음 인덱스 값이 비교값보다 작으면 비교값으로 교체.
#     비교값보다 크면 해당 인덱스에 대해선 결과 찾은 것.
#     너무 근시적으로 해결하게 됨. 2번째 예시 맨 뒤에 10만 붙여봐도..
    
#     이거 좋을수도? 비교값을 계속 들고 있으면 되잖아. 근데, 비교값이 항상 정렬되어있어야 하니까,
#     heapq를 사용하면 될 듯. 항상 그들 중 최솟값이 먼저 나오도록.
#     이러면, 비교값들(내가 들고 다닐 애들) 중 최소값 pop시켜서 보고, 현재 값이 비교값보다 크면 또 pop시켜보고
#     작으면 다시 push로 넣어주면 됨.
#     heap에는 (값, 인덱스) 이렇게 넣고 다녀야 겠네.
    
#     이러면 비교값이라기보다나ㅡㄴ, 답을 못찾은 값들을 들고 다니는거임.
#     이거는 그러면 인덱스 전지마다 항상 해당 인덱스 값을 추가해서 들어야 함.
    
#     빈 리스트에 (numbers랑 동일 크기) 이 결과(인덱스)들을 써두면, 
    
#         result[idx]=value라고 할 때, value가 뒷큰수가 되도록 하자. answer랑 같도록
#         즉, heap들고다니다가 뒷큰수 인덱스에 도착했을 때 pop한 값의 idx에 뒷큰수의 값을 넣자.(result에서), 없으면 -1 넣기 
#         -1은 못찾았을 때 저렇게 놓기로 하자 -> 초기화
    
#     result에서 
    
# ## 수도코드

# result=[-1로 numbers크기만큼. 초기화]
# waiting=[numbers의 첫번째 요소로 (값, 인덱스:0) 넣기]으로 heap으로 사용할 리스트. -> minheap으로 할거임.

# for i  numbers의 1th~끝까지
    
#     while(waiting): waiting이 남아있다면
#         # numbers[i]값이 크면 계속 꺼내야 함.
#         possV, possI = waiting에서 heappop
#         if possV>numbers[i]라면
#             result[possI] = numbers[i]
#         else:
#             다시 꺼낸거 heappush로 줍기
#             반복 종료
    
    
        
#         -----밑에 무시-----
# #     possV, possI = waiting에서 heappop해서 가장 작은 값 꺼내보기
# #     if numbers[i]가 possV보다 크면
# #         result[possI] = numbers[i]: result에서 꺼낸 값의 인덱스에 현재 값 넣기
# #     else: 작거나 같으면
# #         다시 꺼낸 거 주워담기 heappush
#         ---------

#     waiting에 현재 (값, 위치)를 heappush
    
    
#     2,3,2,3,2라면..
#       2 3 23 233
#     1-1-1-1-1
#     __ 알고 28분
#     __ 알고 수정 34분
#     __ 예제 틀려 알고 수정 56분 완료
#     __ 성공 57분
    
    
    
# 시간 복잡도는 NlogN으로 보긴 했음.



import heapq
def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    waiting=[(numbers[0],0)]
    
    for i in range(1,len(numbers)):
        while(waiting):
            
            possV, possI = heapq.heappop(waiting)
            ## test
            # print("i,possV, possI",i, possV, possI)
        
            if numbers[i]>possV:
                answer[possI] = numbers[i]
            else:
                heapq.heappush(waiting, (possV, possI))
                break
        ## test
        # print("answer, waiting: ", answer, waiting)\
        
        heapq.heappush(waiting, (numbers[i],i))
    
    
        
        
    return answer