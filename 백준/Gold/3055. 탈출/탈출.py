from collections import deque


R, C = map(int, input().split())
lists = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물의 좌표를 찾아 인접해있는 곳이 비어있는 곳이면 물로 만들어주는 함수
def flood():
  water = deque()
  
  for i in range(R):
    for j in range(C):
      if lists[i][j] == '*' and not visited[i][j]:
        water.append((i, j))
        visited[i][j] = 1

  while water:
    x, y = water.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
        if lists[nx][ny] == '.':
          lists[nx][ny] = '*'

# 고슴도치가 한 번 이동할 때마다 물로 바꿔주는 함수도 동시에 진행
def bfs(a, b):
  queue = deque()
  
  queue.append((a, b))
  visited[a][b] = 1
  
  while queue:  
    flood()
    
    for _ in range(len(queue)):
      x, y = queue.popleft()
      
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
          # 고슴도치가 이동할 수 있는 곳이면 queue에 삽입
          if lists[nx][ny] == '.':
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            
          # 비버의 동굴에 도착했다면 횟수 리턴
          elif lists[nx][ny] == 'D':
            return visited[x][y]
  
  return "KAKTUS"

# 고슴도치가 있는 곳부터 bfs 실행
for i in range(R):
  for j in range(C):
    if lists[i][j] == 'S':
      print(bfs(i, j))
