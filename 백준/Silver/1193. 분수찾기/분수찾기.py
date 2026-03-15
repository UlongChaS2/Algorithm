import sys

x = int(sys.stdin.readline())
line = 1

while x > line:
    x -= line
    line += 1
    
if line % 2 == 0:
    numberator = x
    denominator = line - x + 1
else:
    numberator = line - x + 1
    denominator = x
        
print(f"{numberator}/{denominator}")