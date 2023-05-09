# import sys

# n = int(input())

# dyn_from_2=[0,1] # 2 동작 개수 해당 stage에서 즉, 2단계 stage 전에거 (1동작+2동작 )*2
# dyn_from_1=[1,1]# 1동작횟수 즉, (2동작+1동작)*1
# dyn_arr=[1,3]
# i=2
# while(i+1<=n):
#     dyn_arr.append((2*dyn_arr[i-2]+dyn_arr[i-1])%796796)
#     i+=1

# print(dyn_arr[n-1])