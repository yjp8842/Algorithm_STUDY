from collections import deque


N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def crash_wall(copy_miro, wall, cnt):
#   if wall == cnt:
#     bfs(0, 0)
#     return
  
#   for i in range(N):
#     for j in range(M):
#       if copy_miro[i][j] == 1:
#         copy_miro[i][j] = 1
#         crash_wall(copy_miro, wall + 1, cnt)
#         copy_miro[i][j] = 0

def bfs(a, b):
  queue = deque()
  queue.append((a, b))
  visited = [[0] * N for _ in range(M)]
  visited[a][b] = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
        # 만약 빈 방이라면
        if miro[nx][ny] == 0:
          # 방문 횟수를 이전 횟수로 이어받고, 부순 횟수의 최솟값을 위해 queue의 가장 앞쪽에 넣어주어 그 다음에 바로 탐색할 수 있도록 함
          visited[nx][ny] = visited[x][y]
          queue.appendleft((nx, ny))
        
        # 벽이라면
        else:
          # 이전 횟수에 +1로 방문 횟수를 지정해줌
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
  
  return visited[M - 1][N - 1] - 1
          
print(bfs(0, 0))