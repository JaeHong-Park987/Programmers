def solution(n):
    sum = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            sum += num
        else:
            pass
    return sum