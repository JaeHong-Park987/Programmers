def solution(quiz):
    answer = []
    
    for i in quiz:
        quiz_list = i.split()
        m = quiz_list[1]
        n1 = quiz_list[0]
        n2 = quiz_list[2]
        r = quiz_list[4]
        
        if m == '-':
            if int(n1) - int(n2) == int(r):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(n1) + int(n2) == int(r):
                answer.append('O')
            else:
                answer.append('X')
        
    return answer
            