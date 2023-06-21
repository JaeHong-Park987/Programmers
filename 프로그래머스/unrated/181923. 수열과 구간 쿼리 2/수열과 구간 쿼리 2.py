def solution(arr, queries):
    arr1 = []
    answer = []
    min_value = 0
    
    for q in queries:
        for i in range(q[0], q[1]+1):
            if arr[i] > q[2]:
                arr1.append(arr[i])
        if len(arr1) == 0:
            min_value = -1
        else:
            min_value = min(arr1)
        answer.append(min_value)
        arr1 = []
    return answer