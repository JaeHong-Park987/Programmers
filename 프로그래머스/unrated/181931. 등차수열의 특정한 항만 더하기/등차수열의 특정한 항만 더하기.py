def solution(a, d, included):
    total = 0
    for i in included:
        if i:
            total += a
        a += d
    return total