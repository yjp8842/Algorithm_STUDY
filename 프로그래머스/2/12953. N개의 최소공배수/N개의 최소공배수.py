def solution(arr):
    lcm = arr[0]

    for i in range(1, len(arr)):
        a = lcm
        b = arr[i]

        # 최대공약수 구하기 (유클리드 호제법)
        while b:
            temp = b
            b = a % b
            a = temp
            
        num = a

        # 최소공배수 갱신
        lcm = (lcm * arr[i]) // num

    return lcm