import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

min_draw = 64

for i in range(n - 7):
    for j in range(m - 7):
        draw_w = 0
        draw_b = 0
        
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r + c) % 2 == 0:
                    if board[r][c] != 'W': draw_w += 1
                    if board[r][c] != 'B': draw_b += 1
                else:
                    if board[r][c] != 'B': draw_w += 1
                    if board[r][c] != 'W': draw_b += 1
                        
        min_draw = min(min_draw, draw_w, draw_b)
        
print(min_draw)