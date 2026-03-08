import sys

n, m = map(int, sys.stdin.readline().split())

matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrix_a[i][j] + matrix_b[i][j], end=" ")
    print()