# from collections import deque

# def solution(m, n, puddles):
#     answer = 0
    
#     dx = [1, 0]
#     dy = [0, 1]
#     visited = [[0 for _ in range(m)] for _ in range(n)]
    
#     queue = deque()
#     queue.append((0, 0))
#     visited[0][0] = 1
    
#     for i in range(len(puddles)):
#         visited[puddles[i][1] - 1][puddles[i][0] - 1] = -1
    
#     while queue:
#         x, y = queue.popleft()
        
#         if x == n - 1 and y == m - 1:
#             break
        
#         for i in range(2):
#             nx, ny = x + dx[i], y + dy[i]
            
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != -1:
#                 queue.append((nx, ny))
#                 visited[nx][ny] += 1
    
#     return visited[n - 1][m - 1] % 1000000007


def solution(m, n, puddles):
    answer = 0
    
    dp = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    dp[1][1] = 1
    
    for i in range(len(puddles)):
        dp[puddles[i][1]][puddles[i][0]] = -1
    # 1, 2
    # 1, 1 + 0, 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                pass
            elif dp[i][j] == -1:
                pass
            elif dp[i][j - 1] == -1:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j] == -1:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                
    return dp[n][m] % 1000000007