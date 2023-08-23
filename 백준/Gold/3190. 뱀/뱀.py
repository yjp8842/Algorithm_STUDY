from collections import deque


N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
  x, y = map(int, input().split())
  # 사과가 위치한 좌표 칸을 구분하기 위해 2로 채우기
  # 행, 열로 입력받아오므로 -1 해주기
  board[x - 1][y - 1] = 2

L = int(input())
direct = [0] * 100000
for _ in range(L):
  time, direction = input().split()
  direct[int(time)] = direction

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가장 처음 뱀은 오른쪽으로 이동하므로 해당 인덱스로 초기화
start = 3
# 뱀의 처음 위치
snake_x, snake_y = 0, 0
queue = deque()
# 양방향리스트를 통해 뱀의 꼬리가 있는 칸의 좌표부터 뱀의 머리가 있는 칸의 좌표까지를 담을 예정
queue.append((0, 0))
times = 0

while 1:
  nx = snake_x + dx[start]
  ny = snake_y + dy[start]
  
  if 0 > nx or nx >= N or 0 > ny or ny >= N or (nx, ny) in queue:
    print(times + 1)
    break
  
  # 범위 안에 있고, 자기 자신과 부딪히지 않았을 경우
  if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in queue:
    # 이동할 칸이 사과가 있는 칸이라면
    if board[nx][ny] == 2:
      # queue에 추가 & 사과가 있던 칸을 0으로 만들어주기
      queue.append((nx, ny))
      board[nx][ny] = 0
    
    # 이동할 칸에 사과가 없다면
    else:
      # queue에 추가 & 꼬리가 있던 칸 (즉, queue에서 맨 왼쪽에 있는 칸) 빼주기
      queue.append((nx, ny))
      queue.popleft()
  
  # 이동한 칸을 새로운 시작 칸으로 갱신
  snake_x, snake_y = nx, ny
  times += 1
  
  # X초 (==times)가 끝난 뒤 왼쪽으로 방향 전환해야 한다면
  if direct[times] == 'L':
    if start == 0:
      start = 2
    elif start == 1:
      start = 3
    elif start == 2:
      start = 1
    elif start == 3:
      start = 0

  # X초 (==times)가 끝난 뒤 오른쪽으로 방향 전환해야 한다면
  if direct[times] == 'D':
    if start == 0:
      start = 3
    elif start == 1:
      start = 2
    elif start == 2:
      start = 0
    elif start == 3:
      start = 1