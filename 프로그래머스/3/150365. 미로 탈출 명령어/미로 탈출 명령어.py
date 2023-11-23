from collections import deque

def solution(n, m, x, y, r, c, k):
    board = [[0] * m for _ in range(n)]
    board[x - 1][y - 1] = 'S'
    board[r - 1][c - 1] = 'E'
    
    def bfs(a, b, dr, dc):
        # 하d 좌l 우r 상u
        dx = [1, 0, 0, -1]
        dy = [0, -1 ,1, 0]
        dirs = ['d', 'l', 'r', 'u']

        queue = deque()
        queue.append((a, b, '', 0))

        while queue:
            x, y, di, cnt = queue.popleft()
            
            if board[x][y] == 'E' and cnt == k:
                return di
            elif board[x][y] == 'E' and (k - cnt) % 2:
                return 'impossible'
            
            for i in range(4):
                nx, ny, ndi = x + dx[i], y + dy[i], dirs[i]
                
                # 만약 남은 거리 + 횟수 + 1 했을 때, k번을 넘어간다면 해당 경우는 보지 않음
                if abs(nx - dr) + abs(ny - dc) + cnt + 1 > k:
                    continue
                
                if 0 <= nx < n and 0 <= ny < m:
                    queue.append((nx, ny, di + ndi, cnt + 1))
                    break
        
        return 'impossible'
                    
    return bfs(x - 1, y - 1, r - 1, c - 1)