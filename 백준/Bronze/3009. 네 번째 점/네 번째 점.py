import sys

x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_coords.append(x)
    y_coords.append(y)
    
ans_x = 0
ans_y = 0

for i in range(3):
    if x_coords.count(x_coords[i]) == 1:
        ans_x = x_coords[i]
    if y_coords.count(y_coords[i]) == 1:
        ans_y = y_coords[i]

print(ans_x, ans_y)