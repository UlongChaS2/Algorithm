import sys

n = int(sys.stdin.readline())
total = 0

for i in range(n):
    word = sys.stdin.readline().strip()
    arr = []
    is_group = True
    
    for char in word:
        if not arr or arr[-1] != char:
            if char in arr:
                is_group = False
                break
            else: 
                arr.append(char)
        
    if is_group:
        total += 1
            
print(total)           