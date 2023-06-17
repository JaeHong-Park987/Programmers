def solution(ineq, eq, n, m):
    op = ineq + eq
    
    if op == '>=':
        if n >= m:
            return 1
        else:
            return 0
    elif op == '<=':
        if n <= m:
            return 1
        else:
            return 0
    elif op == '>!':
        if n > m:
            return 1
        else:
            return 0
    elif op == '<!':
        if n < m:
            return 1
        else:
            return 0