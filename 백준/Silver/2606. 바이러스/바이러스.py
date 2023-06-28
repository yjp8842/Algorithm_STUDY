from collections import deque

N = int(input())
M = int(input())
pairs = [list(map(int, input().split())) for _ in range(M)]

graph = [[] * N for _ in range(N + 1)]
for i in range(M):
  graph[pairs[i][0]].append(pairs[i][1])
  graph[pairs[i][1]].append(pairs[i][0])

visited = [0] * (N + 1)

def bfs(now):
  cnt = 0
  queue = deque([now])
  visited[now] = 1

  while queue:
    x = queue.popleft()
    for i in graph[x]:
      if visited[i] == 0:
        visited[i] = 1
        queue.append(i)
        cnt += 1

  return cnt
        
print(bfs(1))