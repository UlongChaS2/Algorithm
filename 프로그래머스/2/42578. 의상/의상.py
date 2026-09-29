def solution(clothes):
    dic = {}
    answer = 1
    
    for x, y in clothes:
        dic[y] = dic.get(y, 0) + 1
        
    for v in dic.values():
        answer *= v + 1
        
    return answer - 1
    
