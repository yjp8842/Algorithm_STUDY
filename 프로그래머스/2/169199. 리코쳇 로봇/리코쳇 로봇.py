from collections import deque

def solution(board):
    answer = 0
    
    queue = deque()
    # 위 아래 왼 오른
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[-1 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j))
                visited[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x, y
            
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if board[nx][ny] == 'G':
                    return visited[nx][ny]
                queue.append((nx, ny))
    
    return -1