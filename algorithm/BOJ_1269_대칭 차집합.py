from sys import stdin

A, B = map(int, stdin.readline().split())
a_list = list(map(int, stdin.readline().split()))
b_list = list(map(int, stdin.readline().split()))

ab_list = set(a_list) - set(b_list)
ba_list = set(b_list) - set(a_list)

result = len(ab_list) + len(ba_list)
print(result)