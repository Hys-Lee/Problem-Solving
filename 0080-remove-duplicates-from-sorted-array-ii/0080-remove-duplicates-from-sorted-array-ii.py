# nums초기 어레이 길이는 3만이면..

# 뒤에서부터 loop돌면서 진행하는데,
# 포인터 하나 둬서, 얘가 남은 array의 마지막을 가리키도록 함.
# 진행 포인트(loop따라)가 가다가 2개 이상인 지점을 발견해서 
#     해당 부분에서 2개 초과로 만드는 애들 위치를 집으면,
#     얘네들을 교환을 통해 

# ㄴㄴ  
# 걍 이렇게 해보자. (만약에 2개보다 훨씬 많이 같은게 있으면 겁나 귀찮아지니까, 아예 2개만 따로 빼내서 다른 곳으로 옮기는 느낌이라면..?)
# 조건을 만족하는 애들을 맨 앞에서부터 뒤쪽을 그냥 바꿔치기를 하는거임.
# 마지막에 reverse시키면 되니까

# 이러면 조건 만족하는 역arr의 경계선 부분을 pointer로 잡고 있으면 되겠네.
# 다 옮긴 후 pointer 위치로 k값 구하고
# reverse시키면 끝임.

# 아 ㄱ느데, relatively same order여야 하자너. 성립하네 ok가시죠.

# 아닌뎅 이렇게 하면 안되느디...

# ------------
# 아니면 정방향으로 보면서,
# 정리 pointer와 탐색 pointer를 사용하자.
# 정리 poiter는 오답의 시작 부분을 정하는거로 하고 탐색pointer는 미리 다른 값들을 찾아서,
#  정리 pointer에서의 값과 교환시키는 역할 하면 됨

# 그니까, 처음 정리pointer를 0번째 값이 2번 나오는(혹은 1번) 지점으로 이동
# 값이 바뀌거나 2번 이상 나오면 정리 pointer는 멈추기
# 이후 탐색포인터가 값이 정리 pointer지점에 위치함.
#     이후 한칸씩 이동하며 값이 바뀌는 포인트를 찾기.(정리 opinter랑 달라지는 지점)
#     정리 pointer는 1칸 이동하고, 정리 poiner에서랑 탐색 pointer에서랑 값 교환. 탐색 poniter는 1칸 전진
#     탐색 pointer에서의 값이 정리 pointer값이랑 같다면
#         정리 pointer 이전에서 (포함인지는 체크) 같은 값이 있었는지 확인해 처리.
    
#     탐색 pointer가 끝까지 도달할 때까지 반복하면 될 듯.





# ### 수도코드만들기

# # rvpointer= nums길이-1:마지막인덱스 -> 불필요부분 시작지점(역으로)에 위치
# # i=0 -> 얘는 nums정방향 돌릴 pointer
# # while i<=rvpointer 동안 (rvpoiner랑 i랑 만났을 때도 시행해야 rvpointer로 k값 알아낼 수 있음.)
# #   if i==0처음이면
# #     rvpointer와 i에서 교환 (tmp사용)
# #     rvpointer-=1
# #   else:
# #     if rvpointer+1에서와 i에서의 값이 같고, rvpoiner+2에서와 i에서의 값이 같다면,
# #       continue
# #     (else: rvpointer+1만 i에서와 같고 +2에서 i와의 값이 다르면 ok. rvpointer+1과 값이 달라도 ok)
# #     rpointer와 i에서 교환
# #     rvpointer-=1
      
# #   i+=1

# # k값은 nums마지막 인덱스 - rvpointer임.
# # nums이대로 reverse시키면 끝.

  
# ### 수도 다시
# # savep = 0
# # tripp=0
# # for i in range(nums):
# #     if nums[savep+1]!= nums[savep] or nums[savep+1]==nums[savep-1]: => savep위치 세팅하기
# #         break
# #     savep+=1
# # tripp는 save+1에서 시작함.
# # while tripp<len(nums):
# #     if tripp는 savep에서랑 다른 값 발견하지 못하면서(and) savep랑 tripp에서랑 같은데 savep-1에서도 tripp에서랑 같다면
# #       tripp+=1로 continue
    
# #     #else 발견하면
# #     savep+=1로 교체 준비
# #     tripp위치랑 savep(이동한)위치랑 값 교환.
# #     tirpp위치+=1


# # savep위치값이 결과 길이 값임.



# __ 알고 대충 12분
# __ 수도 대충 22분
# __ 엣지  -> 알고 갈아엎기 대충 32분
# __ 수도 다시 41분
# __ 엣지 -> [1,2,2,3]이어도 가능 44분 (그러고보면, savep랑 tripp가 같은 위치가 되는 상황은 미처 생각 안했었음. 좀 떨어진 위치에서 교체된다는 생각만함. 같은 위치일 때는 안정적 상황이거덩.)
# 틀림 -> 맨 처음에 savep위치 초기화 할 떄 savep+1위치가 nums에 존재하지 않을 경우 체크 못 함.
    # ㄴ> 이 상황이 일어나는, 기존코드에서 커버 못하는 부분은 길이가 1짜리 일 때임. 이 때는 걍 return 1하도록 처리하자.



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        savep=0
        if len(nums)==1:
            return 1
        for n in nums:
            if nums[savep+1]!=nums[savep] or nums[savep+1] == nums[savep-1]: #or뒤는 duplicate상황에서 만남.
                break
            savep+=1
        tripp=savep+1
        ## test
        # print(savep, tripp)

        while tripp<len(nums):
            if savep-1>=0 and (nums[savep]==nums[tripp] and nums[savep-1]==nums[tripp]):
                tripp+=1
                continue
            ## else
            savep+=1
            ## test
            # print("savep, tripp",savep, tripp)
            tmp = nums[tripp]
            nums[tripp] = nums[savep]
            nums[savep] = tmp
            tripp+=1
            ## test
            # print("tripp, nums: ", tripp, nums)
        ## test
        # print("nums",nums,savep)
        return savep+1 ## savep는 안전한 위치니까 항상. 바뀔만할 때만 savep이동시켰으니.

