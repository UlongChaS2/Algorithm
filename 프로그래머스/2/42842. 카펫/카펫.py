def solution(brown, yellow):
    total = brown + yellow 
    fairs = []
    i = 3
    
    while i * i <= total:
        if total % i == 0:
            fairs.append([total // i, i])
        i += 1 
    
    for (w, h) in fairs:
        if (w-2) * (h-2) == yellow:
            return [w, h]
        
        
