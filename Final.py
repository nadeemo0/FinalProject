# Print welcome message 
def intro():
    print("Hello, and welcome to tic tac toe")

board = [[" " for _ in range(3)] for _ in range(3)]

def dboard():
    print("0 1 2")
    for i in range(3):
        print(i, end=" ")
    for j in range(3):
        print(board[i][j], end=" ")
        print()

def move():
    # asks user to input row and column
    row = int(input(f"{player}, enter a row:"))
    column = int(input(f"{player}, enter a column:"))
    # moving row and column
    if row in range(3) and column in range(3) and board[row][column] == " ":
        return row, column
    
def checkwin():
    # check column
    if board[0][column] == player and board[1][column] == player and board[2][column] == player:
        return
    # check diagonals
    

def main():


if __name__ == "__main__":
    main()