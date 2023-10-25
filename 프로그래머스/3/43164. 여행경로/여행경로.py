from collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    queue.append(("ICN", ["ICN"], []))
    
    while queue:
        now, path, used = queue.popleft()

        # 모든 티켓을 사용했다면 해당 경로 리스트에 추가
        if len(used) == len(tickets):
            answer.append(path)
        
        # 해당 티켓의 인덱스와 함께 검사하기 위한 enumerate
        for i, ticket in enumerate(tickets):
            if ticket[0] == now and not i in used:
                queue.append((ticket[1], path + [ticket[1]], used + [i]))
                
    # 사전순으로 정렬             
    answer.sort()

    return answer[0]