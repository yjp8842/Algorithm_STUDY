from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(a, b, visited, land, cnt_list):
        queue = deque()
        queue.append((a, b))
        cnt = 1
        visited_y = [b]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                # nx, ny가 범위 안에 있고
                if 0 <= nx < n and 0 <= ny < m:
                    # 석유가 있는 땅을 아직 방문하지 않았다면
                    if visited[nx][ny] == 0 and land[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
                        
                        if ny not in visited_y:
                            visited_y.append(ny)
        
        # 열마다 석유덩어리 크기를 더해줌
        for idx in visited_y:
            cnt_list[idx] += cnt
        
    
    max_cnt = 0
    cnt_list = [0 for _ in range(m)]
    
    # 세로 (열)
    for j in range(m):
        # 가로 (행)
        for i in range(n):
            # 석유가 있는 땅이고, 아직 방문하지 않은 땅이라면
            # visited 처리 & bfs 실행
            if land[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j, visited, land, cnt_list)
    
    print('cnt_list : ', cnt_list)
    return max(cnt_list)
        