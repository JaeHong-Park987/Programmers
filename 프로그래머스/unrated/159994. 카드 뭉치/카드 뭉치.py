def solution(cards1, cards2, goal):
    c1 = 0
    c2 = 0
    for i in goal:
        if len(cards1) > c1 and i == cards1[c1]:
            c1 += 1
        elif len(cards2) > c2 and i == cards2[c2]:
            c2 += 1
        else:
            return "No"
            break
    
    return "Yes"