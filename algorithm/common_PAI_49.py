# 교재 풀이

import collections

class Solution:
    def findMinHeightTrees(n, edges):
        if n <= 1:
            return [0]
				
		# 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        # graph = {
            # 0 : [1]
            # 1 : [0, 2, 3]
            # 2 : [1]
            # 3 : [1]
        # }
			
		# 첫 번째 리프 노드 추가
        # 리프 노드 : 키에 대한 값이 하나밖에 없는 노드
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)
			
		# 루트 노드만 남을 때까지 반복 제거
        # 루트가 2개일 경우도 있어서 n > 2일때까지 반복
        while n > 2:
            n -= len(leaves)
            # 새로운 리프 노드를 담을 리스트
            new_leaves = []
            # leaves = [0, 2, 3]
            for leaf in leaves:
                # pop, remove 두 번 진행하는 이유는 양방향 그래프를 구성했기 때문
                neighbor = graph[leaf].pop()
                # 연결된 값도 제거
                graph[neighbor].remove(leaf)

                # 제거 작업을 마친 후 또 길이가 1이 되는
                # 즉, 리프 노드인 키가 있다면 new_leaves에 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # new_leaves = [1]
            leaves = new_leaves

        # 리프 노드가 모두 제거 된 후
        # 예시의 경우 n = 1이 됐으므로 leaves = [1] 즉, [1] 리턴
        return leaves
    
n = 4
edges = [[1, 0], [1, 2], [1, 3]]