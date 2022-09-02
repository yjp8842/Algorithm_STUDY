# n : 상근이 동기 수
# m : 리스트 길이
# ai, bi : 친구 관계

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    ai, bi = map(int, input().split())
    # 입력받은 ai, bi를 인덱스 값으로 두고 서로의 값을 저장해줌
    friends[ai].append(bi)
    friends[bi].append(ai)

invite = [0] * (n + 1)
# 상근이의 학번 : 1
# 즉, 상근이 친구인 경우 invite에 1로 표시
for i in friends[1]:
    invite[i] = 1
    # 상근이 친구의 친구인 경우,
    for j in friends[i]:
        invite[j] = 1

# 1은 상근이 본인이기에 0으로 할당
invite[1] = 0
cnt = 0
for i in invite:
    # 상근이 친구이거나, 친구의 친구인 경우
    if i == 1:
        cnt += 1
        
print(cnt)