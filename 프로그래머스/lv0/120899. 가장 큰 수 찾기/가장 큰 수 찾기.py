def solution(array):
    for i in range(len(array)):
        if array[i] == max(array):
            index = i
            
    return [max(array), index]