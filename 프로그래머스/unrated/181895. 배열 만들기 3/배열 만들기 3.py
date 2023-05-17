def solution(arr, intervals):
    answer = []
    for i in intervals:
        for j in range(i[0], i[1]+1):
            answer.append(arr[j])
            
    return answer