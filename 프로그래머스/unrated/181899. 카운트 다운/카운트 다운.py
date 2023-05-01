def solution(start, end):
    answer = []
    # 큰 수 부터 작은 수로 범위를 설정할 때는 얼마씩 감소하는지도 명시해야 한다.
    for i in range(start, end-1, -1):
        answer.append(i)
    return answer