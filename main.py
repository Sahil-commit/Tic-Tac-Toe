# Tic Tac Toe (X and O)

board = [" " for _ in range(9)]


def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


def print_positions():
    print("Board Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for condition in win_conditions:
        if (
            board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player
        ):
            return True
    return False


def board_full():
    return " " not in board


def play_game():
    current_player = "X"

    print("=" * 30)
    print("     TIC TAC TOE")
    print("=" * 30)

    print_positions()

    while True:
        print_board()

        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move - 1] != " ":
                print("That position is already taken.")
                continue

            board[move - 1] = current_player

            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} Wins!")
                break

            if board_full():
                print_board()
                print("🤝 It's a Draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Please enter a valid number.")


play_game()