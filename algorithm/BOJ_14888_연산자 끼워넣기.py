from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

lst = ['+', '-', '*', '/']
# 연산자의 개수만큼 하나의 리스트에 다 넣어주기
op_list = []
for _ in range(operator_list[0]):
    op_list.append('+')
for _ in range(operator_list[1]):
    op_list.append('-')
for _ in range(operator_list[2]):
    op_list.append('*')
for _ in range(operator_list[3]):
    op_list.append('/')

# 생성할 수 있는 순열 구하기
if len(op_list) == 1:
    perm_op = op_list
else:
    perm_op = list(permutations(op_list, len(op_list))) 

cal_l = []
max_n = 0
min_n = 0
for j in range(len(perm_op)):
    num = num_list[0]
    for k in range(len(perm_op[j])):
        if perm_op[j][k] == '+':
            num += num_list[k + 1]  
        elif perm_op[j][k] == '-':
            num -= num_list[k + 1]
        elif perm_op[j][k] == '*':
            num *= num_list[k + 1]
        elif perm_op[j][k] == '/':
            if num >= 0:
                num //= num_list[k + 1]
            else:
                num = -(num) // num_list[k + 1]
                num = -num
    
    cal_l.append(num)

print(max(cal_l))
print(min(cal_l))