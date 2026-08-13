def solution(babbling):
    answer = 0

    for word in babbling:                          
        rest = word                                

        while rest:                                
            found = False                          
            for sound in ["aya", "ye", "woo", "ma"]:   
                if rest.startswith(sound):
                    rest = rest[len(sound):]       
                    found = True
                    break                          

            if not found:                          
                break                              

        if len(rest) == 0:                             
            answer += 1                            

    return answer