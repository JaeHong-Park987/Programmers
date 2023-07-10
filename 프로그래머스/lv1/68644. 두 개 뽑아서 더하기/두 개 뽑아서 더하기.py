def solution(numbers):
    answer = []
    numbers.sort()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total = numbers[i]+numbers[j]
            
            if total not in answer:
                answer.append(total)
                
    answer.sort()
    
    return answer
    