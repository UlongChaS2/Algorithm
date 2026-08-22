def solution(keyinput, board):
    moves = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}
    x, y = 0, 0
    x_lim, y_lim = board[0] // 2, board[1] // 2

    for key in keyinput:
        dx, dy = moves[key]
        nx, ny = dx + x, dy + y

        if abs(nx) <= x_lim and abs(ny) <= y_lim:
            x, y = nx, ny
    return [x, y]
