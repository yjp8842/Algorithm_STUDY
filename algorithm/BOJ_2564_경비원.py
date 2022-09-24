import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
K = int(input())
stores = []
for _ in range(K):
    stores.append(list(map(int, input().split())))
dong_d, dong_l = map(int, input().split())

# 상점들의 동서남북 위치에 따른 x, y 좌표 생성
store_xy = []
for i in range(len(stores)):
    if stores[i][0] == 1:
        store_xy.append([0, stores[i][1]])
    if stores[i][0] == 2:
        store_xy.append([M, stores[i][1]])
    if stores[i][0] == 3:
        store_xy.append([stores[i][1], 0])
    if stores[i][0] == 4:
        store_xy.append([stores[i][1], N])

# 동근이의 동서남북 위치에 따른 x, y 좌표
if dong_d == 1:
    dong_xy = [0, dong_l]
if dong_d == 2:
    dong_xy = [M, dong_l]
if dong_d == 3:
    dong_xy = [dong_l, 0]
if dong_d == 4:
    dong_xy = [dong_l, N]

# 최단 거리 구하기    
min_dis = []
sum1 = 0
sum2 = 0
for i in range(len(store_xy)):
    # 동근이와 상점의 위치가 남/북 or 동/서로 반대쪽에 위치했을 때는 왼쪽과 오른쪽 두 방향으로 갈 수 있음
    if abs(dong_xy[0] - store_xy[i][0]) == M or abs(dong_xy[1] - store_xy[i][1]) == N:
        sum1 = sum(dong_xy) + sum(store_xy[i])
        sum2 = (N * 2 + M * 2) - sum1
        
        # 두 방향 중 더 짧은 거리를 넣어줌
        min_dis.append(min(sum1, sum2))
        
    else:
        # sum1 : x 좌표값의 차이
        # sum2 : y 좌표값의 차이
        sum1 = abs(dong_xy[0] - store_xy[i][0])
        sum2 = abs(dong_xy[1] - store_xy[i][1])
        
        # 두 값을 더한 값 : 동근이와 상점의 거리
        min_dis.append(sum1 + sum2)
        
print(sum(min_dis))