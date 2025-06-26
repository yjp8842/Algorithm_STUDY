# tri[1][0] += tri[0][0]
# tri[1][1] += tri[0][0]

# tri[2][0] += tri[1][0]
# tri[2][1] += max(tri[1][0], tri[1][1])
# tri[2][2] += tri[1][1]

# tri[3][0] += max(tri[4][0], tri[4][1])

def solution(triangle):
    answer = 0
    
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])
    
    return triangle[0][0]