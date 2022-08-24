import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10 + 1):
    N = int(input())
    m_table = []
    for _ in range(N):
        m_table.append(list(map(int, input().split())))

    cnt = 0
    # 열 우선 
    for j in range(N):
        status = []
        for i in range(N):
            # status가 비어있다면
            if status == []:
                if m_table[i][j] == 1:
                    status.append(1)
                    
            # status가 비어있지 않다면
            else:
                if m_table[i][j] == 2:
                    cnt += 1
                    status.pop()

    print("#{} {}".format(tc, cnt))