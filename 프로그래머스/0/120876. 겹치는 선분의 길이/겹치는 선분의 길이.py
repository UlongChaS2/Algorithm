def solution(lines):
    lo = min(x for x, _ in lines)
    hi = max(y for _, y in lines)
        
    counts = [0] * (hi - lo)
    
    for x, y in lines:
        for cell in range(x, y):
            counts[cell - lo] += 1
            
    return sum(1 for c in counts if c >= 2)