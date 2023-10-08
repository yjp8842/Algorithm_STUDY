N = int(input())
answer = 0
rows = [0] * N

# 퀸을 놓을 수 있는지 유효성 체크하는 함수
def check(r):
  for i in range(r):
    # 열이 같거나 대각선에 위치라면 false
    if rows[r] == rows[i] or abs(rows[r] - rows[i]) == r - i:
      return False
    
  return True

# r행에 퀸 놓는 함수
def put_queen(r):
  global answer
  
  if r == N:
    answer += 1
    return
  
  for i in range(N):
    rows[r] = i
    if check(r) == True:
      # 해당 자리에 놓을 수 있다면 다음 행으로
      put_queen(r + 1)
    
put_queen(0)
print(answer)