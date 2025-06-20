def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def is_not_divisible(g, arr):
    for x in arr:
        if x % g == 0:
            return False
    return True

def solution(arrayA, arrayB):
    A_gcd = get_gcd(arrayA)
    B_gcd = get_gcd(arrayB)

    answer = 0

    if is_not_divisible(A_gcd, arrayB):
        answer = max(answer, A_gcd)

    if is_not_divisible(B_gcd, arrayA):
        answer = max(answer, B_gcd)

    return answer