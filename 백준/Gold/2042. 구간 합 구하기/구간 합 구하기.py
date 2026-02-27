# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고,
# K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
# 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고
# a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

size = 1
while size < N:
    size *= 2

tree = [0] * (size * 2)

def build():
    # 리프 노드 채우기
    for i in range(N):
        tree[size + i] = numbers[i]

    # 부모 노드 채우기
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

build()

# 업데이트 함수
def update(idx, value):
    idx += size
    tree[idx] = value

    while idx > 1:
        idx //= 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

# 구간합 반환 함수
def sums(left, right):
    left += size
    right += size
    result = 0

    while left <= right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 0:
            result += tree[right]
            right -= 1

        left //= 2
        right //= 2

    return result

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b - 1, c)
    else:
        print(sums(b - 1, c - 1))