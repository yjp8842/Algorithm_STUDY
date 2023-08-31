N = int(input())
M = int(input())
lists = []
for _ in range(M):
  a, b, c = map(int, input().split())
  lists.append((a, b, c))

# 비용(가중치)를 기준으로 정렬
lists.sort(key=lambda x : x[2])

# 각자 자신을 부모로 가지는 배열 만들기
p = [i for i in range(N + 1)]

def Find(now):
  if p[now] == now:
    return now
  p[now] = Find(p[now])
  return p[now]

def Union(a, b):
  pa = Find(a)
  pb = Find(b)
  # a와 b의 부모가 다르면 연결해주기
  if pa != pb:
    p[pa] = pb

cost = 0
for a1, b1, cost1 in lists:
  # a와 b의 부모가 다를 때
  if Find(a1) != Find(b1):
    Union(a1, b1)
    cost += cost1
    
print(cost)