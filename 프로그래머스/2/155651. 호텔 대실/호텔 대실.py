from collections import deque
import heapq
def solution(book_time):
    
    book_time.sort(key=lambda x:x[1]) ## 슈발 key
    
    q = deque(book_time)
    ## test
    # print("Q: ",q)
    
    rooms=[0]
    roomsChecked=[]
    def timeConvert(timeString):
        hh,mm = timeString.split(':')
        return int(mm) + 60*int(hh)
    
    while(q):
        start,end  = q.popleft()
        startTime = timeConvert(start)
        endTime = timeConvert(end)
        ## test
        # print("START TIME, END TIME: ",startTime,endTime)
        
        
        found=False
        rooms.sort()
        rooms.reverse()
        for i in range(len(rooms)):
            ## test
            # print("이번 방 가능시간: ",rooms[i])
            if (rooms[i]<=startTime):
                rooms[i] = endTime+10
                found=True
                ## test
                # print("찾음!")
                break
        if not found:
            rooms.append(endTime+10)
            
        
        
#         roomCheck=False
#         roomLen = len(rooms)
#         for i in range(roomLen):
#             if rooms[i]<=startTime:
#                 rooms[i]  = endTime+10
#                 roomCheck=True
#                 break
        
#         if not roomCheck:
            
            
#             # rooms.append(endTime+10)
#             heapq.heappush(rooms, endTime+10)
#             roomLen+=1
    
    
    answer = len(rooms)
    ## test
    # print("최종 룸 개수: ",answer)
    return answer