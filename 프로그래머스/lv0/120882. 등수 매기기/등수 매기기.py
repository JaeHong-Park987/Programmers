def solution(score):
    mean_score = []
    answer = []
    
    for i in score:
        mean_score.append(sum(i) / 2)
    
    sort_list = sorted(mean_score, reverse = True)
    
    for i in mean_score:
        answer.append(sort_list.index(i)+1)
    
    return answer