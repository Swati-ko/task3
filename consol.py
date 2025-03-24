# Tic-Tac-Toe Game
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        winner = None

        while not winner and not check_draw(board):
            display_board(board)
            print(f"Player {current_player}'s turn.")
            try:
                row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
                if board[row][col] != " ":
                    print("Invalid move! Cell already taken.")
                    continue
                board[row][col] = current_player
                if check_win(board, current_player):
                    winner = current_player
                else:
                    current_player = switch_player(current_player)
            except (ValueError, IndexError):
                print("Invalid input! Please enter row and column values (0, 1, or 2).")

        display_board(board)
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")

        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

# Run the game
play_tic_tac_toe()
