import sys

n = int(sys.stdin.readline())
side_vertices = 2

for _ in range(n):
    side_vertices = side_vertices * 2 - 1
    
print(side_vertices ** 2)
    