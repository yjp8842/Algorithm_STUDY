from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 4중 리스트를 활용
# 빨간 구슬의 좌표와 파란 구슬의 좌표를 같이 확인하기 위함
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]


def move(x, y, idx):
  cnt = 0
  # 구멍이 아니거나, 장애물 또는 벽이 아닐때까지 구슬을 굴려줌
  while board[x + dx[idx]][y + dy[idx]] != '#' and board[x][y] != 'O':
    # 움직인 방향으로 계속해서 공을 굴림
    x += dx[idx]
    y += dy[idx]
    cnt += 1

  return x, y, cnt


def bfs(r1, r2, b1, b2):
  queue = deque()
  queue.append((r1, r2, b1, b2, 1))

  while queue:
    rx, ry, bx, by, cnt = queue.popleft()
    visited[rx][ry][bx][by] = 1

    # 10번 이하로 움직여서 빨간 공을 빼낼 수 없을 때
    if cnt > 10:
      print(-1)
      return

    for i in range(4):
      nrx, nry, rcnt = move(rx, ry, i)
      nbx, nby, bcnt = move(bx, by, i)

      # 파란 구슬이 구멍에 도달하지 않았을 때
      if board[nbx][nby] != 'O':
        # 빨간 구슬이 구멍에 도달했다면
        if board[nrx][nry] == 'O':
          # 카운트 출력해주고 종료
          print(cnt)
          return

        # 빨간 구슬과 파란 구슬이 같은 칸에 있을 경우 재배치해줌
        # 각 구슬의 카운트를 통해 어떤 구슬이 앞에 있던 구슬인지 확인한 후 재배치
        if nrx == nbx and nry == nby:
          if rcnt > bcnt:
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]

        # 방문처리 && queue에 추가
        if visited[nrx][nry][nbx][nby] == 0:
          visited[nrx][nry][nbx][nby] = 1
          queue.append((nrx, nry, nbx, nby, cnt + 1))

  print(-1)
  return


# 빨간 구슬과 파란 구슬의 좌표값을 찾아 bfs 함수에 넣기
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
  for j in range(M):
    if board[i][j] == 'R':
      rx = i
      ry = j
    if board[i][j] == 'B':
      bx = i
      by = j

bfs(rx, ry, bx, by)