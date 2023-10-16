import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = list(int(sys.stdin.readline()) for _ in range(n))

# 시간 초과
# max_cnt = 0
# for i in range(n):
#   cnt = len(set(sushi[i:i + k] + [c]))
#   if max_cnt <= cnt:
#     max_cnt = cnt

# print(max_cnt)

cnt = 1
check = [0] * (d + 1)
check[c] = 1

# 처음 0 ~ k - 1번째 인덱스에 해당하는 값 먼저 설정해줌
for i in range(k):
  check[sushi[i]] += 1
  if check[sushi[i]] == 1:
    cnt += 1
  # print(check)

answer = 0
for i in range(n):
  # print(check)
  start = sushi[i]
  end = sushi[(i + k) % n]
  
  # 투포인터
  # 시작 지점의 초밥의 갯수를 하나 삭제하고, 끝 지점의 초밥의 갯수를 하나 늘림
  check[start] -= 1
  # 시작 지점과 끝 지점을 옮기며 검사할 때
  # 시작 지점의 값이 0이 되면 갯수 하나 줄여줌
  if check[start] == 0:
    cnt -= 1
    
  check[end] += 1
  # 끝 지점의 값이 1이 되면 갯수 하나 늘려줌
  if check[end] == 1:
    cnt += 1
  
  # 검사 진행하며 최댓값 갱신해주기
  answer = max(answer, cnt)

print(answer)