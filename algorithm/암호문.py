import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 10 + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    M = int(input())
    word_list = list(input().split())

    for i in range(len(word_list)):
        if word_list[i] == 'I':
            index = int(word_list[i + 1])
            count = int(word_list[i + 2])
            for j in range(1, count + 1):
                num_list.insert(index + j - 1, int(word_list[i + 2 + j]))

        if word_list[i] == 'D':
            index = int(word_list[i + 1])
            count = int(word_list[i + 2])
            for j in range(count):
                del num_list[index]

        if word_list[i] == 'A':
            count = int(word_list[i + 1])
            for j in range(1, count + 1):
                num_list.append(word_list[i + 1 + j])

    print("#{}".format(tc), *num_list[:10])
