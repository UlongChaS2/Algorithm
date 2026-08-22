def solution(numbers):
    numbers = sorted(numbers)
    x = numbers[:2]
    y = numbers[-2:]
    a, b = x
    c, d = y
    
    return max((a * b), (c * d))