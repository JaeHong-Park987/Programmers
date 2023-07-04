def solution(n, words):
    answer = [words[0]]
    count = 1
    
    for i in range(1,len(words)):
        count += 1
        if (words[i] not in answer) & (words[i-1][-1] == words[i][0]):
            answer.append(words[i])
            print(count, answer)
        else:
            if count % n == 0:
                return [n, count//n]
            else:
                return [count%n, count//n + 1]
            # print(count)
            # break
            
    return [0,0]
        