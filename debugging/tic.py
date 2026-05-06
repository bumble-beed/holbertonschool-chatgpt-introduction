#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    def parse_input(prompt):
        value = input(prompt).strip().lower()
        if value in ('q', 'quit', 'exit'):
            return None
        try:
            return int(value)
        except ValueError:
            return 'invalid'

    def get_player_name(symbol):
        return "Player 1" if symbol == "O" else "Player 2"

    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = parse_input("Enter row (0, 1, or 2) for " + get_player_name(player) + " or q to quit: ")
        if row is None:
            print("Game quit.")
            return
        if row == 'invalid':
            print("Invalid input. Please enter 0, 1, or 2.")
            continue

        col = parse_input("Enter column (0, 1, or 2) for " + get_player_name(player) + " or q to quit: ")
        if col is None:
            print("Game quit.")
            return
        if col == 'invalid':
            print("Invalid input. Please enter 0, 1, or 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid row or column. Please enter 0, 1, or 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print(get_player_name(player) + " wins!")

tic_tac_toe()
