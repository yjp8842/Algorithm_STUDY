# 서류심사 성적 혹은 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않으면 선발
# 서류심사나 면접시험 하나의 기준으로 먼저 정렬
# 그 다음 나머지 기준으로 결정하면 되지 않을까...?

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        
    arr.sort()
    tmp = arr[0][1]
    people = 1
    
    for i in range(1, N):
        if tmp > arr[i][1]:
            tmp = arr[i][1]
            people += 1
    
    print(people)