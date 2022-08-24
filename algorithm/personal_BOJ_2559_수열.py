N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

# 미리 K 인덱스까지의 값을 더하기
num_sum = sum(temp_list[0:K])
temps = []
temps.append(num_sum)

for i in range(N - K):
    temps.append(temps[i] - temp_list[i] + temp_list[i + K])

# temps에 담겨 있는 값 중 가장 큰 값
result = max(temps)
        
print(result)