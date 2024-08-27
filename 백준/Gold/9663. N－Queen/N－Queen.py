import sys
n = int(sys.stdin.readline())

answer=[0] ## 밖에서 참조하기 쉽도록 배열로 해둠.
def dfs(i,selectedQs):
  for j in range(n):
    isPass=True
    for q in selectedQs:
      ## q는 (y,x)   현재 고려 위치는 i,j
      ## test
      # print("고려 위치 (i,j): ",i,j)
      # # 가로 체크  => 필요 없음.
      # if q[0] == i:continue
      ## test
      # print("가로 통과")
      #세로체크
      if q[1] == j:
        isPass=False
        break
      ## test
      # print("세로 통과")
      # 대각 \체크
      if q[0]-i == q[1]-j:
        isPass=False
        break
      ## test
      # print("대각 \ 통과")
      # 대각/체크
      if q[0]-i == j-q[1] : 
        isPass=False
        break
      ## test
      # print("대각 / 통과")
    if not isPass:continue
    ## 가로,세로,대각도 아니라면
    if i==n-1:
      
      answer[0]+=1
      ## test
      # print("마지막까지 도달함, answer: ", answer)
      return
    else:
      # nextSelectedQs=[(i,j)]
      # nextSelectedQs.extend(selectedQs)
      ###시간 아끼기 위해 밑으로 변경
      selectedQs.append((i,j))
      ## test
      # print("다음줄로 가보자, i,j,selectedQs", i,j, selectedQs)
      dfs(i+1, selectedQs)
      selectedQs.pop()

for j in range(n):
  ## test
  # print("시작지점 i,j: ",0,j)
  dfs(1,[(0,j)])
if n==1:
  print(1)
else:
  print(answer[0])