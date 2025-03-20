import sys
n,s = map(int,sys.stdin.readline().split())
arr=list(map(int, sys.stdin.readline().split()))

left=0
right=0
inf = 1e9
minLen = inf

winSum = arr[0]
winLen = 1
while(left<len(arr)):
  if winSum>=s:
    minLen = min(minLen, winLen)

  ## test
  # print("winSum,winLen,minLen,left,right: ",winSum,winLen,minLen,left,right)
  ## 윈도우 변경
  if winSum>=s:
    winSum-=arr[left]
    winLen-=1
    left+=1
  else:
    right+=1
    if right>=len(arr):
      break
    winSum+=arr[right]
    winLen+=1
 
if minLen==inf:
  print(0)
else:
  print(minLen)