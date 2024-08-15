class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLimit(l,r,mode):
            if l>r: return -1
            m=(l+r)//2

            if nums[m]>target:
                return findLimit(l, m-1,mode)
            elif nums[m]<target:
                return findLimit(m+1,r,mode)
            else:# nums[m]==target:
                if mode=='left':
                    if m-1>=0 and nums[m-1]>=target:
                        return findLimit(l,m-1,mode)
                    else:
                        return m
                else:
                    if m+1<len(nums) and nums[m+1]<=target:
                        return findLimit(m+1,r,mode)
                    else:
                        return m
        
        leftLimit = findLimit(0,len(nums)-1, "left")
        rightLimit = findLimit(0,len(nums)-1,"right")
        ## test
        print("LL,RL: ", leftLimit, rightLimit)
        return [leftLimit, rightLimit]

