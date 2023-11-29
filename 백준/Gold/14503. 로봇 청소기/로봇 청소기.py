N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
nr, nc, nd = r, c, d

while True:
  if board[nr][nc] == 0:
    board[nr][nc] = 2
    cnt += 1
  
  elif board[nr - 1][nc] > 0 and board[nr][nc - 1] > 0 and board[nr + 1][nc] > 0 and board[nr][nc + 1] > 0:
    if nd == 0:
      if board[nr + 1][nc] != 1:
        nr, nc = nr + 1, nc
      else:
        break
    elif nd == 1:
      if board[nr][nc - 1] != 1:
        nr, nc = nr, nc - 1
      else:
        break
    elif nd == 2:
      if board[nr - 1][nc] != 1:
        nr, nc = nr - 1, nc
      else:
        break
    else:
      if board[nr][nc + 1] != 1:
        nr, nc = nr, nc + 1
      else:
        break
    
  else:
    if nd == 0:
      nd = 3
      if board[nr][nc - 1] == 0:
        nr, nc = nr, nc - 1
    elif nd == 1:
      nd = 0
      if board[nr - 1][nc] == 0:
        nr, nc = nr - 1, nc
    elif nd == 2:
      nd = 1
      if board[nr][nc + 1] == 0:
        nr, nc = nr, nc + 1
    else:
      nd = 2
      if board[nr + 1][nc] == 0:
        nr, nc = nr + 1, nc
        
  # if nr < 0 or nr >= N or nc < 0 or nc >= M:
print(cnt)