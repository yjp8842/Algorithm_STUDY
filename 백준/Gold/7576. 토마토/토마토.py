from collections import deque


M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  for i in range(N):
    for j in range(M):
      if maps[i][j] == 1:
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
        queue.append((nx, ny))
        maps[nx][ny] = maps[x][y] + 1
  
  for list in maps:
    # 한 줄씩 돌며 0이 있으면 (안 익은 토마토가 있다면) -1 리턴
    if 0 in list:
      return -1

  # 안 익은 토마토가 없다면
  # 최댓값에서 -1 빼고 리턴 (1부터 시작했기 때문에)
  return max(map(max, maps)) - 1

print(bfs())