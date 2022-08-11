X = int(input())
lines = 1

while X > lines:
    X -= lines # 몇번째 칸에 있는지
    lines += 1 # 몇번째 라인인지
    
if lines % 2: # 홀수 라인일 때
    n = lines - X + 1 # 분자
    m = X # 분모
else:
    n = X
    m = lines - X + 1
    
print(f"{n}/{m}")