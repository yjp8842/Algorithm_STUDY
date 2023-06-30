def solve(idx, start, N, M):
  if idx == M:
    for i in stack:
      print(i, end=' ')
    print()
    return

  for i in range(start, N + 1):
    stack.append(i) # 1번
    solve(idx + 1, i, N, M)  # 2번
    stack.pop()     # 3번

N, M = map(int, input().split())
stack = []
solve(0, 1, N, M)
