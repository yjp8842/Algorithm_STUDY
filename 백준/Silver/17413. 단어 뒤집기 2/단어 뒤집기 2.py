strs = list(map(str, input()))
check = False
temp = ''
result = ''

for i in range(len(strs)):
  # 거꾸로 출력
  if check == False:
    if strs[i] == '<':
      temp += strs[i]
      check = True

    elif strs[i] == ' ':
      temp += strs[i]
      result += temp
      temp = ''
      
    else:
      temp = strs[i] + temp

  # 똑바로 출력
  else:
    temp += strs[i]
    if strs[i] == '>':
      result += temp
      temp = ''
      check = False

print(result + temp)