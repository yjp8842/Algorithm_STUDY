# 1946_간단한 압축 풀기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    alphas = []
    for _ in range(N):
        alphas.append(list(input().split()))
    
    # 일단 빈 리스트에 각각의 개수만큼 알파벳 넣어주기
    arr = []
    for i in range(N):
        for j in range(int(alphas[i][1])):
            arr.append(alphas[i][0])
    
    print("#{}".format(tc))
    # 10개씩 끊어서 출력하기
    for i in range(len(arr) // 10 + 1):
        print("".join(arr[i * 10:i * 10 + 10]))