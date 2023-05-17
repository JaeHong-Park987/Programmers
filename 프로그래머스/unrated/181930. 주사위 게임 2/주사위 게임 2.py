def solution(a, b, c):
    if a != b & b != c & c != a:
        return a + b +c
    elif a == b == c:
        return (a*3) * (a**2 * 3) * (a**3 * 3)
    else:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)