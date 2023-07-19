def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            else:
                if i % 2 == 0:
                    answer += code[i]
        else:
            if code[i] == '1':
                mode = 0
            else:
                if i % 2 != 0:
                    answer += code[i]
    if answer == '':
        return 'EMPTY'
    else:
        return answer