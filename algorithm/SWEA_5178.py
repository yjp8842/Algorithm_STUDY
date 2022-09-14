def tree_sum(n):
    if n <= N:
        if tree[n] == 0:
            tree[n] = tree_sum(n * 2) + tree_sum(n * 2 + 1)   # 왼쪽 자식과 오른쪽 자식을 합한 값
        return tree[n]
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]

    for _ in range(M):
        p, c = map(int, input().split())
        tree[p] = c
        
    tree_sum(1)
    ans = tree[L]
    print("#{} {}".format(tc, ans))