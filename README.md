My game is a simple implementation of classic game Tic Tac Toe, where players take alternating turns playing as X and O. 

It can be run by executing: "python3 FinalProject.py"

An introduction message is printed to the user using the "intro()" function. The message appears to be typed out letter-by-letter using the time.sleep(0.05) function.

A 2D list named board that is initialized with blank spaces serves as the representation of the game board. The "dboard()" function is used to display the current state of the game board to the user.

The "move(player)" function asks the user to select a row and column on which to make their move before determining whether the move is legal (i.e., if the specified row and column are within the range of the game board and the location is empty). The player is instructed to try again if the move is invalid.

Using the "checkwin(player)" function to see if a player has won the round by looking for three consecutive player symbols on the game board either diagonally, horizontally or veritcally.

The game's flow is managed by the main() function. The intro() function is used to show the welcome message, while the dboard() function is used to show the first game board. The game then enters a loop in which the code asks the user for movements again (first for player X, then for player O), changes the game board, and determines if either player has won. Additionally, the game uses the any() function on the board variable to determine whether the game is tied after each move and after the checkwin condition. If all the places are filled, the game is a tie. The winning message is shown and the loop is ended once a player has won.
