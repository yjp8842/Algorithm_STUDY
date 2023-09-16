N = int(input())
arr = list(int(input()) for _ in range(N))
result = sorted(arr)

for num in result:
  print(num)