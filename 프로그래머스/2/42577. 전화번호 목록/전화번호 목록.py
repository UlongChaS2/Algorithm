def solution(phone_book):
    s = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in s:
                return False
    return True
