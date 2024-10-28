
## 그냥 간단하게 생각하면, 해당 클래스를 사용해서 처음을 정의히ㅏ고 head의 모든 값을 넣어준 뒤,
# 나머지들도, class로 만들면 되지 않나라는 생각이 드는데..
# random은 리스트 다 만들고 다시 순회하며 연결하면 되지 않나..
# 어차피 1000개가 최대고 뭐..

## 하다보니 문제상황을 제대로 알겠음.
## random도 next처럼 할 수가 없는거임. 
##   어차피 노드가 1000개가 맥스라면, 그냥 리스트하나 만들고 노드들 인덱스랑 매치시켜서, 값은 random 포인팅하는 노드 인덱스 값으로 만들어버리면 간단. null도 있으니, -1이면 null로 하든가.
### 근데, 이 방법 제대로 사용하려면 노드마다 객체가 다를테니, 이를 비교하는수밖에 없음.
### 애초에 새로운 노드 만들면서 random값 체크해야 하는데, random값 갔을 때가 몇번째 노드인지 파악 할 수 있나?
### 기존 head로 시작되는 노드들도 인덱싱을 위해 list에 담으면서 체크해야 겠네.
####  이러면 몇번째 노드인지 판단하는데 비용으로 인해 전체 N^2가 될 듯.

class Solution:
   
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
         # Definition for a Node.
        class Node:
            def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
                self.val = int(x)
                self.next = next
                self.random = random
        
        if head==None:
            return None

        newH= Node(head.val);
        newPointer=newH
        pointer = head


        oriList=[]
        
        newList=[]

        while(pointer!=None):
            oriList.append(pointer)
            ## test
            # print("oriRand val: ", pointer.random if pointer.random==None else pointer.random.val)

            newList.append(newPointer)

            if pointer.next == None:
                newPointer.next = None
            else:
                newPointer.next = Node(pointer.next.val)

            newPointer = newPointer.next
            pointer = pointer.next
            
        

        
        newPointer= newH
        pointer = head
        
        while(pointer!=None):
            if pointer.random == None:
                newPointer.random = None
            else:
                
                
                for i in range(len(oriList)):
                    ## test
                    # print("제대로 도는게 맞나?")
                    if oriList[i] == pointer.random:
                        newPointer.random = newList[i]
                        ## test
                        
                        break
                    
            
            newPointer = newPointer.next
            pointer = pointer.next
            

        return newH

        
