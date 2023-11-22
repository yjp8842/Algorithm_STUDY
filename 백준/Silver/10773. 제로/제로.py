import sys
input = sys.stdin.readline

K = int(input())
nums = list(int(input()) for _ in range(K))

queue = []
for num in nums:
  if num != 0:
    queue.append(num)
  else:
    queue.pop()
    
print(sum(queue))