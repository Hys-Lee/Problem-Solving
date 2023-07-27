# greedy
# 전체가 가장 작은 값이려면
# 부분도 가장 작은 값 -> 다음 -나올 때까지 괄호
#   음수를 가능한한 많이 만들기(음수로 묶기)

# import sys

# input_str = sys.stdin.readline()[:-1]
# input_num_before = input_str.split(sep="+")
# print(input_num_before)
# input_num = []
# for str_line in input_num_before:
#   input_num.extend(list(map(int, str_line.split("-"))))
# print(input_num)

# op = ""

# for i in range(len(input_str)):
#   if input_str[i] == "-" or input_str[i] == "+":
#     op += (input_str[i])

# index = 0
# sub_op = op[0:]
# minus_index = op.find("-")
# result = sum(input_num[:minus_index + 1])

# while (1):
#   minus_index = sub_op.find("-")
#   next_minus_index = sub_op[minus_index + 1:].find("-")
#   if next_minus_index != -1:
#     result += sum(input_num[minus_index + 1:next_minus_index + 1]) * (-1)
#   else:
#     result += sum(input_num[minus_index + 1:]) * (-1)
#     break

# print(result)

### 좀만 더 생각해 보면 사실 2 영역으로 구분할 수 있음을 알 수 있다.
### 앞에서 맨 처음 - 나타날 때까지는 +
### 그 후로 마지막까지는 -를 붙여서 계산하면 끝이다.
###  greedy라서 다음 minus나타날 때까지 -로 계산한다까지만 생각했지만,
### 그 다음 행동까지 생각하면 어차피 그 다음에도 -로 계산한다니까.
### 뒤 행동이 똑같다는 것을 느끼면 2개 영역으로 구분함을 알 수 있음.
# import sys

# input_str = sys.stdin.readline()
# input_arr = []
# num_start_index = 0
# for i in range(len(input_str)):
#   if input_str[i] == "+" or input_str[i] == "-":
#     input_arr.append(int(input_str[num_start_index:i]))
#     input_arr.append(input_str[i])
#     num_start_index = i + 1
# input_arr.append(int(input_str[num_start_index:]))
# print(input_arr)

# first_minus_index = len(input_arr)
# for i in range(len(input_arr)):
#   if input_arr[i] == "-":
#     first_minus_index = i
#     break
# result = 0
# for i in range(0, first_minus_index):
#   if input_arr[i] != "-" and input_arr[i] != "+":
#     result += input_arr[i]
# for i in range(first_minus_index, len(input_arr)):
#   if input_arr[i] != "-" and input_arr[i] != "+":
#     result -= input_arr[i]

# print(result)

### 아니, greedy로 본다면,
### -가 나타날 때마다 끊어 볼 것인데,
#### 결국 -를 기준으로 나머지 수들은 더해주면
###  -로만 분리된 상태가 된다.
###   따라서 이들의 맨 처음 값만 더하고
###   나머지들은 빼서 누적해주면 결과가 나온다.

input_line = input().split('-')
nums = []
for each_one in input_line:
  num = sum(list(map(int, each_one.split("+"))))
  nums.append(num)
result = nums[0]
for i in range(1, len(nums)):
  result -= nums[i]

print(result)
