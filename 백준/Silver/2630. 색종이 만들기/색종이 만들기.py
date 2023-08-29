N = int(input())

paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

white, blue = 0, 0
def color_paper(N, x, y):
    
    global white, blue
    
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 하나라도 색깔이 다르다면
            if paper[i][j] != color:
                color = -1
                break
    
    # 모두 하얀색 종이이면
    if color == 0:
        white += 1
    
    # 모두 파란색 종이이면
    if color == 1:
        blue += 1
    
    # 하얀색이나 파란색이 섞여있는 경우 4등분 해주기
    if color == -1:
        
        N = N // 2
        
        color_paper(N, x, y)            # 1번째 칸       # 1 2
        color_paper(N, x, y + N)        # 2번째 칸       # 3 4
        color_paper(N, x + N, y)        # 3번째 칸
        color_paper(N, x + N, y + N)    # 4번째 칸

color_paper(N, 0, 0)
print(white)
print(blue)

# input
# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1