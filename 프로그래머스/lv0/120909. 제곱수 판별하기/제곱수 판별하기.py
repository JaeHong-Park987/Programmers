def solution(n):
    # n이 제곱수가 맞다면 제곱수를 제곱 전 수로 나누면 나머지가 0이다.
    if n % (n ** 0.5) == 0:
        return 1
    # n이 제곱수가 아니라면 나머지가 0이 아닐 것이다.
    else:
        return 2