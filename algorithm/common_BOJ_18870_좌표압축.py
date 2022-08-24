""" N = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(set(nums)) # set으로 중복을 제거

for i in range(len(nums)):
    for j in range(len(sort_nums)):
        if nums[i] == sort_nums[j]:
            nums[i] = j

print(*nums) """

# 낮은 값이 높은 순위를 가짐 (0순위부터)
# 중복되는 값은 같은 순위를 가짐

# len 함수 구현
def len(a_list) :
	cnt = 0
	for _ in a_list:
		cnt += 1
	return cnt

N = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(set(nums)) # 중복을 제외한 값들을 오름차순으로 정렬
num_dict = {}

for i in range(len(sort_nums)):
    num_dict[sort_nums[i]] = i # {-10: 0, -9: 1, 2: 2, 4: 3}

for num in nums:
    print(num_dict.get(num), end=" ") # 값에 해당하는 value값 불러오기