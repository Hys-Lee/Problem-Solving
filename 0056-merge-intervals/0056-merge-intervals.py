class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer=[intervals[0]]

        for i in range(1,len(intervals)):
            
            if answer[-1][1]>=intervals[i][0]:
                merged=answer.pop() # 초기화.
                merged = [min(merged[0], intervals[i][0]),max(merged[1], intervals[i][1])]
                ## test
                print("병합한 머지드: ",merged)

                
                answer.append(merged)
            else:
                ## test
                print("추가되는 인터벌: ",intervals[i])
                answer.append(intervals[i])
            
        ## test
        print("answer: ",answer)
        return answer