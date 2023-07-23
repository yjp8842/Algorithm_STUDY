import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

INF = int(1e9)
# 모든 노드를 거치고, 각 노드의 가중치가 최대인 10이라는 가정하
distance = [INF] * (V + 1)
def dijkstra(start):
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
        
dijkstra(K)

for i in range(1, V + 1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])