from collections import deque
import math

def get_k_num(n, k, lists):
    a = n // k
    b = n % k
    lists.appendleft(str(b))
    if a == 0 :
        return lists
    else :
        return get_k_num(a, k, lists)

def is_prime_number(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    lists = deque()
    get_k_num(n, k, lists)
    
    nums = ''.join(lists).split('0')
    
    result = 0
    for num in nums:
        if num != '' and num != '1':
            if is_prime_number(int(num)):
                # print(num)
                result += 1
    
    return result