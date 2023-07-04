def solution(strings, n):
    strings.sort()
    word_list = []
    answer = []
    
    for i, s in enumerate(strings):
        word_list.append([s[n], i])

    word_list.sort()
    
    for i in word_list:
        answer.append(strings[i[1]])
        
    return answer