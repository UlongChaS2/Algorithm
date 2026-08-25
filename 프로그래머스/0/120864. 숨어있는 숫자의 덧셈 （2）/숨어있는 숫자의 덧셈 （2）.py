def solution(my_string):
    total = 0
    num_part = ""
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():
                num_part += my_string[i]
        else:
            if num_part:
                total += int(num_part)
                num_part = ""
                
    if num_part:
        total += int(num_part)
        
    return total
