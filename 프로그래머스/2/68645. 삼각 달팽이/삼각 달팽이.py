# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
# 0 1 3 6 7 8 9 5 2 4

def solution(n):
    answer = []
    for i in range(1, n + 1):
        answer.append([0] * i)
    
    x, y = -1, 0
    num = 0
    
    while n > 0:
    	# 아래쪽
        for _ in range(n):
            x += 1
            num += 1
            answer[x][y] = num
            
        # 오른쪽
        for _ in range(n - 1):
            y += 1
            num += 1
            answer[x][y] = num
            
        # 위쪽
        for _ in range(n - 2):
            x -= 1
            y -= 1
            num +=1
            answer[x][y] = num
            
        n -= 3
    
    return sum(answer, [])