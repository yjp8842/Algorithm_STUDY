def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_lst = [0] * bridge_length
    now_weight = 0

    while truck_weights:
        now_weight -= bridge_lst.pop(0)

        if truck_weights[0] + now_weight <= weight:
            bridge_lst.append(truck_weights.pop(0))
            now_weight += bridge_lst[-1]
        else:
            bridge_lst.append(0)
            
        answer += 1

    return answer + bridge_length