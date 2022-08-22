def f(i, N):
    global answer
    if i == N:
        s = 0
        for i in range(N):
            if bit[i]:
                s += A[i]
            
        if s == 10:
            answer += 1
            for i in range(N):
                if bit[i]:
                    print(A[i], end = ' ')
            print()
            
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
f(0, 10)
print(answer)