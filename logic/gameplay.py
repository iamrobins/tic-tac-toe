def check_winner(player, board):
    count = 0
    for i in range(3):
        # row check
        for j in range(3):
            if board[i][j] == player: count += 1
        if count == 3: return (True, player, "row", i+1)
        count = 0

        # col check
        for j in range(3):
            if board[j][i] == player: count += 1
        if count == 3: return (True, player, "col", i+1)
        count = 0

        # dig check 1
        for j in range(3):
            if board[j][j] == player: count += 1
        if count == 3: return (True, player, "digonal", "first")
        count = 0

        # dig check 2
        k = 0
        for j in range(2, -1, -1):
            if board[k][j] == player: count += 1
            k += 1
        if count == 3: return (True, player, "digonal", "second")
        count = 0
    
    return (False, None, None, None)

def safe_move(player, board, move):
    valid_inputs = ['1', '2', '3']
    if len(move) < 2 or move[0] not in valid_inputs or move[1] not in valid_inputs: return False

    if board[int(move[0]) - 1][int(move[1]) - 1] == player or board[int(move[0]) - 1][int(move[1]) - 1] != " ": return False
    board[int(move[0]) - 1][int(move[1]) - 1] = player
    return True