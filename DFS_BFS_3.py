# # 맨 처음에는 BFS로 하려고 했었고, 인접 행렬 방식으로 다시 2차원 리스트 만드려고 했었음.
# # 사실 이미 입력을 그래프 형식으로 줬기 때문에 굳이 또 인접 행렬로 만들 필요 없었고, DFS가 어올렸음
# # 나는 DFS,BFS문제는 다 두 방법으로 풀 수 있는 줄 알았는데, 한 방법으로만 풀 수 있는 문제들도 있었음.(더 생각해보면 가능할 수도 있지만...)

# #밑은 정답을 보고 내가 DFS로 다시 짜본 것.
# ## 정답지에는

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#   graph.append(list(map(int, input())))
# count = 0

# def dfs(graph, m, n):
#   if m < 0 or m >= len(graph[0]) or n < 0 or n >= len(graph): return
#   if graph[n][m] == 1: return

#   graph[n][m] = 1
#   dfs(graph, m + 1, n)
#   dfs(graph, m, n + 1)
#   dfs(graph, m - 1, n)
#   dfs(graph, m, n - 1)

#   pass

# for i in range(n):
#   for j in range(m):

#     if graph[i][j] == 0:
#       count += 1
#       dfs(graph, j, i)
# print(count)
