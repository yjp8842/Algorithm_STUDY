N = int(input())
words = [list(map(str, input().split())) for _ in range(N)]

stack = []
for i in range(N):
  if words[i][0] == 'push':
    stack.append(words[i][1])
  
  if words[i][0] == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      top = stack.pop()
      print(top)
      
  if words[i][0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      
  if words[i][0] == 'size':
    print(len(stack))
    
  if words[i][0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)