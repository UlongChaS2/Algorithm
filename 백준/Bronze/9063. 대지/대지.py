import sys

n = int(sys.stdin.readline())

if n == 1:
    sys.stdin.readline()
    print(0)
    sys.exit()

x_coords = []
y_coords = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_coords.append(x)
    y_coords.append(y)
    
width = max(x_coords) - min(x_coords)
height = max(y_coords) - min(y_coords)
    
print(width * height)