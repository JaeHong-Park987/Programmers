def solution(absolutes, signs):
    answer = 0
    for i, b in enumerate(signs):
        if b:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
            
    return answer