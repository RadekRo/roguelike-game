board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#"\u2584" góra
#wall = "\u2580"
#"\u2588" boki



def display_board(board):
    print("\u2584"*(len(board[0])+2))
    for row in board:
        wall = "\u2588"
        for col in row:
            if col == 0:
                insert = " "
            wall += insert
        wall += "\u2588"
        print(wall)
    print("\u2580"*(len(board[0])+2))



    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    pass

display_board(board)


LEVEL1 = (''' 
-------------------------------- 
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
-------------------------------- 
''')
               
#def uidisplay_board():

#def engine.put_player_on_board: