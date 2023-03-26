import engine

def display_board(board):
    north_wall = "\u2584"*(len(board[0])+2)
    open_door(north_wall, 4) #zmiana rozmiaru drzwi
    for row in board:
        wall = "\u2588"
        for col in row:
            if col == 0:
                insert = " "
            else:
                insert = col
            wall += insert
        wall += "\u2588"
        print(wall)
    print("\u2580"*(len(board[0])+2))

def open_door(wall, door_size = 4):
    wall = list(wall)
    half_wall = int(len(wall)  / 2) - int(door_size/2)
    for i in range(half_wall, half_wall + door_size):
        wall[i] = " "
    wall = "".join(wall)    
    print(wall)

    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    pass