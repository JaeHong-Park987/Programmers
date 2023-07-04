def solution(rank, attendance):
    rank_list = []
    
    for i, r in enumerate(rank):
        if attendance[i]:
            rank_list.append([r,i])
            
    rank_list.sort()
    a = rank_list[0][1]
    b = rank_list[1][1]
    c = rank_list[2][1]
    
    return 10000 * a + 100 * b + c