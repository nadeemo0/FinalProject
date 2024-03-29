import time


def intro():
    message = "Hello, and welcome to tic tac toe\n"
    for char in message:
        print(char, end='', flush = True)
        time.sleep(0.05)
    print("\n")
    

board = [[" " for _ in range(3)] for _ in range(3)]


def dboard():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()


def move(player):
    while True:
        try:
            # asks user to input row and column
            row = int(input(f"{player}, enter a row:"))
            column = int(input(f"{player}, enter a column:"))
            # checking if row is full or not
            if row in range(3) and column in range(3) and board[row][column] == " ":
                return row, column
            print("Invalid move, try again")
        except ValueError:
            print("Invalid move, try again")
    

def checkwin(player):
    # check column
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            return True
    # check diagonals
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # check row
    for row in range(3):
        if board[row] == [player, player, player]:
            return True
    return False


def main():
    intro()
    time.sleep(3)
    dboard()
    while True:
        # prompt for X's turn
        row, column = move("X")
        board[row][column] = "X"
        dboard()
        if checkwin("X"):
            print("X wins")
            break
        # tie game possibility on X turn
        if not any(" " in sublist for sublist in board):
            print("Tie game!")
            break
        # prompt for O's turn
        row, column = move("O")
        board[row][column] = "O"
        dboard()
        if checkwin("O"):
            print("O wins!")
            break
        # tie game possibility on O turn
        if not any(" " in sublist for sublist in board):
            print("Tie game!")
            break


if __name__ == "__main__":
    main()