N, M, X, Y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

# 방향에 맞게 설정
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

for i in range(K):
  nx = X + dx[orders[i] - 1]
  ny = Y + dy[orders[i] - 1]
  
  if not 0 <= nx < N or not 0 <= ny < M:
    continue
  
  else:
    # 동쪽으로 이동
    if orders[i] - 1 == 0:
      dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 서쪽으로 이동
    elif orders[i] - 1 == 1:
      dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 북쪽으로 이동
    elif orders[i] - 1 == 2:
      dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    # 남쪽으로 이동
    elif orders[i] - 1 == 3:
      dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    # 지도상의 값이 0일 때 주사위 숫자 복사해주기
    if maps[nx][ny] == 0:
      maps[nx][ny] = dice[5]
    # 0이 아닐 때 칸의 숫자를 주사위에 복사 & 칸의 숫자는 0으로
    else:
      dice[5] = maps[nx][ny]
      maps[nx][ny] = 0

  X, Y = nx, ny
  print(dice[0])
  
# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2