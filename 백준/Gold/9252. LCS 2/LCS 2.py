import sys
arr1  = list(sys.stdin.readline())[:-1]
arr2 = list(sys.stdin.readline())[:-1]

dp = [["" for _ in range(len(arr1))] for _ in range(len(arr2))]

for i in range(len(dp)):
  for j in range(len(dp[0])):
    thisCell=""
    if arr1[j]==arr2[i]:
      if i-1>=0 and j-1>=0:
        thisCell+=dp[i-1][j-1]
      thisCell+=arr1[j]

      if j-1>=0 and len(dp[i][j-1])>len(thisCell):
        thisCell = dp[i][j-1]
    
    else:
      if j-1>=0 and len(dp[i][j-1])>0:
        thisCell = dp[i][j-1]
      if i-1>=0 and len(dp[i-1][j])>len(thisCell):
        thisCell = dp[i-1][j]

      

    

    ## thisCell을 dp에 넣는걸 안했네;;
    dp[i][j] = thisCell
## test
# print("dp: ",dp)

answer = dp[-1][-1]
print(len(answer))
if len(answer)>0:
  print(answer)