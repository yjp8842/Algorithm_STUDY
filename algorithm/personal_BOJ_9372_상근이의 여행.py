from sys import stdin

def dfs(i, cnt):
    # 방문 처리
    visit[i] = 1
    for n in arr[i]:
        # 방문되지 않았다면,
        if visit[n] == 0:
            # dfs 재귀 진행
            cnt = dfs(n, cnt + 1)
    
    # 모든 노드가 방문되었다면 cnt 리턴       
    return cnt
        
T = int(input())
for _ in range(1, T + 1):
    N, M = list(map(int, stdin.readline().split()))
    arr = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        # 양방향을 모두 넣은 list 생성
        arr[A].append(B)
        arr[B].append(A)
       
    airplane = dfs(1, 0)
    print(airplane)

# 최소 신장 트리를 활용한 풀이 해설
# 모든 국가가 연결되어 있기 때문에 최소 간선의 수는 "국가의 수 - 1"    

# from sys import stdin

# T = int(input())
# for _ in range(1, T + 1):
#     N, M = list(map(int, stdin.readline().split()))
#     for _ in range(M):
#         input = stdin.readline()
        
#     print(N - 1)