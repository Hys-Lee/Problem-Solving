## 솔직히 dynamic하고 뭔 차인지 애매했음.
## 다이나믹이 잘 기억이 안나서..

n = int(input())

save=[-1 for _ in range(n+1)]
save[3] = 1
if n>4:
  save[5] = 1

for i in range(6,n+1):
  if save[i-5]!=-1:
    save[i] = save[i-5]+1
  elif save[i-3]!=-1:
    save[i]=save[i-3]+1


print(save[n])
  
## n=4일 때 save[5] 할당이 안되는 경우를 생각 못했었음.

### 짜면서 체크하자.

## greedy 몇 문제 풀고 dynamic 공부해서 비교해보자.