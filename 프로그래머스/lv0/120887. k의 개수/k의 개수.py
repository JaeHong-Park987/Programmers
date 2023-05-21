def solution(i, j, k):
    answer = 0
    num_s = ''
    for n in range(i, j+1):
        num_s += str(n)
    for a in num_s:
        if a == str(k):
            answer += 1
    return answer