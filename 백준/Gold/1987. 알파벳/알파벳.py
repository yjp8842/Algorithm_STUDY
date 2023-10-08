import sys

R, C = map(int, input().split())
maps = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1

# bfs 함수
def bfs():
  global ans
  # 중복되는 것은 제외하기 위한 set 사용
  queue = set([(0, 0, maps[0][0])])
  
  while queue:
    x, y, str = queue.pop()

    # 최댓값으로 갱신
    ans = max(ans, len(str))

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 내에 있고 알파벳이 중복이 안된다면 탐색
      if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] not in str:
        queue.add((nx, ny, maps[nx][ny] + str))

bfs()
print(ans)