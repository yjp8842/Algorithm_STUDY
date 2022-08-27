import sys
sys.stdin = open('input.txt', 'r')

def my_len(arr):
    cnt = 0
    for _ in arr:
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    x = y = 0
    direction = 0
    num = 1

    arr[0][0] = 1
    arr[0][N] = -1
    arr[N][N - 1] = -1
    arr[N - 1][-1] = -1

    while True:
        if num < N * N:

            if direction == 0:
                if arr[x][y + 1] == 0:
                    y += 1
                    num += 1
                    arr[x][y] = num
                else:
                    direction = 1

            if direction == 1:
                if arr[x + 1][y] == 0:
                    x += 1
                    num += 1
                    arr[x][y] = num
                else:
                    direction = 2

            if direction == 2:
                if arr[x][y - 1] == 0:
                    y -= 1
                    num += 1
                    arr[x][y] = num
                else:
                    direction = 3

            if direction == 3:
                if arr[x - 1][y] == 0:
                    x -= 1
                    num += 1
                    arr[x][y] = num
                else:
                    direction = 0

        if num == N * N:
            break

    print("#{}".format(tc))
    for i in range(my_len(arr) - 1):
        for j in range(my_len(arr) - 1):
            print(arr[i][j], end=' ')
        print()