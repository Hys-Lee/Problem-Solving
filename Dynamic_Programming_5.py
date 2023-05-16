# 4번 문제는 리플릿 교체하다가 날라감 개가튼거
import sys
n,m = map(int,sys.stdin.readline().split()) 

token={}
for i in range(n):
  token.append(int(input()))

dp_table=[0]

#초기화
for i in range(1,m+1): #1~m
  med=[] #초기화 매 i마다
  for j in range(n):
    
    if i==token[j]: #초기허ㅔㅘ
      dp_table[i]=1
    elif i>max(token): #계산
      prev= dp_table[i-token[j]]
      if prev!= 0:
        med.append(prev+1)
      else: dp_table[i]=0
    else: #계산 못하는값
      dp_table[i]=0
  dp_table[i]=min(med)

if(dp_table[m]==0):
  print(-1)
else:
  print(dp_table[m])



## 코드짜고 머리고 몇개 돌려보면 어느정도 처음 에러는 걸러지네

