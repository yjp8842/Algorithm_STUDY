from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
#   첫번째 숫자가 양수, 음수일 때의 두 경우를 queue에 넣어줌
    queue.append((numbers[0], 0))
    queue.append((-numbers[0], 0))
    cnt = 0
    
    while queue:
        number, i = queue.popleft()
        # print(number)
        
#       인덱스 하나 증가시켜줌
        i += 1
#       아직 인덱스가 범위를 벗어나지 않았을 때
        if i < len(numbers):
            queue.append((number + numbers[i], i))
            queue.append((number - numbers[i], i))
        else:
            if number == target:
                cnt += 1
        
    return cnt