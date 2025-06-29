from collections import deque

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, time in road:
        graph[a].append((b, time))
        graph[b].append((a, time))
        
    queue = deque()
    queue.append((1, 0))
    visited = [0 for _ in range(N + 1)]
    visited[1] = 1
    
    while queue:
        n, dis = queue.popleft()
        
        for v, t in graph[n]:
            if dis + t <= K:
                if not visited[v] or dis + t <= visited[v]:
                    queue.append((v, dis + t))
                    visited[v] = dis + t
    
    answer = 0
    for i in range(1, N + 1):
        if visited[i] != 0:
            answer += 1
    
    return answer