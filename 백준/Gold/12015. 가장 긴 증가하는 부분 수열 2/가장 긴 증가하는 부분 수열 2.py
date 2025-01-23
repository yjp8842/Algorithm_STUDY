# 이분탐색

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
lst = [0]

for num in A:
    if lst[-1] < num:
        lst.append(num)
    else:
        left = 0
        right = len(lst)

        while left < right:
            mid = (right + left) // 2
            if lst[mid] < num:
                left = mid + 1
            else:
                right = mid
                
        lst[right] = num
    # print('num: ', num, 'lst: ', lst)

print(len(lst) - 1)