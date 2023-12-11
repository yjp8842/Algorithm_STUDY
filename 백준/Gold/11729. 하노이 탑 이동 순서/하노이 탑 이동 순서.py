def hanoi(n, a, b, c):
  if n == 0:
    return
    
  else:
    hanoi(n - 1, a, c, b)
    print(a, c)
    hanoi(n - 1, b, a, c)
    

N = int(input())

cnt = 2 ** N - 1
print(cnt)
hanoi(N, 1, 2, 3)