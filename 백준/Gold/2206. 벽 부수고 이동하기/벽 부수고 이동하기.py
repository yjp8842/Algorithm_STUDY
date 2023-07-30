from collections import deque


N, M = map(int, input().split())
maps = [] * N
for _ in range(N):
  maps.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
        
def bfs():
  visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
  # visited[x][y][0]은 이동할 수 있는 위치를 방문했을 때의 방문 체크와 횟수
  # visited[x][y][1]은 벽을 뚫고 방문했을 때의 방문 체크와 횟수
  queue = deque()
  queue.append((0, 0, 0))
  visited[0][0][0] = 1
  
  while queue:
    x, y, w = queue.popleft()
    
    if x == N - 1 and y == M - 1:
      return visited[x][y][w]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M:
        # 현재 위치로 이동할 수 있고, 아직 방문하지 않았다면
        if visited[nx][ny][w] == 0 and maps[nx][ny] == 0:
          queue.append((nx, ny, w))
          visited[nx][ny][w] = visited[x][y][w] + 1
        
        # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
        elif maps[nx][ny] == 1 and w == 0:
          visited[nx][ny][w + 1] = visited[x][y][w] + 1
          queue.append((nx, ny, w + 1))
        
  return -1

print(bfs())