def solution(my_string, alp):
    new = ''
    for i in my_string:
        if i == alp:
            i = i.upper()
            new += i
        else:
            new += i
    
    return new
            