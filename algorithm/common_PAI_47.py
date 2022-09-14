# 교재 풀이

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    # 직렬화
    def serialize(self, root):
        # queue = [1, 2, 3, Null, Null, 4, 5]
        queue = collections.deque([root])
        # 1번 인덱스부터 시작하므로 빈 리스트가 아닌 '#'으로 초기화
        result = ['#']
        
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
                # result에는 현재 노드 값을 삽입
                result.append(str(node.val))
                
            else:
                # 노드가 존재하지 않으면 Null 의미의 # 삽입
                result.append('#')
        
        return ' '.join(result)
        # '# 1 2 3 # # 4 5 # # # #'
        # 마지막 '# # # #'은 4와 5에 해당하는 값일듯
    
    # 역직렬화
    def deserialize(self, data):
        
        # 예외처리
        # '# 1 2 3 # # 4 5 # # # #'
        if data == '# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
                
            index += 1
            
            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
                
            index += 1
            
        return root