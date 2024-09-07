class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer =1
        for i in range(m-1+n-1,m-1, -1): # n-1번 곱
            ## test
            # print(i)
            answer*=i
        for i in range(1,n): # 1~n-1
            ## test
            # print("나누기: ",i)
            answer//=i
        return answer