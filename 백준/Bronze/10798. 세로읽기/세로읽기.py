import sys

matrix_word = [sys.stdin.readline().strip() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(matrix_word[i]):
            print(matrix_word[i][j], end="")