class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        checklist=[[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ## test
        # print("CH: ", checklist)
        dydx=[(0,+1),(+1,0),(0,-1),(-1,0)]#우하좌상
        dpointer=0
        cycx=(0,0)
        answer=[]
        def isValid(pos):
            y,x = pos
            ## test
            # print("valid? pos: ", pos)
            ## 맵 외부 체크
            if y<0 or len(matrix)<=y: return False
            if x<0 or len(matrix[0])<=x: return False
            ## 갔던곳인지 체크
            if checklist[y][x]: return False
            ## test
            # print("뭐야")
            return True

        while(1):
            answer.append(matrix[cycx[0]][cycx[1]])
            checklist[cycx[0]][cycx[1]] = True ## 이거 까먹었네
            ## test
            # print("answer: ", answer)
            endFlag=True
            for _ in range(4):
                ny = cycx[0]+dydx[dpointer][0]
                nx = cycx[1]+dydx[dpointer][1]
                ## test
                # print("ny,nx,cycx, dpointer", ny,nx,cycx,dpointer)
                if isValid((ny,nx)) is True:
                    cycx = (ny,nx)
                    endFlag=False
                    ## test
                    # print("멈춰야지 이제, cycx: ", cycx)
                    break
                dpointer=(dpointer+1)%4
            if endFlag is True:
                return answer

