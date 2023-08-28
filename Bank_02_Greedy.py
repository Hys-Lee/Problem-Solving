# 최대한 큰 수 만들기
# 각 연산에서 최대한 크게 만들기 -> 최종 결과 max됨.
# greedy인듯
# 각 연산에서 최대한 크려면,
# 0과 1을 만날 때는 +
# 나머지는 * 으로 해주기.abs

s = input()
result = 0
for i in range(len(s)):
  # 연산 대상인 2개 중 하나라도 0,1이면 합
  next = int(s[i])
  # print("next: ", next, "result: ", result)
  if next > 1 and result > 1:
    result *= next
  else:
    result += next

print(result)
