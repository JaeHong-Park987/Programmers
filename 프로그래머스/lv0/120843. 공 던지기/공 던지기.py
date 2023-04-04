def solution(numbers, k):
#     numbers *= k
#     answer = numbers[2 * (k-1)]
    
#     return answer
    return numbers[(2 * (k-1)) % len(numbers)]