# N X N 크기의 땅
# r행 c열에는 A[r][c]명의 인구
# 국경선 공유하는 두 나라의 인구 차 : L먕 이상 & R명 이하
# 연합을 이루고 있는 각 칸의 인구 수 = 연합 인구 수 // 연합 이루고 있는 칸 개수

from collections import deque


N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_map(a, b):
  queue = deque()
  queue.append((a, b))
  visited[a][b] = 1
  
  # 국경선이 열리는 나라들의 좌표 값을 넣을 리스트
  lists = []
  lists.append((a, b))
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        # 두 나라의 인구 차가 L명 이상 R명 이하일 때
        if L <= abs(countries[nx][ny] - countries[x][y]) <= R:
          visited[nx][ny] = 1
          queue.append((nx, ny))
          lists.append((nx, ny))
  
  # 국경선이 열릴 모든 나라들의 좌표값을 담은 리스트 반환
  return lists


days = 0
while True:
  visited = [[0 for _ in range(N)] for _ in range(N)]

  # flag : 0 (열릴 국경선이 없다는 의미)
  # flag : 1 (아직 열릴 국경선이 있다는 의미)
  flag = 0
  for i in range(N):
    for j in range(N):
      if visited[i][j] == 0:
        check_list = check_map(i, j)
        
        totals = 0
        cnt = 0
        
        # (0, 0)을 제외하고 lists에 값이 담겨있어야 하기 때문에
        if len(check_list) > 1:
          flag = 1
          
          # 연합을 이루고 있는 국가들의 인구수 & 국가 개수 
          for x, y in check_list:
            totals += countries[x][y]
            cnt += 1
          
          # 해당 연합 국가들의 인구 수 갱신해주기
          for sx, sy in check_list:
            countries[sx][sy] = totals // cnt

  if flag == 0:
    print(days)
    break
  
  days += 1