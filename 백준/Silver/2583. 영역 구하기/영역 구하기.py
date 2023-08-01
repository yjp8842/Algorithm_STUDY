from collections import deque


M, N, K = map(int, input().split())
squares = [[0 for _ in range(N)] for _ in range(M)]

# 구역 안에 있는 좌표값들은 1로 만들어주기
for i in range(K):
  a, b, c, d = map(int, input().split())
  for i in range(M - b - 1, M - d - 1, -1):
    for j in range(a, c):
      squares[i][j] = 1

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  squares[x][y] = 1
  
  # 0으로 되어 있는 곳들의 숫자를 세기 위한 변수
  ans = 1
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < M and 0 <= ny < N and not squares[nx][ny]:
        queue.append((nx, ny))
        squares[nx][ny] = 1
        ans += 1
  
  # 결과값 리스트에 각 칸들의 숫자를 삽입
  result.append(ans)

# 0으로 되어 있는 곳의 좌표를 기점으로 bfs 함수 실행
for i in range(M):
  for j in range(N):
    if squares[i][j] == 0:
      bfs(i, j)

# 오름차순으로 출력하기 위한 정렬
result.sort()
print(len(result))

for size in result:
  print(size, end=' ')