import sys

N, M = map(int, sys.stdin.readline().split())
board = [[0] * (N + 1)]

for _ in range(N):
  board.append([0] + [int(x) for x in sys.stdin.readline().split()])

# 가로로 더하기
for i in range(1, N + 1):
  for j in range(1, N):
    board[i][j + 1] += board[i][j]

# 세로로 더하기
for j in range(1, N + 1):
  for i in range(1, N):
    board[i + 1][j] += board[i][j]
        
for _ in range(M):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  # (x1, y1)에서 (x2, y2)까지의 합 = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
  result = board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1]
  print(result)