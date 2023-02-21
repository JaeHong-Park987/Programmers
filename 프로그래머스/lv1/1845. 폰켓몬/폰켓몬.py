def solution(nums):
    a = []
    for i in range(len(nums)):
        if nums[i] in a:
            pass
        else:
            a.append(nums[i])
    
    if len(a) > (len(nums) / 2):
        answer = len(nums) / 2
    else:
        answer = len(a)
    return answer