# Print welcome message 
def intro():

board = [[" " for _ in range(3)] for _ in range(3)]

def dboard():
    print("1 2 3")
    for i in range(3):
        print(i, end=" ")
    for j in range(3):
        print(board[i][j], end=" ")
        print()

def move():
    row = int(input(f"{player}, enter a row:"))
    column = int(input(f"{player}, enter a column:"))
    if row in range(3) and column in range(3) and board[row][column] = " ":
def checkwin():

def main():


if __name__ == "__main__":
    main()