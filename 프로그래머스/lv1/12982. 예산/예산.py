def solution(d, budget):
    answer = 0
    d.sort()
    if sum(d) == budget:
        return len(d)
    else:
        for i in d:
            if budget - i >= 0:
                answer += 1
                budget -= i
        return answer