# bans에 있는 애들의 원본 주문서에서의 순서를 각각 알아내면 되지 않음?
# 일단 정렬도 해두고.

# n이 이 순서들에서 어느 위치에 있는지 일단 알아내야지.
# 그리고, bans들 중 n안쪽에 있는 개수만큼 일단 실제 찾는 target은 n에서 +해야지.
# 이 때, target이랑 n뒤쪽에 있는 bans비교해서, 
# target보다 작은게 존재한다면, 역시 그 개수만큼 target은 +하기
# ㄴ> target보다 남은 애들 중 작은개 존재하지 않을 때까지 반복.

# 이후 원본에서 target번째를 만들어내면 됨.

# 그럼, 어떻게 만드냐 그리고 어케 순서를 알아내냐?
# 이거 사실상 알파벳 개수 만큼의 진수잖음.
# 26개. 그러면 26진수임.

# 1번째부터 새고 있으니까, 고려하면.
# 그럼 뭐, ["a",...]이렇게 26길이 arr만들어두고,
# 주분->순서 만들어내는건, (26^0*알파벳맨뒷자리) + ... +1 (순서는 1부터 시작) 이런 느낌이네.
# 순서->주문은 -1뺀 후  26으로 계속 나누면서 몫이 0나올 때까지 나머지 저장하면 구할 수 있지.
#   q로 저장해서 처리하면 깔끔함. 처음은 26진수의 0승, 다음은 1승... 이런 식이니까.

# 2ㄴ24
# 2ㄴ12 ...0
# 2ㄴ6 ...0
# 2ㄴ3 ...0
# 2ㄴ1 ...1
#    0 ...1
           
# -> 1 1 0 0 0

# ## 수도코드만들기
# 알파벳 그냥 수동으로 정리하자. 아스키 변환 함수를 몰라서 ㅎㅎ
# alphabets=["a",...] 26개임.
# seqForAlpha=dict([])
# for i  alphabets길이 대해
#  seqForAlpha[alphabets[i]] = i로 매핑하기
    
# def spellToSeq (주문)
#   seq = 1 : 1부터시작
    # 주문을 list로 만들기
    # 주문 리스트를 뒤집기
#   for i in 주문 개수 : 거꾸로해야 맞다.
#     seq += seqForAlpha[주문리스트[i]] ** (26*i)
#   return seq

# def seqToSpell(seq)
#     인덱스값들 = []
#     while (seq가 0될 때까지)
#         seq%26을 인덱스값들에 추가
#         seq//=26
#     인덱스들 reverse() :문자열 순서대로
#     주문=[]: 캐릭터 하나씩 담을거임.
#     for 인덱스값들
#       주분.append(alphabets[인덱스값])
#     return "".join(주문)

# bansSeq=[]
# for bans들
#   bansSeq.append를 spellToSeq(ban)에 대해
# bansSeq를 sort하기 : 오름차순

# target=n초기화
# bansSeqI = 0
# while(bansSeqI<bansSeq길이) : 일단 명시적이지. target이 다 뛰어넘을수도 있으니까.
#   if bansSeqI에서 값이 target보다 작다면
#     bansSeqI+=1
#     target+=1
#   else
#     break

# seqToSpell로 target번째 주문 찾아 반환.

# __ 알고 대충 10분?
# __ 수도 대충 35분?
# __ 엣지 대충.. 시간 복잡도는 대충 백만단위. 맞는 듯. 40분?
 

def solution(n, bans):
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    seqForAlphabets=dict([])
    for i in range(len(alphabets)):
        seqForAlphabets[alphabets[i]] = i
    
    def spellToSeq(spell): ## 순서 개념이 좀 꼬였는디..
        seq  =0
        spellList = list(spell)
        ## test
        spellList.reverse()
        # print("spellList: ",spellList)
        for i in range(len(spell)):
            ## test
            seq+=26**i*(seqForAlphabets[spellList[i]]+1)
        
        return seq
    
#     잠만, 순서는 a는 1번째, z는 26번째, aa는 27번째, 
    
#     간추려서, a,b,c,d,만존재한다치면
#     a,b,c,d,aa,ab,ac,ad,ba, bb, bc, bd
#     1,2,3,4,5, 6, 7, 8, 9,  10, 11, 12,
    
    # print("seq: ", spellToSeq("ba"))
    
    def seqToSpell(seq):
        
        idxs=[]
        # if seq==0:
        #     idxs.append(seq)
        while(seq>0): ## 0들어올 때가 엣지였음.
            seq-=1 ## 1부터 시작을 0기준으로 맞췄어야지
            idxs.append(seq%26)
            seq//=26
        idxs.reverse()
        ## test
        # print("idxs: ",idxs)
        spellChrs=[]
        for i in idxs:
            spellChrs.append(alphabets[i])
        spell = "".join(spellChrs)
        return spell
    
    # print("spell",seqToSpell(53))
    
    bansSeq = []
    for b in bans:
        bansSeq.append(spellToSeq(b))
    bansSeq.sort()
    ## test
    # print("bansSeq정렬: ",bansSeq)
    
    target = n
    bansSeqI = 0
    while(bansSeqI<len(bansSeq)):
        if bansSeq[bansSeqI] <= target:
            bansSeqI+=1
            target+=1
        else:
            break
    ## test
    # print("target: ", target)
    
    answer = seqToSpell(target)
    
    return answer