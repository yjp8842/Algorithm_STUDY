def solution(s):
    answer = ''
    nums = list(map(int, s.split()))
    sort_nums = sorted(nums)
    answer = str(sort_nums[0]) + ' ' + str(sort_nums[-1])
    return answer