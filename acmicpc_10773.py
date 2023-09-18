k = int (input())

my_stack = []
for i in range(k):
  n = int(input())
  if n!=0:
    my_stack.append(n)
  else:
    my_stack.pop()
print(sum(my_stack))
  
