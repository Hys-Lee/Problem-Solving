# 그냥 길이 최대 5가 고정이니까, 규칙에 따라 값만 찾아내면 되는데?

# 6^5 라고 해도 되지. =2^5*3^5 = 32*243 = 만따리.
# 이러면 그냥 문자열 다 만들고, 정렬시키는 방식으로 해도 되겠는데?
# 0번째는 빈문자열로 하면 되고.

# 그리고 찾는거니까,O(1)로 해도 되겠는데? dict에 저장하면?

# recursoin 함수 만들고,

# 1~5 depth까지 만들고, 내부에선 for돌려서 0~5까지 중에 0은 빈문자열 되게 하고.
# 5depth에 도착하면, array에 일단 넣도록 하자.
# 그리고 정렬 후 dict에 넣어서 찾게 하면 되지 뭐 (아니면 귀찮으니까 걍 찾게 할까? O(1만)으로?)

# 일단 array문자 정렬에서, A다음AA오게 되는지나 체크해봄. -> 되네.. 너무 쉬운데..

### 수도코드만들기

# allWords=[]

# def recur(depth,myword) # depth는 1~5
#   alpha = ['','A','E','I','O','U']
#   if depth==5:
#         allWords.append(myword)
#         return
#   newWord =''
#   for i in range(6)
#     newWord=myword+alpha[i]
#     recur(depth+1, newWord)

#   return

# recur에 (1, '')넘기고 실행하기

# allWords를 sort하기
# mydict=dict([])
# for i in range(len(allWords))
#   mydict[단어] = i 로 인덱스랑 단어 채우기

# return mydict[word]가 정답

# __ 알고 대충 6분
# __ 수도 대충 13분
# __ 엣지는 없다
## 는 개뿔, 겹치는 경우가 꽤 생긴다. A를 만들 때 ''이 계속 붙다가 마지막에 A가 붙든, 처음에 A가 붙든 동일하니까. 그냥 ''를 없애고, 기존거 활용하기 위해서 maxDepth를 props로 넣어 수정하면 될 듯?
def solution(word):
    # tmp=["E","A","AA"]
    # tmp.sort()
    # print(tmp)
    
    allWords=[]
    def recur(depth, myword,maxDepth):
        if depth==maxDepth:
            allWords.append(myword)
            return
        alpha = [ 'A','E','I','O','U']
        newWord=''
        for i in range(len(alpha)):
            newWord = myword+alpha[i]
            recur(depth+1, newWord,maxDepth)
        return
    
    recur(0,'',1)
    ## test
    # print("allWords: ", allWords)
    recur(0,'',2)
    ## test
    # print("allWords: ", allWords)
    recur(0,'',3)
    recur(0,'',4)
    recur(0,'',5)
    allWords.sort()
    ## test
    # print("allWords: ", allWords)
    
    mydict=dict([])
    
    for i in range(len(allWords)):
        mydict[allWords[i]] = i+1## 1번부터 시작
    
    
    
    
    
    answer = mydict[word]
    return answer