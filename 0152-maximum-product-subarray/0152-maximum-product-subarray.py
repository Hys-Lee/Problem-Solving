# 걍 dp아님?
# an은 an-1과 곱했을 때 an-1보다 커진다면 곱하고, 아니면 그냥 자기자신(inputn[n]).
# -> 이런 dp array에서 max값 뽑으면 product결과가 나오겠지.
# 시간복잡도는 O(N)일거고.

# 엣지가 있나? 원소 개수가 1개라면, 그냥 그 원소를 반환하면 됨. (an-1을 모르니까 이러면.)
# 그렇다고 0번째를 비우고 1로 만들면 그것도 안됨. 음수원소가 있을경우 1이 나와버리니까.
# 첫 인덱스 처리는 따로 해야겠네. (an-1이 없으니 그냥 자기자신으로.)

# 음수들만 나올 때->이러면 위의 알고리즘 못쓰지 -2-2-2-2...이러면, 짝수개만 곱하면 되는데,
# 위 알고리즘대로라면 그냥 홀수번째에서 멈출거자너.

# 음수일 때만 다르게 보면 되나?
#     ㄴ> 음수를 만나면, 나까지 곱했을 때 음수라면 ->다음 값이 음수라면 걍 곱하고, 아니면 자기자신.
#                         양수라면 위의 첫 알고리즘과 같은 원리네.

#         ㄴ> 이대로면, 다음 값을 알아내야 함.
#         그러면 마지막 인덱스라면, 나까지 곱했을 때 음수라면 걍 자기자신, 양수라면 첫 알고리즘대로.
    

# 혹은, 당장은 줄어드는데, 그냥 쭉 가보면 더 큰 경우?
#     앞에서 100만들어놨고, 이후 0.1 그 다음에 2가 등장한다면, 0.1만났다해서 끊으면 손해임.

# 그러면 자기까지 연결한거랑 자기에서 시작한거 둘다 들고 있으면?
#     문제가 어디까지 줄어드는지 모르니까, 이러면 다 들고 있어야 하는데, 이러면 한칸 전진마다 고려할 개수가 개많아짐

# 그러면 전진할 칸을 간추리자-> 줄어드는 애는 줄어드는 애들끼리 미리 곱해두는거임.

# 앞에서부터 순차로 하면 나름 정리 될 듯? -> 새로운 정리된 nums를 만드는거.
# 1이상 양수끼리 만나면(이전과 현재) 곱해두기
# 0~1사이 양수 만나면 (이전과 현재) 곱해두기  => 이 경우 없음.
# -1~0사이 음수도 위와 같이 처리한다면, 2개씩 짝지어져서 0~1사이 양수 됨.  => 이 경우 없음.
# -1이하 양수끼리도 위와 같이하면, 2개씩 짝지어져서 1이상 양수됨.
# ---- -> 이 결과 남은 음수들은 1개씩이 되겠지. 얘네는 무조건 피해야 하고.

# 방금의 정리를 한번만 더 하면 줄어드는 애들은 음수, 0~1양수 2개로 분류되어 1칸씩 차지하게 됨.
# 그러면 0~1과 음수가 번갈아 나오면..? -> 좋을수도 있짜너..
# 0~1사이가 없어도,
# 음수 양수 반걸아 나오면 좋을수도 있거든요.
# 그럼, 음수, 양수, 0으로 분류하면 될거고,
# 0을 기준으로 무조건 끊기기는 함.
# 0을 기준으로 끊어서, 각각의 내부에서 음수가 짝수가 되게끔 묶어보면 될 것 같은데
# 짝수개가 되게하면 무조건 값은 커지니까.
# 다만 이러면 음수가 홀수개일 때, 외쪽끝까지를 포함시킬지, 오른쪽끝까지를 포함시킬지 정해야 하지.
#     이거는 해당 양쪽 끝부터 각각 가장 가까운 음수 만날 때까지의 곱이 큰쪽으로 결정하면 됨.
#         나머지 가운데 부분은 공통일테니.

# ㄴ> 이게 맞는거 같은디... 그냥 저런 결과들을 다 array에 모아서 max값 뽑아내면 되니까..



# 2차원 dp? -> 이럴리 없음. 일단 또다른 기준으로 둘 애가 없고, 인덱스로 또 두면 1억번이라 초과됨.

# 이전 값이랑 

# #### 수도코드만들기
# 원소가 1개면 원소 반환.
# nums를 0으로 끊어서 0없게 만들어 nzNumArrs로 만들기
# archive:=[] (부분 곱 저장)
# 각 리스트에서 음수 개수 카운팅하기
#     만약에 0이나 짝수다 -> 전체 곱 때려서 archive에 저장
#     음수 개수가 1개라면 (원소 2개이상)
#         해당 음수 기준으로 쪼개서 양쪽의 곱을 archive에 각각 넣기
#     홀수다  (음수가 3개 이상일 때 가정이긴 함.) => 키야 내 수도나 알고 보고 어떤 가정에서 진행했는지체크해서 알아냄
#         양쪽 끝 ㅇㅡㅁ수 위치 체크 - left, right
#         left와right미포함 사이 곱 계산 := 공통부분
#         첫인덱스~left포함 곱과 공통부분 곱 archive에 넣기
#         right포함~마지막인덱스 곱과 공통부분 곱 archive에 넣기   (걍 archive에서 한번에 판단하게)

# archive에서 max가 정답임.



# _ 알고 대충 33분
# _ 수도 대충 38분
# - 엣지 -> 원소가 1개면 걍 원소 반환. 음수 홀수개에서 1개라면? ->  40분
## ㄴ> 엣지 또 체크 못한게, 0이 제일 큰거일 수도 있음..
## 다른 엣지도 있었음. 내 알고리즘은 nzNums원소개수가 여러개 가정이라 1개일 때 추가해야했음.
#### 이렇게 엣지가 많고 고려 케이스가 많으면 보통 알고리즘 잘 못 선택한건데..

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        zeroIs=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeroIs.append(i)
        nzNumArrs=[]
        archive=[]

        for i in range(len(zeroIs)):  #앞에서 이번 i까지를 끊자. 마지막 i에서 끝까지는 for이후에
            if i==0 : ## 여건 첫번째 0위치를 고려하지 않았네.
                nzNumArrs.append(nums[:zeroIs[i]])
                continue
            nzNumArrs.append(nums[zeroIs[i-1]+1:zeroIs[i]])
        ## test
        # print("ZeorIos: ", nzNumArrs)
        if len(zeroIs)>0:
             ## 0이 있다면 archive에는 하나 넣어줘야함.
            archive.append(0)

        # 0이 nums맨 마지막에 있어서 빈리스트를 넣지 않도록 하기
        if len(zeroIs)>0 and zeroIs[-1]!=len(nums)-1: # 밑의 zeroIs[-1]+1 에러 방지이기도 함.
            nzNumArrs.append(nums[zeroIs[-1]+1:])
           
        elif len(zeroIs)==0: ## 0이 없을 때... 테스트케이스에 있어서 망정이지.
            nzNumArrs.append(nums) 
        
        ## test
        # print(nzNumArrs)
   

        def production(arr):
            res=1
            for n in arr:
                res*=n
            return res
        
        for nzNums in nzNumArrs:
            ## test
            print("nzNums, archive: ", nzNums, archive)
            if len(nzNums)==1:
                archive.append(nzNums[0])
                continue
            elif len(nzNums)<1:
                continue

            ## 밑은 원소 여러개 가정임.
            negativeIs = []
            for i in range(len(nzNums)):
                if nzNums[i]<0:
                    negativeIs.append(i)
            
            if len(negativeIs)%2==0:
                archive.append(production(nzNums))
            elif len(negativeIs)==1: ## 원소가 이거 1개일 수도 있음.
                archive.append(production(nzNums[:negativeIs[0]]))
                if negativeIs[0]!=len(nzNums)-1 : ## 마지막 원소가 음수만 아니면 2개로 분리되니
                    archive.append(production(nzNums[negativeIs[0]+1:]))
            else: # 음수 3개이상 홀수개
                leftI = negativeIs[0]
                rightI = negativeIs[-1]
                common = production(nzNums[leftI+1: rightI])
                left = production(nzNums[:leftI+1]) # 음수 포함시키기
                right = production(nzNums[rightI:]) # ㅇㅅ ㅍㅎㅅㅋㄱ
                archive.append(left*common)
                archive.append(common*right)
            
            ## test
            # print("nzNums, archive: ", nzNums, archive)
        answer = max(archive)
        return answer

                



        