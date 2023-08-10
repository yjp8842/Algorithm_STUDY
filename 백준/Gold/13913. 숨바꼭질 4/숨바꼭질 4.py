from collections import deque

N, K = map(int, input().split())
max_n = 100000
visited = [0] * (max_n + 1)
path = [0] * (max_n + 1)
q = deque()

def bfs():
  q.append(N)
  
  while q:
    x = q.popleft()
    
    if x == K:
      print(visited[x])
      arr = []
      temp = x
      for _ in range(visited[x] + 1):
        arr.append(temp)
        temp = path[temp]
      print(' '.join(map(str, arr[::-1])))
      break
    
    for i in (x - 1, x + 1, x * 2):
      if 0 <= i <= max_n and visited[i] == 0:
        visited[i] = visited[x] + 1
        q.append(i)
        path[i] = x

bfs()