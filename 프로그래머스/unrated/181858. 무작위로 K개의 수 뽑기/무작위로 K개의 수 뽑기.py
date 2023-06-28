def solution(arr, k):
    answer = []
    
    for i in arr:
        if i not in answer:
            answer.append(i)
    
    while len(answer) != k:
        if len(answer) > k:
            answer.pop()
        elif len(answer) < k:
            answer.append(-1)
        
    return answer