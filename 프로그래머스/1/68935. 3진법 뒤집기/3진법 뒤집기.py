def solution(n):
    base_3 = ''
    while n > 0:
        base_3 += str(n % 3)
        n = n // 3
            
    return int(base_3, 3)