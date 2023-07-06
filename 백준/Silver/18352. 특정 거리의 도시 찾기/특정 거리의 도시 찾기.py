import sys
input = sys.stdin.readline
from collections import deque


N, M, K, X = map(int, input().split())
maps = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  maps[a].append(b)

queue = deque()
visited = [0] * (N + 1)  # 방문 확인
distance = [0] * (N + 1) # 거리 확인
cities = []

def bfs(x):
  queue.append(x)
  visited[x] = 1
  
  while queue:
    x = queue.popleft()
    
    for i in maps[x]:
      if visited[i] == 0:
        visited[i] = 1
        queue.append(i)
        # 방문할 때마다 이전 거리에서 +1
        distance[i] = distance[x] + 1
        
        # 거리가 K가 되면 cities라는 결과 리스트에 추가  
        if distance[i] == K:
          cities.append(i)
  
  # 거리가 K인 도시가 없다면
  if cities == []:
    print(-1)
  else:
    # 오름차순 출력을 위한 sort
    cities.sort()
    for city in cities:
      print(city)
    
bfs(X)