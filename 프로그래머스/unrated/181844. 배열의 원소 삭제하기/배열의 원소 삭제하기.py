def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
            
    return arr

#     for i in arr:
#         if i in delete_list:
#             arr.remove(i)
            
#     return arr
# 위 방법대로 하면 arr이 지워진 시점에서 인덱스가 하나씩 당겨지기 때문에 거치지 않는 값들이 발생한다.
# input: [1, 2, 3, 4, 5, 6, 7, 8, 9] / delete_list : [1, 2, 3] / output: [4, 5, 6, 7, 8, 9] 이걸로 검토해보기 -> 실제로 [2,4,5,6,7,8,9]로 출력도니다.
