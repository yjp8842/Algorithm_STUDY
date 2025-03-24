def solution(players, callings):
    # 선수들의 현재 등수를 딕셔너리로 저장
    rank = {player: i for i, player in enumerate(players)}

    for calling in callings:
        idx = rank[calling]
        if idx > 0:
            rank[calling] -= 1
            rank[players[idx - 1]] += 1
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
            

    return players