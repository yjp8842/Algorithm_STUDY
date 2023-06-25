while 1:
  str_s = list(map(str, input()))
  
  if str_s[0] == '.':
    break

  tests = []
  for i in range(len(str_s)):
    if str_s[i] == ')':
      if tests and tests[-1] == '(':
        tests.pop()
      else:
        tests.append(str_s[i])
        break
    elif str_s[i] == '(':
      tests.append(str_s[i])
    
    elif str_s[i] == ']':
      if tests and tests[-1] == '[':
        tests.pop()
      else:
        tests.append(str_s[i])
        break
    elif str_s[i] == '[':
      tests.append(str_s[i])
    
    else:
      continue

  if tests != []:
    print('no')
  else:
    print('yes')