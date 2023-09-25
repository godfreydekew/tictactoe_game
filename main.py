board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
info_board = ['1', '2', '3',
              '4', '5', '6',
              '7', '8', '9']

currentPlayer = 'X'
gameOn = True


def welcome(info_board):
    print("WELCOME TO TICTACTOE!!!!")
    print(f"{info_board[0]} | {info_board[1]} | {info_board[2]} ")
    print(f"{info_board[3]} | {info_board[4]} | {info_board[5]} ")
    print(f"{info_board[6]} | {info_board[7]} | {info_board[8]} ")
    print("instructions : Please choose any number from the above board to play")


def printBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print(f"{board[6]} | {board[7]} | {board[8]} ")


def takePlayerinput(board):
    global currentPlayer
    position = int(input(f"Please enter position player {currentPlayer}:"))
    if board[position - 1] == '-':
        board[position - 1] = currentPlayer
    else:
        print(" Sorry position entered before:")
        takePlayerinput(board)


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


def checkrows(board):
    if board[0] == board[1] == board[2] and board[0] != '-':
        return True
    if board[3] == board[4] == board[5] and board[4] != '-':
        return True
    if board[6] == board[7] == board[8] and board[6] != '-':
        return True


def checkcolumns(board):
    if board[0] == board[3] == board[6] and board[0] != '-':
        return True
    if board[1] == board[4] == board[7] and board[1] != '-':
        return True
    if board[2] == board[5] == board[8] and board[2] != '-':
        return True


def checkDiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != '-':
        return True
    if board[2] == board[4] == board[6] and board[2] != '-':
        return True


def checkWinner():
    global gameOn, currentPlayer
    if checkDiagonal(board) or checkrows(board) or checkcolumns(board):
        print(f"\n____________ Player {currentPlayer} won!_____________")
        gameOn = False


def board_full(board):
    global gameOn
    if '-' not in board:
        print("_______NO FREE POSITIONS _____GAME END!!!!!")
        gameOn = False


welcome(info_board)
while gameOn:
    board_full(board)
    checkWinner()
    if gameOn:
        takePlayerinput(board)
    switchPlayer()
    printBoard(board)
