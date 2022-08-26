import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10 + 1):
    N = int(input())
    num_list = list(input().split())
    M = int(input())
    word_list = list(input().split())

    print(num_list)
    # print(word_list)

    for i in range(M):
        if word_list[i] == 'I':
            for j in range(1, int(word_list[i + 2]) + 1):
                num_list[int(word_list[i]) + j] = word_list[i + 2 + j]

        elif word_list[i] == 'D':
            for _ in range(int(word_list[i + 2])):
                num_list[int(word_list[i]) + 1].pop()

        elif word_list[i] == 'A':
            for j in range(int(word_list[i + 1])):
                num_list[-1] = word_list[i + 2 + j]

    print(num_list[:10])
