N, K = map(int, input().split())

coins = list(int(input()) for _ in range(N))
# 내림차순으로 정렬해주기
# 동전을 큰 금액부터 사용해서 최소 개수를 구하기 위함
coins.sort(reverse=True)

cnt = 0
for coin in coins:
  # 해당 금액으로 나누어 진다면
  if K // coin > 0:
    cnt += K // coin
  
  # 나머지 금액으로 재할당
  K = K % coin
    
print(cnt)