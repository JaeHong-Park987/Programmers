def solution(n):
    for i in range(n,1,-1):
        if n % i == 1:
            answer = i
    return answer