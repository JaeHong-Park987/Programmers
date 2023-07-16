def solution(s):
    answer = []
    new_str = ''
    for i, a in enumerate(s):
        if a not in new_str:
            answer.append(-1)
        else:
            answer.append(i - new_str.find(a))
            new_str = new_str.replace(a, '*')
        new_str += a
        # print(new_str)
    return answer