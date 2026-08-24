def solution(polynomial):
    x_sum = 0
    const_sum = 0
    
    for term in polynomial.split(" + "):
        if "x" in term:
            coef_str = term[:-1]
            coef = int(coef_str) if coef_str else 1
            x_sum += coef
        else:
            const_sum += int(term)
    
    x_part = ""
    if x_sum == 1:
        x_part = "x"
    elif x_sum > 1:
        x_part = f"{x_sum}x"
        
    const_part = str(const_sum) if const_sum >= 1 else ""
    
    return " + ".join(p for p in [x_part, const_part] if p)
            
            