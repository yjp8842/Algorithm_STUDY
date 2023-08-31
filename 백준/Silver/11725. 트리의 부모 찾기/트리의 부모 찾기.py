import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
lists = [0 for _ in range(N + 1)]

for _ in range(N - 1):
  a, b = map(int, sys.stdin.readline().split())
  # 양방향으로 값을 넣어줌
  graph[a].append(b)
  graph[b].append(a)

def bfs(n):
  queue = deque()
  queue.append(n)
  
  while queue:
    node = queue.popleft()
    
    for i in graph[node]:
      if lists[i] == 0:
        queue.append(i)
        lists[i] = node

# 1번부터 노드 순회
bfs(1)

for i in range(2, N + 1):
  print(lists[i])