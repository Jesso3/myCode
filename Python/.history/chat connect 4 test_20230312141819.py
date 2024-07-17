def count_wins(games):
    player_wins = [0, 0, 0]
    draws = 0

    for game in games:
        board = [[0 for _ in range(7)] for _ in range(7)]
        turn = 0

        # process moves in the game
        for move in game:
            col = int(move) - 1
            for row in range(6, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = turn + 1
                    break

            # check for a winner
            if check_winner(board):
                player_wins[turn] += 1
                break

            turn = (turn + 1) % 3

        else:
            # no winner, game ended in a draw
            draws += 1

    return player_wins, draws

def check_winner(board):
    # check for horizontal wins
    for row in range(7):
        for col in range(4):
            if board[row][col] != 0 and \
               board[row][col] == board[row][col+1] == \
               board[row][col+2] == board[row][col+3]:
                return True

    # check for vertical wins
    for col in range(7):
        for row in range(3):
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col] == \
               board[row+2][col] == board[row+3][col]:
                return True

    # check for diagonal wins
    for row in range(3):
        for col in range(4):
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col+1] == \
               board[row+2][col+2] == board[row+3][col+3]:
                return True

    for row in range(3, 7):
        for col in range(4):
            if board[row][col] != 0 and \
               board[row][col] == board[row-1][col+1] == \
               board[row-2][col+2] == board[row-3][col+3]:
                return True

    return False

# example usage
games = ["5615177132314422633773357162745162431525676654244",         "1234567123456712345671234567123456712345671234567"]
player_wins, draws = count_wins(games)
print(player_wins)  # [1, 0, 1]
print(draws)  # 0
print(player_wins[0] * player_wins[1] * player_wins[2])
