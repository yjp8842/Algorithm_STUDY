def solution(participant, completion):
    answer = ''
    part_hash = {}
    for person in participant:
#       동명이인이 있을 경우를 대비해 해당 사람의 수만큼 value값 설정
        if person in part_hash:
            part_hash[person] += 1
        else:
            part_hash[person] = 1
    
#   완주자 명단에 있다면 -1
    for p in completion:
        part_hash[p] -= 1

#   value가 0이 아니라면 완주하지 못한 사람이므로 return
    for person in part_hash:
        if part_hash[person] != 0:
            return person