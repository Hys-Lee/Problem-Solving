import sys
sys.setrecursionlimit(100_000)

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
inf = 1e10
minAbs=[inf]
minAbsEles=[arr[0],arr[n-1]]

def bs(left, right):
  if left>=right:
    return
  
  tmpSum = arr[left] + arr[right]
  if abs(tmpSum) < minAbs[0]:
    minAbs[0] = abs(tmpSum)
    minAbsEles[0] = arr[left]
    minAbsEles[1] = arr[right]
  if tmpSum>0:
    right-=1
  else:
    left+=1

  bs(left,right)

bs(0,n-1)
print(minAbsEles[0], minAbsEles[1])