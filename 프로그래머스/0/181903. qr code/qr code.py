def solution(q, r, code):
    char = ''
    for i in range(len(code)):
        if i % q == r:
            char += code[i]
    return char