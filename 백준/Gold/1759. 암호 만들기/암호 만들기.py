import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()

arr = []
visited = [0] * C
vowel = ['a', 'e', 'i', 'o', 'u']

# 모음과 자음의 포함 여부 확인 함수
def check(list):
  v_cnt, c_cnt = 0, 0 # 모음 개수, 자음 개수

  for alpha in list:
    if alpha in vowel:
      v_cnt += 1
    else:
      c_cnt += 1

  if v_cnt >= 1 and c_cnt >= 2:
    return True
  else:
    return False

def backtrack(iter):
  # L개가 되면 모음/자음 개수에 따른 참거짓 판단으로 출력
  if len(arr) == L:
    if check(arr):
      print(''.join(arr))
      return
    
  for i in range(iter, C):
    if not visited[i]:
      visited[i] = 1
      arr.append(alphas[i]) # 1
      backtrack(i) # 2
      visited[i] = 0 
      arr.pop() # 3
            
backtrack(0)