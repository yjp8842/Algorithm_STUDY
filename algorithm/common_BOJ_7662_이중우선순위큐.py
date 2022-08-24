import heapq

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    
    for i in range(k):
        alpha, val = input().split()
        