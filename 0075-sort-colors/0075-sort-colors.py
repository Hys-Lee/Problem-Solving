# 2번 훑어서 처리하는건 할 수 있는데.
# 그냥 0이랑 1,2개수를 각각 알면 되자너.
# 걍 덮어쓰기해도 되는데.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##  몰라 두번 훑을거임.
        zeroes=0
        ones=0
        twoes=0
        for n in nums:
            if n==0:
                zeroes+=1
            elif n==1:
                ones+=1
            else:
                twoes+=1
        i=0
        while(i<zeroes):
            nums[i] = 0
            i+=1
        ## test
        # print('zeroes, i',zeroes,i)
        while(i<zeroes+ones):
            nums[i] = 1
            i+=1

        while(i<zeroes+ones+twoes):
            ## test
            # print("i",i)
            nums[i]=2
            i+=1

        