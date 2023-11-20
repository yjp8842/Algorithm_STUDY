n = int(input())

dp = [0] * 1001

# n이 1과 2일 경우
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
  # n이 3일때부터는 이 전과 이 전전의 결과값을 더한 값이 나옴
  dp[i] = dp[i - 1] + dp[i - 2]

result = dp[n] % 10007
print(result)