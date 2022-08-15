N, M = map(int, input().split())

# N개의 입력받은 문자열을 str_s에 넣어준다
str_s = [input() for _ in range(N)]
cnt = 0

# M만큼 검사해야 할 문자열을 입력받는데
for i in range(M):
    word = input()
    # 만약 그 문자열이 str_s에 포함되어 있다면 cnt +1
    if word in str_s:
        cnt += 1
        
print(cnt)