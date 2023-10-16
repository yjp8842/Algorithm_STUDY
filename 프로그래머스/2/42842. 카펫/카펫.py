def solution(brown, yellow):
    total = brown + yellow
    
    # 약수 구하기
    divide = []
    for height in range(1, total + 1):
        if (total % height == 0):
            width = total / height
            # 바깥 테두리를 뺀 부분의 영역이 yellow랑 같다면
            if (height - 2) * (width - 2) == yellow:
                return [width, height]
    
    

