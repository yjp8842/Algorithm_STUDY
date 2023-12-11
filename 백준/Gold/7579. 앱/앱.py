N, M = map(int, input().split())
apps = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * sum(cost) for _ in range(N)]
ans = sum(cost)

for i in range(N):
  for j in range(len(dp[i])):
    # 현재 앱의 비용이 j보다 클 경우
    if cost[i] > j:
      dp[i][j] = dp[i - 1][j]
    else:
      # 현재 앱을 끈 뒤의 바이트와 그렇지 않은 경우의 바이트 중 더 큰 값
      dp[i][j] = max(dp[i - 1][j - cost[i]] + apps[i], dp[i - 1][j])
    
    # dp[i][j] 값이 만들고자 하는 M바이트 이상이라면 더 작은 값이 결과값
    if dp[i][j] >= M:
      ans = min(ans, j)

print(ans)