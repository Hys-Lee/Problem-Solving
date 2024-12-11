import sys
import math

n = int(sys.stdin.readline())

k = int(math.log2((n // 3)))

unit = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "],
        ["*", "*", "*", "*", "*"]]

## k==0이면 밑의 과정 필요 없음. 밑은 오히려 k>=1에서 성립함 answer크기가.
unitAts=[]
answerWLen = 5*2**k + (2**k-1  if k>=1 else 0) 
answer=[[" " for _ in range(answerWLen)] for _ in range(3*2**k)]

## test
# print(answer, answerWLen)

def findThree(kLevel):
  if kLevel==0:
    return [(0,0)]
  return [(3*(2**(kLevel-1)), 0), (0,3*(2**(kLevel-1))), (3*(2**(kLevel-1)), 2*3*(2**(kLevel-1)))]

def recur(kLevel, startP):
  if kLevel==0:
    unitAts.append(startP)
    return
  nextDetails = findThree(kLevel-1)
  for nextD in nextDetails:
    nextP = (startP[0]+nextD[0], startP[1]+nextD[1])
    ## test
    # print("Kelvel, startP, nextP: ", kLevel, startP, nextP)
    recur(kLevel-1, nextP)

startingPs = findThree(k)
for sp in startingPs:
  recur(k, sp)
## test
# print("k,unitAts:" , k,unitAts, startingPs)
for unitAt in unitAts:
  unitAtY, unitAtX = unitAt
  ## test
  # print("answerY크기, answerX크기, unitAt: ", len(answer),len(answer[0]), unitAt )
  for i in range(len(unit)):
    for j in range(len(unit[0])):
      answer[unitAtY+i][unitAtX+j] = unit[i][j]

for line in answer:
  print(''.join(line))