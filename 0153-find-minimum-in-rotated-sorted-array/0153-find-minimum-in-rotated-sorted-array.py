# 회전되어 있는 상태라면(즉, 오름차순 상태가 아니라면 즉, n번 회전한게 아니라면)
#   중간에 최대값과 최솟값이 나란히 있다는 말.
#   ㄴ> bs를 사용한다고 할 때, m에서의 값이 l보다 크다면 -> m의 오른쪽에 최솟값 존재하니 l을 m로 하기
#      m에서의 값이 l보다 작다면, m의 왼쪽에 최솟값 존재하니, r을 m로하기(m이 최소일 때 포함)
#         ㄴ> m포함한 범위로 해야함 새로운 범위도.
#           m위치가 최솟값일 수도 있으니.

#     ㄴ> m과 l위치가 동일(즉, 값도 동일)하다면?
#          -> 2개일 때 or 1개일 때-> l,m,r위치 중 최소값을 반환하도록 하자 걍.

# 회전되어 있지 않다면 최댓값은 맨 오른쪽, 최솟값은 맨 왼쪽에
#     ㄴ> 따라서, 맨 오른쪽>맨 왼쪽 -> 맨 왼쪽을 반환.

# #### 수도코드만들기
# answer=[0]초기화 (참조 가능하도록)
# def bs(l,r)
#   m = l과 r의 절반 (//2)
#   if 넘스의 l번째 값<m번째 값
#     l = m
#   elif l번째 값>m번째 값
#     r = m
#   else # l이 m이랑 같다면
#     answer = min(l번째,r번째)
#     return
#   bs(l,r)

    

# if l에서의 값<r에서의 값:
#     return l에서의 값

# bs(l, len(nums)-1)
# return answer
  


# __ 알고 대충 23분
# __ 수도 대충 30분


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        
        answer=[0]
        def bs(l,r):
            m = (l+r)//2
            if nums[l]<nums[m]:
                l=m
            elif nums[l]>nums[m]:
                r = m
            else:
                answer[0] = min(nums[l],nums[r])
                return
            bs(l,r)

        bs(0,len(nums)-1)
        return answer[0]

        