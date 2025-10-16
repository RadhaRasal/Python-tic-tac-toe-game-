
def display_board(board):
    # board is a list of 9 elements (indexes 0..8)
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(board, player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a]==player and board[b]==player and board[c]==player for a,b,c in wins)

def check_draw(board):
    return all(cell != " " for cell in board)

def get_move(board, player):
    while True:
        try:
            move = input(f"Player {player} — choose a cell (1-9): ").strip()
            if move.lower() in ("q", "quit", "exit"):
                print("Goodbye!")
                raise SystemExit
            pos = int(move) - 1
            if pos < 0 or pos > 8:
                print("Please enter a number from 1 to 9.")
                continue
            if board[pos] != " ":
                print("That cell is already taken. Pick another one.")
                continue
            return pos
        except ValueError:
            print("Invalid input. Enter a number from 1 to 9, or 'q' to quit.")

def main():
    board = [" "] * 9
    current = "X"  # X always starts
    print("Tic-Tac-Toe — Two players")
    print("Cells are numbered 1 to 9 like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Type 'q' to quit anytime.\n")

    while True:
        display_board(board)
        pos = get_move(board, current)
        board[pos] = current

        if check_win(board, current):
            display_board(board)
            print(f"Player {current} wins — congratulations!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # switch player
        current = "O" if current == "X" else "X"

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    main()
