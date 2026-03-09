import sys

paper = [[0] * 100 for _ in range(100)]
n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
            
print(sum(sum(row) for row in paper))