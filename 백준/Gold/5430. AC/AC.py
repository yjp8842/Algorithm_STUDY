from collections import deque

T = int(input())
for tc in range(T):
  p = list(input())
  k = int(input())
  arr = deque(input()[1:-1].split(','))
  is_reversed = False
  
  if k == 0:  
    arr = []
  
  for i in range(len(p)):
    if p[i] == 'R':
      is_reversed = not is_reversed
    elif p[i] == 'D':
      if len(arr) == 0:
        print('error')
        break
      else:
        if is_reversed == True:
          arr.pop()
        else:
          arr.popleft()
                      
  else:
    if is_reversed == True:
      arr.reverse()
    print('[' + ','.join(arr) + ']')