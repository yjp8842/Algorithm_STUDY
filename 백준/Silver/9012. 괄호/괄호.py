T = int(input())
arr = []
for _ in range(T):
  arr.append(list(map(str, input().strip())))
  
for list in arr:
  stack = []
  check = []
  for j in range(len(list)):
    if list[j] == '(':
      stack.append(list[j])
      
    if list[j] == ')':
      if len(stack) == 0:
        check.append(list[j])
      else:
        stack.pop()
  
  if len(stack) == 0 and len(check) == 0:
    print("YES")
  else:
    print("NO")