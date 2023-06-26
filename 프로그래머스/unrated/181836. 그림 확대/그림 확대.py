def solution(picture, k):
    answer = ''
    result = []
    
    for p in picture:
        for i in p:
            answer += i * k
            
        for n in range(k):
            result.append(answer)
        answer = ''
    
    return result