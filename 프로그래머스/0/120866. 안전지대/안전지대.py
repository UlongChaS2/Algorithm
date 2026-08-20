def solution(board):
    n = len(board)
    answer = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < n and 0 <= c < n and board[r][c] == 0:
                        board[r][c] = -1
                        
    return sum(row.count(0) for row in board)