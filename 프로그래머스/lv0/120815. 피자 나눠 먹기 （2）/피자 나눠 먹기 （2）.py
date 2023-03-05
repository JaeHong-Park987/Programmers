def solution(n):
    answer = 1
    while (6 * answer) % n != 0:
        answer += 1
    return answer