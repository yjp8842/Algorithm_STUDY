from collections import deque


N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hour = 0

def bfs(a, b):
  queue = deque()
  queue.append((a, b))
  visited = [[0 for _ in range(M)] for _ in range(N)]
  visited[0][0] = 1
    
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
        # 치즈라면 공기와 닿아있다는 의미로 +1
        if cheeze[nx][ny] != 0:
          cheeze[nx][ny] += 1
        
        # 공기일 경우 방문 체크 & queue에 넣어주기
        else:
          visited[nx][ny] = 1
          queue.append((nx, ny))

while 1:
  bfs(0, 0)

  flag = 0
  for i in range(N):
    for j in range(M):
      # 2개 이상의 공기와 접촉되어 있다면 (원래 치즈가 있는 칸이 1로 채워져있으므로)
      if cheeze[i][j] >= 3:
        cheeze[i][j] = 0
        
      elif 0 < cheeze[i][j] <= 2:
        flag = 1
        # 원래 치즈의 상태로 초기화
        cheeze[i][j] = 1
        
  hour += 1

  # 모든 치즈가 다 녹았다면
  if flag == 0:
    print(hour)
    break