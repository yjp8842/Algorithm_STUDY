# 비교대상 두 개의 노드를 받았을 때
# 한 개의 노드에서 출발해서
# 다른 한 개의 노드에 도착할 때까지의 횟수를 출력
from collections import deque


n = int(input())
p, q = map(int, input().split())
m = int(input())
maps = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  maps[a].append(b)
  maps[b].append(a)
  
queue = deque()
visited = [0] * (n + 1)

def bfs(x):
  queue.append(x)
  visited[x] = 1
  
  while queue:
    x = queue.popleft()
    
    for i in maps[x]:
      if visited[i] == 0:
        # 방문 처리 & 횟수를 한 번에 처리
        visited[i] = visited[x] + 1
        queue.append(i)
        
        if i == q:
          return visited[i] - 1
  
  # 만약 queue가 비었는데 q에 방문하지 못했다면
  # 친척 관계가 전혀 없다는 뜻 (연결되어있지 않다)
  if visited[q] == 0:
    return -1

print(bfs(p))