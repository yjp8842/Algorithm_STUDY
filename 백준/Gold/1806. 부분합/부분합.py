# 10 15
# 5 1 3 5 10 7 4 9 2 8

N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 100000
start, end = 0, 0
current_sum = 0


while True:
  if current_sum >= S:
    answer = min(answer, end - start)
    current_sum -= arr[start]
    start += 1

  elif end == N:
    break

  else:
    current_sum += arr[end]
    end += 1
    
if answer != 100000:
    print(answer)
else:
    print(0)