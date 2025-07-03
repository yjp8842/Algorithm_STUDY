N = int(input())
nums = set(map(int, input().split()))
M = int(input())
check_lst = list(map(int, input().split()))

for check in check_lst:
    if check in nums:
        print(1)
    else:
        print(0)