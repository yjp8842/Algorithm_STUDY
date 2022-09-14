# 중위순회
def inorder(n):
  global cnt
  if n == 0:
    return
  cnt += 1
  inorder(ch1[n])
  inorder(ch2[n])

T = int(input())
for tc in range(1, T + 1) :
  E, N = map(int, input().split())
  arr = list(map(int, input().split()))
  V = E + 1
  
  ch1 = [0] * (V + 1)
  ch2 = [0] * (V + 1)
  
  for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i + 1]
    if ch1[p] == 0:      # 아직 자식이 없으면
        ch1[p] = c       # 자식1에 보관
    else:
        ch2[p] = c       # 자식2에 보관
        
  cnt = 0
  inorder(N)
  print("#{} {}".format(tc, cnt))