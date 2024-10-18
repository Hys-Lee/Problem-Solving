# 메인 컨베이어는 queue
# 보조는 stack인데

# 실제로 구현해서 진행하면 될라나?
# 아니면 계산?

# 상황이 복잡하진 않아서 실제 구현하면 뇌 빼고 걍 해도 됨.
# 최대 공간복잡도도 O(백만)임.

# 궁금한게, q에서 빠져나온걸 다시 q에 넣을수도 있나? => 이러면 안되는게 없으니까 이 방법은안될듯

# 그러면 시간복잡도를 봐도, 백만단위라 걍 하면 되나본데.

# 그렇다면..

# q에 일단 1~order길이 이하의 수들을 모조리 넣어놔야함.

# 각 order차례마다
#     q랑 stack에서 가능한 친구 찾기.
#     없으면 q에서 stack에 빼와서 반복.
#     q에서 더 없으면 종료
    
# ## 수도코드만들기

# 1.자료구조 세팅
# 3.q:=deque로 큐 만들기1~order길이만큼 채우기
#   stack:=리스트로 스택 만들기 빈스택
#   orderI=0 : 넣은 물건 수 겸 현재 order에서 고려되늰 index
# 1.order순서따라 돌리기 iter수 세는 변수 필요 - 종료 세팅해서
#    q에서와 stack에서 후보자 보기.
#     두 후보자중 타겟대상이 있으면 그거 뽑아내기.
#         다음 대상으로 넘어가기
    
#     타겟 대상이 없다면
#       q에서 하나 뽑아서 stack에 보내고, q의 새 후보자랑 타겟대상이랑 비교
#       위를 반복.


# 2.while orderI가 order최대인덱스까지가능,q와 stack모두 비지 않는한 가능
#   3.다음 stack에 넣을 것 임시저장소 []로 초기화해야겠다.
#   3.if q가 비지 않았따면
#       q에서 꺼내보고, 
#       order[orderI]랑 맞으면 그냥 버리기, orderI를 +=1
#       order랑 안맞으면 임시저장소에 넣기
#   3.if stack비지 않았다면
#       stack의 최상단이 order[orderI]랑 맞다면 pop, orderI를 +=1
#       아니라면 냅두기
#   임시저장소에 뭐가 있으면 stack에 넣기. (길이 0보다 크면)

# 2.orderI를 반환
  

# 3.for box order에서: 박스 넘버로 체크
#   2.종료결정위한변수(큐 상태 및 스택 상태) - 못가져올 때 False하기
#   qok:=True
#   stok:=True
#   2.큐 상태 체크
#   3.if 큐에서 더 꺼낼게 없거나 원하는게 없는 경우 qok:=false
#   3.else 여기서 찾는게 나오면 큐에서 popleft,  
  
#   2.스택 상태 체크
#   3.if 스택ㄱ에서 더 꺼낼게 없거나 우너하는거 없능ㄹ 때 이번분기 넘긱기 stok:=False
#   3.else 여기서 찾는게 나오면  stack에서 pop
  
#   2.종료결정: 큐와 스택에서 모두 원하는거 못가져오는 경우
#   if qok와 stok중 모두 False면 (큐나 스택 한쪽에만 있으니)
#     return count
#   count+=1 :공통작업
    
# 1.count를 반환 : 전체 성공 케이스




    
# __ 알고리즘 13분
# __ 수도코드 27분->수정 33분
# __ 엣지 - 따깋 없음.


from collections import deque
def solution(order):
    q=deque([i for i in range(1,len(order)+1)])
    stack=[]
    orderI=0
    while(orderI<len(order) and (len(q)>0 or len(stack)>0 )):
        if len(q)>0 and q[0]==order[orderI] :
            q.popleft()
            orderI+=1
            continue
        elif len(stack)>0 and stack[-1]==order[orderI]:
            stack.pop()
            orderI+=1
            continue
        
        # while (len(q)>0):
        if len(q)>0:
            stack.append(q.popleft())
        if len(q)==0 and len(stack)>0:
            break
            
        
            
#         ## test
#         print("orderI, len(q),len(stsack: ): ", orderI, len(q),len(stack))
#         tmpstore=[]
#         if len(q)>0:
#             target = q.popleft()
            
#             ## test
#             print("q,target,order[I]: ",q,target,order[orderI])
#             if order[orderI]==target:
#                 orderI+=1
#                 continue
#             else:
#                 tmpstore.append(target)
#         if len(stack)>0:
#             ## test
#             print("stack,order[I]: ",stack,order[orderI])
#             if stack[-1]== order[orderI]:
#                 stack.pop()
#                 orderI+=1
#                 continue
#         ## test
#         print("q,tmpstore: ",q,tmpstore)
#         if len(tmpstore)>0:
#             stack.append(tmpstore.pop())
    
    
    return orderI