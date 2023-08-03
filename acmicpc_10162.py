# 전형적인 greedy
# 각 단위끼리는 배수관계
# 300, 60, 10이니까
# 가장 큰 것부터 최대한 하면 됨.


t = int(input())

a_times = t//300
b_times = (t%300)//60
c_times = ((t%300)%60)//10 # 사실 %300없어도됨
left=t%300%60%10 # 사실 %300%60없어도 됨
if left!=0:
  print(-1)
else:
  print(a_times, b_times, c_times)