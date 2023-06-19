def solution(spell, dic):
    answer = []
    for word in dic:
        for s in spell:
            if s not in word:
                answer.append(word)
    
    if len(list(set(answer))) == len(dic):
        return 2
    else:
        return 1