# 중위 순회
def inorder(n):
    global num

    if n <= N:
        inorder(n * 2)
        arr[n] = num
        num += 1
        inorder(n * 2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0 for _ in range(N + 1)]
    
    num = 1
    inorder(1)
    # arr[1] : 트리의 루트 / arr[N // 2] : 문제에서 원하는 값
    print("#{} {} {}".format(tc, arr[1], arr[N // 2]))