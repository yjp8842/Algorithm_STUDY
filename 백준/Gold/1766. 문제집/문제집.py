# 위상 정렬 알고리즘을 통해 풀어야 하는 문제
import heapq

N, M = map(int, input().split())
indegree = [0] * (N + 1)  # 진입차수를 나타내는 리스트
lists = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  lists[a].append(b)
  indegree[b] += 1

queue = []
for i in range(1, N + 1):
  # 진입차수가 0이 되는 정점이 있다면
  if indegree[i] == 0:
    heapq.heappush(queue, i)

result = []
while queue:
  now = heapq.heappop(queue)
  result.append(now)

  for i in lists[now]:
    # 간선 제거
    indegree[i] -= 1
    
    # 진입차수가 0이 되는 정점이 있다면
    if indegree[i] == 0:
      heapq.heappush(queue, i)
  
for res in result:
  print(res, end=" ")