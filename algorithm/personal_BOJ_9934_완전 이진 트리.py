K = int(input())
tree = list(map(int, input().split()))

arr = [[] for _ in range(K)]

def dfs(tree, depth):

    # 트리의 root = 배열의 중간값
    root = (len(tree) // 2)

    # 해당 깊이에 해당하는 node를 추가
    arr[depth].append(tree[root])

    if len(tree) == 1:
        return

    # 왼쪽 서브트리
    dfs(tree[:root], depth + 1)
    # 오른쪽 서브트리
    dfs(tree[root + 1:], depth + 1)


dfs(tree, 0)
for li in arr:
    print(*li)
    
# 1 6 4 3 5 2 7
# [3]
# [6, 2]
# [1, 4, 5, 7]