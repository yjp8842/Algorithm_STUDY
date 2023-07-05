from collections import deque

def dfs(x):
  visited_2[x] = 1        
  print(x, end = " ")
  for i in range(1, N + 1):
    if visited_2[i] == 0 and graph[x][i] == 1:
      dfs(i)
    
def bfs(x):
  q = deque()
  q.append(x)       
  visited_1[x] = 1   
  while q:
    x = q.popleft()
    print(x, end = " ")
    for i in range(1, N + 1):
      if visited_1[i] == 0 and graph[x][i] == 1:
        q.append(i)
        visited_1[i] = 1

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)] 
visited_1 = [0] * (N + 1)
visited_2 = [0] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)