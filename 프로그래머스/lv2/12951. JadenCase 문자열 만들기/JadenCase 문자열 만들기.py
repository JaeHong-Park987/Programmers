def solution(s):
    s_list = s.split(' ')
    word = ''
    word_list = []
    
    for i in s_list:
        for j in range(len(i)):
            if j == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        word_list.append(word)
        word = ''
    
    return ' '.join(word_list)