# 문제 이해함.
# 그럼 그냥 원형으로 만들필요 없이, 길이 2배로 늘려 하나 더 붙이면 될 것 같은데요

# 79114|79114 이렇게 붙이면,
# 7,9,1,1,4,/7,9,1,1,4랑
# 79,91,11,14,47/,79,...렁
# 791,911,114,147,479/,791,...랑
# 7911,9114,1147,1479,4791,...랑
# 79114/,79114가 나올 것. 
# 어차피 얘네들 중에서도 합을 구해서 중복을 추려야 하기 때문에 set으로 저장시키고.

# 시간 복잡도는 2000+1999+1998,...,2가 될 것임. => 1000^2이니 쌉가능.


def solution(elements):
    double = []
    double.extend(elements)
    double.extend(elements)
    ## ㅅㄷㄴㅅ
    # print("더블: ",double)
    answer = set([])
    
    for i in range(len(double)):
        for j in range(1,len(elements)+1): ## 개수
            if i+j-1>=len(double): break
            subarr = double[i:i+j]
            subres = sum(subarr)
            answer.add(subres)
            ## test
            # print("subarr, subres: ",subarr, subres)
    ## test
    # print("answer: ",answer)
    return len(answer)