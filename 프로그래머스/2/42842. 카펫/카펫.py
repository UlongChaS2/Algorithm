def solution(brown, yellow):
    total = brown + yellow
    i = 3
    while i * i <= total:
        if total % i == 0:
            w, h = total // i, i
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
        i += 1
        
        
