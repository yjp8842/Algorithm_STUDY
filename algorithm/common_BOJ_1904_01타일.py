N = int(input())

# DP 활용
# N이 3 이상일 때부터는 경우의 수 == 그 전 + 그 전전 단계의 경우의 수
dp = [0, 1, 2]
for i in range(3, N + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 15746)
    
print(dp[N])