def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1,yellow+1):
        w = i
        h = yellow // i
        if (yellow % i == 0) & (w >= h) & ((w+2) * (h+2) == total):
            return [w+2, h+2]
            