# xor이 다른 값일 때 1을 주는거였나봄?

# 예시에서 0 은 000, 4는 100으로 보니, 000 xor 100은 100이라 4로 하는 듯.
# 정렬하고 S_i구하는건 쉬운데,
# 문제는 xor임.

# xor을 최대 2500번 해야하는데, 데이터 값이 100만까지니까...
# 뭔가 문자열로 변환해서 하니씩 살펴보며 xor하면 시간초과 날 것 같은데... 대충 2의 20승정도니까 100만단위가.
#     20*2자리를 2500번 살펴보면=> 10만으로 되긴 하네.

# 그럼 비트와이즈 문자열로 바꾸는 작업에 드는 시간은, 하나당 최대 20번쯤으로 잡으면,
#     2500*20이라 괜찮음.
#     알고리즘은,
#         4가 //2...0 , //2...0, //2 ...1 이 되니까
#         arr에는 001이 들어가는데, 얘를 reverse시키고 join으로 합치면 됨.
#     걍 for문으로 몫이 0나올 때까지 돌리면 될 듯.

        
    
# ok갑시다.

# ### 수도코드짜기

# data를 col-1번째 idx에 대해 오름정렬(1차), 2차로는 0th idx대해 내림차순정렬

# def toBitwise(num):
#     result=[]
#     while(num>0인동안)
#         result에 num%2를 append
#         num//=2
    
#     result.reverse()하고
#     result를 join해서 문자열로 만들기
#     ret result
# def toNum(bitString):
#     result=0
#     for i bitString길이만큼
#         if bitStrig i번째가 1이면
#             result+= i**2 
#     ret result

# # data길이에 맞는 S_i 리스트를 만들어서, data각 i번째 row에 대해, row내 모든 값들에 각각 i로 나눈 나머지를 합하고 2진수 문자열로 만들어(toBitwise) 넣기
# s_i=[]
# for i data대해
#     rowsum=0
#     for j row대해
#         rowsum+=data의 [i][j]에 %(i+1) 누적  : 1번부터니까.
    
#     bitString = toBitwise(rowsum) 비트와이즈로 만들기
#     bitString을 s_i에 append

# bitAnswer=s_i의 row_begin번째 스트링
# answer=0

# for i [row_begin+1,row_end]
#     #bitAnswer에 s_i의 i번째에 대해 bitwise XOR
#     nextBitAnswer=''
#     j=0
#     for j min(각각의 길이)대해 (짧은쪽에 일담 맞추고 긴쪽은 따로처리)
#         if bitAnswer이랑 s_i의 i번째 값이 다르면
#             nextBitAnswer에 '1'을 +
#         else: 같응면 
#             '0'을 +
#     j값부터 (위의 for문에서 거친 인덱스 값 바로 다음이어야 함. 체크할 것.)
#     longer = 두 비트 길이 중 긴 것을 longer로 한다. bitAnswer if len이 bit이 더길면 else s_i
#     for j 두 비트의 길이 차이만큼
#         if longer의 j번째가 1일 때는
#             '1'을 +
#         else: 0일 때
#             '0'을 +
#     bitAnswer에 nextBitAnswer값을 덧씌우기
    
            
    
    
    
    







# __ 알고리즘 13분
# __ 수도코드 29분
# __ 엣지 딱히 없음. 구현이라. 32분
#   코드 쓰다가 수정필요 발견. 비트 스트링 뒤에서부터 생각해야함...


def solution(data, col, row_begin, row_end):
    
    data.sort(key=lambda x: (x[col-1],-x[0]))
    # data = sorted(data,key=lambda x: (x[col-1],-x[0]))
    ## test
    # print("정렬된 데이터: ", data)
    
    def toBitwise(num): 
        result=[]
        while(num>0):
            if num%2==1:
                result.append('1')
            else:
                result.append('0')
            num//=2
        result.reverse()
        stringRes=''
        for char in result:
            stringRes+=char
        if len(result)==0:
            stringRes='0'
        return stringRes
    ## test
    # print("toBit잘되나요 4,5,6넣어봄", toBitwise(4), toBitwise(5),toBitwise(6))
    
    
    def toNum(bitString): ## 최대 200번 연산(1+2+...+20) 얘도 뒤에서부터 봐야함.
        result=0
        for i in range(len(bitString)-1,-1,-1):
            if bitString[i]=='1':
                result+=2**(len(bitString)-1-i)
        return result
    ## test
    # print("toNum잘되나요 100,101넣어봄", toNum('100'), toNum('101'))
    
    
    
    s_i=[]
    for i in range(row_begin-1, row_end): ## 필요한 만큼만 
        rowsum=0
        for j in range(len(data[0])):
            rowsum+=data[i][j]%(i+1)
            ## test
            # print("나머지 합 연산후 rowsum, data값, i", rowsum, data[i][j], i+1)
            
        ## test
        # print("rowsum, i", rowsum, i)
        
        bitRowsum = toBitwise(rowsum)
        ## test
        # print("bit된 rowsum: ", bitRowsum)
        
        s_i.append(bitRowsum)
    
    # bitAnswer=s_i[row_begin]
    bitAnswer=s_i[0]
    
    
    # for i in range(row_begin+1, row_end+1):
    for i in range(1,len(s_i)):
        nextBitString=''
        j=0
        ## test
        # print("bitAnswer과 s_i[i]", bitAnswer, s_i[i])
        for j in range(min(len(bitAnswer), len(s_i[i]))):
            
            if bitAnswer[-1-j]!=s_i[i][-1-j]:
                nextBitString='1'+nextBitString ## 순서
            else:
                nextBitString='0'+nextBitString
            
            ## test
            # print('겹치는 영역 nextBitString: ', nextBitString)
        ## 다음 인덱스를 위해
        j+=1
        
        
        ## test
        # print("j, bitAnswer길이, s_i[i]길이, nextBitString, i", j, len(bitAnswer), len(s_i[i]),nextBitString, i )
        
        longer = bitAnswer if len(bitAnswer)>len(s_i[i]) else s_i[i]
        ## test
        # print("longer: ", longer)
        for _ in range(abs(len(bitAnswer)-len(s_i[i]))):
            if longer[-1-j]=='1':
                nextBitString='1'+nextBitString
            else:
                nextBitString='0'+nextBitString
            ## test
            # print("남은부분 nextBitString붙이기, -1-j: ", nextBitString, -1-j, longer[-1-j])
            j+=1
        
        bitAnswer = nextBitString
    
    ## test
    # print("최종 bitAnswer: ", bitAnswer)
    answer = toNum(bitAnswer)
    
    
    return answer