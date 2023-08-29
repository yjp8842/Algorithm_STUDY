from collections import deque
import sys

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  queue = deque()
  queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
        # 갈 수 있는 땅이면 queue에 추가 & 방문횟수 처리
        if board[nx][ny] == 1:
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
        
        # 갈 수 없는 땅이면 1로 설정
        elif board[nx][ny] == 0: 
          visited[nx][ny] = 1

# bfs 함수 실행
for i in range(N):
  for j in range(M):
    # 목적지 좌표부터 bfs 함수 시작
    if board[i][j] == 2 and visited[i][j] == 0:
      visited[i][j] = 1
      bfs(i, j)

# 결과 출력
for i in range(N):
  for j in range(M):
    if board[i][j] == 0:
      print(0, end=' ')
    else:
      # 원래 갈 수 있는 땅이지만 도달할 수 없는 위치일 때 -1 출력
      if visited[i][j] == 0:
        print(-1, end=' ')
      else:
        # 1부터 시작했으니까 -1 해줘야힘
        print(visited[i][j] - 1, end=' ')
  print()