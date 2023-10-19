def solution(clothes):
    answer = 0
    clothes_map = {}
    for i in range(len(clothes)):
        type = clothes[i][1]
#       해당 타입이 이미 해시맵에 존재한다면
        if type in clothes_map:
            clothes_map[type].append(clothes[i][0])
#       해당 타입이 해시맵에 없다면
        else:
            clothes_map[type] = [clothes[i][0]]
    
    cnt = 1
    for type in clothes_map:
        cnt *= len(clothes_map[type]) + 1
    
    return cnt - 1