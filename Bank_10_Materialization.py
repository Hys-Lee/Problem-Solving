이거만 한 3시간은 한 것 같은데 개 박살남 

# # # 키가 자물쇠 밖으로 삐져나와도 상관 없고, 그냥 모든 홈에 맞추기만 하면 되는 듯.
# # # 돌리는 것도 상관 없고. 이동도 괜찮고. 좌우 반전은 안 되겠찌.

# # # 홈이 포함된 정 사각형의 공간을 체크해야 할 듯?
# # # key를 돌린 4가지 형태에서, 그 공간만큼 자를 때 자물쇠 홈과 맞는다면 
# # # true일 듯.

# # def solution(key, lock):
# #     # lock의 0, key의 1을 맞추기
    
# #     # lock에서 0을 포함하는 정사각형 사이즈 측정하기
# #     # 0인 곳들 x,y에서 가장 큰것과 작은 것들이 있는 점 2개를 각각 뽑아서
# #     # 차이 중 가장 큰 것을 한 변의 길이로 하는 정사각형.
# #     # index이므로 두 index차이+1하면 됨.
    
# #     # lock에서 봐야할 부분 정사각형으로 뽑기 (위치, 한 변 길이)
# #     x_min_max=[]
# #     y_min_max=[]
# #     grid_len = 0
# #     for i in range(len(lock)):
# #         for j in range(len(lock[0])):
# #             if lock[i][j]==0:
# #                 # 처음 찾은 홈이면 선택(추가?)
# #                 if len(x_min_max)==0: # 이 말은 y에서도 처음이라는 뜻
# #                     x_min_max=[j,j]
# #                     y_min_max=[i,i]
# #                 # 각 부분에서 보다 크거나 작은게 있다면 교체
# #                 x_min_max[0] = min(x_min_max[0], j)
# #                 x_min_max[1] = max(x_min_max[1], j)
# #                 y_min_max[0] = min(y_min_max[0], i)
# #                 y_min_max[1] = max(y_min_max[1], i)
                
    
# #     grid_len = max(x_min_max[1]-x_min_max[0]+1,\
# #                      y_min_max[1]-y_min_max[0]+1)
# #     # test
# #     print(grid_len)
    
# #     # 생각해보니까 key에서 grid크기만큼 보며 이동시킬 때 맞는 grid위치가 가운데 쯤에 있고
# #     # 주변에도 돌기가 있는데, 이게 lock의 돌기랑도 부딪힐 수 있을 듯.
# #     # 위치 맞춘다음에, key랑 lock전체 비교해보면서 부딪히는 부분 있는지 체크해야 할 듯...
    
# #     keys_spin=[key]
# #     for k in range(3):
# #         new_key=[[0 for _ in range(len(key))] for _ in range(len(key))]
# #         for i in range(len(key)):
# #             for j in range(len(key[0])):
# #                 new_key[j][len(key)-1-i] = key[i][j]
# #         keys_spin.append(new_key)
        
# #     print(keys_spin)
    
# #     # key랑 lock 매칭 부분부터 찾기
# #     grid_key_matching_num=len(key)-grid_len  
    
# #     matching_point=[] # 여러개 가능
# #     for k in range(4):
# #         # i, j는 key랑 grid랑 채크하는 첫 포인트 위치(grid기준이 좌상일 때.)
        
# #         # key에서의 포인트
# #         for key_init_i in range(grid_key_matching_num):
# #             for key_init_j in range(grid_key_matching_num):
# #                 matching_flag = True
# #                 # key의 이 부분에서
# #                 for grid_i in range(grid_len):
# #                     for grid_j in range(grid_len):
# #                         if keys_spin[k][key_init_i+grid_i][key_init_j+grid_j] == lock[y_min_max[0]+grid_i][x_min_max[0]+grid_j]:
                            
# #                             print(keys_spin[k][key_init_i+grid_i][key_init_j+grid_j])
# #                             print(lock[y_min_max[0]+grid_i][x_min_max[0]+grid_j])
                        
# #                             matching_flag = False
# #                 if matching_flag==True:
# #                     matching_point.append([k,key_init_i, key_init_j])
# #     # test
# #     print(matching_point)
    
    
# # #     total_ys_len = [len(lock)+len(key)-matching_point[i][1]+1 for i in range(len(matching_point))] 
# # #     total_xs_len = [len(lock)+len(key)-matching_point[i][1]+1 for i in range(len(matching_point))]
    
# # #     # # nothing 부분은 -1로
# # #     # totals = [[[-1 for _ in range(len(total_xs_len[i]))]\
# # #     #            for _ in range(len(total_ys_len[i]))]\
# # #     #           for i in range(len(matching_point))]
    
# # #     # matching point마다의 결과
# # #     result =[]
# # #     for k in range(len(matching_point)):
# # #         # total있으면 더 불편함.
# # #         # # 일단 lock부터 채우기
# # #         # for i in range(len(lock)):
# # #         #     for j in range(len(lock)):
# # #         #         totals[k][i][j] = lock[i][j]
        
# # #         # 매칭되는 key 전체 체우기  (돌기 부분끼리 부딪히는지 체크)
        
# # #         # 생각해보니 굳이 key에서 grid를 사용할 필요 없이, 그냥 lock에서 고려되는 정사각형 부분 시작점(좌상)에
# # #         # 4개의 keys의 시작점을 갖다 대면 됨.. => 안됨. key의 돌기가 key가운데에만 있을수도...
        
# # #         # 이번 결과 true로 가정하고 체크
# # #         sub_result = 1
        
# # #         for i in range(len(key)):
# # #             for j in range(len(key)):
# # #                 #lock이랑 key 시작점 차이 체크
# # #                 key_init_y_on_lock = y_min_max[0]-matching_point[1]
# # #                 key_init_x_on_lock = x_min_max[0]-matching_point[2]
                
# # #                 if lock[y_min_max[0]+i][x_min_max[0]+j]==key[i][j]:
                    
# # #                     # 돌기끼리 마주치면 false
# # #                     if considering_lock_value==1 and key[i][j] ==1:
# # #                         sub_result = 0
                    
                    
# # #         result.append(sub_result)
                    
                    
            
                
    
    
    
    
# # #     ## 홈이 없는 경우 => square_len = 0 항상 false를 출력해야 함.
    
# # #     ####
# # #     # answer = True
# #     answer = False
# #     # if sum(result)>0:
# #     #     answer = True
# #     return answer



# ## 생각해보니까 굳이 맞는 부분을 grid로 오려서 key랑 lock위치를 맞추고 거기서부터 나머지 부분 key랑 lock가 부딪히는지 체크할 필요 없이,
# ## 그냥 모든 lock부분과 key부분 시작 지점 다르게 하면서 맞춰보면 될 것 같은데.
# # 다만 key를 돌리는 부분은 가져와 쓸만 할 듯

# def solution(key, lock):

    
#     #// 스핀도 잘 못 됐음. 바로 직전걸 또 돌렸어야 했는데
#     keys_spin=[key]
#     for k in range(3):
#         new_key=[[0 for _ in range(len(key))] for _ in range(len(key))]
#         for i in range(len(key)):
#             for j in range(len(key[0])):
#                 new_key[j][len(key)-1-i] = keys_spin[-1][i][j]
#         keys_spin.append(new_key)
        
#     # lock복제
#     same_locks=[]
#     for _ in range(4):
#         new_lock = [[0 for _ in range(len(key))] for _ in range(len(key))]
#         for i in range(len(key)):
#             for j in range(len(key)):
#                 new_lock[i][j] = lock[i][j]
#         same_locks.append(new_lock)
    
#     # 중요한건 lock에서 부딪히냐니까, 
#     result=[0,0,0,0] 
#     for k in range(4): # key spin
#         for i in range(len(lock)):
#             for j in range(len(lock)):
#                 # key_init_pos_on_lock=[i,j]        
#                 sub_result = 1
#                 # 겹치는 부분 외의 lock부분에서 홈이 존재할 때 sub_result = 0
                
#                 for y in range(i):
#                     # x축으로 체크
                    
                    
#                     if sum(lock[y])<len(lock):
#                         sub_result = 0
                        
#                 for x in range(j):
#                     # y축을 체크
                    
#                     if sum(lock[:][x])<len(lock):
#                         sub_result = 0       
                        
                
#                 for p in range(len(key)):
#                     for q in range(len(key)):
#                         # lock안에 있는 key들에 대해
#                         if i+p<len(lock) and j+q<len(lock):
                            
                                
#                             # 하나라도 같은 부분이 만나면 sub_result = 0
#                             if keys_spin[k][p][q] == same_locks[k][i+p][j+q]:
#                                 sub_result = 0
                                
#                             # else: # 홈과 돌기가 만나면 -1 =>lock에 아직 0이 있으면 sub_result = 0
#                             #     same_locks[k][i+p][j+q] = -1
                
                
                            
#                     # 1개라도 성공하면 성공표시        
#                 if sub_result ==1:
                    
                    
#                     result[k] = 1 
#     print(result)
#     answer = False                        
#     if sum(result)>0:
#         answer = True
#     return answer