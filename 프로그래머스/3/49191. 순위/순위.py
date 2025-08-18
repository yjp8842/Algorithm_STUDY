def solution(n, results):
    answer = 0
    wins = {}
    loses = {}

    # 기본값 초기화
    for i in range(1, n + 1):
        wins[i] = set()
        loses[i] = set()

    for A, B in results:
        wins[A].add(B)
        loses[B].add(A)

    for player in range(1, n + 1):
        for loser in wins[player]:
            loses[loser].update(loses[player])

        for winner in loses[player]:
            wins[winner].update(wins[player])

    for player in range(1, n + 1):
        # print('wins: ', wins[player])
        # print('loses: ', loses[player])
        if len(wins[player]) + len(loses[player]) == n - 1:
            answer += 1

    return answer
