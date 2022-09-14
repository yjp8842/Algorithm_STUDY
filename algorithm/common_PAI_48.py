#교재 풀이
# dfs

def isBalanced(root):
    def check(root):
        # 맨 마지막 노드에 내려가면 (리프 노드인 경우)
        # left = 0, right = 0이 될 수 있도록 함
        if not root:
            return 0

        # 왼쪽 자식 & 오른쪽 자식
        # check 함수 재귀 호출로 마지막 리프 노드까지 내려감
        left = check(root.left)
        right = check(root.right)
        # for i in range(1, len(list)):
        #     left = check(list[i * 2])
        #     right = check(list[i * 2 + 1])

        # 높이 차이가 1을 초과하는 경우 -1 리턴
        # 한 번 -1을 리턴하는 경우 계속해서 -1 리턴
        # 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    # 재귀를 돌렸을 때 최종적으로 -1이 리턴되면 False / -1이 아닌 값이 리턴되면 True 반환
    return check(root) != -1