from collections import deque

def bfs_start_to_lever(a, b, n, m, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[a][b] = 1
    
    queue = deque()
    queue.append((a, b))
    
    flag = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
                if maps[nx][ny] == 'L':
                    return visited[nx][ny]
                
def bfs_lever_to_end(a, b, n, m, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[a][b] = 1
    
    queue = deque()
    queue.append((a, b))
    
    flag = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
                if maps[nx][ny] == 'E':
                    return visited[nx][ny]

def solution(maps):
    answer_1 = 0
    answer_2 = 0
    n, m = len(maps[0]), len(maps)
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                if bfs_start_to_lever(i, j, n, m, maps):
                    answer_1 += bfs_start_to_lever(i, j, n, m, maps) - 1
                else:
                    return -1
            elif maps[i][j] == 'L':
                if bfs_lever_to_end(i, j, n, m, maps):
                    answer_2 += bfs_lever_to_end(i, j, n, m, maps) - 1
                else:
                    return -1
    
    return answer_1 + answer_2