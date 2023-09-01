from collections import deque

def bfs(a, b):
  queue = deque()
  queue.append((a, 1))

  while queue:
    num, cnt = queue.popleft()
    
    if num == b:
      return cnt

    if num * 2 <= b:
      queue.append((num * 2, cnt + 1))
      
    if num * 10 + 1 <= b:
      queue.append((num * 10 + 1, cnt + 1))
          
  return -1

A, B = map(int, input().split())
print(bfs(A, B))