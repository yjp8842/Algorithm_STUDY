def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        nums = array[commands[i][0] - 1:commands[i][1]]
        sort_nums = sorted(nums)
        answer.append(sort_nums[commands[i][2] - 1])
    return answer