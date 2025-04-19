import math

# Define the board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Check for win conditions
def check_win(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0  # No winner yet

# Evaluate the board
def evaluate(board):
    winner = check_win(board)
    if winner == 1:  # Player A ('X')
        return 1
    elif winner == -1:  # Player B ('O')
        return -1
    return 0

# Minimax algorithm
def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 1:
        return score
    if score == -1:
        return score
    if all(board[i][j] != 0 for i in range(3) for j in range(3)):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = 0
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = 0
        return best

# Find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1  # Make the move for Player A ('X')
                move_val = minimax(board, 0, False)
                board[i][j] = 0  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage
move = find_best_move(board)
print(f"Optimal move for Player A: Row {move[0]}, Col {move[1]}")
