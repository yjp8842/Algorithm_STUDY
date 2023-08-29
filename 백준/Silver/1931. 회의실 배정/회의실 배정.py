N = int(input())

info = []
for _ in range(N):
  start, end = map(int, input().split())
  info.append([start, end])

# 끝나는 시간을 기준으로 먼저 오름차순 정렬
# 다음으로 시작하는 시간을 기준으로 오름차순 정렬
info = sorted(info, key = lambda x : (x[1], x[0]))

end_time = 0
cnt = 0
for start, end in info:
  # 시작 시간 >= 끝나는 시간
  # 즉, 어떤 회의가 끝나고 그 다음 회의가 시작될 수 있다는 의미
  if start >= end_time:
    cnt += 1
    end_time = end

print(cnt)