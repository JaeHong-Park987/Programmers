def solution(binomial):
    b_list = binomial.split(' ')
    
    a = int(b_list[0])
    op = b_list[1]
    b = int(b_list[2])
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b