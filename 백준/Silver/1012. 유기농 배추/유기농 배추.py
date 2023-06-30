from collections import deque


T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  maps = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    maps[y][x] = 1
  
  # 상 하 좌 우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  visited = [[0] * M for _ in range(N)]

  def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
      x, y = queue.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and visited[nx][ny] == 0:
          queue.append((nx, ny))
          maps[nx][ny] = 0
          visited[nx][ny] = 1
          
    return 1
  
  bugs = 0
  for i in range(N):
    for j in range(M):
      if maps[i][j] == 1:
        bugs += bfs(i, j)

  print(bugs)