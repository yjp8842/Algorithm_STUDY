N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

for _ in range(S):
# 현재 위치해있는 바이러스의 좌표값 찾기
# 바이러스의 번호 순서대로 !
    xy_list = []
    for x in range(N):
        for n in range(1, K + 1):
            if n in arr[x]:
                y = arr[x].index(n)
                xy_list.append([x, y])

    # 상 하 좌 우
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(K):
        cr = xy_list[i][0]
        cc = xy_list[i][1]
        for j in range(N + 1):
            nr = cr + dr[j]
            nc = cc + dc[j]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = arr[cr][cc]
    print(xy_list)
    print(arr)