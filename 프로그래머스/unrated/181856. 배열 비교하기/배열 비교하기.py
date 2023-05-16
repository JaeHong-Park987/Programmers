def solution(arr1, arr2):
    if len(arr1) > len(arr2): # arr1 길이가 길면
        return 1
    elif len(arr1) < len(arr2): # arr2 길이가 길면
        return -1
    else: # 길이가 같다면
        if sum(arr1) > sum(arr2): # arr1 합이 크면
            return 1
        elif sum(arr1) < sum(arr2): # arr2 합이 크면
            return -1
    return 0 # 