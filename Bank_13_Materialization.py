# 완전 탐색 인 듯?
# 모든 경우를 다 생각해봐야 함.

# 각 집마다의 치킨거리를 계산,저장하자.
# 각 케이스 따라 치킨거리를 비교하자.

# M은 주어지니까 어떤 것을 선택하느냐를 구현해야
# 최대 M개니까, 1~M까지 다 따져야 함...
# 근데, 굳이 조합으로 할 필요가 있나?
# 최대 50*50에
# 13*12*11*10*9*8하면 안되네
# 조합으로 가야 하네.
# 뭐가 되었든 안겹치게
#  -> for문 3개로.
#
# 집, 치킨집 위치를 좌표로 저장하자.

import sys
import itertools# 이러면 끝나긴 함.

#print(list(itertools.combinations([1,2,3,4,5,6],2)))



n, m = map(int, sys.stdin.readline().split())

# 좌표로 위치 저장.
chickens = []
houses = []
for r in range(n):  # r위치
  input_row = list(map(int, sys.stdin.readline().split()))
  for c in range(len(input_row)):  # c위치
    if input_row[c] == 1:
      houses.append((r, c))
    elif input_row[c] == 2:
      chickens.append((r, c))
      
#//
city_value=[] #1~m
for r in range(1,m+1):
  for case in list(itertools.combinations(chickens,r)):
    chick_lens=[]
    for h in houses:
      h_len=101
      for c in case:
        h_len=min(h_len,abs(c[0]-h[0])+abs(c[1]-h[1]))
      chick_lens.append(h_len)
    city_value.append(sum(chick_lens))

print(min(city_value))

    




#city_value = []
#chickens_cases = []  # ->이미 했던 것들
# 치킨 집 추리기
#for i in range(1, m + 1):
  # 새 chickens복사
#  new_case = [ele for ele in chickens]
#  rest_history = []
#  pick_history = []

  # history 채우기
##  tmp = []
  #for j in range(len(new_case) - i):
    #tmp.append(new_case.pop())
   # pick_history.append(tmp[:])
   # rest_history.append(new_case[:])

 # print("전: ", pick_history)
#  make_all_cases(pick_history, rest_history)

  # 어케 모든 케이스를 만들지?
  # 버리는 방식으로 가고,
  # 각 버릴 때 마다, array를 남겨두자.
  # 다음 버릴 때는 남은 애들 중에 버리게 하면 딜 듯.

  # 도시 값 계산 후



# 파이썬 call by ref, call by value 다시 보기
