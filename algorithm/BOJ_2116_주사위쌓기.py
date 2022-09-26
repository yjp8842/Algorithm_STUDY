# 2116_주사위 쌓기

# 밑면이 정해졌을 때 옆면의 최댓값을 구하는 함수
def dice_max(i, idx):
    if idx == 0 or idx == 5:
        return max(dice[i][1], dice[i][2], dice[i][3], dice[i][4])
    if idx == 1 or idx == 3:
        return max(dice[i][0], dice[i][2], dice[i][4], dice[i][5])
    if idx == 2 or idx == 4:
        return max(dice[i][0], dice[i][1], dice[i][3], dice[i][5])

N = int(input())
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

top = 0
bottom = 0
sums = 0
# 밑면이 정해졌을 때 나올 수 있는 값들을 넣어줄 리스트
sum_list = []
# 각각의 짝이 되는 인덱스 값을 넣어줌
# (0 - 5) | (1 - 3) | (2 - 4)
p = [5, 3, 4, 1, 2, 0]

# 1번 주사위의 bottom이 0번 인덱스 값일때
bottom = dice[0][0]
top = dice[0][5]
sums += dice_max(0, 0)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    # 이전 주사위의 top이 현재 주사위의 bottom이 되어야 함
    # 현재 주사위에서 top의 값을 가지고 있는 인덱스를 구함
    # 이하 동일
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 0번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)

sums = 0
# 1번 주사위의 bottom이 1번 인덱스 값일때
bottom = dice[0][1]
top = dice[0][3]
sums += dice_max(0, 1)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 1번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)
    
sums = 0
# 1번 주사위의 bottom이 2번 인덱스 값일때
bottom = dice[0][2]
top = dice[0][4]
sums += dice_max(0, 2)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 2번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)
    
sums = 0
# 1번 주사위의 bottom이 3번 인덱스 값일때
bottom = dice[0][3]
top = dice[0][1]
sums += dice_max(0, 3)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 3번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)
    
sums = 0
# 1번 주사위의 bottom이 4번 인덱스 값일때
bottom = dice[0][4]
top = dice[0][2]
sums += dice_max(0, 4)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 4번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)
    
sums = 0
# 1번 주사위의 bottom이 5번 인덱스 값일때
bottom = dice[0][5]
top = dice[0][0]
sums += dice_max(0, 5)
# 2번 ~ N번까지의 주사위일때
for i in range(1, N):
    k = dice[i].index(top)
    bottom = dice[i][k]
    top = dice[i][p[k]]
    sums += dice_max(i, k)
# 1번 주사위의 bottom이 5번 인덱스 값일때 나오는 최댓값들의 합을 넣어줌
sum_list.append(sums)

# 담아져 있는 값들 중 최댓값을 뽑으면 됨 !
print(max(sum_list))