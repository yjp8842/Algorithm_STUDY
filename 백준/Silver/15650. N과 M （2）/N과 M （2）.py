def solve(idx, start, N, M):
  if idx == M:
    for i in stack:
      print(i, end=' ')
    print()
    return

  for i in range(start, N + 1):
    if dat[i] == 1:
      continue
    stack.append(i) # 1번
    dat[i] = 1
    solve(idx + 1, i + 1, N, M)  # 2번
    stack.pop()     # 3번
    dat[i] = 0

N, M = map(int, input().split())
stack = []
dat = [0] * (N + 1)
solve(0, 1, N, M)
