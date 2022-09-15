import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    V = N + 1

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    