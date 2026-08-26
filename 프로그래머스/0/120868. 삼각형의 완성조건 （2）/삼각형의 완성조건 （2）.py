def solution(sides):
    max_val = max(sides)
    min_val = min(sides)
    limit_side = sum(sides)
    count = 0

    for num in range(1, limit_side):
        if max_val - min_val < num <= max_val:
            count += 1
        elif max_val < num:
            count += 1
    return count
