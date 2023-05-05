def solution(myString, pat):
    changeString = ''
    for i in myString:
        if i == 'A':
            i = 'B'
            changeString += i
        else:
            i = 'A'
            changeString += i
    
    if pat in changeString:
        return 1
    else:
        return 0