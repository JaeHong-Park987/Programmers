def solution(s):
    word_list = s.split(' ')
    answer = ''
    
    for w in word_list:
        if len(w) == 0:
            answer += ' '
        else:
            for l in range(len(w)):
                if l % 2 == 0:
                    answer += w[l].upper()
                else:
                    answer += w[l].lower()
            answer += ' '
    return answer[:-1]
            