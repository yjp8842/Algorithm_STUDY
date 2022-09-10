a_list = str(input())

# 중복을 제외한 값만 출력해야 하기 때문에 set 사용
subsets = set()
size = len(a_list)

for i in range(size):
    for j in range(i, size):
        subsets.add(a_list[i:j + 1])

print(len(subsets))