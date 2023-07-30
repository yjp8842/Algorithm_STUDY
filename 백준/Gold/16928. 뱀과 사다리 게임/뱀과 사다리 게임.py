from collections import deque


N, M = map(int, input().split())
info = [i for i in range(101)]
# 사다리에 대한 정보를 info에 담기
for _ in range(N):
  x, y = map(int, input().split())
  info[x] = y
  
# 뱀에 대한 정보를 info에 담기
for _ in range(M):
  u, v = map(int, input().split())
  info[u] = v

def bfs(start):
  queue = deque()
  queue.append(start)
  # 방문 여부와 횟수를 함께 체크하기 위한 리스트
  visited = [0] * 101
  visited[start] = 1
  
  while queue:
    num = queue.popleft()
    
    if num == 100:
      print(visited[num] - 1)
      break
    
    for i in range(1, 7):
      # 다음에 이동해야 할 칸의 숫자
      next = num + i
      if next <= 100 and visited[next] == 0:
        # 만약 사다리나 뱀이 있는 칸이라면
        if info[next] != 0:
          next = info[next]
        
        if visited[next] == 0:
          visited[next] = visited[num] + 1
          queue.append(next)

bfs(1)