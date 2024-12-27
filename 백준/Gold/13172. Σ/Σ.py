import sys
m = int(sys.stdin.readline())
sns = []
for _ in range(m):
  n,s = map(int, sys.stdin.readline().split())
  sns.append((n,s))

## test
#print("SMS: ", sns)

def tenSeong(i,val):
  if i==1:
    return val
  
  prev = tenSeong(i-1, val)
  return prev**10%1_000_000_007
  ## tset
  #print("아닌 경우가 있나?")


  # if i%2==0:
  #   prev = tenSeong(i//2, val)
  #   return prev*prev
  # else:
  #   return tenSeong(i-1,val) * val

x = 1_000_000_007
Nnums = []
for n,s in sns:
  five = n**5
  ten = five**2
  nYeok = tenSeong(9, ten) * five
  Nn = (s * nYeok)%x
  ## test
  #print("n역, Nn: ", nYeok, Nn)
  Nnums.append(Nn)

print(sum(Nnums)%x)
  
  