from collections import deque

N, M = map(int, input().split())
maps = []
for _ in range(N):
  maps.append(list(map(int, input())))
  
queue = deque()

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # nx, ny가 범위 안에 들어올 때 + 이동할 수 있는 경로 1일 때
      if 0<= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
        queue.append((nx, ny))
        # 계속 1을 더해주며 검사 진행
        maps[nx][ny] = maps[x][y] + 1
  
  # 마지막에 도착하는 부분의 값을 리턴
  return maps[N - 1][M - 1]
  
print(bfs(0, 0))
