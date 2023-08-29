from collections import deque


M, N, K = map(int, input().split())
maps = [[list(map(int, input().split())) for _ in range(N)] for _ in range(K)]

# 위 아래 앞 뒤 좌 우를 모두 확인하기 위함
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
  queue = deque()
  # 삼중리스트를 통해 위아래앞뒤좌우를 함께 확인
  visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K)]
  
  # 익은 토마토일 경우 queue에 넣어주기
  for i in range(K):
    for j in range(N):
      for k in range(M):
        if maps[i][j][k] == 1 and visited[i][j][k] == 0:
          queue.append((i, j, k))
          visited[i][j][k] = 1
          
  while queue:
    x, y, z = queue.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      
      # 범위 안에 있고, 아직 익지 않은 토마토이고, 방문하지 않았을 경우 queue에 추가
      if 0 <= nx < K and 0 <= ny < N and 0 <= nz < M and maps[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
        queue.append((nx, ny, nz))
        maps[nx][ny][nz] = maps[x][y][z] + 1
        visited[nx][ny][nz] = 1

bfs()

# bfs 함수 실행 후 토마토 확인
days = 0
flag = 0
for lists in maps:
  for list in lists:
    # 아직 익지 않은 토마토가 있을 경우
    if 0 in list:
      flag = 1
      break
    
    days = max(days, max(list))

if flag == 0:
  print(days - 1)
else:
  print(-1)