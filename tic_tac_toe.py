import random
from colorist import green, red, blue

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!\n")

    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)

        if player == 'X':
            row, col = get_user_move(board)
        else:
            row, col = get_computer_move(board)

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            if player == 'X':
                green('You win!')
            else:
                red('You lose.')
            break
        elif is_board_full(board):
            print_board(board)
            blue("It's a tie.")
            break

        # Switch player for the next turn
        player = 'O' if player == 'X' else 'X'

def print_board(board):
    print('\n')
    for i,row in enumerate(board):
        print(" | ".join(row))
        if i != len(row)-1:
            print("-" * 9)
    print('\n')

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_user_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

