# import DFS_BFS_3
# import DFS_BFS_4
#import QuickSortPracticing

#import Sort_2
# import Sort_3
#import Sort_4
# import BinarySearch_2
# import BinarySearch_3
# import Dynamic_Programming_2
# import Shortest_Path_2
# import Shortest_Path_3
# import Graph_Theory_2
# import Graph_Theory_3
# import Graph_Theory_4
# import Bank_Greedy_1
# import Bank_Greedy_2
# import Bank_Greedy_3
# import Bank_Greedy_4
# import Bank_Greedy_5
# import Bank_Greedy_6
# import acmicpc_2839
# import acmicpc_11399
# import acmicpc_11047
# import acmicpc_1931
# import acmicpc_1541
# import acmicpc_1026
# import acmicpc_2217
# import acmicpc_1789
# import acmicpc_13305
# import acmicpc_10162
# import acmicpc_1715
## 2023-08-05
# import acmicpc_10610
## 2023-08-06
# import acmicpc_16953
## 2023-08-07 다시 풀어야할 거
# import acmicpc_1946
## 2023-08-08
# import acmicpc_2720
# import acmicpc_1339
## 2023-08-14
# import acmicpc_1202
## 2023-08-25
# import Bank_Materialization_7
# import Bank_Materialization_8
## 2023-08-28
# Bank_09_Materialization(programmers에서)
#################
#################
#################
###### 알고리즘문풀 세미나 연습
#ㄴ> colab으로 하려고 했는데, colab은 readline이 안된데.
#백준 10810
# import sys
# n, m = map(int, sys.stdin.readline().split())
# arr=[]
# for i in range(n):
#   arr.append(0)

# for p in range(m):
#   i,j,k = map(int, sys.stdin.readline().split())
#   for q in range(i-1,j):
#     arr[q] = k

# for i in range(len(arr)):
#   print(arr[i], end=" ")

#백준 10813
# import sys
# n,m = map(int, sys.stdin.readline().split())
# arr=[]
# for i in range(n):
#   arr.append(i+1)
# for k in range(m):
#   i,j = map(int, sys.stdin.readline().split())
#   arr[i-1],arr[j-1] = arr[j-1],arr[i-1]
# for i in range(len(arr)):
#   print(arr[i], end=" ")

#백준 3052
# import sys
# map = set([])
# for i in range(10):
#   map.add(int(sys.stdin.readline())%42)
# print(len(map))

# 세미나장님이 갖고오신 문제 2 : 배열이 주어질 때, 연속된 같은 수를 하나로 합친 배열을 만들기.
# arr = [3, 3, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 1]
# result=[]
# result.append(arr[0])
# for i in range(1,len(arr)):
#   if arr[i-1]!=arr[i]:
#     result.append(arr[i])
# print(result)

#백준 1913 (실버3)
