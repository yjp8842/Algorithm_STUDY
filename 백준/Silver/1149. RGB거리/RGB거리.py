N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
  colors[i][0] = min(colors[i - 1][1], colors[i - 1][2]) + colors[i][0] # 빨간색
  colors[i][1] = min(colors[i - 1][0], colors[i - 1][2]) + colors[i][1] # 초록색
  colors[i][2] = min(colors[i - 1][0], colors[i - 1][1]) + colors[i][2] # 파란색

print(min(colors[N - 1]))