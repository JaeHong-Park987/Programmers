def solution(a, b):
    total = 0
    if a == b:
        return a
    else:
        for i in range(min(a,b), max(a,b)+1):
            total += i
        return total