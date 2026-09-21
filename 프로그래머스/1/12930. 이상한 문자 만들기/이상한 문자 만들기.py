def solution(s):
    words = []
    for word in s.split(' '):
        chars = [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)]
        words.append(''.join(chars))
    return ' '.join(words)
