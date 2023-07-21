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
import Bank_Greedy_6
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
