def solution(people, limit):
    people.sort()
    count = 0
    
    a = 0
    b = len(people)-1
    
    while a < b:
        total = people[a] + people[b]
        if total <= limit:
            a += 1
            count += 1
        b -= 1
    
    return len(people) - count