def solution(todo_list, finished):
    answer = []
    
    for i in range(len(finished)):
        if finished[i]:
            pass
        else:
            answer.append(todo_list[i])
    return answer