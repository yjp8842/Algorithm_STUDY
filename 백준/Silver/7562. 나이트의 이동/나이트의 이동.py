from collections import deque


T = int(input())
for _ in range(T):
  I = int(input())
  maps = [[0] * (I) for _ in range(I)]
  a, b = map(int, input().split())
  # maps[a][b] 현재 있는 자리
  c, d = map(int, input().split())
  # maps[x][y] 이동해야 하는 자리

  visited = [[0] * (I) for _ in range(I)]
  queue = deque()

  # 갈 수 있는 8가지의 방향
  dx = [-2, -1, 1, 2, 2, 1, -1, -2]
  dy = [1, 2, 2, 1, -1, -2, -2, -1]

  def bfs(x, y):
    queue.append((x, y))
    
    while queue:
      x, y = queue.popleft()
      
      if x == c and y == d:
        break
      
      for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
          queue.append((nx, ny))
          visited[nx][ny] = 1
          maps[nx][ny] = maps[x][y] + 1
        
        if nx == c and ny == d:
          break
        
    return maps[c][d]

  print(bfs(a, b))