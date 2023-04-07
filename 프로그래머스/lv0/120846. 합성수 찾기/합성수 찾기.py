def solution(n):
    answer = 0
    for i in range(1, n+1):
        number = 0
        for j in range(1, i+1):
            if i % j == 0:
                number += 1
        if number >= 3:
            answer += 1
                
    return answer