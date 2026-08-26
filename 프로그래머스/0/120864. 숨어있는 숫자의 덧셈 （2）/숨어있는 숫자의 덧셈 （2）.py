def solution(my_string):
    return sum(int(num_str) for num_str in "".join(ch if ch.isdigit() else " " for ch in my_string).split())
    