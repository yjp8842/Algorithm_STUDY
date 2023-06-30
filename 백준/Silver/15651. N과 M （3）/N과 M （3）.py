def solve(idx, N, M):
  if idx == M:
    for i in stack:
      print(i, end=' ')
    print()
    return

  for i in range(1, N + 1):
    stack.append(i) # 1번
    solve(idx + 1, N, M)  # 2번
    stack.pop()     # 3번

N, M = map(int, input().split())
stack = []
solve(0, N, M)
