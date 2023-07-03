def solution(A, B):
    if A == B:
        return 0

    else:
        count = 0
        for _ in range(len(A)):
            newA = ''
            newA += A[-1]
            for a in range(len(A)-1):
                newA += A[a]
            A = newA
            count += 1
            if newA == B:
                return count
        return -1