###
# 테스트 케이스 때 운 좋았다
#  숫자 없는 입력 경우 체크해봤음.
###

s = input()

askii_from_s = []
print(ord("Z"))
print(ord("9"))
num_end_askii = ord("9")
is_there_num = False
num_sum = 0
for i in range(len(s)):
  if ord(s[i]) > num_end_askii:
    askii_from_s.append(ord(s[i]))
  else:
    is_there_num = True
    num_sum += int(s[i])

askii_from_s.sort()

for i in range(len(askii_from_s)):
  print(chr(askii_from_s[i]), end="")
if is_there_num:
  print(num_sum)
# # print(a.sort())
