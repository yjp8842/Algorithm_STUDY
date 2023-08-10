from collections import deque
import copy


N = int(input())
maps = [list(map(str, input())) for _ in range(N)]
re_maps = copy.deepcopy(maps)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일반인 bfs
visited = [[0 for _ in range(N)] for _ in range(N)]
def bfs(a, b, color):
  queue = deque()
  queue.append((a, b))
  visited[a][b] = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maps[nx][ny] == color:
        queue.append((nx, ny))
        visited[nx][ny] = 1
  
  return 1

# 적록색약 bfs
re_visited = [[0 for _ in range(N)] for _ in range(N)]
def re_bfs(a, b, color):
  queue = deque()
  queue.append((a, b))
  re_visited[a][b] = 1
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0 <= nx < N and 0 <= ny < N and not re_visited[nx][ny] and re_maps[nx][ny] == color:
        queue.append((nx, ny))
        re_visited[nx][ny] = 1
  
  return 1

# 적록색약인 사람이 보는 새로운 맵 만들기
for i in range(N):
  for j in range(N):
    if re_maps[i][j] == 'R':
        re_maps[i][j] = 'G'

cnt = 0
re_cnt = 0
# 각각 bfs 진행
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      cnt += bfs(i, j, maps[i][j])
    if not re_visited[i][j]:
      re_cnt += re_bfs(i, j, re_maps[i][j])
      
      
print(cnt, re_cnt)