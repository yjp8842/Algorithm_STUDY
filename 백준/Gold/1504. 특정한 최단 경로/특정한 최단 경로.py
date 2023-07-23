import heapq
import sys
input = sys.stdin.readline


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
  distance = [int(1e9)] * (N + 1)
  queue = []
  # (가중치, 시작점)으로 queue에 push
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  while queue:
    dist, now = heapq.heappop(queue)

    # 현재 노드에서의 거리가 뽑아낸 가중치보다 이미 작은 것으로 되어있다면 확인할 필요 X 
    if distance[now] < dist:
      continue

    # 현재 노드와 연결된 인접 노드 확인
    for i in graph[now]:
      # i[1] => i[0]으로 가기 위한 노드의 가중치
      cost = dist + i[1]
      # 만약 cost가 i[0]으로 가기 위해 현재 거리 그래프에 저장된 가중치보다 작다면
      if cost < distance[i[0]]:
        # i[0]으로 가기 위한 거리를 cost로 변경
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

  return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= int(1e9) and path2 >= int(1e9):
  print(-1)
else:
  print(min(path1, path2))
