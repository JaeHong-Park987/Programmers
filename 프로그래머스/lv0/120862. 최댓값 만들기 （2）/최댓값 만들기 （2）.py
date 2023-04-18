def solution(numbers):
    multi = []
    for f in range(0, len(numbers)):
        for s in range(f+1, len(numbers)):
            multi.append(numbers[f] * numbers[s])
    answer = max(multi)
    
    return answer