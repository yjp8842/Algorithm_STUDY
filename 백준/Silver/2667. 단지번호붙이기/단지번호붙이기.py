from collections import deque


N = int(input())
maps = [list(map(int, input())) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
visited = [[0] * N for _ in range(N)]

def bfs(x, y):
  queue.append((x, y))
  cnt = 0
  visited[x][y] = 1
  
  while queue:
    x, y = queue.popleft()
    cnt += 1
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1 and visited[nx][ny] == 0:
        queue.append((nx, ny))
        maps[nx][ny] = 0
        visited[nx][ny] = 1
        
  return cnt

result = []
towns = 0
for i in range(N):
  for j in range(N):
    if maps[i][j] == 1:
      result.append(bfs(i, j))
      towns += 1

print(towns)
result.sort()
for i in range(towns):
  print(result[i])