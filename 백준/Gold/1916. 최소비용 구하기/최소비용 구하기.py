import heapq
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

distance = [int(1e9)] * (N + 1)
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
  
dijkstra(start)
print(distance[end])