def solution(dots):
    def slope(x, y):
        return (y[1] - x[1]) / (y[0] - x[0])
    
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    elif slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    elif slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    else:
        return 0
    
