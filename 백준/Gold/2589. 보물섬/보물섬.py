from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
maps = [list(map(str, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  global ans
  queue = deque()
  queue.append((a, b))
  visited = [[0 for _ in range(M)] for _ in range(N)]
  visited[a][b] = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        # 육지로 이동하여 방문횟수 처리
        if maps[nx][ny] == 'L':
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
  
  ans = max(ans, visited[x][y] - 1)

# 육지인 곳마다 시작점으로 하여 bfs 실행
ans = 0
for i in range(N):
  for j in range(M):
    if maps[i][j] == 'L':
      bfs(i, j)
      
print(ans)