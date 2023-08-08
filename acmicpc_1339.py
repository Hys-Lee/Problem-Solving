# # 일단 greedy인 것 같기도 함.
# # dynamic은 아닌 것 같아서..

# # 일단 ABC+DEF+GHI+J까진 고려해야 할 듯
# # 동일 자리수 계싼은 말이지.

# # 기본적으로 자리수가 크면 큰 쪽에 가장 높은 숫자를 부여하면 됨.
# # 또한 각 수는 높은 자리부터 큰 숫자가 들어가면 됨.
# # 어차피 순서는 상관 없으니,
# # 각 자리마다 끊어서 순서를 매기고
# # 어떤 수에서든 높은 자리 수부터 높은 값의 숫자를 주면 될 듯.

# n = int(input())
# alps = ['' for _ in range(n)]

# ## 최대 8자리니까.
# ## 각 자리마다 extend해주면 됨.
# alps_order=[[]for _ in range(8)]

# # # 이미 값을 부여한 알파벳 체크 -> 1로
# # alps_used=[0 for _ in range(10)]
# # # 

# # idx: 대상-ord('A'), 값: 부여된 숫자
# ### 미친 빼기 순서를 뒤집어 생각했음;;
# alp_to_num=[-1 for _ in range(26)]
# max_able_num=9 # 얘로 카운트



# for i in range(n):
#   alps[i] = input()
#   for j in range(len(alps[i])):
    
#     alps_order[len(alps[i])-1-j].extend(alps[i][j]) 




# # 알파벳마다 숫자 부여하기
# for i in range(7,-1,-1):
#   for j in range(len(alps_order[i])):
#     idx = ord(alps_order[i][j])-ord('A')
#     if alp_to_num[idx] ==-1:
#       alp_to_num[idx] = max_able_num
#       max_able_num-=1

# # print(alp_to_num)
# ####


# # 수 만들기

      




# result=0
# for i in range(len(alps_order)):
#   for j in range(len(alps_order[i])):
#     result += alp_to_num[ord(alps_order[i][j])-ord('A')]*(10**i)

# print(result)
    


    
## 질문 게시판에서 찾았는데
## 반례 ABB랑 9개의 BB면 B에 9를 부여하는게 맞다는 거였음.

## 그 전에 사실 각 알파벳들을 자리수 고려해서 식으로 쫙 계산해야한다고 생각했었는데, 결국 그럼 최대 10개의 연립방정식이 나오는게 아닌가 싶어서 걍 안했었거든.

## 다시 생각해보면, 전체 합이 최대이려면,
## 식으로 정리해서 가장 높은 값이 (자리수 + 반복횟수 고려) 가장 높은 숫자를 가져야 하는게 맞는 것이지.

## 따라서, ABB랑 BB 9개는, 식으로 정리하면, A=10**3, B:10*10**3+1*10 이므로,
## B가 더 큼.
## 따라서, 이 경우엔 B에 9를 주는게 맞았던 것임...
## element을 정렬할 때 이 기준으로 정렬했어야 하는 것.


n=int(input())

alp_to_num=[0 for _ in range(26)]

values_for_alps = [(0,'') for _ in range(26)]

for i in range(n):
  alps = input()
  for j in range(len(alps)):
    idx = ord(alps[j])-ord('A')
    values_for_alps[idx]=(values_for_alps[idx][0]+10**(len(alps)-1-j),alps[j])


values_for_alps.sort()
values_for_alps.reverse()
# print(values_for_alps)
# 부여되는 최대 값.
max_applied_num=9
result=0
for i in range(26):
  if values_for_alps[i][0]!=0:
    idx = ord(values_for_alps[i][1])-ord('A')
    alp_to_num[idx] = max_applied_num
    result+=values_for_alps[i][0]*alp_to_num[idx]    
    max_applied_num-=1


    
print(result)

## 코테 문제는 구현은 모르겠나 나머지는 설계좀 하자
## sub-problem이 optimal이 되도록 하는 방법을 제대로 파악하자 문제마다.
## 그리고 한번 해보고 판단하자. 이건 아닌 것 같다고 막 하지는 말고.