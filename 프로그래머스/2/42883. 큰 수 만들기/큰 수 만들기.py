def solution(number, k):
    stack = []

    for n in number:
        if n == 9 and stack and stack[-1] < n:
            stack.pop()
            stack.append(n)
        
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
            
        stack.append(n)

    while k:
        # print(stack)
        stack.pop()
        k -= 1

    return ''.join(stack)