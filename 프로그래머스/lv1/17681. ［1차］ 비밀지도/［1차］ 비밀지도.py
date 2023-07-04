def solution(n, arr1, arr2):
    map = []
    for i in range(n):
        num1 = bin(arr1[i])[2:]
        num2 = bin(arr2[i])[2:]
        
        num1 = "0" * (n-len(num1)) + num1
        num2 = "0" * (n-len(num2)) + num2
        
        answer = ""
        
        for j in range(n):
            if (num1[j] == "0") & (num2[j] == "0"):
                answer += " "
            else:
                answer += "#"
        
        map.append(answer)
        
    return map