def solution(spell, dic):
    for word in dic:
        if len(word) < len(spell):
            continue
            
        copy_word = word
        
        for aha in spell:
            if aha in word:
                idx = copy_word.index(aha)
                copy_word = copy_word[:idx] + copy_word[idx + 1:]
                
        if len(copy_word) == 0:
            return 1

    return 2            
                