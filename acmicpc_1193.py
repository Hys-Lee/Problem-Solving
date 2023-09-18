# (0)+1=1번: 1/1 -> 1+1=2, 1번째.
# (1)+1=2번: 2/1 -> 2+1=3, 1번
# (1+2)+2=5번: 2/2 -> 2+2=4,

# 대각선 몇번째 줄, 어디에 있는지 알면 됨.
x = int(input())


# 1~to까지 정수 합
def cumul_sum(to):
  return (1 + to) * to / 2


line = 0
while (cumul_sum(line) < x):
  line += 1

son_mom_sum  = line+1

if line%2==1:
  mom = line -(cumul_sum(line)-x)
  son = son_mom_sum-mom
else:
  son = line -(cumul_sum(line)-x)
  mom = son_mom_sum-son
print(int(son),"/",int(mom), sep='')
