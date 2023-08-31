# A, B, C = map(int, input().split())
# print((A ** B) % C)

# 분할정복
# 10^11 -> ((10^5)^2)*10 -> ((((10^2)^2)*10)^2)*10 -> ...

def calc(a, b, c):
  if b == 1:
    return a % c

  # 짝수일 때 
  elif b % 2 == 0:
    return (calc(a, b // 2, c) ** 2) % C
  
  # 홀수일 때
  else:
    return ((calc(a, b // 2, c) ** 2) * a) % c

A, B, C = map(int, input().split())
print(calc(A, B, C))