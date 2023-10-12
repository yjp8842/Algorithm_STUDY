from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    
    queue = deque()
    queue.append(1)
    dist = [0] * (n + 1)
    dist[1] = 1
    
    while queue:
        num = queue.popleft()
        
        for i in graph[num]:
            if dist[i] == 0:
                queue.append(i)
                dist[i] = dist[num] + 1
    
    cnt = 0
    for i in dist:
        if i == max(dist):
            cnt += 1
    
    return cnt