from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] * (n + 1) for _ in range(n + 1)]
#     양방향 그래프로 값 넣어주기
    for i in range(len(roads)):
        a, b = roads[i]
        graph[a].append(b)
        graph[b].append(a)
    
#     destination부터 시작해서 각 지역에 몇 번의 방문으로 도착할 수 있는지 visited를 통해 체크
    queue = deque([destination])
    visited = [0 for _ in range(n + 1)]
    visited[destination] = 1
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    
#     sources에 있는 지역만 answer에 방문 횟수 넣어주기
    for i in sources:
        answer.append(visited[i] - 1)
    return answer