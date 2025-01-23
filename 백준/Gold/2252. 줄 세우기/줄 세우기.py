# -*- coding: utf-8 -*-
# 위상정렬 문제

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
lines = []

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    in_degree[B] += 1 # 진입차수 저장

# 진입차수가 0인 정점 큐에 저장
q = deque()
for n in range(1, N + 1):
    if in_degree[n] == 0:
        q.append(n)

while q:
    n = q.popleft()
    lines.append(n)
    
    for edge in graph[n]:
        in_degree[edge] -= 1 # 인접한 간선 제거 & 진입차수 제거
        if in_degree[edge] == 0: # 진입차수가 0이 되면 또 큐에 저장장
            q.append(edge)
            
print(*lines)