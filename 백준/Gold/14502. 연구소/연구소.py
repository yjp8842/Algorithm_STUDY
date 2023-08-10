from collections import deque
import copy
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
virus_l = [list(map(int, input().split())) for _ in range(N)]

# 3개의 벽을 세우기 위한 백트래킹 함수
def three_walls(walls):
  # 벽이 3개 세워졌다면 bfs 함수 실행
  if walls == 3:
    bfs()
    return
  
  for i in range(N):
    for j in range(M):
      # 빈 벽이 있다면
      if virus_l[i][j] == 0:
        # 벽으로 세우기
        virus_l[i][j] = 1
        three_walls(walls + 1)
        # 빈 칸으로 복구
        virus_l[i][j] = 0

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽이 세워진 뒤 바이러스가 퍼진 모습을 구현하기 위한 함수
def bfs():
  global max_cnt
  copy_virus = copy.deepcopy(virus_l)
  queue = deque()
  # 바이러스 리스트를 순회하며 바이러스가 있는 좌표를 queue에 넣음
  for i in range(N):
    for j in range(M):
      if virus_l[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    
    # 상 하 좌 우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 범위 안에 있고, 빈 칸이라면
      if 0 <= nx < N and 0 <= ny < M:
        if copy_virus[nx][ny] == 0:
          queue.append((nx, ny))
          # 바이러스가 퍼졌으므로 2로 갱신
          copy_virus[nx][ny] = 2
  
  cnt = 0
  # 바이러스 리스트를 돌며 빈 칸이 있으면 cnt + 1
  for i in range(N):
    for j in range(M):
      if copy_virus[i][j] == 0:
        cnt += 1

  max_cnt = max(max_cnt, cnt)

max_cnt = 0    
three_walls(0)

print(max_cnt)