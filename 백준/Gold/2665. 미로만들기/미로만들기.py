from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().strip())) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  queue = deque()
  queue.append((0, 0))
  visited = [[0] * N for _ in range(N)]
  visited[0][0] = 1
  
  while queue:
    x, y = queue.popleft()
    
    if x == N - 1 and y == N - 1:
      return visited[x][y] - 1
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
        # 흰 방일 경우
        if maps[nx][ny] == 1:
          # queue의 가장 첫 번째로 넣어주기
          queue.appendleft((nx, ny))
          visited[nx][ny] = visited[x][y]
        else:
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1

print(bfs())