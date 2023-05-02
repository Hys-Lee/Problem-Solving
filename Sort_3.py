###밑에는 내가 다시 풀어본 풀이
# n = int(input())
# dict = {}
# for i in range(n):
#   tmp = input()
#   dict[int(tmp.split()[1])] = tmp.split()[0]

# resultdict = sorted(dict.items())
# # dict = sorted(dict, key=dict.values())
# for tup in resultdict:
#   print(tup[1], end=" ")
# # print(type(tmpdict))

## 답지에서는 tuple을 사용했다 dictionary대신.
# 그리고 sorted에서 key attribute에 어떤 것을 넘겨야 하는지 알았따.
# key에는 기본적으로 array에서 각 원소들이 오는데, 여기서 원소가 특정 자료구조라서 원소안에서 키를 분리해야 한다면 lambda를 사용하면 된다.
# array = sorted(array, key=lambda student:student[1]) 이런식으로.
