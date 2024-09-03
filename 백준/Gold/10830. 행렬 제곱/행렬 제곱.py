import sys
N,B = map(int, sys.stdin.readline().split())

pointer=[]
for _ in range(N):
  row = list(map(int,sys.stdin.readline().split()))
  pointer.append(row)


useSq=[]
tmpB=B
while tmpB>0:
  useSq.append(tmpB%2)
  tmpB = tmpB//2

# useSq.reverse() ## 이거 하면 안됐네..
## test
# print("B를 2진수로 useSq: ", useSq)

answer=[[1 if i==j else 0 for i in range(N)] for j in range(N)] ## 행렬 I는 대각선만 1이어야 함.

def matrixProd(mtrxF,mtrxB):
  ## 1000 나눈 나머지로 하는거 까먹었음.
  
  # 두 인자 모두 N*N
  result=[[0 for _ in range(N)] for _ in range(N)]

  for i in range(N):
    for j in range(N):
      # mtrxF[i]랑 mtrxB[:][j](표현만).
      subsum=0
      for k in range(N):
        subsum=(subsum+mtrxF[i][k]*mtrxB[k][j])%1000
      result[i][j] = subsum
  return result
      
      
      

for i in range(len(useSq)):
  ## test
  # print("현재 포인터: ", pointer)
  if useSq[i]==1:
    answer = matrixProd(answer, pointer)
    ## test
  # print("i, answer: ", i, answer)
  pointer = matrixProd(pointer, pointer)

  



# print(answer)
### 출력 제대로 해야함.
for i in range(N):
  for j in range(N):
    print(answer[i][j], end=' ')
  print()