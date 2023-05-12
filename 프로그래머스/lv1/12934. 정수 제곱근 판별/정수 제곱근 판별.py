def solution(n):
    sr = n ** 0.5 # 제곱근
    
    if sr == int(sr): # 제곱근이 정수라면
        return (sr+1) ** 2
    else:
        return -1