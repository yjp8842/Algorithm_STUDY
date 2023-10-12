from collections import deque

def solution(n, computers):            
    answer = 0
    visited = [0] * n

    def bfs(a, visited, computers):
        visited[a] = 1
        queue = deque([a])
        
        while queue:
            x = queue.popleft()
            
            for i in range(n):
                if computers[x][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = 1

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1

    return answer