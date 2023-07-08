def solution(n,a,b):
    count = 0
    while a != b :
        count += 1
        a = a // 2 + a % 2
        b = b // 2 + b % 2
    return count