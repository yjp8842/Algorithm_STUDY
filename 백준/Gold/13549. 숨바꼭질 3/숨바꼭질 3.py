from collections import deque

N, K = map(int,input().split())
time = [0] * 100001

def bfs(num):
  queue = deque()
  
  if num == 0 :
    queue.append(1)
  else :
    queue.append(num)
  
  while queue:
    num = queue.popleft()
    
    if num == K:
      return time[num]
    
    for next_num in (num - 1, num + 1, num * 2):
      if 0 <= next_num < 100001 and time[next_num]==0:
        if next_num == num * 2 :
          time[next_num] = time[num]
          queue.appendleft(next_num)
        else : 
          time[next_num] = time[num] + 1
          queue.append(next_num)

if N == 0:
  print(bfs(N) + 1)
else :
  print(bfs(N))
