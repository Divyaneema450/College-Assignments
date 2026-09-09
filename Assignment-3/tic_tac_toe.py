# Tic-Tac-Toe Game
# Assignment No. 3
# Language: Python


def initialize_board():
    """Create and return an empty 3x3 Tic-Tac-Toe board."""
    return [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


def display_board(board):
    """Display the current Tic-Tac-Toe board."""
    print("\n  1 2 3")

    for i, row in enumerate(board):
        print(f"{i + 1} {' '.join(row)}")

    print()


def check_win(board, player):
    """Check whether the given player has won."""

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True

    # Check main diagonal
    if (
        board[0][0] == player
        and board[1][1] == player
        and board[2][2] == player
    ):
        return True

    # Check opposite diagonal
    if (
        board[0][2] == player
        and board[1][1] == player
        and board[2][0] == player
    ):
        return True

    return False


def check_draw(board):
    """Check whether the board is completely filled."""

    for row in board:
        for cell in row:
            if cell == '-':
                return False

    return True


def player_move(board, player):
    """Take a valid move from the current player."""

    while True:
        move = input(
            f"Player {player}, enter your move as 'row,col': "
        )

        try:
            row, col = map(int, move.split(','))

            # Convert user input from 1-3 to Python index 0-2
            row -= 1
            col -= 1

            if (
                0 <= row < 3
                and 0 <= col < 3
                and board[row][col] == '-'
            ):
                board[row][col] = player
                break

            print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Please enter in the format row,col.")


def play_tic_tac_toe():
    """Start and control the Tic-Tac-Toe game."""

    board = initialize_board()

    # Player X starts
    current_player = 'X'

    print("================================")
    print("       TIC-TAC-TOE GAME")
    print("================================")

    while True:

        display_board(board)

        player_move(board, current_player)

        # Check whether the current player has won
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check whether the game is a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


# Start the game
if __name__ == "__main__":
    play_tic_tac_toe()
