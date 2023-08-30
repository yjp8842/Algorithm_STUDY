N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

for i in range(1, N):
  for j in range(len(triangle[i])):
    # 가장 처음에 위치한 값은 위에 위치한 리스트의 가장 처음 값 더하기
    if j == 0:
      triangle[i][j] += triangle[i - 1][j]
    # 가장 마지막에 위치한 값은 위에 위치한 리스트의 가장 마지막 값 더하기
    elif j == i:
      triangle[i][j] += triangle[i - 1][j - 1]
    # 중간에 위치한 값들은 본인 위에 위치한 두 값 중 큰 값 더하기
    else:
      triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

print(max(triangle[N - 1]))