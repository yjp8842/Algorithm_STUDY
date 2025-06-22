from collections import deque

def solution(order):
    answer = 0
    main = deque()
    assist = []
    idx = 0
    
    for i in range(1, len(order) + 1):
        main.append(i)

    while main or assist:
        # 메인 벨트에서 꺼낼 수 있고, 순서가 맞는 경우
        if main and main[0] == order[idx]:
            main.popleft()
            answer += 1
            idx += 1
        # 보조 벨트에서 꺼낼 수 있고, 순서가 맞는 경우
        elif assist and assist[-1] == order[idx]:
            assist.pop()
            answer += 1
            idx += 1
        # 메인 벨트에서 꺼내서 보조 벨트에 쌓기
        elif main:
            assist.append(main.popleft())
        # 둘 다 안되면 종료
        else:
            break

    return answer