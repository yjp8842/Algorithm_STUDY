import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
check = [[0] * N for _ in range(N)]

# 숫자가 1개일 경우
for i in range(N):
  # 1로 채우기
  check[i][i] = 1

# 숫자가 2개일 경우
for i in range(N - 1):
  # 같은 숫자라면 1로 채우기
  if nums[i] == nums[i + 1]:
    check[i][i + 1] = 1
  # 같지 않다면 0으로 채우기
  else:
    check[i][i + 1] = 0

# 숫자가 3개 이상일 경우
for cnt in range(N - 2):
  for i in range(N - 2 - cnt):
    j = i + 2 + cnt
    # 양 끝의 숫자가 같고 & 그 사이가 팰린드롬 숫자이면 1로 채우기
    if nums[i] == nums[j] and check[i + 1][j - 1] == 1:
      check[i][j] = 1

M = int(input())
for _ in range(M):
  S, E = map(int, sys.stdin.readline().split())
  print(check[S - 1][E - 1])