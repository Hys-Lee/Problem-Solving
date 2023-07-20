## 일단 수학적으로 풀면...

# import sys
# n,m = map(int, sys.stdin.readline().split())

# mass=[0 for _ in range(m+1)]

# input_arr = list(map(int, sys.stdin.readline().split()))
# for i in range(n):
#   mass[input_arr[i]]+=1


# total = sum(mass)*(sum(mass)-1)/2

# dupli = 0
# for i in range(m+1):
#   if mass[i]>1:
#     dupli+=mass[i]*(mass[i]-1)/2


# print(int(total-dupli))


## 이게 무슨 유형이지?
## greedy로 볼 수 있지 않나
## input 무게 별로 개수 측정한걸 
## greedy 각 step의 element로 보자.
## 그러면, A가 선택한 것들은 1,2,3,...이렇게 앞으로만 감.
## B는 그럼 (2,3,4...),(3,4,5,...) 이런식임.

## step1 (1){2,3,4,5,6,...}
## step2 [1](2){3,4,5,6,...}
## step3 [1,2](3){4,5,6,...}
##    []는 A가 과거 ()는 A가 현재 {}는 B가 고를 것.
import sys
n,m = map(int, sys.stdin.readline().split())

mass=[0 for _ in range(m+1)]

input_arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
  mass[input_arr[i]]+=1

result=0


for i in range(1,m): # 맨 마지막 제외.
  result+=mass[i]*sum(mass[i+1:])
print(result)