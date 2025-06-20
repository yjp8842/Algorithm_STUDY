def solution(dirs):
    visited = []
    x, y = 5, 5
    answer = 0

    move = {
        'U': (1, 0),
        'D': (-1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    for dir in dirs:
        dx, dy = move[dir]
        nx, ny = x + dx, y + dy
    
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            # 경로로 저장
            path = ((x, y), (nx, ny))
            reverse_path = ((nx, ny), (x, y))

            if path not in visited:
                visited.append(path)
                visited.append(reverse_path)
                answer += 1

            x, y = nx, ny

    return answer