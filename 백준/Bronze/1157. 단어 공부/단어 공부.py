import sys

word = sys.stdin.readline().strip().upper()
counter = {}

for char in word:
    counter[char] = counter.get(char, 0) + 1

max_val = 0
result = ""

for char, count in counter.items():
    if count > max_val:
        max_val = count
        result = char
    elif count == max_val:
        result = "?"
        
print(result)
