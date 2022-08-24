""" n = int(input())
nums = list(map(int, input().split()))
x = int(input())
cnt = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == x:
            cnt += 1
        else:
            continue
        
print(cnt) """

# 시간초과 망할
# 투포인터 알고리즘
n = int(input())
nums = list(map(int, input().split()))
x = int(input())
cnt = 0
a = 0      # 시작 지점
z = n - 1  # 마지막 지점

nums.sort() # 오름차순으로 정렬
while a < z:
    if nums[a] + nums[z] == x: # 두 값을 더해서 x가 나오면
        cnt += 1
        a += 1
        z -= 1
    elif nums[a] + nums[z] < x: # 두 값을 더했는데 x보다 작으면
        a += 1
    else: # 두 값을 더했는데 x보다 크면
        z -= 1

print(cnt)