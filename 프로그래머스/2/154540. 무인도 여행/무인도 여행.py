from collections import deque

def bfs(a, b, n, m, maps, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((a, b))
    
    day = int(maps[a][b])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                queue.append((nx, ny))
                visited[nx][ny] = 1
                day += int(maps[nx][ny])
        
    return day

def solution(maps):
    answer = []
    n, m = len(maps[0]), len(maps)
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                visited[i][j] = int(maps[i][j])
                answer.append(bfs(i, j, n, m, maps, visited))
                # print(bfs(i, j, n, m, maps, visited))
    
    if answer:
        answer = sorted(answer)
    else:
        answer = [-1]
    
    return answer