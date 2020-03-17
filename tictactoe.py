# utf-8
def showboard(board):
    print(board[0])
    print(board[1])
    print(board[2])


def playerTurn(activeplayer, board, symbol):
    while True:
        try:
            selection = (input((activeplayer, 'Please choose your position ')))
            if selection == 'stop':
                exit()
            elif int(selection) not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                raise ValueError()
            elif int(selection) <= 3:
                try:
                    board[0].index(str(selection))
                except ValueError:
                    print('Already chosen, please try another')
                board[0] = board[0].replace(str(selection), symbol)
            elif 4 <= int(selection) <= 6:
                try:
                    board[1].index(str(selection))
                except ValueError:
                    print('Already chosen, please try another')
                board[1] = board[1].replace(str(selection), symbol)
            elif int(selection) >= 7:
                try:
                    board[2].index(str(selection))
                except ValueError:
                    print('Already chosen, please try another')
                board[2] = board[2].replace(str(selection), symbol)
            return board
        except ValueError:
            print('An incorrect option was chosen. Please choose again')


def checkwinner(board, marker):
    showboard(board)
    gamefull = True
    wincheck = ''.join(board)
    winner = marker+marker+marker
    wincheck = wincheck.replace('|', '')
    if wincheck[0:3] == winner or wincheck[3:6] == winner or wincheck[7:] == winner or wincheck[::3] == winner \
            or wincheck[1::3] == winner or  wincheck[2::3] == winner or wincheck[1::4] == winner:
        print('winner!')
        exit()
    else:
        for x in wincheck:
            if x == 'X' or x == 'O':
                pass
            else:
                return board
        if gamefull:
            print('board is full, resetting')
            top = '|1|2|3|'
            middle = '|4|5|6|'
            bottom = '|7|8|9|'
            board = [top, middle, bottom]
            showboard(board)
            return board


def ticTacToeBoard(playerone, playertwo, board):
    print('good luck!')
    showboard(board)
    gamerunning = True
    while gamerunning:
        playerTurn(playerone, board, 'X')
        board = checkwinner(board, 'X')
        playerTurn(playertwo, board, 'O')
        board = checkwinner(board, 'O')


top = '|1|2|3|'
middle = '|4|5|6|'
bottom = '|7|8|9|'
board = [top, middle, bottom]
x = input('Please enter a name for player 1 ')
o = input('Please enter a name for player 2 ')
ticTacToeBoard(x, o, board)
