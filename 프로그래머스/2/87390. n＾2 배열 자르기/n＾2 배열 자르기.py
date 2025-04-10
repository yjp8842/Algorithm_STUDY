# i\j | 0 1 2
# ----+--------
#  0  | 1 2 3
#  1  | 2 2 3
#  2  | 3 3 3

# a[0][0] = max(1, 1) = 1
# a[0][1] = max(1, 2) = 2
# a[1][0] = max(2, 1) = 2
# a[2][2] = max(3, 3) = 3

def solution(n, left, right):
    answer = []

    # left부터 right까지 하나씩 순회하면서
    for idx in range(left, right + 1):
        i = idx // n  # 몇 번째 행인지
        j = idx % n   # 몇 번째 열인지

        value = max(i + 1, j + 1)
        answer.append(value)

    return answer