N = int(input())
M = int(input())

if M == 0:
  broken = []
else:
  broken = list(input().split())

remote = [i for i in range(1000001)]

# 지금 보고 있는 채널 100번에서 + 혹은 -로만 이동할 수 있는 경우
min_cnt = abs(100 - N)

cnt = 0
for num in remote:
  for n in str(num):
    if n in broken:
      # min_cnt = 0
      break
  else:
    cnt = len(str(num)) + abs(N - num)
    min_cnt = min(min_cnt, cnt)

print(min_cnt)