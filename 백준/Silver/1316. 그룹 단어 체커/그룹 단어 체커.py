N = int(input())
words = [list(map(str, input())) for _ in range(N)]

cnt = 0
for i in range(N):
  temp = 1
  tests = []
  for j in range(len(words[i])):
    if words[i][j] in tests and tests[len(tests) - 1] == words[i][j]:
      continue
    if words[i][j] in tests and tests[len(tests) - 1] != words[i][j]:
      temp = 0
      break
    if words[i][j] not in tests:
      tests.append(words[i][j])
  
  if temp == 1:
    cnt += 1

print(cnt)