import sys

N = int(input())
tree = dict()

for _ in range(N):
  root, left, right = map(str, sys.stdin.readline().split())
  tree[root] = left, right

# 전위 순회
def preorder(x):
  if x == '.':
    return
  else:
    print(x, end='')
    preorder(tree[x][0]) # 왼쪽 노드 탐색
    preorder(tree[x][1]) # 오른쪽 노드 탐색

# 중위 순회
def inorder(x):
  if x == '.':
    return
  else:
    inorder(tree[x][0]) # 왼쪽 노드 탐색
    print(x, end='')
    inorder(tree[x][1]) # 오른쪽 노드 탐색

# 후위 순회
def postorder(x):
  if x == '.':
    return
  else:
    postorder(tree[x][0]) # 왼쪽 노드 탐색
    postorder(tree[x][1]) # 오른쪽 노드 탐색
    print(x, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')