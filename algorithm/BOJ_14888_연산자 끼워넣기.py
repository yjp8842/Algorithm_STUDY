def perm(arr, n):
    answer = []
    if n > len(arr):
        return answer

    if n == 1:
        for i in arr:
            answer.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in perm(ans, n - 1):
                answer.append([arr[i]] + j)

    return answer

N = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

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
    perm_op = list(set(list(map(tuple, perm(op_list, len(op_list))))))

cal_l = []
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