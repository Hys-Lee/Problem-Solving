class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zidxs=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                zidxs.append(i)
        ## test
        # print("zdixs: ", zidxs)

        for i in range(len(nums)):
            ## test
            print("i: ", i)
            if len(zidxs)==0:
                ## test
                # print("더는 0이 없어")
                continue
            if i == zidxs[-1]:
                if zidxs[-1]==len(nums)-1:
                    return True
                ## test
                print("여기까지 넘길 수 있는 애를 못 찾았어")
                return False
            while len(zidxs)>0:
                if i+nums[i]>zidxs[-1]:
                    ## test
                    # print("이번 0은 넘길 수 있음. i, nums[i], zidxs",i,nums[i], zidxs )
                    zidxs.pop()
                else:
                    # if zidxs[-1]==len(nums)-1 and nums[i]>0:
                    #     ## test
                    #     print("마지막 idx에 간신히 도달")
                    #     zidxs.pop()
                    ## test
                    # print("이번 0은 못 넘김")
                    break
        return True
        