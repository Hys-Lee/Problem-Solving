def solution(k, tangerine):
    tangerine.sort()
    nums=[0]
    nIdx=0
    ## test
    # print("tangerine: ", tangerine)
    for i in range(len(tangerine)):
        if i==0:
            nums[0]=1
            continue
        if tangerine[i]!=tangerine[i-1]:
            nums.append(1)
            nIdx+=1
        else:
            nums[nIdx]+=1
        
        ## tset
        # print("nums, nIdx: ", nums, nIdx)
    
    nums.sort()
    nums.reverse()
    ## test
    # print("final nums: ", nums)
    count = 0
    answer=0
    for i in range(len(nums)):
        count+=nums[i]
        answer+=1
        if count>=k:
            return answer
        ## test
        # print("count,answer, i: ",count, answer, i)
    return answer