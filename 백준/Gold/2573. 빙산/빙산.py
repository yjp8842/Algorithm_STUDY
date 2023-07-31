from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  queue = deque()
  queue.append((a, b))
  visited[a][b] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 내에 있고 탐색하지 않았다면
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
        # 빙산이라면 큐에 추가
        if maps[nx][ny] != 0:
          visited[nx][ny] = 1
          queue.append((nx, ny))

        # 주변이 바닷물이면
        elif maps[nx][ny] == 0 and maps[x][y] > 0:
          maps[x][y] -= 1
  
  # 연결되어 있는 모든 빙산을 탐색했다면
  return 1

year = 0

# 모든 얼음이 녹을 때까지
while 1:
  cnt = 0
  visited = [[0] * M for _ in range(N)]
  
  for i in range(N):
    for j in range(M):
      # 빙산이고, 아직 방문하지 않았다면
      if maps[i][j] != 0 and visited[i][j] == 0:
        cnt += bfs(i, j)
        
  # 빙산이 다 녹았으면
  if cnt == 0:
    year = 0
    break
  
  # 2개 이상으로 쪼개졌다면
  if cnt >= 2:
    break
  
  year += 1
  
print(year)